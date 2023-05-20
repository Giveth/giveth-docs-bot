import interactions
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from langchain.agents import Tool, initialize_agent
from langchain.chains import LLMMathChain, LLMChain, RetrievalQA
from langchain.prompts import PromptTemplate
import os

from knowledge_base import load_knowledge_base

load_dotenv()
bot = interactions.Client(os.getenv('DISCORD_TOKEN'))
knowledge_base = None
    
    
@bot.command(
    name="reload",
    description="Reload the knowledge base",
)
async def reload(ctx: interactions.CommandContext):
    global knowledge_base
    await ctx.defer()
    knowledge_base = load_knowledge_base()
    await ctx.send(content="Knowledge base reloaded")

@bot.command(
        name="ask",
        description="Ask a question about Giveth",
        options = [
            interactions.Option(
                name="question",
                description="Ask a question about Giveth",
                type=interactions.OptionType.STRING,
                required=True,
            ),
    ])
async def ask(ctx: interactions.CommandContext, question: str):
    if question:
        await ctx.defer()
        docs = knowledge_base.similarity_search(question)

        llm = ChatOpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=question)
            print(cb)

        response = f"**Question:** {question}\n**Answer:** {response}"
        await ctx.send(content=response)

@bot.command(
    name="experimental_agent",
    description="Ask a question to the agent",
    options = [
        interactions.Option(
            name="question",
            description="Ask a question to the agent",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ])
async def experimental_agent(ctx: interactions.CommandContext, question: str):
    if question:
        await ctx.defer()

        llm = ChatOpenAI(
            model_name="gpt-4"
        )
        llm_math = LLMMathChain(llm=llm)
        prompt = PromptTemplate(
            input_variables=["query"],
            template="{query}"
        )
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        knowledge_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=knowledge_base.as_retriever())

        math_tool = Tool(
            name="calculator",
            func=llm_math.run,
            description="Calculate a math expression",
        )
        llm_tool = Tool(
            name="language model",
            func=llm_chain.run,
            description="General purpose queries and logic",
        )
        knowledge_tool = Tool(
            name="knowledge base",
            func=knowledge_chain.run,
            description="Queries about Giveth",
        )

        tools = [math_tool, llm_tool, knowledge_tool]
        
        # Initialize and run the agent
        agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True, max_iterations=3)
        response = agent.run(question)
        
        response = f"**Question:** {question}\n**Agent's Answer:** {response}"
        await ctx.send(content=response)

if __name__ == '__main__':
    knowledge_base = load_knowledge_base()
    bot.start()
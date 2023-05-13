import interactions
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
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

        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=question)
            print(cb)

        response = f"**Question:** {question}\n**Answer:** {response}"
        await ctx.send(content=response)

if __name__ == '__main__':
    knowledge_base = load_knowledge_base()
    bot.start()
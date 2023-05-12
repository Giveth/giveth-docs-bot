import interactions
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import os

load_dotenv()
bot = interactions.Client(os.getenv('DISCORD_TOKEN'))


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
    # user input
    user_question = question
    if user_question:
        await ctx.defer()
        docs = knowledge_base.similarity_search(user_question)

        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
            print(cb)

        await ctx.send(content=response)

if __name__ == '__main__':
    # open giveth.md
    text = open("giveth.md", "r").read()

    # split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # create embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    bot.start()
import subprocess
import glob
import os

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# functoin to load the knowledge base
def load_knowledge_base():
    # Path to the giveth-docs directory
    path = 'giveth-docs'

    # URL of the git repository
    url = "https://github.com/giveth/giveth-docs.git"

    # If giveth-docs directory doesn't exist, perform a shallow clone of the git repository
    if not os.path.exists(path):
        subprocess.run(['git', 'clone', '--depth', '1', url, path])
    else:
        # If giveth-docs directory exists, navigate to it and perform a git pull
        os.chdir(path)
        subprocess.run(['git', 'pull'])
        # Navigate back to the original directory
        os.chdir('..')

    # read all .md files into a single string
    text = ""
    for filename in glob.glob(path + '/**/*.md', recursive=True):
        with open(filename, 'r') as file:
            text += file.read()

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
    return FAISS.from_texts(chunks, embeddings)

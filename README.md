# Giveth Docs Bot

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)

This project allows you to ask questions about Giveth, a non-profit organization focused on blockchain-based donations and decentralized governance, by utilizing a bot which fetches answers directly from Giveth's documentation.

## Requirements
1. Python 3.7 or later.
2. Git

## Installation

1. Ensure you have the required dependencies installed.
2. Clone the repository.
3. Install the required Python libraries by running `pip install -r requirements.txt` in the root directory of the project.

## Usage

The bot is intended for use within a Discord server. Here is how you can utilize the bot's commands:

- `/reload` - This command reloads the knowledge base from the Giveth's documentation.
- `/ask <your question here>` - This command fetches the answer to your question from the knowledge base. Replace `<your question here>` with your actual question about Giveth.
- `/experimental_agent <your question here> - This command fetches the answer to your question using the experimental agent. Replace `<your question here>` with your actual question about Giveth.

## Setting up Discord Bot Token and OpenAI API Key

The bot uses Discord's token for authentication and OpenAI's API key to generate text embeddings.

### Discord Token

To obtain a token, follow these steps:

1. Visit the Discord Developer Portal (https://discord.com/developers/applications)
2. Click on "New Application"
3. Name your application and click "Create"
4. On the left panel, click on "Bot"
5. Click on "Add Bot"
6. Under the bot settings, click on "Copy" to copy the bot token

### OpenAI API Key

To obtain the OpenAI API key, follow these steps:

1. Visit the OpenAI website and create an account (https://www.openai.com/)
2. Navigate to the API section (https://platform.openai.com/account/api-keys)
3. Generate a new key

Next, create a `.env` file in the root directory of the project and paste your bot token and OpenAI API Key like this:

```
DISCORD_TOKEN=your_discord_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_discord_token_here` with the actual token and `your_openai_api_key_here` with the actual API key.

## Setting up the Knowledge Base

The bot relies on the Giveth's documentation as its knowledge base. The documentation is fetched from the Giveth's GitHub repository.

Upon running the bot for the first time, it automatically clones the Giveth's documentation repository, if it doesn't already exist in the `giveth-docs` directory. If the repository already exists, it performs a git pull to fetch the latest documentation.

The bot then reads all markdown files from the repository, breaks the text into chunks, and generates embeddings for each chunk. The embeddings are used to perform a similarity search when a question is asked.

## Running the Bot

To run the bot, simply execute the `main.py` script:

```
python main.py
```

The bot then connects to your Discord server and is ready to accept commands.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the LICENSE file for details.

# Telegram Bot for Downloading Media from Social Media Links

This is a Telegram bot built with Python that can download media from various social media platforms such as YouTube, Twitter, and Instagram. It uses the respective APIs provided by these platforms to fetch the media and send it as a file or document to the user who sends the link to the bot in a Telegram chat.

## Setup and Installation

### Prerequisites

- Python 3.6 or higher
- Telegram Bot API token
- Twitter API credentials (consumer key, consumer secret, access token, and access secret)
- Instagram username and password

### Installation

1. Clone the repository or download the source code.

git clone https://github.com/your_username/telegram-bot.git
cd telegram-bot


2. Install the required packages.

pip install -r requirements.txt


3. Set the environment variables.

export TELEGRAM_TOKEN=your_telegram_token
export TWITTER_CONSUMER_KEY=your_twitter_consumer_key
export TWITTER_CONSUMER_SECRET=your_twitter_consumer_secret
export TWITTER_ACCESS_TOKEN=your_twitter_access_token
export TWITTER_ACCESS_SECRET=your_twitter_access_secret
export INSTAGRAM_USERNAME=your_instagram_username
export INSTAGRAM_PASSWORD=your_instagram_password


You can also set these variables permanently by adding them to your shell's configuration file (e.g. `.bashrc`, `.zshrc`, etc.).

4. Run the bot.

python telegram_bot.py


The bot should now be running and ready to respond to messages sent to it in a Telegram chat.

## Usage

1. Start a chat with the bot in Telegram.

2. Send a message with a link to a video or image on YouTube, Twitter, or Instagram.

3. The bot should respond with the downloaded media as a file or document.

## Docker

A Dockerfile is included in the repository to build a container for the bot. To use it:

1. Build the Docker image.

docker build -t telegram-bot .


2. Set the environment variables as above.

3. Run the container.

docker run -d --name my-telegram-bot telegram-bot


Make sure to replace `your_telegram_token`, `your_twitter_consumer_key`, `your_twitter_consumer_secret`, `your_twitter_access_token`, `your_twitter_access_secret`, `your_instagram_username`, and `your_instagram_password` with the appropriate values.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

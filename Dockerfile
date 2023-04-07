FROM python:3.9-slim-buster

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port 8443 for the telegram bot API
EXPOSE 8443

# Set environment variables
ENV TELEGRAM_TOKEN=your_telegram_token
ENV TWITTER_CONSUMER_KEY=your_twitter_consumer_key
ENV TWITTER_CONSUMER_SECRET=your_twitter_consumer_secret
ENV TWITTER_ACCESS_TOKEN=your_twitter_access_token
ENV TWITTER_ACCESS_SECRET=your_twitter_access_secret

# Run the bot
CMD ["python", "telegram_bot.py"]

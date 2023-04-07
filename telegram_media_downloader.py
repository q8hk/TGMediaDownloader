import telegram
import logging
import urllib.request
import tweepy
from pytube import YouTube
import instaloader
import os
from telegram.ext import CommandHandler, Updater


# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Read environment variables
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
logger.info(TELEGRAM_TOKEN)
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
logger.info(TWITTER_CONSUMER_KEY)
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
logger.info(TWITTER_CONSUMER_SECRET)
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
logger.info(TWITTER_ACCESS_TOKEN)
TWITTER_ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')
logger.info(TWITTER_ACCESS_SECRET)

# Set up the telegram bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Set up the twitter API client
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
twitter_api = tweepy.API(auth)

# Define a function to handle YouTube links
def handle_youtube(update, context):
    # Get the YouTube link from the user's message
    youtube_link = update.message.text.split(' ')[1]

    # Download the video
    yt = YouTube(youtube_link)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download()

    # Send the video to the user
    chat_id = update.message.chat_id
    bot.send_video(chat_id=chat_id, video=open(video.title + '.mp4', 'rb'))

# Define a function to handle Twitter links
def handle_twitter(update, context):
    # Get the Twitter link from the user's message
    twitter_link = update.message.text.split(' ')[1]

    # Get the tweet ID from the link
    tweet_id = twitter_link.split('/')[-1]

    # Get the tweet object from the tweet ID
    tweet = twitter_api.get_status(tweet_id, tweet_mode='extended')

    # Check if the tweet contains any media
    if 'media' in tweet.entities:
        # Download the first media attachment in the tweet
        media_url = tweet.entities['media'][0]['media_url']
        urllib.request.urlretrieve(media_url, 'twitter_media')

        # Send the media to the user
        chat_id = update.message.chat_id
        bot.send_photo(chat_id=chat_id, photo=open('twitter_media', 'rb'))
    else:
        # Send an error message to the user
        chat_id = update.message.chat_id
        bot.send_message(chat_id=chat_id, text='No media found in tweet.')

# Define a function to handle Instagram links
def handle_instagram(update, context):
    # Get the Instagram link from the user's message
    instagram_link = update.message.text.split(' ')[1]

    # Download the post
    L = instaloader.Instaloader()
    L.download_post(instagram_link, target='instagram')

    # Send the post to the user
    chat_id = update.message.chat_id
    with open('instagram/{}'.format(list(L.get_hashtags())[0]), 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

# Set up the telegram bot's message handler
updater = telegram.ext.Updater(token=TELEGRAM_TOKEN, use_context=True)

# Add the handlers for the different types of media links
updater.dispatcher.add_handler(CommandHandler('youtube', handle_youtube))
updater.dispatcher.add_handler(CommandHandler('twitter', handle_twitter))
updater.dispatcher.add_handler(CommandHandler('instagram', handle_instagram))


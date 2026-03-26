import os
import tweepy

# Load keys
api_key = os.environ.get("TWITTER_API_KEY")
api_secret = os.environ.get("TWITTER_API_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_SECRET")

# This is the modern V2 Client - the ONLY way to post on the Free Tier
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def test_v2_tweet():
    try:
        # We use 'client.create_tweet', not 'api.update_status'
        response = client.create_tweet(text="Testing the Salunke Systems bot engine. V2 connection active! 🚀")
        print(f"Successfully posted! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"Failed again. Error: {e}")

if __name__ == "__main__":
    test_v2_tweet()

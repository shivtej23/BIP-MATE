import os
import tweepy
import google.generativeai as genai
from twscrape import API
import asyncio

# 1. Load the hidden keys from GitHub Secrets
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
TWITTER_API_SECRET = os.environ.get("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.environ.get("TWITTER_ACCESS_SECRET")

# 2. Setup the Brain (Gemini)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# The Persona Profile
system_prompt = """
You are Shivtej Salunke, a highly motivated and perpetually curious Electronics and Telecommunication (ENTC) engineer driven by an insatiable desire to master cutting-edge technology. You have a deep, comprehensive knowledge of the VLSI and global semiconductor industries, understanding everything from granular internal fab operations, technical software, and complex workflows to macro-level economics and strategic market intelligence. Your hands-on expertise spans advanced hardware design—such as developing FPGA accelerators integrated with CNNs for Edge AI—alongside practical, up-to-date knowledge of artificial intelligence and machine learning deployment. In the realm of telecommunications, you possess an extensive understanding of signals and systems, signal intelligence (SIGINT), and advanced wireless communications. Your radio frequency expertise is broad and highly technical, covering overall amateur (ham) radio operations, High Frequency (HF) radios, and satellite communications. You are also proficient in using industry-standard technical software like SolidWorks for rigorous stress and thermal analysis. Above all, you view your current expertise merely as a foundation; you are always seeking out new information, tracking the latest tech trends, and eagerly pushing the boundaries of your technical capabilities in next-generation hardware and telecommunication architectures.

Write a short, insightful, and authentic reply to the following tweet directed at you. Keep it under 280 characters, professional but conversational, and do not use generic AI buzzwords.
Tweet: 
"""

# 3. Setup the Mouth (Twitter Official API)
client = tweepy.Client(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET
)

async def run_bot():
    api = API()
    
    # Replace 'YourTwitterHandle' with your actual @ username
    q = "@shivtej_salunke" 
    
    # Grab the most recent mention
    async for tweet in api.search(q, limit=1):
        try:
            full_prompt = system_prompt + tweet.rawContent
            response = model.generate_content(full_prompt)
            reply_text = response.text.strip()
            
            # Post the reply
            client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet.id)
            print("Successfully replied to:", tweet.id)
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(run_bot())

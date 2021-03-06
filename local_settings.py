'''
Local Settings for a heroku account.
'''

#configuration
MY_CONSUMER_KEY = 'TODO'
MY_CONSUMER_SECRET = 'TODO'
MY_ACCESS_TOKEN_KEY = 'TODO'
MY_ACCESS_TOKEN_SECRET = 'TODO'

SOURCE_ACCOUNTS = ["SenSanders"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "BernieBot1" #The name of the account you're tweeting from.

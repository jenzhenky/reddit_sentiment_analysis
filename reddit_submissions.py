import requests
import json

x = 0

# Set initial parameters to get the 500 most recent comments
parameters = {"subreddit": "lawschooladmissions", "size": 500}
dict = []

# Loop to append all comments to dict
while True:
    try:
        response = requests.get("https://api.pushshift.io/reddit/search/submission/", params=parameters)
        dict_response = response.json()
        dict.append(dict_response)
        i = dict_response['data'][-1]['created_utc'] # timestamp of oldest result
        parameters = {"subreddit": "lawschooladmissions", "size": 500, "before":i} # add "before" parameter to get the next 500 comments
        x += 1
        print(x)
    except:
        break

# Write dict to reddit_comments.json
with open('reddit_submissions.json', 'w') as f:
    json.dump(dict, f)

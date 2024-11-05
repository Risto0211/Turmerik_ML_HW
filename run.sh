#!/bin/bash

# CLIENT_ID:        Reddit API client ID 
# CLIENT_SECRET:    Reddit API client secret 
# USER_AGENT:       Name of Reddit API user agent, e.g. "health_research_bot"
# USERNAME:         Reddit username, e.g. "username"
# PASSWORD:         Reddit password, e.g. "password"
# TIMEFRAME:        time frame for posts, e.g. "year" 
# MAXPOSTS:         maximum number of posts to retrieve each topic, e.g. 10 
# KEYWORDS:         keywords to search for in posts, split by space, e.g. "clinical trial" "healthcare" 

CLIENT_ID=None
CLIENT_SECRET=None
USER_AGENT=None
USERNAME=None
PASSWORD=None
TIMEFRAME=None   
MAXPOSTS=0    
KEYWORDS=None

python3 reddit_crawl.py \
#   --client_id "$CLIENT_ID" \
#   --client_secret "$CLIENT_SECRET" \
#   --user_agent "$USER_AGENT" \
#   --username "$USERNAME" \
#   --password "$PASSWORD" \
#   --timeframe "$TIMEFRAME" \
#   --keywords "$KEYWORDS" \
#   --maxposts "$MAXPOSTS"       # if you want to edit the arguments, uncomment specific lines and change the values

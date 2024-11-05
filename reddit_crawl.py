import praw
import argparse
from sentiment_analyze import analyze_sentiment
from openai_message import generate_response


# define global variables
CLIENT_ID = "Lv3Sh9YU3vphhHPuNgRpPA"
CLIENT_SECRET = "TaWhHsDWTeG_0dMCxi779d-slU4ndA"
USER_AGENT = "health_research_bot"
USERNAME = "Risto0211"
PASSWORD = "Lsd020211"
TIMEFRAME = "year"
MAXPOSTS = 5
KEYWORDS = ["clinical trials", "drug trials", "experimental treatments", 
                "chronic illness", "cancer trials", "mental health trials", "rare diseases"]

def get_arguments():
    parser = argparse.ArgumentParser(description="Reddit Health Research Bot")
    parser.add_argument("--client_id", type=str, help="Reddit API client ID", default=CLIENT_ID)
    parser.add_argument("--client_secret", type=str, help="Reddit API client secret", default=CLIENT_SECRET)
    parser.add_argument("--user_agent", type=str, help="Reddit API user agent", default=USER_AGENT)
    parser.add_argument("--username", type=str, help="Reddit username", default=USERNAME)
    parser.add_argument("--password", type=str, help="Reddit password", default=PASSWORD)
    parser.add_argument("--timeframe", type=str, help="Timeframe for search (day, week, month, year, all)", default=TIMEFRAME)
    parser.add_argument("--maxposts", type=int, help="Maximum number of posts to retrieve", default=MAXPOSTS)
    parser.add_argument("--keywords", type=str, nargs='+', help="Keywords to search for", default=KEYWORDS)
    args = parser.parse_args()
    print(args)
    return args

# define the main function
def main():
    args = get_arguments()
    # set up Reddit API
    reddit = praw.Reddit(
        client_id=args.client_id,
        client_secret=args.client_secret,
        user_agent=args.user_agent,
        username=args.username,
        password=args.password
    )

    # define keywords to search for
    keywords = args.keywords

    # open file to save posts
    with open("reddit_health_posts.txt", "w", encoding="utf-8") as file:
        for keyword in keywords:
            file.write(f"### Searching for keyword: {keyword} ###\n\n")
            # set counter to keep track of the number of posts
            count = 0
            
            # sort by relevance and filter by year
            for submission in reddit.subreddit("all").search(keyword, sort="relevance", time_filter=args.timeframe):
                if count >= args.maxposts:
                    break
                # if the post is less than 10 characters, skip it
                if len(submission.selftext) < 10:
                    continue
                post_text = submission.title + ". " + submission.selftext
                # if the post is too long, truncate it
                if len(post_text) > 1000:
                    post_text = post_text[:1000]
                sentiment_score = analyze_sentiment(post_text)
                personalized_message = generate_response(sentiment_score, post_text)
                # write post details to file
                file.write(f"Title: {submission.title}\n")
                file.write(f"Upvotes: {submission.score}\n")
                file.write(f"Comments: {submission.num_comments}\n")
                file.write(f"Text: {submission.selftext}\n\n") 
                file.write(f"Sentiment Score: {sentiment_score}\n\n")
                file.write(f"Personalized Message: {personalized_message}\n\n")
                file.write("While this clinical trial avoids many of the issues you mentioned, we still recommend considering any potential risks. Feel free to ask more questions to ensure you fully understand the trial.\n\n")
                file.write("This message is generated based on your feedback about clinical trials. We value your input and have considered it in our recommendations.\n\n")
                file.write("-" * 40 + "\n\n")
                count += 1

            file.write(f"### Found {count} posts for keyword: {keyword} ###\n\n")

    print("Finished writing posts to file.")


# call the main function
if __name__ == "__main__":
    main()

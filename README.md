# RedditPostRemover
Simple script that removes submissions matching an array of strings on a subreddit or from a specific user

### Summary
This is a simple script that will perpetually run to check if any posts or comments from a specified subreddit or user contain one of a set of substrings. If any do, the submission will be removed. This post was created in order to combat spam with similar formatting to ease moderation stress.

### Requirements
- Reddit account (with moderator permissions on the subreddit you would like to edit)
- Subreddit to scan OR user to scan
- Populated array of strings to match against
- PRAW required parameters (client ID, client secret, user agent)

### Dependencies
- **praw** to interact with the Reddit API
- **os** for the environment variables
- **time** to delay subsequent scans
- **datetime** to print out the timestamp for when removals occur

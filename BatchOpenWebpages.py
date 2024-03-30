import webbrowser
import urllib.parse

# Read the query.txt file
with open("query.txt", "r") as file:
    queries = file.readlines()

# Iterate over each query line
for query in queries:
    # Remove the newline character from the query
    query = query.strip()
    
    # URL-encode the query
    encoded_query = urllib.parse.quote(query)
    
    # Construct the Twitter search URL
    twitter_url = f"https://twitter.com/search?q={encoded_query}"
    
    # Construct the YouTube search URL
    youtube_url = f"https://www.youtube.com/results?search_query={encoded_query}"
    
    # Construct the Xiaohongshu search URL
    xiaohongshu_url = f"https://www.xiaohongshu.com/search_result?keyword={encoded_query}&source=unknown"
    
    # Open the default browser and navigate to the search result pages
    webbrowser.open(twitter_url)
    webbrowser.open(youtube_url)
    webbrowser.open(xiaohongshu_url)
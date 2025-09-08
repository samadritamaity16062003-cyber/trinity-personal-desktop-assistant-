import requests

# Make the API request
url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=aac1b86e06944ce3a91d5f1cbff0983d"
response = requests.get(url)

# Convert the response to JSON

data = response.json()
articles = data.get("articles")
for article in articles:
    print(article["title"]+"\n")
    # newsapi = aac1b86e06944ce3a91d5f1cbff0983d



# # Extract all titles
# if "articles" in data:
#     titles = [article["title"] for article in data["articles"] if "title" in article]
#     for i, title in enumerate(titles, start=1):
#         print(f"{i}. {title}")
# else:
#     print("No articles found")
# 
# import requests

# def get_news():
#     url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY"
#     try:
#         # 1. Send request to NewsAPI server
#         response = requests.get(url)

#         # 2. Convert JSON response into Python dictionary
#         data = response.json()

#         # 3. Check if 'articles' key exists in the response
#         if "articles" in data:

#             # 4. Extract only the "title" field from each article
#             headlines = [article["title"] for article in data["articles"] if "title" in article]

#             # 5. Return top 5 headlines
#             return headlines[:5]
#         else:
#             return ["No news found."]

#     # 6. If something goes wrong (like no internet), handle the error
#     except Exception as e:
s = "harry is a good boy so everyone loves him"
word = s.split("good",1)
print(word)
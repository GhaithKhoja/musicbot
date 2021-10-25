import requests

def search(query):
    url = f"https://www.youtube.com/results?search_query={query}"

    r = requests.get(url)

    # Parse response
    for idx, chr in enumerate(r.text):
        if chr == "?":
            if r.text[idx+1] == "v":
                return [f"https://www.youtube.com/watch{r.text[idx:idx+14]}", "video_title"]

# API_KEY = 'AIzaSyCrFFN6cuJVShMzEg0sZBxGkBS1nZdhces'

# def old_search(query, MAX_RESULTS=1):
#     URL = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults={MAX_RESULTS}&q={query}&key={API_KEY}"
#     response = requests.get(URL).json()
#     video_id = response['items'][0]['id']['videoId']
#     video_title = response['items'][0]['snippet']['title']
#     video_link = f"https://youtube.com/watch?v={video_id}"
#     return [video_link, video_title]

if __name__ == "__main__":
    # pass
    # Test
    while True:
        query = input("Type video name: ")
        print(search(query))
    
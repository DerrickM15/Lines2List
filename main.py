import re
import requests
import json

# From https://developer.spotify.com/documentation/web-api/tutorials/getting-started
# curl -X POST "https://accounts.spotify.com/api/token" 
#      -H "Content-Type: application/x-www-form-urlencoded" 
#      -d "grant_type=client_credentials&client_id=5981a6ae97e844e59927cc6744fb3f99&client_secret=dce31918a9714120b5267bf94f5183bd"

data = {
    'grant_type': 'client_credentials',
    'client_id': '5981a6ae97e844e59927cc6744fb3f99',
    'client_secret': 'dce31918a9714120b5267bf94f5183bd',
}

response = requests.post('https://accounts.spotify.com/api/token', data=data)
data = response.json()
access_token = data['access_token']

headers = {
    'Authorization': 'Bearer ' + access_token
}

# response = requests.get('https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb', headers=headers)
# print(response.json())




### Prompt user for lines
lines = input('Enter lines or .txt file: \n') 

### Check if lines ends with .txt, import txt file if they do
if '.txt' in lines: 
    f = open(lines, 'r', encoding='UTF-8')
    lines = f.read() 

### If lines contain !@#$%^&*(){}[]-=+_, remove and replace with space
pattern = r"[^a-zA-Z'’]+" 
lines = re.sub(pattern, ' ', lines) 
# print(lines)  #TODO: DEL

for word in lines.split():
    q = word
    params = {
        'q': q,
        'type': 'track',
    }
    response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)
    song_data = response.json()
    names = [item["name"] for item in song_data["tracks"]['items']]
    print(word)
    print(names)

### Prompt user for Playlist Title

# playlist = input('Enter playlist title: \n') #TODO: Remove comment

### Iterate through lines by word, check against Spotify API for song titles, start with 5 words and reduce down until song titles are found


### If no song titles are found, remove 1 word from the string and check again

### If song titles are found, add title to playlist

### Once complete, provide URL to playlist
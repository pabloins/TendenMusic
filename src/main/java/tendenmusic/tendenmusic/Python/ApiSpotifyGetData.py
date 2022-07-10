#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import datetime
import json
import csv
from urllib.parse import urlencode


# In[3]:


import base64


# In[4]:


client_id="6027cd821062416aa63f349653ccab78"
client_secret="e4e461cd9b5d426b97c231d433ec020e"


# In[5]:


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"
    
    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
    
    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }
    
    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        } 
    
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            raise Exception("Could not authenticate client.")
            # return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True
    
    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token() 
        return token
    
    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        return headers
        
        
    def get_resource(self, lookup_id, resource_type='albums', version='v1'):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()


    def get_several_Artists(self, lookup_id, resource_type='albums', version='v1'):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}?ids={lookup_id}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()    
    
    def get_album(self, _id):
        return self.get_resource(_id, resource_type='albums')
    
    def get_artist(self, _id):
        return self.get_several_Artists(_id, resource_type='artists')

    def get_playlist(self, _id):
        return self.get_resource(_id, resource_type='playlists')

    def get_tracks(self, _id):
        return self.get_resource(_id, resource_type='tracks')
    
    def base_search(self, query_params): # type
        headers = self.get_resource_header()
        endpoint = "https://api.spotify.com/v1/search"
        lookup_url = f"{endpoint}?{query_params}"
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 299):  
            return {}
        return r.json()
    
    def search(self, query=None, operator=None, operator_query=None, search_type='artist' ):
        if query == None:
            raise Exception("A query is required")
        if isinstance(query, dict):
            query = " ".join([f"{k}:{v}" for k,v in query.items()])
        if operator != None and operator_query != None:
            if operator.lower() == "or" or operator.lower() == "not":
                operator = operator.upper()
                if isinstance(operator_query, str):
                    query = f"{query} {operator} {operator_query}"
        query_params = urlencode({"q": query, "type": search_type.lower()})
        print(query_params)
        return self.base_search(query_params)
    


# In[6]:


spotify = SpotifyAPI(client_id, client_secret)


# In[7]:


def get_data_album_to_CSV(self, _id):
    album_data = spotify.get_album(_id)
    album_data.keys()

    nameAlbum = album_data['name']
    artists = album_data['artists'][0]['name']
    total_tracks = album_data['total_tracks']
    artists_list = []
    album_list = []
    song_name_list = []
    songId_list = []
    popularity_list = []

    i=0
    while i<total_tracks:
        uri = album_data['tracks']['items'][i]['uri']
        uri = uri.replace('spotify:track:','')
        song_data = spotify.get_tracks(uri)
        song_name = song_data['name']
        popularity = song_data['popularity']
        artists_list.append(artists)
        album_list.append(nameAlbum)
        song_name_list.append(song_name)
        popularity_list.append(popularity)
        i+=1
        songId_list.append(i)
        

    final_data = list(zip(songId_list,album_list,artists_list,song_name_list,popularity_list))
    TituloCSV = "C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/AlbumData.CSV"
    Details = ["ID","Album","Artista","Cancion","Popularidad"]
    rows = final_data
    with open(TituloCSV,'w', newline='',encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerow(Details)
        write.writerows(rows)


# In[8]:


def get_data_playlist_to_CSV(self, _id):
    playlist_data = spotify.get_playlist(_id)
    tracks = playlist_data['tracks']
    items = tracks['items']

    id_list = []
    album_list = []
    song_list = []
    popularity_list = []
    artists_list = []

    i = 0
    for track in items:
        song = items[i]['track']['name']
        album = items[i]["track"]["album"]["name"]
        popularity = items[i]['track']['popularity']
        artists = [k["name"] for k in items[i]["track"]["artists"]]
        artists = ','.join(artists)
        album_list.append(album)
        song_list.append(song)
        popularity_list.append(popularity)
        artists_list.append(artists)
        i+=1
        id_list.append(i)

    final_data = list(zip(id_list,song_list,popularity_list,artists_list,album_list))
    TituloCSV = "C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/SongData.CSV"
    Details = ["ID","Cancion","Popularidad","Artistas","Album"]
    rows = final_data
    with open(TituloCSV,'w', newline='',encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerow(Details)
        write.writerows(rows)


# In[9]:


def get_data_artist_to_CSV(self, _id):
    # artists_ids = "768O5GliF0bqscyghggrbE,4yxLYO2imECxGYTTV7RQKb,2LRoIwlKmHjgvigdNGBHNo,7rOlQwf8OuFLFQp4aydjBt,3EiLUeyEcA6fbRPSHkG5kb,4q3ewBCX7sLwd24euuV69X,37230BxxYs9ksS7OkZw3IU,0Yg29FX1M4ayqjXs0ttZFq,5n9bMYfz9qss2VOW89EVs2,790FomKkXshlbRYZFtlgla,0EmeFodog0BfCgMzAIvKQp"
    artist_data = spotify.get_artist(_id)

    id_list = []
    name_list = []
    genres_list = []
    popularity_list = []
    followers_list = []
    artist = artist_data['artists']

    i=0
    for numbersOfArtists in artist:
        name = artist[i]['name']
        genres = artist[i]['genres']
        followers = artist[i]['followers']['total']
        popularity = artist[i]['popularity']
        name_list.append(name)
        genres_list.append(genres)
        followers_list.append(followers)
        popularity_list.append(popularity)
        i+=1
        id_list.append(i)

        final_data = list(zip(id_list,name_list,genres_list,followers_list,popularity_list))
        TituloCSV = "C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/ArtistData.CSV"
        Details = ["ID","NombreArtista","Generos","Followers","Popularidad"]
        rows = final_data
        with open(TituloCSV,'w', newline='',encoding='utf-8') as f:
            write = csv.writer(f)
            write.writerow(Details)
            write.writerows(rows)


# In[ ]:


# spotify.search(query="Danger", operator='NOT', operator_query='Zone', search_type="track")


# In[ ]:


# spotify.search(query="Danger Zone", search_type="track")


# In[ ]:


# spotify.search({"track": "Time"}, search_type="track")


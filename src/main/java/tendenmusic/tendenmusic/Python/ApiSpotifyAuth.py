#!/usr/bin/env python
# coding: utf-8

# In[2]:


import base64
import requests
import datetime


# In[3]:


client_id="6027cd821062416aa63f349653ccab78"
client_secret="e4e461cd9b5d426b97c231d433ec020e"


# In[4]:


# do a lookup for a token
# this token is for future requests


# In[5]:


client_creds = f"{client_id}:{client_secret}"
type(client_creds)


# In[6]:


client_creds_b64 = base64.b64encode(client_creds.encode())
type(client_creds_b64)


# In[7]:


#base64.b64decode(client_creds_b64)


# In[8]:


token_url="https://accounts.spotify.com/api/token"
method="POST"
token_data = {
    "grant_type": "client_credentials"
}
token_headers = {
    "Authorization" : f"Basic {client_creds_b64.decode()}" # <base64 encoded client_id:client_secret>
}
token_headers


# In[9]:


r = requests.post(token_url, data=token_data, headers=token_headers)
print(r.json())
valid_request = r.status_code in range(200,299)


# In[10]:


if valid_request:
    token_response_data = r.json()
    now = datetime.datetime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in']
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now
    print('Conexión API Spotify Exitosa')


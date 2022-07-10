#!/usr/bin/env python
# coding: utf-8

# In[2]:


from operator import contains
from turtle import pd
from typing_extensions import Self
from fpdf import FPDF
import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns


# In[48]:


def graphSongData():
    dataSong = pd.read_csv("DataDir/SongData.CSV")
    datagraph = sns.catplot(x='Popularidad',y='Cancion',data=dataSong,ci=None, height=10,aspect=1, kind="bar")
    datagraph.savefig("DataDir/graphs/SongData.png")


# In[33]:


def graphAlbumData():
    dataAlbum = pd.read_csv("DataDir/AlbumData.CSV")
    albumTitle = dataAlbum.iloc[1][1]
    artistName = dataAlbum.iloc[1][2]
    datagraph = sns.catplot(x='Popularidad',y='Cancion',data=dataAlbum,ci=None, height=5,aspect=2, kind="bar").set(title='Album: '+albumTitle+' by '+artistName)
    datagraph.savefig("DataDir/graphs/AlbumData.png")


# In[ ]:


def graphArtistData():
    dataArtist = pd.read_csv("DataDir/ArtistData.CSV")
    artistPopularity = sns.catplot(x='Popularidad',y='NombreArtista',data=dataArtist,ci=None, height=5,aspect=2, kind="bar").set(title='Artistas Influyentes')

    artistFollowing = sns.catplot(x='Followers',y='NombreArtista',data=dataArtist,ci=None, height=5,aspect=8, kind="bar").set(title='Seguidores')

    densityPopulFollow = sns.displot(dataArtist, x="Followers",y='Popularidad', kind="kde",height=10).set(title='Densidad entre Popularidad y Seguidores')

    artistPopularity.savefig("DataDir/graphs/ArtistPopularity.png")
    artistFollowing.savefig("DataDir/graphs/ArtistFollowers.png")
    densityPopulFollow.savefig("DataDir/graphs/densityPopularityFollowing.png")


# In[72]:





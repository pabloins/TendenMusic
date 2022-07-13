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
import logging

# In[48]:

logging.basicConfig(level=logging.INFO)
logging.info("Generando Graficos")


def graphSongData():
    dataSong = pd.read_csv("C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/SongData.CSV")
    datagraph = sns.catplot(x='Popularidad',y='Cancion',data=dataSong,ci=None, height=10,aspect=1, kind="bar")
    datagraph.savefig("C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/graphs/SongData.png")
    logging.info("Grafico SongData Generado")


# In[33]:


def graphAlbumData():
    dataAlbum = pd.read_csv("C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/AlbumData.CSV")
    albumTitle = dataAlbum.iloc[1][1]
    artistName = dataAlbum.iloc[1][2]
    datagraph = sns.catplot(x='Popularidad',y='Cancion',data=dataAlbum,ci=None, height=5,aspect=2, kind="bar").set(title='Album: '+albumTitle+' by '+artistName)
    datagraph.savefig("C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/graphs/AlbumData.png")
    logging.info("Grafico AlbumData Generado")
    

# In[ ]:


def graphArtistData():
    dataArtist = pd.read_csv("C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/ArtistData.CSV")
    artistPopularity = sns.catplot(x='Popularidad',y='NombreArtista',data=dataArtist,ci=None, height=5,aspect=2, kind="bar").set(title='Artistas Influyentes')

    artistFollowing = sns.catplot(x='Followers',y='NombreArtista',data=dataArtist,ci=None, height=5,aspect=8, kind="bar").set(title='Seguidores')

    densityPopulFollow = sns.displot(dataArtist, x="Followers",y='Popularidad', kind="kde",height=10).set(title='Densidad entre Popularidad y Seguidores')

    artistPopularity.savefig("C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/graphs/ArtistPopularity.png")
    logging.info("Grafico ArtistPopularity Generado")
    artistFollowing.savefig("C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/graphs/ArtistFollowers.png")
    logging.info("Grafico ArtistFollowers Generado")    
    densityPopulFollow.savefig("C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/graphs/densityPopularityFollowing.png")
    logging.info("Grafico FollowerPopularityDensity Generado")


# In[72]:





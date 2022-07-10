from operator import contains, ge
from turtle import pd
from typing_extensions import Self
from fpdf import FPDF
from matplotlib import artist
import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import ApiSpotifyGetData
import MakeGraphs

get_data = ApiSpotifyGetData
get_data.get_data_playlist_to_CSV(Self,'37i9dQZEVXbL0GavIqMTeb')
artists_ids = "768O5GliF0bqscyghggrbE,4yxLYO2imECxGYTTV7RQKb,2LRoIwlKmHjgvigdNGBHNo,7rOlQwf8OuFLFQp4aydjBt,3EiLUeyEcA6fbRPSHkG5kb,4q3ewBCX7sLwd24euuV69X,37230BxxYs9ksS7OkZw3IU,0Yg29FX1M4ayqjXs0ttZFq,5n9bMYfz9qss2VOW89EVs2,790FomKkXshlbRYZFtlgla,0EmeFodog0BfCgMzAIvKQp"
get_data.get_data_album_to_CSV(Self,'3RQQmkQEvNCY4prGKE6oc5')
get_data.get_data_artist_to_CSV(Self,artists_ids)

graphing = MakeGraphs
graphing.graphAlbumData()
graphing.graphArtistData()
graphing.graphSongData()

title = 'Reporte TendenMusic'

class PDF(FPDF):
    def header(self):
        # Fuente: Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculo del ancho del titulo y posición
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colores del frame, fondo y el texto
        self.set_draw_color(0, 0, 0)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(0, 0, 0)
        # Borde de frame (1 mm)
        self.set_line_width(1)
        # Titulo
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Salto de Linea
        self.ln(10)

    def footer(self):
        # Posicion es 1.5 cm desde el fondo (Y)
        self.set_y(-15)
        # Fuente: Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Color del texto in gris
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Fuente: Arial 12
        self.set_font('Arial', '', 12)
        # Color de Fondo
        self.set_fill_color(200, 220, 255)
        # Titulo
        self.cell(0, 6, 'Sección %d : %s' % (num, label), 5, 1, 'L', 1)
        # Salto de Linea
        self.ln(4)

    def chapter_body_file(self, name):
        # Leer archivo de texto
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Tamaño Fuente 12
        self.set_font('Times', '', 12)
        # Output Texto Justificado
        self.multi_cell(0, 5, txt)
        # Salto de Linea
        self.ln()
        # Mencion en italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def chapter_body(self, text):
        # Tamaño Fuente 12
        self.set_font('Times', '', 12)
        # Output Texto Justificado
        self.multi_cell(0, 5, text)
        # Salto de Linea
        self.ln()
        # Mencion en italics
        self.set_font('', 'I')
        # self.cell(0, 5, 'Fin Reporte')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)


pdf = PDF()
pdf.set_title(title)
pdf.set_author('UFRO')

pdf.print_chapter(1, 'Tendencia', 'A continuación se muestraran los graficos generados por el sistema con datos obtenidos de la API Spotify.')
pdf.chapter_title(2,'Graficos')
pdf.image('C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/SongData.png', x=10,y=60,w=200,h=130)
pdf.image('C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/AlbumData.png', x=20,y=190,w=160,h=90)
pdf.add_page()

pdf.image('C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/ArtistPopularity.png', x=20,y=20,w=160,h=90)
pdf.image('C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/ArtistFollowers.png', x=10,y=120,w=190,h=90)
pdf.add_page()

pdf.image('C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/densityPopularityFollowing.png', x=20,y=20,w=160,h=160)

pdf.output('C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/Reporte.pdf', 'F')
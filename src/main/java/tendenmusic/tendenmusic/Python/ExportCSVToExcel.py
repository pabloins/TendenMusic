from re import I
import pandas as pd
import glob
import sys
import datetime
import logging


logging.basicConfig(level=logging.INFO)

logging.info("Inicializando Proceso Exportación de Datos a Planilla")


now = datetime.datetime.now()
todaysDate = now.strftime("%d-%m-%y")

def export():

    path = "C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir/"
    filesCSV = glob.glob(path + "*.CSV")
    extension = todaysDate+'.xlsx'
    i=0
    for filename in filesCSV:
        CSVfile = filename
        read_file = pd.read_csv(CSVfile)
        CSVfile = CSVfile.replace('.CSV',extension)
        excelWriter = pd.ExcelWriter(CSVfile)
        read_file.to_excel(excelWriter, engine = 'openpyxl')
        logging.info("Planilla:" + str(CSVfile) + " Realizada")
        i=+1
        read_file = type(filename)
        excelWriter.save()

    logging.info("Proceso de Exportación Finalizado")
    


if __name__ == "__main__":
    export()


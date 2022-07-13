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

    path = "C:/Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/DataDir"
    filesCSV = glob.glob(path + "/*.CSV")
    extension = todaysDate+'.xlsx'

    for filename in filesCSV:
        
        read_file = pd.read_csv(filename,index_col=None)
        excelWriter = pd.ExcelWriter(filename.replace('.CSV',extension))
        read_file.to_excel(excelWriter, engine = 'openpyxl')
        logging.info("Planilla:" + str(filename) + "Realizada")

    excelWriter.save()
    logging.info("Proceso de Exportación Finalizado")

if __name__ == "__main__":
    export()


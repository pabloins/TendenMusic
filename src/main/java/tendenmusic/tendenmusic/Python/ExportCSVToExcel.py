import pandas as pd
import glob
import sys
import datetime

now = datetime.datetime.now()
todaysDate = now.strftime("%d-%m-%y")

def export():

    path = "DataDir"
    filesCSV = glob.glob(path + "/*.CSV")
    extension = todaysDate+'.xlsx'

    for filename in filesCSV:

        read_file = pd.read_csv(filename,index_col=None)
        excelWriter = pd.ExcelWriter(filename.replace('.CSV',extension))
        read_file.to_excel(excelWriter, engine = 'openpyxl')

    excelWriter.save()

if __name__ == "__main__":
    export()


import voting
import openpyxl
wb=openpyxl.load_workbook('C:/Users/EDGAR/OneDrive/Documentos/MSc Data Science and AI/COMP517/COMP517_Assignment3/voting.xlsx')
ws=wb.active



preferencia=voting.generatePreferences(ws)





lista=[alt for alt in range(1,len(preferencia)+1)]
lista.append('max')
lista.append('min')


res=[]
for item in range(1,len(preferencia)+1):
    res.append(voting.dictatorship(preferencia,item))

print(res)

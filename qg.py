import pyodbc

try:
    conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
except Exception as e:
    print("Erro na conexão:", e)
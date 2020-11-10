import pyodbc
server = 'iot-db-roijenga.database.windows.net'
database = 'iot-db-weather-roijenga'
username = 'iot-joeri-roijenga'
password = 'cO1WfBYif7eA'   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP (1000) * FROM [dbo].[dataweather]")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()

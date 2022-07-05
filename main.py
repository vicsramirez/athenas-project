import time
from datetime import datetime

from SeleniumClass import SeleniumClass
from O365Connect import O365Class


print(f"Iniciando la captura....")

format = '%Y-%m-%d'
fecha_consulta = datetime.now().strftime(format)
print("Consultando actividades para " + fecha_consulta)
O365Class.openConnection(fecha_consulta)

if O365Class.body != None:
    _activities = O365Class.parserResponse(O365Class.body)
    selenium = SeleniumClass()
    if len(_activities) > 0:
        selenium = SeleniumClass()
        for activitie in _activities:
            if selenium != None:
                selenium.captureTask(activitie)
                time.sleep(5)
        selenium.close()
        print(f"Termine de capturar {len(_activities)} actividades")
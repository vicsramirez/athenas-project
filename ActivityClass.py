import time
from datetime import datetime as dt
import re

class Activity:
    name = ""
    date = ""
    category = ""
    project = ""
    consultancy = ""
    description = ""
    horas = 0

  
        
    def __init__(self, data):

        now = dt.now()
        self.name = "Víctor Sánchez"
        self.date = now.strftime("%d/%m/%y")

        #
        # Sí la categoría de la actividad en el calendario es 402 es proyecto.
        #
        self.category = data["categories"][0] if re.search('^499[0-9]{4}-*',data["categories"][0]) != None  else "Implementación"

        print(self.category)
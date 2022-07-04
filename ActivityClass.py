from datetime import datetime
from datetime import timedelta
import re
from  CategoryClass import CategoryClass


class Activity:
    name = ""
    date = ""
    category = ""
    project = ""
    consultancy = ""
    description = ""
    horas = 0

    INTERNAL_ACTIVITY = "^499[0-9]{4}-*"
    PROJECT_THIS_YEAR = "^402[0-9]{4}-*"
    SOPORTE = "Soporte Interno Enter"
    ADMIN = "Administración"
    CONSULTANCY = "Consultoría"

    def __init__(self, data):

        now = datetime.now()
        self.name = "Víctor Sánchez"
        self.date = now.strftime("%d/%m/%y")

        #
        # Sí la categoría de la actividad en el calendario es 402 es proyecto.
        #
        _subject = data["subject"].strip()
        if re.search(Activity.PROJECT_THIS_YEAR,data["categories"][0]) != None:
            self.category = CategoryClass.IMPLEMENTACION
            self.project = re.search(Activity.PROJECT_THIS_YEAR,data["categories"][0]).group()
            self.consultancy = ""
        elif re.search(Activity.INTERNAL_ACTIVITY,data["categories"][0]) :
            self.category = CategoryClass.CONSULTORIA
            self.consultancy = re.search(Activity.INTERNAL_ACTIVITY,data["categories"][0]).group()
        if re.search("^INC[- ]",_subject) != None:
            self.category = CategoryClass.S_NIVEL
        elif re.search("^REQ[- ]",_subject) != None:
            self.category = CategoryClass.TICKET
            self.consultancy = ""
            self.project = ""
        elif re.search(Activity.INTERNAL_ACTIVITY,data["categories"][0]) != None and data["categories"][0] in CategoryClass.ADMIN_ACTIVITIES:
            self.category = CategoryClass.ADMINISTRACION
            self.project = re.search(Activity.PROJECT_THIS_YEAR,data["categories"][0]).group()
            self.consultancy = ""
        elif re.search(Activity.ADMIN, data["categories"][0]) != None:
            self.category = CategoryClass.ADMINISTRACION
        elif re.search(Activity.SOPORTE,data["categories"][0]) != None :
            self.category = CategoryClass.SOPORTE
            self.project = ""
            self.consultancy = ""
        elif re.search(Activity.CONSULTANCY,data["categories"][0]) != None :
            self.category = CategoryClass.CONSULTORIA
            self.project = ""
            self.consultancy = ""

        # Si la importancia de la tarea es menor se fue de apoypo
        if data["importance"] != "normal":
            self.category = CategoryClass.APOYO

        self.horas = self._calculateTime(data["start"],data["end"])
        self.description = data["subject"]

    def _calculateTime(self,start_t,end_t):
        format = '%Y-%m-%d %H:%M:%S'
        _timestart = start_t["dateTime"][0:start_t["dateTime"].find(".")].replace("T"," ")
        _timeend = end_t["dateTime"][0:end_t["dateTime"].find(".")].replace("T"," ")
        if start_t["timeZone"] == "UTC":
            _timestart = (datetime.strptime(_timestart,format)- timedelta(hours=5))
            _timeend = (datetime.strptime(_timeend,format)- timedelta(hours=5))
        return ((_timeend - _timestart).total_seconds() / (60 * 60) )

    def __str__(self):
        return f"{self.date:10} |{self.category}|{self.project}|{self.consultancy}|{self.description}|{self.horas}"


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from ActivityClass import Activity
import time
import configparser

class SeleniumClass:

    browser = None

    def openBrowser(self):
        service_object = Service(binary_path)
        self.browser = webdriver.Chrome(service=service_object)


    def captureTask(self,actividad: Activity):

        if self.browser == None:
            self.openBrowser()
        print("Continuando...")
        config = configparser.ConfigParser()
        config.read(['config.cfg'])
        smart_settings = config['smartsheet']
        print(smart_settings["url"])
        if smart_settings != None:
            if smart_settings != "" and smart_settings["url"] != None:
                print("Leyendo página.. " + smart_settings["url"])
                self.browser.get(smart_settings["url"])
                time.sleep(5)
        print(actividad)
        for box_path in ["xpath_name","xpath_date","xpath_category","xpath_project","xpath_consultancy","xpath_actividad","xpath_horas"]:
            box = self.browser.find_element(By.XPATH,smart_settings[box_path])
            if box_path == "xpath_name":
                box.send_keys(actividad.name)
            elif box_path == "xpath_date":
                box.send_keys(actividad.date)
            elif box_path == "xpath_category":
                box.send_keys(actividad.category)
            elif box_path == "xpath_project":
                box.send_keys(actividad.project)
            elif box_path == "xpath_consultancy":
                box.send_keys(actividad.consultancy)
            elif box_path == "xpath_actividad":
                box.send_keys(actividad.description)
            elif box_path == "xpath_horas":
                box.send_keys(actividad.horas)
            box.send_keys(Keys.TAB)

        remitir_box = self.browser.find_element(By.XPATH,smart_settings["xpath_submit"])
        remitir_box.submit()

    def close(self):
        self.browser.close()

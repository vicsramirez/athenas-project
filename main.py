from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path



import time

def main():
    service_object = Service(binary_path)
    chrome = webdriver.Chrome(service=service_object)
    print("Continuando...")
    chrome.get("https://app.smartsheet.com/b/form/f45cd2847d4749a8935336c2f14be061")
    name_box = chrome.find_element(By.XPATH,"/html/body/div[1]/div/div/div/section[2]/div/div/form/div[1]/div/div/div/div[1]/div[2]/div/input")
    name_box.send_keys("Víctor Sánchez")
    name_box.send_keys(Keys.TAB)


    fecha_box = chrome.find_element(By.XPATH,"/html/body/div[1]/div/div/div/section[2]/div/div/form/div[2]/div/div/input")
    fecha_box.send_keys("27/06/2022")

    categoria_box = chrome.find_element(By.XPATH,"/html/body/div[1]/div/div/div/section[2]/div/div/form/div[3]/div/div/div/div[1]/div[2]/div/input")
    categoria_box.send_keys("Implementación")
    categoria_box.send_keys(Keys.TAB)

    proyecto_box = chrome.find_element(By.XPATH,"/html/body/div[1]/div/div/div/section[2]/div/div/form/div[4]/div/div/div/div[1]/div[2]/div/input")
    proyecto_box.send_keys("4020227")
    proyecto_box.send_keys(Keys.TAB)

    actividad_box = chrome.find_element(By.XPATH,"/html/body/div[1]/div/div/div/section[2]/div/div/form/div[6]/div/div[2]/input")
    actividad_box.send_keys("Revisión interna Proyecto AGP - Servidor Lenovo")

    horas_box = chrome.find_element(By.XPATH,"/html/body/div[1]/div/div/div/section[2]/div/div/form/div[7]/div/div[2]/input")
    horas_box.send_keys("1")

    remitir_box = chrome.find_element(By.XPATH,"/html/body/div[1]/div/div/div/section[2]/div/div/form/div[9]/button")
    remitir_box.submit()

    time.sleep(5)
main()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
import time
import pandas as pd

def parseImgSize(text):
    return (text.split("<img")[0], text.split(">")[-1])

options = Options()
options.add_argument('--disable-gpu')

chromedriver_path = 'wayOfChromedriverOnYourPC/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
driver.get('https://webspeedtest.cloudinary.com/')

testid = 'yourEntirePageLink'
input_element = driver.find_element(By.NAME, 'testid').send_keys(testid)

button_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/form/button')
button_element.click()

for i in tqdm(range(90)):
    time.sleep(1)

gradesElements = driver.find_elements(By.XPATH, "//*[contains(@class, 'image-data-grading grade')]")
grades = [letter.text for letter in gradesElements]

imgElements = driver.find_elements(By.XPATH, "//*[contains(@class, 'image-data-name')]")
imgNames = [name.text for name in imgElements] 

linkElements = driver.find_elements(By.XPATH,"//*[contains(@class, 'image-orig image')]//img")
linkImgs = [img.get_attribute("src") for img in linkElements]

imgsSizeElements = driver.find_elements(By.XPATH, "//*//div[contains(@class, 'image-final-pixel')]")
imgsSize = [parseImgSize(sizes.get_attribute("innerHTML")) for sizes in imgsSizeElements]

elements= {
    'Notas': grades,
    'Nome Imgs': imgNames,
    'Links': linkImgs,
    'Tamanho atual': [imgSize[0] for imgSize in imgsSize],
    'Tamanho ideal': [imgSize[1] for imgSize in imgsSize]
}
print('----------------------------')
print('Teste em:', testid)
print('Grade Array Contains:', (len(grades)), 'itens')
print('Images Name Contains:', (len(imgNames)), 'itens')
print('Images Links Contais:', (len(linkImgs)), 'itens')
print('Images Sizes Contains:', (len(imgsSize)), 'itens')
table = pd.DataFrame(data = elements)
table.to_csv('nameYourTable.csv', index=False)
print(table)
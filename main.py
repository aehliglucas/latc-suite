from selenium import webdriver
from chromedriver_py import binary_path
import json

stationsFile = open('stations.json')
stations = json.load(stationsFile)

radioDriver = webdriver.Chrome(executable_path=binary_path)

for s in stations:
    print(s)
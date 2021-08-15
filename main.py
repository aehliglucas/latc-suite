from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
from webdriver_manager.chrome import ChromeDriverManager
import logging
import json

seleniumLogger.setLevel(logging.WARNING)
options = Options()
adsbOptions = Options()
options.add_argument("--headless")
adsbOptions.add_argument("--start-maximized")
settingsFile = open('settings.json')
settings = json.load(settingsFile)

radioDriver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
adsbDriver = webdriver.Chrome(ChromeDriverManager().install(), options=adsbOptions)

# Audio session creation
i = 0
while True:

    s = settings['liveatc'][0]['stations'][i]
    radioDriver.get("https://www.liveatc.net/hlisten.php?mount=" + s + "&icao=" + settings['liveatc'][0]['airport_icao'])
    radioDriver.find_element_by_xpath("//*[@id='mep_0']/div/div[3]/div[1]/button").click()

    if i > 0:
        radioDriver.execute_script("window.open('about:blank', 'tab" + str(chr(i)) + "')")
        radioDriver.switch_to.window("tab" + str(chr(i)))

    radioDriver.get("https://www.liveatc.net/hlisten.php?mount=" + settings['liveatc'][0]['stations'][i] + "&icao=" + settings['liveatc'][0]['airport_icao'])
    print("Created audio session for " + settings['liveatc'][0]['stations'][i])

    if i + 1 == len(settings['liveatc'][0]['stations']):
        break

    i = i + 1


adsbDriver.get("https://globe.adsbexchange.com/?lat=" + settings['adsbexchange'][0]['lat'] + "&lon=" + settings['adsbexchange'][0]['lon'] + "&zoom=" + settings['adsbexchange'][0]['zoom'])
# 5 Feladat: Bingo

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html")

# tesztadatok


# gomb és beviteli mező definíciók
spin = driver.find_element_by_id('spin')
init = driver.find_element_by_id('init')


def play_button():
    """ play gomg nyomogatása """
    spin.click()


def check_bingo():
    """ bingo felirat ellenőrzése """
    bingo = driver.find_elements_by_xpath('//*[@id="messages"]')
    print(len(bingo))
    while len(bingo) == 0:
        bingo = driver.find_elements_by_xpath('//*[@id="messages"]')
        play_button()


# TC1: Az applikáció helyesen megjelenik:
# A bingo tábla 25 darab cellát tartalmaz
# A számlista 75 számot tartalmaz
def test_TC1_number_elements():
    """ játéktábla elemek számolása"""
    assert len(driver.find_elements_by_xpath('//input[@name="number"]')) == 25
    assert len(driver.find_elements_by_xpath('//ol/li')) == 75


# TC2: Bingo számok ellenőzrzése:
# Addig nyomjuk a play gobot amíg az első bingo felirat meg nem jelenik
# Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki
def test_TC2_check_bingo():
    check_bingo()


# TC3: Új játékot tudunk indítani
# az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
# új bingo szelvényt kapunk más számokkal.
def test_TC3_init():
    init.click()

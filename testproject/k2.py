# 2 Feladat: Színes reakció

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html")

# tesztadatok
result_msg = ['Incorrect!', 'Correct!']

# gomb és beviteli mező definíciók
start = driver.find_element_by_id('start')
stop = driver.find_element_by_id('stop')
allcolors = driver.find_element_by_id('allcolors')
randomColorName = driver.find_element_by_id('randomColorName')
randomColor = driver.find_element_by_id('randomColor')
testColorName = driver.find_element_by_id('testColorName')
testColor = driver.find_element_by_id('testColor')
result = driver.find_element_by_id('result')


def check_color():
    """ szín ellenőrzése """
    if randomColorName.text == testColorName.text:
        assert result.text == result_msg[1]
    else:
        assert result.text == result_msg[0]


def start_stop():
    """ játék indítása"""
    start.click()
    time.sleep(0.1)
    stop.click()


# TC1: Helyesen jelenik meg az applikáció betöltéskor:
# Alapból egy random kiválasztott szín jelenik meg az == bal oldalanán.
# A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ]
def test_TC1_startpage_check():
    """ applikáció megjelenés ellenőrzése """
    assert randomColorName.text in allcolors.text
    assert testColorName.text == ''


# TC2: El lehet indítani a játékot a start gommbal.
# Ha elindult a játék akkor a stop gombbal le lehet állítani.
def test_TC2_start_stop():
    """ start-stop változást hoz """
    start_stop()
    assert not testColorName.text == ''


# TC3: Eltaláltam, vagy nem találtam el.
# Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le amikor a bal és
# a jobb oldal ugyan azt a színt tartalmazza akkor a Correct! felirat jelenik meg.
# ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az Incorrect! felirat kell megjelenjen.
def test_TC3_correct_work():
    """ kiértékelés ellenőrzése """
    for i in range(100):
        start_stop()
        check_color()

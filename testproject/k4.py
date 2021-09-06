# 4 Feladat: Műveletek karakterekkel

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html")

# tesztadatok
op = ['-', '+']

# gomb és beviteli mező definíciók
ascii_text = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
ascii_table = driver.find_element_by_xpath('//div/div/p[3]')
chr_field = driver.find_element_by_id('chr')
op_field = driver.find_element_by_id('op')
num_field = driver.find_element_by_id('num')
button = driver.find_element_by_id('submit')
result = driver.find_element_by_id('result')


# TC1:Helyesen betöltődik az applikáció:
# Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~
def test_TC1_correct_loading():
    print(ascii_table.text)
    assert ascii_table.text == ascii_text


# TC2: Megjelenik egy érvényes művelet:
# chr megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
# op mező vagy + vagy - karaktert tartlamaz
# num mező egy egész számot tartalamaz
def test_TC2_correct_operating():
    assert chr_field.text in ascii_text
    assert op_field.text in op
    # assert isinstance(num_field, int)

# TC3: Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
# A megjelenő chr mezőben lévő karaktert kikeresve a táblában
# Ha a + művelet jelenik meg akkor balra lépve ha a - akkor jobbra lépve
# A num mezőben megjelenő mennyiségű karaktert
# az result mező helyes karaktert fog mutatni

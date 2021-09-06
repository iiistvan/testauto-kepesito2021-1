# 3 Feladat: Alfanumerikus mező

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html")

# tesztadatok
testdata = ['abcd1234', 'teszt233@', 'abcd']
error_msg = [0, 'Only a-z and 0-9 characters allewed', 'Title should be at least 8 characters']

# gomb és beviteli mező definíciók
input = driver.find_element_by_id('title')
error_fields = driver.find_elements_by_class_name('error.active')
span = driver.find_element_by_tag_name('span')


def data_fill(data):
    """ adattörlés és adatbetöltés"""
    input.clear()
    input.send_keys(data)


# TC1: Helyes kitöltés esete:
# title: abcd1234
# Nincs validációs hibazüzenet
def test_TC1_correct_fill():
    data_fill(testdata[0])
    assert len(error_fields) == 0


# TC2: Illegális karakterek esete:
# title: teszt233@
# Only a-z and 0-9 characters allewed.
def test_TC2_illegagal_char():
    data_fill(testdata[1])
    time.sleep(1)
    assert span.text == error_msg[1]


# TC3: Tul rövid bemenet esete:
# title: abcd
# Title should be at least 8 characters; you entered 4.
def test_TC3_short_data():
    data_fill(testdata[2])
    time.sleep(1)
    assert error_msg[2] in span.text

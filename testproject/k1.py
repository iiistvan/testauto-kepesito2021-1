# 1 Feladat: Pitagorasz-tétel

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html")

# tesztadatok
test_data = [[2, 3, 10], ['', '', 'NaN']]

# gomb és beviteli mező definíciók
a = driver.find_element_by_id('a')
b = driver.find_element_by_id('b')


def refresh_field_url():
    driver.refresh()
    time.sleep(1)
    a = driver.find_element_by_id('a')
    b = driver.find_element_by_id('b')
    kalk = driver.find_element_by_id('submit')


def fill_data(testdata):
    driver.refresh()
    print(testdata)
    a.send_keys(testdata[0])
    b.send_keys(testdata[1])
    kalk.click()


def check_data(testdata_c):
    result = driver.find_elements_by_id('result')
    assert result.text == str(testdata_c)


# TC1: Induló állapot:
def test_TC1_starting():
    assert a.text == ''
    assert b.text == ''
    assert not driver.find_element_by_id('result').is_displayed()


# TC2: Számítás helyes, megfelelő bemenettel
# a: 2
# b: 3
# c: 10
# def test_TC2_correct_data():
    # fill_data(test_data[0])
    # check_data(test_data[0][2])



# # TC3: Üres kitöltés
# a: <üres>
# b: <üres>
# c: NaN

# def test_TC3_empty_data():
#     fill_data(test_data[1])
#     check_data(test_data[1][2])

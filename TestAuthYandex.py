from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from ynd_creds import LOGIN, PASS
import time
URL = 'https://passport.yandex.ru/auth/'


def test_login(url, login, password):
    """
    Tries to authenticate in Yandex.Passport
    :param url: URL for Yandex.Passport
    :param login: User login
    :param password: User password
    :return: Status of an attempt
    """
    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    try:
        assert "Авторизация" in driver.title
    except AssertionError:
        return 'Invalid URL'
    elem = driver.find_element(By.NAME, "login")
    time.sleep(1)
    elem.send_keys(login)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    try:
        assert driver.current_url == 'https://passport.yandex.ru/auth/welcome'
    except AssertionError:
        return 'Invalid login'
    time.sleep(2)
    pass_window = driver.find_element(By.NAME, 'passwd')
    time.sleep(1)
    pass_window.send_keys(password)
    pass_window.send_keys(Keys.RETURN)
    time.sleep(2)
    try:
        assert driver.current_url != 'https://passport.yandex.ru/auth/welcome'
    except AssertionError:
        return 'Invalid password'
    driver.close()
    driver.quit()
    return 'Success'


def main():
    data = [
        [URL, LOGIN, PASS],
        ['https://google.com', LOGIN, PASS],
        [URL, '_sdad', '123'],
        [URL, 'python', '123']
    ]
    for try_num, creds in enumerate(data):
        print(f'\nAttempt number {try_num + 1}:')
        result = test_login(creds[0], creds[1], creds[2])
        print('Result:', result)
        print('_' * 50)


if __name__ == '__main__':
    main()

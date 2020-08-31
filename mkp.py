import os
import sys
import time
from selenium import webdriver
from id import username, password


def login(projectName):
    browser = webdriver.Firefox()
    time.sleep(.01)
    browser.get('https://github.com/login')

    login_username = browser.find_element_by_xpath('//*[@id="login_field"]')
    login_password = browser.find_element_by_xpath('//*[@id="password"]')
    login_button = browser.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]')

    login_username.send_keys(username)
    login_password.send_keys(password)
    login_button.click()

    browser.get('https://github.com/new')
    repo = browser.find_element_by_xpath('//*[@id="repository_name"]')
    repo.send_keys(projectName)

    create_repo = browser.find_element_by_css_selector('button.first-in-line')
    create_repo.submit()
    time.sleep(.5)
    browser.quit()

def create(directory):
    '''Create new folder in the projects directory.'''

    parent_dir = '/home/charles/Coding/Projets'
    path = os.path.join(parent_dir, directory)

    try:
        os.mkdir(path)
    except OSError as error:
        print(error)

def check():
    try:
        directory = str(sys.argv[1])
        print('Génération...')
        login(directory)
        create(directory)
    except IndexError:
        print('Veuillez saisir un nom de projet.')

if __name__ == '__main__':
    check()


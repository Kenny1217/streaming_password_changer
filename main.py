import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def f_change_netflix_pwd(email, password):
    print('Changing Netflix Password')
    new_password=""
    netflix_login_url = "https://www.netflix.com/login"
    print("Going to " + netflix_login_url)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(netflix_login_url)
    driver.find_element(By.ID,'id_userLoginId').send_keys(email)
    driver.find_element(By.ID,'id_password').send_keys(password)
    submit = driver.find_element(By.CLASS_NAME,"login-button")
    submit.click()
    time.sleep(5)
    driver.get("https://www.netflix.com/password")
    driver.find_element(By.ID,'id_currentPassword').send_keys(password)
    driver.find_element(By.ID,'id_newPassword').send_keys(new_password)
    driver.find_element(By.ID,'id_confirmNewPassword').send_keys(new_password)
    submit2 = driver.find_element(By.ID,"btn-save")
    submit2.click()
    time.sleep(25)
    driver.quit()

def f_change_disney_pwd(email, password):
    print('Changing Disney Password')
    new_password=""
    disney_login_url = "https://www.disneyplus.com/login"
    print("Going to " + disney_login_url)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(disney_login_url)
    driver.find_element(By.ID,'email').send_keys(email)
    submit = driver.find_element(By.NAME,'dssLoginSubmit')
    submit.click()
    time.sleep(5)








def f_change_hbo_pwd():
    print('Changing HBO Password')

def f_change_peacock_pwd():
    print('Changing Peacock Password')

def f_change_hulu_pwd():
    print('Changing Hulu Password')

def f_change_paramount_pwd():
    print('Changing Paramount Password')

def f_change_discovery_pwd():
    print('Changing discovery Password')




def main():
    print("Running script...")
    #f_change_netflix_pwd("", "")

    print("DONE!")



 
if __name__ == "__main__":
    main()
 






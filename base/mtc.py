import time

import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager

driver = uc.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://nowsecure.nl/')
time.sleep(300)
driver.quit()
print("Program Ended")
#
# def add_account(number):
#
#     driver = uc.Chrome()
#     driver.get(f'https://login.mts.ru/amserver/UI/Login')
#     time.sleep(100)


# add_account(123132)

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://en.wikipedia.org/wiki/Wiki/')
#If it is not immediate available then it should wait maximum 10 sec
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


title=driver.find_element(By.XPATH,'//span[@class="mw-page-title-main"]')
print(title.text)

driver.close()
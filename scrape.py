from bs4 import BeautifulSoup
import requests
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# user=requests.get('https://twitter.com/Pegalo0/following')
# soup = BeautifulSoup(user.text,features="html.parser")
# # print(soup)
# spans = soup.find_all('div', {'class' : 'css-1dbjc4n r-18u37iz'})
#
# # spans = soup.find_all('span', {'class' : 'css-901oao css-16my406 r-1k78y06 r-ad9z0x r-bcqeeo r-qvutc0'})
# print(spans)
# lines = [span.get_text() for span in spans]
# print(lines)

driver = webdriver.Chrome(executable_path=r'C:\Users\Asus\Desktop\chromedriver.exe')
# driver.maximize_window()
driver.get('https://twitter.com/Godookhak')

# c = driver.page_source
# soup = BeautifulSoup(c, "html.parser")
# alii=driver.find_element_by_class_name('css-901oao css-16my406 r-1k78y06 r-ad9z0x r-bcqeeo r-qvutc0').text

# ali = driver.find_element_by_xpath("//*[contains(text(), 'AghaFariid')]")
# driver.implicitly_wait(150)
# print(WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,"//h1[@data-test='seller_name']/following::p[@data-test='seller_active']"))).text)

date = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "////*[@class='css-901oao css-16my406 r-1k78y06 r-ad9z0x r-bcqeeo r-qvutc0']")))
print(date.gettext())
driver.quit()



from selenium import webdriver
from time import sleep 
import requests

driver = webdriver.Chrome()
driver.get("https://ssb.ua.edu/pls/PROD/bwskfreg.P_AltPin")

#login
driver.find_element_by_xpath('//input[@id="UserID"]').send_keys("jlbalthasar")
driver.find_element_by_xpath('//input[@id="PIN"]').send_keys("Tennispro89!")
driver.find_element_by_xpath('//input[@type="submit"]').click()

#Get to add and drop
driver.get("https://ssb.ua.edu/pls/PROD/bwskflib.P_SelDefTerm?calling_proc_name=bwskfreg.P_AltPin")
driver.find_element_by_xpath("/html/body/div[3]/form/input").click()

driver.find_element_by_xpath("/html/body/div[3]/form/input[20]").click()


driver.find_element_by_xpath('//*[@id="subj_id"]/option[42]').click()

#Go to my class
driver.find_element_by_xpath('/html/body/div[3]/form/input[108]').click()
driver.find_element_by_xpath('/html/body/div[3]/table[2]/tbody/tr[3]/td[3]/form/input[122]').click()

value = driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[5]/td[1]/abbr').text
print(value)

if(value == "C"):
    print("not worth")
else:
    requests.post("https://maker.ifttt.com/trigger/jack/with/key/lmRrnJJWM7oHvMkAuqiYQSFUzA9vGGXET77e6igrvy4")


sleep(5)
#driver.quit()
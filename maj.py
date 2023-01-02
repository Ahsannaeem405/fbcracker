import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')  # to open the chromebrowser
driver.get("https://m.facebook.com/")
driver.maximize_window()


# In[117]:


loginId = "ahsan.naeem.9484"


# In[118]:


my_password = "Raptor11122@@"


# In[119]:


user_name = driver.find_element(By.XPATH,"//input[@type='text']")
user_name.send_keys("cosmosic19@gmail.com")

password = driver.find_element(By.XPATH,"//input[@placeholder='Password']")
password.send_keys(my_password)


# In[120]:


log_in_button = driver.find_element(By.XPATH,"//button[@name='login']")
log_in_button.click()

save_button = driver.find_element(By.XPATH,"//span[text()='OK']")
save_button.click()


# In[121]:


my_profile = driver.find_element(By.XPATH,"//span[text()='Saad Ejaz']")
my_profile.click()
sleep(3)



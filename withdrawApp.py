from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
import time


# Create driver
driver = webdriver.Chrome(executable_path = "./chromedriver")

# Open website
driver.get("https://northeastern-csm.symplicity.com/students/?signin_tab=0")

studentLoginBtn = driver.find_element_by_css_selector("input")
studentLoginBtn.click()

# User enters input, wait for 20 seconds
time.sleep(20)
driver.get("https://northeastern-csm.symplicity.com/students/index.php?s=jobs&ss=applied&mode=list&subtab=nocr")

# driver.maximize_window()

def cancelEachApp():
    try:
        time.sleep(5)
        withdrawBtn = driver.find_element_by_css_selector("a[onclick*='confirmWithdraw']")
        driver.execute_script("arguments[0].click();", withdrawBtn)
        # Accept alert
        Alert(driver).accept()
        # Recur
        cancelEachApp()
    except NoSuchElementException:
        pass

        
def turnPage():
    time.sleep(3)
    nextBtn = driver.find_element_by_css_selector("a.btn.btn_default.lst-next-btn")
    driver.execute_script("arguments[0].click();", nextBtn)


while driver.find_element_by_css_selector("a.btn.btn_default.lst-next-btn").is_enabled():
    print(driver.find_element_by_css_selector("a.btn.btn_default.lst-next-btn").is_enabled())
    cancelEachApp()
    turnPage()

print("All available applications are removed from NUworks.")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
from openai import OpenAI


with open("apikey.txt", "r") as file:
    api_key = file.read().strip()
if api_key:
    print("Open API key found: " + api_key)
else:
    print ("API Key not found!")
client = OpenAI(api_key)

driver = webdriver.Chrome()
url = "https://server.thecoderschool.com/thegames/results.php?game_id=B2F502ESNAKET&results_code_id=1&showall"
counter = 0
login_flag = False
print("im looking :o")

while True:
    driver.get(url)
    time.sleep(0.1)

    if login_flag == False:
        time.sleep(6)
        login_flag = True
    
    try:
        unscored_links = driver.find_elements(By.XPATH, "//div[contains(text(),'Unscored Games')]/following-sibling::a")
        if unscored_links:
            for link in unscored_links:
                link_text = link.text.lower()
                if "currently being scored by" not in link_text:
                    href = link.get_attribute("href")
                    if href and "score.php?game_id=" in href and "team_id=" in href:
                        print("I found! :D")
                        print(f"unscored game link: {href}")
                        driver.execute_script("window.open(arguments[0], '_blank');", href)
                        counter += 1
                        with open("graded.txt", "w") as file:
                                file.write(str(counter))
                        time.sleep(1)
                        input("keep looking? :]")
                        driver.switch_to.window(driver.window_handles[0])
                        print("back to looking :o")
                        break

    except Exception as e:
        print("brokey :( ->", e)
driver.quit()
    

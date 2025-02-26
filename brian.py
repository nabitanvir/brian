from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://server.thecoderschool.com/thegames/results.php?game_id=B2F502ESNAKET&results_code_id=1&showall"

print("its brian time")

login = False

while True:
    driver.get(url)
    time.sleep(0.2)  # allow page to load

    if login == False:
        time.sleep(7)
        login = True
    
    try:
        unscored_links = driver.find_elements(
            By.XPATH,
            "//div[contains(text(),'Unscored Games')]/following-sibling::a"
        )
        
        if unscored_links:
            for link in unscored_links:
                href = link.get_attribute("href")
                if href and "score.php?game_id=" in href and "team_id=" in href:
                    print(f"Found unscored game link: {href}")
                    link.click()
                    print("Clicked the unscored game link!")
                    time.sleep(1)
        else:
            print("No unscored games found.")
    except Exception as e:
        print("Error while processing unscored games:", e)

driver.quit()

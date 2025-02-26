from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://server.thecoderschool.com/thegames/results.php?game_id=B2F502ESNAKET&results_code_id=1&showall"
counter = 0

print("im about to brian everywhere")
login = False

while True:
    driver.get(url)
    time.sleep(0.2)

    if login == False:
        time.sleep(7)
        login = True
    
    try:
        unscored_links = driver.find_elements(By.XPATH, "//div[contains(text(),'Unscored Games')]/following-sibling::a")
        
        if unscored_links:
            for link in unscored_links:
                link_text = link.text.lower()
                if "currently being scored by" not in link_text:
                    href = link.get_attribute("href")
                    if href and "score.php?game_id=" in href and "team_id=" in href:
                        print(f"unscored game link: {href}")
                        link.click()
                        counter += 1
                        print("i brianed")
                        with open("graded.txt", "w") as file:
                                file.write(str(counter))
                        time.sleep(1)

    except Exception as e:
        print("Error while processing unscored games:", e)
driver.quit()
    

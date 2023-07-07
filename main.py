from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import re

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(5)

query = "Python"

browser.get("https://wikipedia.org/")

search_input = browser.find_element(By.ID, "searchInput")
search_input.send_keys(query)

suggestions = browser.find_elements(By.CLASS_NAME, 'suggestion-link')
assert len(suggestions) > 0

for suggestion in suggestions:
    title_element = suggestion.find_element(
        By.CLASS_NAME, 'suggestion-highlight')
    assert re.search(query, title_element.text)

suggestions[0].click()
assert re.search(query, browser.current_url)

page_heading = browser.find_element(By.ID, "firstHeading")
assert re.search(query, page_heading.text)

print("tests passed")
browser.quit()
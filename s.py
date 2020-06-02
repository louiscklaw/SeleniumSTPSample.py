from selenium import webdriver

driver = webdriver.Safari()
driver.get('http://example.selenium.jp/reserveApp/')
driver.save_screenshot("screenshots/exampleseleniumjp.png")
driver.quit()

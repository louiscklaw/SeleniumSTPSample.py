from selenium import webdriver

driver = webdriver.Safari(executable_path='/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver')
driver.get('http://example.selenium.jp/reserveApp/')
driver.quit()

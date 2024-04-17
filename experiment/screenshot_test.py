from selenium import webdriver

# Launch a browser
driver = webdriver.Chrome()  # You need to have Chrome webdriver installed

# Open a webpage
driver.get("https://www.instagram.com")

# Take a screenshot of the current window
driver.save_screenshot("screenshot.png")

# Close the browser
driver.quit()

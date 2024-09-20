from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Taking input from user 
search_string = input("Input the URL or string you want to search for:") 

# This is done to structure the string 
# into search url.(This can be ignored) 
search_string = search_string.replace(' ', '+') 

# Provide the absolute path to the chromedriver executable
service = Service('C:\Program Files\Google\Chrome\Application\chrome.exe')  # Update this path to the correct location of your chromedriver
browser = webdriver.Chrome(service=service)

for i in range(1): 
    browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))

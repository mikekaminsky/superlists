from selenium import webdriver

# Must have firefox installed in applications
# use `cd /Applications && ln -s ~/Applications/Firefox.app` if firefox is installed elsewhere

browser = webdriver.Firefox() 
browser.get('http://localhost:8000')

assert 'Django' in browser.title

from selenium import webdriver

print('Schoology Auto-Login')
print('Please enter your username:')
userName = input()
print('Please enter your password:')
userPass = input()

browser = webdriver.Firefox()
browser.get('http://schoology.com')

loginElem = browser.find_element_by_id('login-header')
loginElem.click()

emailElem = browser.find_element_by_id('edit-mail')
loginElem.send_keys(userName)

passwordElem = browser.find_element_by_id('edit-pass')
passwordElem.send_keys(userPass)
passwordElem.submit()

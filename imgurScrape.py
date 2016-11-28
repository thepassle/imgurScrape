import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


keywords = ["brexit"]
#trump, brexit

linkResults = []

for keyword in keywords:

	driver = webdriver.Chrome('/Users/Pascalschilp/Desktop/imgur/chromedriver')  # Optional argument, if not specified will search path.
	print "Initializing..."
	driver.get('http://www.imgur.com/');
	print "Opening..."
	time.sleep(1)
	search_box = driver.find_element_by_class_name('icon-search')
	search_box.click()
	time.sleep(1)

	search_box = driver.find_element_by_class_name('search')
	print "Sending "+str(keyword)+"..."
	search_box.send_keys(str(keyword))
	search_box.submit()
	time.sleep(2)
	#scroll down page and wait to load
	for i in range(2):
		print "Scrolling..."
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		print "Waiting..."
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		time.sleep(7)

	#find all posts
	for image in driver.find_elements_by_xpath("//a[@class='image-list-link']"):
	    linkResults.append(image.get_attribute('href'))
	
	time.sleep(2)

	print "\n\n\n ################################ \n\n\n"

	print "Initializing 2..."

	for link in linkResults:
		driver.get(link);

		for image in driver.find_elements_by_xpath('//img[@src]'):
		    print "'"+str(image.get_attribute('src'))+"',"

	linkResults = []

	print "\n\n\n ################################ \n\n\n"



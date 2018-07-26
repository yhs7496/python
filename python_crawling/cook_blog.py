from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')

try:
	driver.get('http://www.naver.com')
	print(driver.title)

	elem = driver.find_element_by_id('query')
	elem.clear()
	# clear()를 해주는 이유는 간혹 포털마다 검색어가 이미 입력되어 있는 경우가 있기 때문
	
	elem.send_keys('요리')
	elem.send_keys(Keys.RETURN)

	blogs = driver.find_element_by_class_name('_blogBase')
	blogs_list = blogs.find_elements_by_tag_name('li')
	# blogs_list 자료형은 list

	for post in blogs_list:
		post_title = post.find_element_by_class_name('sh_blog_title')	
		print(post_title.get_attribute('title'))
		print(post_title.get_attribute('href'))

except Exception as e:
	print(e)

finally:
	driver.close()	
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')

try:
	driver.get('http://www.naver.com')
	print(driver.title)

	elem = driver.find_element_by_id('query')
	elem.clear()
	# clear()를 해주는 이유는 간혹 포털마다 검색어가 이미 입력되어 있는 경우가 있기 때문
	
	elem.send_keys('오늘 날씨')
	elem.send_keys(Keys.RETURN)

	news = driver.find_element_by_class_name('news')
	# news_list = news.find_elements_by_tag_name('li')
	# li 태그를 가진 하위 뉴스 리스트까지 불러오게 됨
	news_list = news.find_elements_by_xpath('./ul/li')

	for news in news_list:
		news_title = news.find_element_by_class_name('_sp_each_title')
		print(news_title.text)


except Exception as e:
	print(e)

finally:
	driver.close()	
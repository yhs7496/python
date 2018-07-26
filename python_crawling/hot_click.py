from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
driver = webdriver.Chrome('chromedriver')

ex = Workbook()
es = ex.active

try:
	driver.get('http://www.11st.co.kr')
	print(driver.title)

	elem = driver.find_element_by_class_name('header_inp_txt')
	elem.clear()
	# clear()를 해주는 이유는 간혹 포털마다 검색어가 이미 입력되어 있는 경우가 있기 때문
	
	elem.send_keys('라즈베리파이')
	elem.send_keys(Keys.RETURN)

	hot_click = driver.find_element_by_class_name('total_listing_wrap')
	hot_click_list = hot_click.find_elements_by_tag_name('li')

	for title in hot_click_list:
		title = title.find_element_by_class_name('info_tit')
		print(title.text)
		es.append([title.text])
	ex.save('list.xlsx')	


except Exception as e:
	print(e)

finally:
	driver.close()	
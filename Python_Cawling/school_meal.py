# 크롬 브라우저를 뛰우기 위해 selenium으로 웹 드라이버를 가져옴
from selenium import webdriver

# 크롬 드라이버로 크롬 브라우저 실행
driver = webdriver.Chrome('Chromedriver')

try:
	# http://dsm2015.cafe24.com/#/로 접속 
	driver.get('http://dsm2015.cafe24.com/#/')
	
	# id로 접근
	title_id = driver.find_element_by_id('meal-content-wrapper')
	
	# class로 접근
	meal_list = title_id.find_elements_by_class_name('food')

	# 가져온 태그들에 대해 반복문을 수행하면서 각각의 태그 안에 있는 요소들을 텍스트파일로 저장
	for meal in meal_list:
		print(meal.text)
		
except Exception as e:
	print(e)

finally:
	driver.quit()	
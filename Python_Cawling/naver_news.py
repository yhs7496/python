# 크롬 브라우저를 뛰우기 위해 selenium으로 웹 드라이버를 가져옴
from selenium import webdriver

# 크롬 드라이버로 크롬 브라우저 실행
driver = webdriver.Chrome('Chromedriver')

try:
	driver.get('http://news.naver.com')
	# 네이버 뉴스임을 알 수 있도록 현재 타이틀 출력
	print(driver.title)

	# 최근 뉴스 목록을 가진 div id 태그를 가져옴 
	title_id = driver.find_element_by_id('right.ranking_contents')

	# 위 div_id안에 li태그로 구분 되어 있는 정보를 가져와 리스트로 저장
	news_list = title_id.find_elements_by_tag_name('li')

	# 가져온 태그들에 대해 반복문을 수행하면서 각각의 문자열을 출력
	for news in news_list:
		print(news.text)

except Exception as e:
	print(e)

finally:
	driver.quit()	

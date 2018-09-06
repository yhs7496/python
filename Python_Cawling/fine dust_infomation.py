'''
1. 크롤링 하고자 하는 요소
- 미세먼지 상태(좋음, 보통, 나쁨)
- 미세먼지 농도
- 활동 안내 메시지( ex 오늘은 야외활동을 삼가하여 주세요.)  

2. 크롤링 목적
- 많은 사람들이 항상 관심 있어하고 이슈가 되는 미세먼지 정보를 습득하기 위해서이다.

3. 동작과정
- 크롬브라우저에서 Daum사이트로 접속하여 검색창에 '대전광역시 미세먼지' 라는 
  검색어를 검색하여 미세먼지 정보를 txt파일로 저장한다. 

4. 기대효과
- 크롤링을 통해 얻어진 미세먼지 정보를 통하여 자신의 건강을 챙길 수 있고, 자신이 야외에서 활동가능한지 판단하는 근거가 된다.

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')

try:
	driver.get('http://www.daum.net')
	print(driver.title)

	elem = driver.find_element_by_id('q')
	elem.clear()
	# clear()를 해주는 이유는 간혹 포털마다 검색어가 이미 입력되어 있는 경우가 있기 때문
	
	elem.send_keys('대전광역시 미세먼지')
	elem.send_keys(Keys.RETURN)
 
	fine_dust = driver.find_element_by_id('airPollutionNColl')
	find_dust_concentration = fine_dust.find_element_by_class_name('info_air')
	
	# 미세먼지 정보를 텍스트파일로 저장
	f = open("미세먼지 정보.txt", "w")
	f.write(find_dust_concentration.text)
	f.close()

except Exception as e:
	print(e)

finally:
	driver.close()	
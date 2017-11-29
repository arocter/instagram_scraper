import urllib
import time
import requests
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver

base_url = "https://www.instagram.com/p/BaZjAbyj_Cf/"
driver = webdriver.Chrome("/Users/arocter/Desktop/itp2017_spring/detourning_web/detourn/chromedriver")
driver.get(base_url)
button = driver.find_element_by_css_selector('._m3m1c')
count = 0
count_2 = 0;


def get_comments(url):
	global count
	global count_2
	html = requests.get(url).text
	soup = BeautifulSoup(driver.page_source, "html.parser")
	account_names = soup.select('._2g7d5')
	# print ("haha")
	for account_name in account_names:
		count+=1
		print account_name.text

	comment_divs = soup.select('._ezgzd')

	for comment_div in comment_divs:
		# comments = soup.select_one("span:nth-of-type(1)")
		comments = comment_div.find_all("span")
		print comments[0].text
		# account_names = soup.find_all('a','._2g7d5 ._95hvo')
		# if account_names!=None or account_names>0:

	# print comments
	
	# for comment in comments:
	# 	count_2 += 1;
	# 	# if count_2 % 2 != 1:
	# 	print comment.text

	return count

for i in range(300):
	button.click()
	get_comments(base_url)
	time.sleep(5)

# get_comments(base_url)

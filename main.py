from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import io
import random
import os
import string

#add options google chrome browser
options = webdriver.ChromeOptions()
options.add_argument("window-size=600,730")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

#get word search
with io.open('word.txt', 'r') as f:
	word = f.read()
#get tweet
with io.open('tweet.txt', 'r') as f:
	tweet = f.read()
#random proxy
with io.open('proxies.txt', "r", encoding="utf-8") as f:
	lines = f.readlines()
	proxie = random.choice(lines)
	proxie = proxie.rstrip("\n")

#open browser
options.add_argument('--proxy-server=%s' % proxie)
driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=options)
driver.get('https://twitter.com/i/flow/login')

#clear window bash
os.system('cls')

#wait user input info login
input('Enter your info login and clcik <ENTER> key to contine...')
driver.get(f'https://twitter.com/')

#modify word
if '#' in word:
	word = word.replace('#', '%23')


#open url search
driver.get(f'https://twitter.com/search?q={word}&src=typed_query')
time.sleep(1)
driver.refresh() 

#chak open browser
while True:
	try:
		driver.find_element(By.XPATH, '//*[@data-testid="tweet"]').get_attribute('aria-labelledby')
		break
	except:
		pass

list_id_tweets = []
x = 0
#chak new tweet
while True:
	#random any key
	temp = random.sample(string.ascii_lowercase,5)
	key = "".join(temp)
	tweet = tweet + '\n' + key
	while True:
		try:
			driver.find_element(By.XPATH, '//*[@aria-selected="false"]').click()
			break
		except:
			pass
	time.sleep(0.5)
	#get id of first tweet
	while True:
		try:
			id_tweet = driver.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-18u37iz.r-1q142lx').get_attribute('innerHTML').split('/')[3].split('"')[0]
			break
		except:
			pass

	if id_tweet not in list_id_tweets:
		
		#add comment in first tweet
		while True:
			try:
				driver.find_element(By.XPATH, '//*[@data-testid="reply"]').click()
				break
			except:
				pass
		while True:
			try:
				driver.find_element(By.XPATH, '//*[@data-testid="tweetTextarea_0"]').send_keys(tweet)
				break
			except:
				pass
		
		driver.find_element(By.XPATH, '//*[@data-testid="tweetButton"]').click()

		x = x + 1
		print(f'[{x}] add comment:', id_tweet)
		list_id_tweets.append(id_tweet)
		
	
	while True:
		try:
			driver.find_element(By.XPATH, '//*[@aria-selected="false"]').click()
			break
		except:
			pass
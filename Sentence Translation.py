from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pyperclip
import time
import os

# 자동 번역기 프로그램
# 한글을 다른 언어로 번역

memo_name = input("번역할 메모를 말해주세요: ")
language = input("언어를 선택해주세요 (영어,일본어,중국어(간체),중국어(번체),스페인어,프랑스어,독일어,러시아어,포르투갈어,이탈리아어,베트남어,태국어,인도네시아어,힌디어,아랍어): ")

# WebDriver 설정
browser = webdriver.Chrome("./chromedriver.exe") #chromedriver가 있는 파일 경로 입력
browser.get('https://papago.naver.com/')
browser.maximize_window()

# 로컬 파일 시스템에서 메모 파일을 읽어옵니다.
file_path = f'./{memo_name}.txt'  # 메모 파일의 경로와 이름을 지정하세요.

# 맞춤법 수정한 메모를 새로 저장할 파일을 만듭니다.
memo_translation_file = f'./{memo_name}_{language} 번역.txt'

# 기존 번역 파일이 존재하는 경우 삭제합니다.
if os.path.exists(memo_translation_file):
    os.remove(memo_translation_file)

# 메모 파일을 읽어옵니다.
with open(file_path, 'r', encoding='utf-8') as file:
    memo_content = file.read()

# 문자 수를 계산합니다.
character_count = len(memo_content)
print('글자 수: ',character_count)

# 문자열을 500자씩 나누어 리스트에 저장합니다.
chunks = [memo_content[i:i+500] for i in range(0, len(memo_content), 500)]

browser.implicitly_wait(2)

# 언어 선택
browser.find_element(By.CSS_SELECTOR, '#ddTargetLanguage2 > div.dropdown_top___13QlJ > button:nth-child(2)').click()
elements = browser.find_element(By.CSS_SELECTOR, '#ddTargetLanguage2 > div.dropdown_menu___XsI_h.active___3VPGL').find_elements(By.TAG_NAME, 'li')
for element in elements:
    text = element.find_element(By.TAG_NAME, 'span').text
    if language in text:
        element.click() 
        print('언어 있음')
        break
    else:
        print('해당 언어 없음')

# 번역 진행
for i, chunk in enumerate(chunks):
    search_box = browser.find_element(By.CSS_SELECTOR, '#txtSource')
    search_box.send_keys(chunk)

    # 요소가 나타날 때까지 대기합니다.
    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#root > div > div.wrap___1rX6i.rwd.rwd___3Qe-c.banner_active___3MQbf > section > div > div.rwd_layout___2qH8c > div:nth-child(4) > div > ul')))

    # 수정된 글을 복사합니다. 
    browser.find_element(By.CSS_SELECTOR, '#root > div > div.wrap___1rX6i.rwd.rwd___3Qe-c.banner_active___3MQbf > section > div > div.rwd_layout___2qH8c > div:nth-child(4) > div > div:nth-child(7) > span:nth-child(5) > span > span > button').click()  

    # 클립보드에서 복사된 내용을 가져옵니다.
    memo_translation = pyperclip.paste()

    # 메모장 파일을 열고 입력된 내용을 파일에 씁니다.
    with open(memo_translation_file, 'a', encoding='utf-8') as file:
        file.write(memo_translation)
    browser.find_element(By.CSS_SELECTOR, '#sourceEditArea > button').click()  # 다름 텍스트를 검사하기 위해 X버튼 눌러줍니다.

# 브라우저 종료
browser.quit()

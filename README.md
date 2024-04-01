# Sentence-Translation
## 💎 번역하기

개발 기간: 5시간

개발 언어: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">

## 📌 미리 보기
- [프로젝트 소개](#-프로젝트-소개)
- [실행 전 주의 사항](#-실행-전-주의-사항)
- [실행 영상](#-실행-영상)
- [주요 코드 설명](#-주요-코드-설명)
- [프로젝트를 하며 느낀점](#-프로젝트를-하며-느낀점)

## 🎤 프로젝트 소개
- 파파고 번역기는 한번에 검사가능한 3000자 글자 제한이 있습니다.
- 글자가 3000자가 넘어도 번역을 해주는 프로그램입니다.
- 순서는 아래와 같습니다.
1. 메모장에 글을 적습니다.
2. 코드와 같은 디렉토리에 메모 파일을 저장합니다.
3. 번역할 언어를 선택합니다.
4. 파파고로 번역을 합니다.
5. 번역 완료된 파일을 따로 저장합니다.


## 🦍 실행 전 주의 사항
- https://chromedriver.chromium.org/downloads 에서 크롬 버전에 맞는 Chrome driver를 설치해야 합니다.
- 크롬 버전 확인하는 법: 크롬실행-> 브라우저 오른쪽 상단의 점 세개 클릭-> 도움말-> Chrome 정보
- 다운로드한 Chrome driver 압축을 풀고 Sentence Spelling.py와 같은 디렉토리에 위치시켜야 합니다.
- Selenium과 Beautifulsoup4을 설치해야 합니다.


  prompt실행 후
  ```
  pip install selenium
  pip install bs4
  ```

## 💿 실행 영상
![만우절 유래 영어 번역](https://github.com/SeungHuiHan/Sentence-Translation/assets/98226400/ce24b4e2-7464-4e1a-a576-cc0e7eb892be)


- 나무위키에서 만우절> 유래를 가져왔습니다.

  
## 🗣 주요 코드 설명
```python
memo_name = input("번역할 메모를 말해주세요: ")
language = input("언어를 선택해주세요 (영어,일본어,중국어(간체),중국어(번체),스페인어,프랑스어,독일어,러시아어,포르투갈어,이탈리아어,베트남어,태국어,인도네시아어,힌디어,아랍어): ")

file_path = f'./{memo_name}.txt'
memo_translation_file = f'./{memo_name}_{language} 번역.txt'
```
- Sentence Spelling.py와 같은 디렉토리에 있는 메모중 번역할 메모를 입력합니다.
- 영어,일본어,중국어(간체),중국어(번체),스페인어,프랑스어,독일어,러시아어,포르투갈어,이탈리아어,베트남어,태국어,인도네시아어,힌디어,아랍어 중 번역할 언어를 입력합니다.
- 번역이 완료된 메모는 원래 이름_번역 언어 번역으로 저장됩니다. (ex. 원래 메모 이름: 만우절 유래, 영어로 번역 완료된 메모 이름: 만우절 유래_영어 번역)


```python
with open(file_path, 'r', encoding='utf-8') as file:
    memo_content = file.read()

```
- 메모를 읽어옵니다.

```python
chunks = [memo_content[i:i+500] for i in range(0, len(memo_content), 500)]

```
- 글자를 500자씩 잘라서 리스트에 저장합니다.

```python

 element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
      '#root > div > div.wrap___1rX6i.rwd.rwd___3Qe-c.banner_active___3MQbf > section > div > div.rwd_layout___2qH8c > div:nth-child(4) > div > ul')))
 browser.find_element(By.CSS_SELECTOR,
        '#root > div > div.wrap___1rX6i.rwd.rwd___3Qe-c.banner_active___3MQbf > section > div > div.rwd_layout___2qH8c > div:nth-child(4) > div > div:nth-child(7) > span:nth-child(5) > span > span > button').click() 
```
- 번역이 완료될 때까지 대기합니다.
- 번역이 완료되면 복사하기 버튼을 클릭합니다.

  
```python
with open(memo_modification_file, 'a', encoding='utf-8') as file:
        file.write(memo_modification)

```
- 번역 완료 글을 저장합니다.
  

## 🐽 프로젝트를 하며 느낀점

글자를 한번에 많이 넣으면 번역이 시간이 길어진다. 주의해야될 듯 하다.
아직 아쉬운 점은 없고 계속 사용해보면서 적어나가겠다.

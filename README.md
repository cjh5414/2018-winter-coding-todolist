## 결과물 URL
http://182.162.104.151/

## 스펙
- python 3.5.2
- django 2.1.2
- pytest 3.9.3
- sqlite3
- bootstrap4
- nginx 1.4.6 
- uwsgi 2.0.17.1
- Ubuntu 14.04.5

## 서버 배포 과정

### pyenv & pyenv-virtualenv & autoenv 설치 및 설정  

python 가상 환경 설정을 위해 pyenv, pyenv-virtualenv 를 사용했습니다.  
(Ubuntu 서버에 설치하는 참고자료: https://cjh5414.github.io/ubuntu-pyenv-virtualenv/)  
(Mac OS 설치방법: https://cjh5414.github.io/ubuntu-pyenv-virtualenv/)

아래의 명령으로 설정을합니다.   
```
$ pyenv install 3.5.2
$ pyenv virtualenv 3.5.2 todo-list
$ echo "pyenv activate todo-list" > .env
$ cd .
```  

### python 패키지 설치  

```
$ pip install -r requirements.txt
```  

### 로결 환경에서 서버 구동  

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### 단위 테스트 실행방법  
```
$ pytrest
```

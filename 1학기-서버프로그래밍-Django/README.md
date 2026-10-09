# Django REST API 프로젝트

## 설치 및 실행 방법

### 가상환경 생성 및 활성화
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Django 설치
```
pip install django djangorestframework
```

### 환경 설정 및 새 DB 생성

`.env.example`은 필요한 프로세스 환경변수 목록이며 자동 로드되지 않습니다. 실제 환경 파일·SQLite 파일·인증 토큰은 커밋하지 않습니다. PowerShell에서 다음처럼 현재 프로세스에 새 키를 생성합니다. 값을 출력하거나 문서에 복사하지 않습니다.

```powershell
$env:DJANGO_SECRET_KEY = python -c "import secrets; print(secrets.token_urlsafe(64))"
$env:DJANGO_DEBUG = "true" # 개인 로컬 개발에서만 사용; 기본값 false
$env:DJANGO_ALLOWED_HOSTS = "localhost,127.0.0.1"
python manage.py migrate
```

실제 배포에서는 직접 관리하는 환경 파일이나 실행 환경에서 고정된 새 키를 주입합니다. 재시작마다 키를 재생성하지 않습니다. 예전에 공개한 키·DB·토큰은 재사용하지 않습니다. DB의 Git 추적 해제는 현재 로컬 파일을 지우지 않으며 과거 Git 이력도 정리하지 않습니다. 새 클론은 마이그레이션으로 빈 DB를 만들고 본인 계정을 생성합니다. [Django 배포 점검 안내](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)

### 슈퍼유저 생성 (최초 1회)
```
python manage.py createsuperuser
```

### Django 서버 실행
```
python manage.py runserver
```

**URL** : http://127.0.0.1:8000

---

## API 명세서

### 📌 기본 정보
- **Base URL**: `http://127.0.0.1:8000`
- **인증 방식**: Token Authentication
- **Content-Type**: `application/json`

### 🔐 인증

#### 토큰 발급
```http
POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

**응답:**
```json
{
    "token": "YOUR_TOKEN"
}
```

#### 인증 헤더
발급받은 토큰을 모든 API 요청 헤더에 포함:
```
Authorization: Token YOUR_TOKEN
```

---

### 📋 학생 정보 (Hacsam) API

#### 1. API Root
```http
GET /api/
Authorization: Token {your_token}
```

**응답:**
```json
{
    "hacsams": "http://127.0.0.1:8000/api/hacsams/"
}
```

#### 2. 학생 목록 조회
```http
GET /api/hacsams/
Authorization: Token {your_token}
```

**응답:**
```json
[
    {
        "id": 1,
        "name": "홍길동",
        "birthday": "2000-01-01",
        "stdnum": 20200001,
        "major": "컴퓨터공학과",
        "email": "hong@example.com"
    }
]
```

#### 3. 학생 정보 생성
```http
POST /api/hacsams/
Authorization: Token {your_token}
Content-Type: application/json

{
    "name": "김철수",
    "birthday": "2001-05-15",
    "stdnum": 20210002,
    "major": "소프트웨어학과",
    "email": "kim@example.com"
}
```

#### 4. 특정 학생 정보 조회
```http
GET /api/hacsams/{id}/
Authorization: Token {your_token}
```

#### 5. 학생 정보 수정
```http
PUT /api/hacsams/{id}/
Authorization: Token {your_token}
Content-Type: application/json

{
    "name": "김철수",
    "birthday": "2001-05-15",
    "stdnum": 20210002,
    "major": "컴퓨터공학과",
    "email": "kim.updated@example.com"
}
```

#### 6. 학생 정보 삭제
```http
DELETE /api/hacsams/{id}/
Authorization: Token {your_token}
```

---

### 🌐 웹 페이지 (템플릿 뷰)

- **메인 페이지**: `http://127.0.0.1:8000/`
- **학생 생성**: `http://127.0.0.1:8000/create/`
- **학생 상세**: `http://127.0.0.1:8000/detail/{id}/`
- **학생 수정**: `http://127.0.0.1:8000/update/{id}/`
- **학생 삭제**: `http://127.0.0.1:8000/delete/{id}/`
- **관리자 페이지**: `http://127.0.0.1:8000/admin/`

---

### 📝 데이터 모델

#### Hacsam (학생)
| 필드 | 타입 | 설명 | 필수 |
|------|------|------|------|
| id | Integer | 자동 생성 ID | - |
| name | String (100) | 학생 이름 | ✅ |
| birthday | Date | 생년월일 (YYYY-MM-DD) | ✅ |
| stdnum | Integer | 학번 | ✅ |
| major | String (50) | 전공 | ✅ |
| email | Email | 이메일 주소 | ✅ |
| user | ForeignKey | 연결된 사용자 | 자동 |

---

### 🔧 에러 응답

#### 인증 오류 (401)
```json
{
    "detail": "Authentication credentials were not provided."
}
```

#### 권한 오류 (403)
```json
{
    "detail": "You do not have permission to perform this action."
}
```

#### 찾을 수 없음 (404)
```json
{
    "detail": "Not found."
}
```

---

### 💡 사용 예시

#### Python requests 예제
```python
import requests

# 토큰 발급
response = requests.post('http://127.0.0.1:8000/api/token/', {
    'username': 'your_username',
    'password': 'your_password'
})
token = response.json()['token']

# 학생 목록 조회
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/hacsams/', headers=headers)
print(response.json())
```

#### curl 예제
```bash
# 토큰 발급
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"your_username","password":"your_password"}'

# 학생 목록 조회
curl -X GET http://127.0.0.1:8000/api/hacsams/ \
  -H "Authorization: Token YOUR_TOKEN"
```
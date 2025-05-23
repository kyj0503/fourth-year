# Django 프로젝트 - cntech

이 프로젝트는 Student 모델을 다루는 Django 웹 애플리케이션입니다.

## 설치 및 실행 방법

### 1. 가상환경 활성화
```bash
source .venv/bin/activate
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 4. 개발 서버 실행
```bash
python manage.py runserver
```

서버가 실행되면 http://127.0.0.1:8000/ 에서 애플리케이션에 접근할 수 있습니다.

## 프로젝트 구조

- `cntech/` - Django 프로젝트 설정
- `hello/` - Student 모델을 다루는 앱
- `static/` - 정적 파일 (CSS, JavaScript, 이미지)
- `templates/` - Django 템플릿 파일
- `db.sqlite3` - SQLite 데이터베이스 파일

## 관리자 계정 생성

```bash
python manage.py createsuperuser
```

관리자 페이지는 http://127.0.0.1:8000/admin/ 에서 접근할 수 있습니다.

## API 엔드포인트

- `/` - Student 목록 (ListView)
- `/create/` - Student 생성
- `/update/<id>/` - Student 수정
- `/detail/<id>/` - Student 상세 정보
- `/delete/<id>/` - Student 삭제
- `/api/` - Student API 목록
- `/api/<id>/` - Student API 상세 정보 
# Database

> 체계화된 데이터의 모임, 공유 및 사용을 목적으로 통합 관리되는 정보의 집합
>
> 조직적으로 통합하여 중복을 없애고 자료를 구조화하여 효율을 높인다.

- 데이터 중복 최소화
- 데이터 무결성 : 정확한 정보를 보장
- 데이터 일관성
- 데이터 독립성 
  - 물리적 독립성 : 클라이언트 및 서버와 통신으로 정보를 주고받을 뿐 물리적으로 단단하게 연결돼있지 않다.
  - 논리적 독립성 : 하위 단계의 변경이 상위 단계에 영향을 끼치지 않는다.
- 데이터 표준화
- 데이터 보안 유지



## RDBMS (관계형 데이터베이스 관리 시스템)

> 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템

### 스키마 (Schema)

> 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조

| column    | datatype |
| --------- | -------- |
| id        | INT      |
| something | TEXT     |
| anything  | INT      |
| ...       | ...      |



## SQL (Structured Query Language)

> 관계형 데이터베이스 관리 시스템의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

### 데이터 정의 언어 (Data Definition Language - DDL)

> 데이터를 정의하기 위한 언어

```sqlite
CREATE, DROP, ALTER, ...
```



### 데이터 조작 언어 (Data Manipulation Language - DML)

> 데이터를 저장, 수정, 삭제, 조회 등을 하기 위한 언어

```sqlite
INSERT, UPDATE, DELETE, SELECT, ...
```



### 데이터 제어 언어 (Data Control Language - DCL)

> 사용자의 권한 제어를 위한 언어

```sqlite
GRANT, REVOKE, COMMIT, ROLLBACK, ...
```



### SQLite 설치

- 공식 사이트에서 설치를 한다
- PATH로 SQLite 폴더를 지정한다.
- vi ~/.bashrc 로 `alias sqlite3 "winpty sqlite3" 해주기 (옵션)
- bash에서 sqlite3로 SQLite 실행

### 간단한 명령어들

- `sqlite3 db명.sqlite3` : 데이터베이스 생성 및 열기
- `.mode csv` : csv 모드
- `.import CSV파일명.csv 테이블명` : 파일을 가져와서 테이블로 만들기
- `.headers on` : 컬럼명 같이 출력
- `.mode column` : 표 형태로 보기
- `.tables` : 테이블 보기
- `.schema 테이블명` : 테이블의 구조확인



## 키워드는 대문자로

#### 조회

`SELECT * FROM 테이블명` : SELECT와 FROM은 키워드이기때문에 대문자로 작성한다.

#### 테이블 생성

SQLite는 따로 PRIMARY KEY를 작성하지 않으면 자동으로 PK 옵션을 가진 **rowid**를 갖는다.

```sqlite
CREATE TABLE 테이블명(
	id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    컬럼명 컬럼타입 기타옵션
)
```

AUTOINCREMENT 사용도 가능하나 SQLite는 PK를 따로 만들지않고 **rowid**를 사용하는 것을 권장한다.

#### 테이블 삭제

`DROP TABLE 테이블명`



## 데이터 추가, 읽기, 수정, 삭제

### 데이터 추가 (INSERT)

**INSERT INTO** 테이블명 (컬럼명1, 컬럼명2, ...) **VALUES** (값1, 값2, ...)

모든 컬럼을 채우는 경우 컬럼명을 생략할수 있다.

**INSERT INTO** 테이블명 **VALUES** (값1, 값2, ...)

한번에 여러개 추가도 가능하다.

**INSERT INTO** 테이블명 **VALUES** (값1, 값2, ...), (값1, 값2, ...), (값1, 값2, ...)



### 데이터 조회 (SELECT)

**SELECT** * **FROM** 테이블명

- 전체 데이터 가져오기

**SELECT** 컬럼명1, 컬럼명2 **FROM** 테이블명

- 특정 컬럼의 데이터만 가져오기

**SELECT** 컬럼명1, 컬럼명2 **FROM** 테이블명 **LIMIT** 개수

- 특정 개수만큼만 데이터 가져오기

**SELECT** 컬럼명1, 컬럼명2 **FROM** 테이블명 **LIMIT** 개수 **OFFSET** 숫자

- 숫자만큼 앞에 있는 데이터를 제외한 후 개수만큼 가져오기

**SELECT** 컬럼명1, 컬럼명2 **FROM** 테이블명 **WHERE** 컬럼명=값

- 해당 컬럼명이 값인 (조건을 만족하는) 데이터만 가져오기

**SELECT DISTINCT** 컬럼명 **FROM** 테이블명

- 중복없이 해당 컬럼의 값을 가져오기



### 데이터 삭제 (DELETE)

**DELETE FROM** 테이블명 **WHERE** 조건

- 테이블 내 조건이 맞는 데이터 삭제하기



### 데이터 수정 (UPDATE)

**UPDATE** 테이블명 **SET** 컬럼명1=값1, 컬럼명2=값2, ... **WHERE** 조건

- 조건이 맞는 데이터의 각 컬럼을 매칭되는 값으로 변경하기



## SQL 활용

### 비교문

**SELECT** * **FROM** 테이블명 **WHERE** 컬럼명 >= 숫자

- 숫자와 부등호의 조건에 만족하는 모든 데이터를 가져온다.
  - `>=, <=, <, >, =`

### 여러개

**SELECT** * **FROM** 테이블명 **WHERE** 컬럼명 >= 숫자 **AND|OR** 컬럼명 = something



### 수식

**SELECT COUNT(**컬럼명**) FROM** 테이블명

- 해당 컬럼 혹은 전체(*) 개수를 센다.

**SELECT AVG(**컬럼명**) FROM** 테이블명

- AVG() : 평균값
- SUM() : 전체합
- MIN() : 최소값
- MAX() : 최대값



### LIKE

> 정확한 값에 대한 비교가 아닌 패턴을 분석한다.

- `-` : 반드시 한 개의 문자가 존재한다.
- `%` : 문자가 있을수도 없을수도 있다.

#### WHERE 컬럼명 LIKE

| %    | a%     | a로 시작하는 값      |
| ---- | ------ | -------------------- |
|      | %a     | a로 끝나는 값        |
|      | %a%    | a를 포함하는 값      |
| -    | _a%    | a가 두번째로 있는 값 |
|      | a_ _ _ | a로 시작하며 4자리   |



### 정렬 (ORDER)

**SELECT** 컬럼명 **FROM** 테이블명 **ORDER BY** 컬럼명, 컬럼명 **ASC**(오름차)|**DESC**(내림차)



### GROUP

> 지정된 기준에 따라 그룹으로 결합한다.

**SELECT** 컬럼명, 컬럼명 **FROM** 테이블명 **GROUP BY** 컬럼명



## 테이블 활용

### 테이블 이름 변경

**ALTER TABLE** 테이블명 **RENAME TO** 새로운테이블명

### 새로운 컬럼 추가

**ALTER TABLE** 테이블명 **ADD COLUMN** 컬럼명 컬럼타입 기타조건



# Django에서 활용

annotate, aggregate
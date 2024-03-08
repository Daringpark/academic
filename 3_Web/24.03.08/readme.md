# Bootstrap
CSS 프론트엔드 프레임워크(TOOLKIT)
- 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

---
### CDN
Content Delivery Network
- 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술

---
### Bootstrap의 기본 사용 방법
```html
<p class="mt-5">Hello, World!</p>
```
{property}{sides}-{size}
- property
    - m : margin
    - p : padding

- sides
    - t : top
    - b : bottom
    - s : left (start)
    - e : right (end)
    - y : top, bottom (both)
    - x : left, right (start, end both)
    - blank : 4 sides

- size
    - 0 : 0 rem (0px)
    - 1 : 0.25 rem (4px)
    - 2 : 0.5 rem (8px)
    - 3 : 1 rem (16px)
    - 4 : 1.5 rem (24px)
    - 5 : 3 rem (48px)
    - auto : auto (auto)

https://getbootstrap.com/docs/5.3/utilities/spacing/#margin-and-padding

---
## Reset CSS
모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트
- HTML Element, Table, List 등의 요소들에 일관성 있게 스타일을 적용 시키는 기본 단계
- 모두 다 똑같은 스타일 상태로 만들고 스타일 개발을 시작하자!!

### Normalize CSS
- Reset CSS 방법 중 대표적인 방법
- 웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법

---
# Typography
제목, 본문 텍스트, 목록 등

### Colors
### components
### Carosel
- 주의 : ID와 data-bs-target를 잘 봐야 한다.

### Modal
- 주의 : modal 코드가 다른 코드 안쪽에 중첩되어 들어가면, modal이 켜졌을때 회색 화면 뒤로 감춰질 수 있다.

- 주의 2 : modal과 button 코드가 같이 붙어 있을 필요없이 data=bs-target과 modal의 ID를 알맞게 설정하면 된다.

---
# Semantic Web
웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식

"이 요소가 시각적으로 어떻게 보여질까?" --> "이 요소가 가진 목적과 역할은 무엇일까?"

### HTML 요소가 의미와 목적, 역할을 갖는다라..

SEO (Search Engline Optimization)
- 검색엔진 사용하



---
# CSS 방법론과 의미론적 마크업이 필요한 이유
CSS를 효율적으로 사용하고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인

### OOCSS
### Semantic Tag 사용
Object Oriented CSS
- 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론
- OOCSS 기본 원칙
    1. 구조와 스킨을 분리
    2. 컨테이너와 콘텐츠를 분리

### 웹 접근성
- 웹 사이트, 도구, 기술 등이 고령자나 장애를 가진 사용자들이 사용할 수 있도록 설계 및 개발한 것이다.
- 

(예시)
```css
.botton {
    border: none;
    font-size: 1 em;
    padding: 10px 20px;
}

.button-blue {
    background-color: blue;  
    color: white;
}

.button-red {
    background-color: red;
    color: white
}
```


(예시)
```css
.container .title {
    font-size : 24px;
}

.header {  
    color: white;
}

.footer {
    color: black
}
```
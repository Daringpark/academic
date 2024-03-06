# WEB
https://married-spot-253.notion.site/5fef18bbcd4b467fb8c7ed819250e1e8?v=d7d02b0f89684f7e8e5650572eb693e2

---
### Web_1

---
### Web
- Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

### Web site
- 인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간

### Web page
= HTML, CSS 등 Web 기술을 이용하여 만들어진, Web site를 구성하는 하나의 요소

## Web page의 구성
- 상위 : Web page
- 하위 : HTML(Structure), CSS(Styling), Javascript(Behavior)

---
### HTML
- HyperText Markup Language (HTML)
- 웹 페이지의 의미와 구조를 정의하는 언어

### Hypertext
- 웹 페이지를 다른 페이지로 연결하는 링크 (한 문서에서 다른 문서로 바로 접근할 수 있는 텍스트)

### Markup Language
- 태그 등을 이용하여 문서나 데이터 구조를 명시하는 언어 (ex.HTML, Markdown)
- 구조화 이후에 HTML language를 이용해서 작성할 수 있다!

### <> : Tag
< !DOCTYPE html >
- html로 보이기 되어서 실제로는 괄호를 잘 붙이자.
- 최상단에 해당 문서가 html로 이뤄진 문서라는 것을 알 수 있다.
<html> 과 </html>
- 여는 구조와 닫는 구조가 있다. (ex. (<head>, </head>), (<body>, </body>))

### <head>, <body>
<head>
- HTML 문서에 관련한 설명, 설정 등을 담는다.
- 사용자에게는 보이지 않는다.
<body>
- 페이지에 표시되는 모든 콘텐츠

### HTML Element
(ex.) <p>My chat is very grumpy</p>
Element = <opening tag> content <closing tag>

### HTML Attributes
(ex.) <p class = "editor-note">My cat is very grumpy</p>
- 속성은 요소 이름과 속성 사이에 공백이 있어야 함.
- 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분한다.
- 속성 값은 열고 닫는 따옴표로 감싸야 한다.

- 나타내고 싶지 않지만, 추가적인 기능 혹은 내용을 담고 싶을 때 사용
- css에서 해당 요소를 선택하기 위한 값으로 활용

# MDN을 검색해보자.
내가 사용하고자 하는 태그를 참고서를 통해서 활용하는 법을 배워보자.
신뢰성이 높으면서 활용 사례도 여러 개 있어서 활용을 제대로 배울 수 있다.

---
# CSS
- 웹 페이지 디자인과 레이아웃을 구성하는 언어다.

### CSS Selectors
- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자
(ex.) 기본 선택자 : *, tag, class, id, attr; 결합자 : "", ">"

---
# Specificity 명시도
- CSS selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정
- 동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있을 경우, 가장 높은 명시도를 가진 선택자의 우선순위를 적용한다.

### Cascade
- 웹 페이지 디자인과 레이아웃을 구성하는 언어
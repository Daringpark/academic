
## Box Model

---
모든 HTML 요소를 사각형 박스로 표현한 개념이다.

그럼 박스 모델 안의 요소들은 어떻게 될까?

### CSS Box Model

---
- Content (내용) : 콘텐츠가 표시되는 제일 안 영역
- Padding (안쪽 여백) : 콘텐츠 주위의 공백 영역
- Border (테두리) : 콘텐츠와 패딩을 감싸는 테두리 영역
- Margin (외부 간격) : 박스와 다른 요소 사이의 공백, 가장 밖 영역

: 각 요소는 4 방향이 있다. (TOP, BOTTON, LEFT, RIGHT)

---
### Box-Sizing
CSS 중 box-sizing을 사용하여 content-box 혹은 border-box 크기로 조절하여 width 값을 조절할 수 있다.

### Inline Element과 Block Element
- Inline 요소는 좌에서 우측으로 배치가 되지만, Block 요소는 상단에서 아래로 내려가는 배치다.

### Inline Elements
- Inline 요소의 width, height의 속성을 사용할 수 없다.
- Inline 요소의 Padding, Border, Margin을 수직 방향으로 다른 요소를 밀어낼 수 없다.
- Inline 요소의 Padding, Border, Margin을 수평 방향으로 다른 요소를 밀어낼 수 있다.
- a, img, span
- 하지만, img는 예외로 width, height을 변경할 수 있다.

### Block Elements
- Block 요소는 새로운 행으로 나뉘게 된다.
- width와 height 속성을 사용하여 너비와 높이를 지정할 수 있다.
- Inline 방향으로 사용가능한 공간을 모두 차지하고 싶어한다.
- p, h1~h6, div

### margin-direction
마진 영역을 어떻게 줘야할까?

text-align : left; == margin-right : auto;
text-align : right; == margin-left : auto;
text-align : center; == margin-left : auto; margin-right : auto;

align과 다르게 margin을 주는 것은 영역 먹는 싸움이다.

---

# CSS Layout
- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
- Display, Position, Float, Flexbox 등

### CSS Position
- 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
- 다른 요소 위로 올리거나 화면의 특정 위치에 고정시키기 등
- Z축 위에 올린다는 느낌


















### 목적에 따른 속성 분류
- 배치를 목적으로
    - flex-direction
    - flex-wrap
- 공간을 목적으로
    - justify-content
    - algin-content
- 정렬을 목적으로
    - align-items
    - algin-self

### 속성명
- justify : 주 축
- algin : 교차 축
- justify-items와 justify-self라는 속성이 없는 이유
    - 필요 없다!
    - 왜? margin auto를 통해서 다 정렬, 배치가 가능하기 때문에
### flex-grow
비율에 따라서


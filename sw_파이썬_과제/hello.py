import turtle  # 터틀 그래픽 모듈 임포트

# 원 그리기
def draw_circle(t, x, y, radius, color, fill=False):
    t.pensize(3)  # 펜 두께 설정
    t.penup()  # 펜 들기(펜 떼기)
    t.goto(x, y - radius)  # 펜 이동
    t.pendown()  # 펜 내리기(그리기 시작)
    t.color(color)  # 펜 색상 설정
    if fill:  # 채우기 옵션 True일 경우
        t.begin_fill()  # 색깔 채우기 시작
        t.circle(radius)  # 원 그리기
        t.end_fill()  # 색깔 채우기 끝
    else:  # 채우기 옵션 False일 경우
        t.circle(radius)  # 색깔 채우지 않고 원 그리기
    t.penup()  # 펜 들기(펜 떼기)


# 타원 그리기
def draw_oval(t, x, y, radius1, radius2, color, fill=False):
    t.penup()  # 펜 들기(펜 떼기)
    t.goto(x, y)  # 타원의 중심으로 이동합니다.
    t.pendown()  # 펜 내리기(그리기 시작)
    t.color(color)  # 펜 색상 설정
    if fill:  # 채우기 옵션이 True일 경우
        t.begin_fill()  # 채우기 시작
        t.setheading(0)  # 방향 0도로 설정
        for _ in range(2):  # 타원 그리기 (반원 두 번 그리기)
            t.circle(radius1, 90)  # 첫 번째 반원
            t.circle(radius2, 90)  # 두 번째 반원
        t.end_fill()  # 채우기 끝
    else:
        t.setheading(0)  # 방향을 0도로 설정합니다.
        for _ in range(2):  # 타원 그리기 (반원 두 번 그리기)
            t.circle(radius1, 90)  # 첫 번째 반원
            t.circle(radius2, 90)  # 두 번째 반원
    t.penup()  # 펜 들기(펜 떼기)

# 곡선 그리기
def draw_curve(t, x, y, heading, radius, extent):
    t.penup()  # 펜 들기(펜 떼기)
    t.goto(x, y)  # 시작 위치로 이동
    t.pendown()  # 펜 내리기(그리기 시작)
    t.setheading(heading)  # 방향 0도로 설정
    t.circle(radius, extent)  # 곡선 그리기
    t.penup()  # 펜 들기(펜 떼기)

# 얼굴의 동그란 요소들 그리기(얼굴, 귀, 눈, 코)
def draw_face(t):
    draw_circle(t, 0, 20, 100, 'black')  # 얼굴
    draw_circle(t, -50, 120, 10, 'black')  # 왼쪽 귀
    draw_circle(t, 50, 120, 10, 'black')  # 오른쪽 귀
    draw_oval(t, -25, 32, 7, 5, 'black', True)  # 왼쪽 눈
    draw_oval(t, 25, 32, 7, 5, 'black', True)  # 오른쪽 눈
    draw_oval(t, 0, 0, 5, 5, 'black', True)  # 코



# 입 그리기 함수
def draw_mouth(t):
    t.pensize(8)  # 펜 두께 설정
    draw_curve(t, 0, 0, -80, -10, 160)  # 입의 왼쪽 곡선
    draw_curve(t, 3, 0, -100, 10, 160)  # 입의 오른쪽 곡선


# 농담곰 그리기 함수
def draw_jokebear():
    t = turtle.Turtle()  # 터틀 객체 생성
    t.speed(3)  # 터틀 속도 설정
    draw_face(t)  # 얼굴 그리기
    draw_mouth(t)  # 입 그리기
    t.hideturtle()  # 터틀 숨기기

# 이니셜 그리기 함수
def draw_initials():
    t = turtle.Turtle()  # 터틀 객체 생성
    t.speed(3)  # 터틀 속도 설정
    t.pensize(3)  # 펜 두께 설정
    t.penup()  # 펜 들기(펜 떼기)
    t.goto(150, 0)  # 시작 위치로 이동
    t.pendown()  # 펜 내리기(그리기 시작)

    # 'M' 그리기
    t.setheading(90)  # 방향 설정
    t.forward(50)  # 50픽셀 앞으로 이동
    t.right(135)
    t.forward(35)
    t.left(90)  # 왼쪽 90도 회전
    t.forward(35)
    t.right(135)
    t.forward(50)
    t.penup()  # 펜 들기(펜 떼기)

    # 'J' 그리기
    t.goto(215, 50)  # 시작 위치로 이동
    t.pendown()  # 펜 내리기(그리기 시작)
    t.goto(255, 50)  # 255, 50 좌표로 이동
    t.goto(240, 50)
    t.forward(35)
    t.circle(-15, 180)  # 반원 그리기
    t.hideturtle()  # 터틀 숨기기

# 1. 파이썬 터틀 그래픽을 통해 간단한 도형이나 그림을 그리시오: 자유 그림
# 농담곰 그리기
draw_jokebear()

# 2. 1번 그림 옆에 터틀 그래픽으로 본인 이름 이니셜을 그리시오(조금 이상하게 그려져도 OK) : 홍길동의 경우 이름은 길동 => GD 그리기
# 이니셜 - 김민주(MJ)
draw_initials()

# 터틀 그래픽 창 유지
turtle.done()

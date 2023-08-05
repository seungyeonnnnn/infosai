import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 1920, 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("버튼 예시 게임")

# 색깔 정의
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# 버튼 초기 위치와 크기 설정
button_width, button_height = 200, 200
button_x, button_y = (screen_width - button_width) // 2, (screen_height - button_height) // 2

# 초기 배경 색상 설정
background_color = red

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # ESC 키를 누르면 게임 종료
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:  # 스페이스바를 누를 때마다 배경색 변경
                if background_color == red:
                    background_color = blue
                else:
                    background_color = red

    # 화면 배경 색상 설정
    screen.fill(background_color)

    # 버튼 그리기
    pygame.draw.rect(screen, black, (button_x, button_y, button_width, button_height))

    # 화면 업데이트
    pygame.display.flip()
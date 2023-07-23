import pygame

# 화면 크기
WIDTH = 1920
HEIGHT = 720

# 색상 정의
WHITE = (255, 255, 255)

def main():
    # Pygame 초기화
    pygame.init()

    # 화면 생성
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # 창 제목 설정
    pygame.display.set_caption("Pygame 1920 x 720 해상도")

    # 게임 루프
    running = True
    while running:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 화면을 흰색으로 채우기
        screen.fill(WHITE)

        # 여기에 원하는 내용을 그리는 코드를 작성하세요.

        # 모든 그리기 작업을 마쳤으면, 화면 업데이트
        pygame.display.flip()

    # Pygame 종료
    pygame.quit()

if __name__ == "__main__":
    main()

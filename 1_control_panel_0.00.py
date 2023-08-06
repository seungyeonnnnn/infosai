import pygame
############################################################################
# def

def scene_button_init():
    pygame.draw.rect(screen, NORMAL, button_scene1)
    pygame.draw.rect(screen, NORMAL, button_scene2)
    pygame.draw.rect(screen, NORMAL, button_scene3)

def check_buttons(pos):
    global scene_no
    if button_scene1.collidepoint(pos):
        if scene_no == 1:
            pass
        else:
            scene_no = 1
            scene_button_init()
            pygame.draw.rect(screen, SELECTED, button_scene1)
            screen.blit(img_scene1, (0, 40))
    elif button_scene2.collidepoint(pos):
        if scene_no == 2:
            pass
        else:
            scene_no = 2
            scene_button_init()
            pygame.draw.rect(screen, SELECTED, button_scene2)
            screen.blit(img_scene2, (0, 40))
    elif button_scene3.collidepoint(pos):
        if scene_no == 3:
            pass
        else:
            scene_no = 3
            scene_button_init()
            pygame.draw.rect(screen, SELECTED, button_scene3)
            screen.blit(img_scene3, (0, 40))

############################################################################
pygame.init()
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Control Panel")

# FPS
# clock = pygame.time.Clock()
############################################################################

# 1. 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

#COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
SELECTED = (255, 255, 255)
NORMAL = (0, 0, 0)

#FONT
sai_font = pygame.font.Font(None, 32)

scene_no = 1

button_scene1 = pygame.Rect(0, 0, 96, 40)
button_scene2 = pygame.Rect(96, 0, 96, 40)
button_scene3 = pygame.Rect(96*2, 0, 96, 40)

text_scene1 = sai_font.render("# 1", False, GRAY)
text_scene2 = sai_font.render("# 2", False, GRAY)
text_scene3 = sai_font.render("# 3", False, GRAY)

img_scene1 = pygame.image.load("C:/Users/SEUNGYEON/Desktop/SY/infosai/Test_RSC_SY/scene_1.png")
img_scene2 = pygame.image.load("C:/Users/SEUNGYEON/Desktop/SY/infosai/Test_RSC_SY/scene_2.png")
img_scene3 = pygame.image.load("C:/Users/SEUNGYEON/Desktop/SY/infosai/Test_RSC_SY/scene_3.png")

screen.fill(BLACK)
pygame.draw.rect(screen, SELECTED, button_scene1)
pygame.draw.rect(screen, NORMAL, button_scene2)
pygame.draw.rect(screen, NORMAL, button_scene3)

screen.blit(img_scene1, (0, 40))

running = True
while running:
    # dt = clock.tick(30)
    click_pos = None

    # 2. 이벤트 입력 판단
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    # 3. 위치 정의
    # screen.fill(BLACK)
    
    # 4. 이벤트 처리
    if click_pos:
        check_buttons(click_pos)

    # 5. 화면에 그리기
    screen.blit(text_scene1, (34, 10))
    screen.blit(text_scene2, (34+96, 10))
    screen.blit(text_scene3, (34+96*2, 10))


    pygame.display.update() # 게임화면을 다시 그리기

pygame.quit()
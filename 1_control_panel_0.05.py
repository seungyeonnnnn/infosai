#Add TTS
import pygame
import cv2
import os
from gtts import gTTS
from playsound import playsound
import threading
############################################################################
# function def

def scene_button_init():
    pygame.draw.rect(screen, NORMAL, button_scene1)
    pygame.draw.rect(screen, NORMAL, button_scene2)
    pygame.draw.rect(screen, NORMAL, button_scene3)

def video_init():
    global video, playing, path_video
    video = None
    playing = False
    path_video = None

def sequence_init():
    global path_sequence, list_sequence, current_sequence
    path_sequence = None
    list_sequence.clear()
    current_sequence = 0

def draw_tab_list():
    scene_button_init()
    if scene_no == 1:
        pygame.draw.rect(screen, SELECTED, button_scene1)
        # screen.blit(img_scene1, (0, 40))
    elif scene_no == 2:
        pygame.draw.rect(screen, SELECTED, button_scene2)
        # screen.blit(img_scene2, (0, 40))
    elif scene_no == 3:
        pygame.draw.rect(screen, SELECTED, button_scene3)
        # screen.blit(img_scene3, (0, 40))
    screen.blit(text_scene1, (10, 17+54*0))
    screen.blit(text_scene2, (10, 17+54*1))
    screen.blit(text_scene3, (10, 17+54*2))

def check_buttons(pos):
    global scene_no, path_video, path_sequence
    if button_scene1.collidepoint(pos):
        if scene_no == 1:
            pass
        else:
            scene_no = 1
            video_init()
            sequence_init()
            path_video = "Test_RSC_SY/video_3.mp4"
    elif button_scene2.collidepoint(pos):
        if scene_no == 2:
            pass
        else:
            scene_no = 2
            video_init()
            sequence_init()
            path_video = "Test_RSC_SY/video_5.mp4"
            # thread_1.start()
            # playsound(file_name)
            sound.play()
    elif button_scene3.collidepoint(pos):
        if scene_no == 3:
            pass
        else:
            scene_no = 3
            video_init()
            sequence_init()
            rect_black = pygame.Rect(0, 360, 1920, 720)
            pygame.draw.rect(screen, BLACK, rect_black)
            path_sequence = "Test_RSC_SY/Rookie_cut"
            # playsound(file_name)
            sound.play()

def play_video():
    global playing, screen, path_video, video
    if playing == False:
        playing = True
        print("playing is True")
        video = cv2.VideoCapture(path_video)
        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
            screen.blit(video_surf, (0, 0))
        else:
            playing = False
            path_video = None
            video = None
    else:
        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
            screen.blit(video_surf, (0, 0))
        else:
            playing = False
            path_video = None
            video = None
    
def play_sequence():
    global path_sequence, list_sequence, current_sequence
    if current_sequence == 0:
        for (root, directories, files) in os.walk(path_sequence):
             for file in files:
                list_sequence.append(file)
        img = pygame.image.load(os.path.join(path_sequence, list_sequence[current_sequence]))
        screen.blit(img, (270, 590))
        current_sequence += 1
    else:
        img = pygame.image.load(os.path.join(path_sequence, list_sequence[current_sequence]))
        screen.blit(img, (270, 590))
        current_sequence += 1
        if current_sequence == len(list_sequence):
            path_sequence = None
            list_sequence.clear()
            current_sequence = 0

############################################################################
# initialization


pygame.init()
screen_width = 1080
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Control Panel")

# FPS
# clock = pygame.time.Clock()
############################################################################

# 1. 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

#SOUND
text = '지금 갈 수 있어요'
file_name = 'you_can_pass.wma'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
sound = pygame.mixer.Sound(file_name)

#COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
SELECTED = (255, 255, 255)
NORMAL = (0, 0, 0)

# Text
sai_font = pygame.font.Font(None, 32)

text_scene1 = sai_font.render("Scene # 1", False, GRAY)
text_scene2 = sai_font.render("Scene # 2", False, GRAY)
text_scene3 = sai_font.render("Scene # 3", False, GRAY)

button_scene1 = pygame.Rect(0, 54*0, 220, 54)
button_scene2 = pygame.Rect(0, 54*1, 220, 54)
button_scene3 = pygame.Rect(0, 54*2, 220, 54)

img_scene1 = pygame.image.load("Test_RSC_SY/scene_1.png")
img_scene2 = pygame.image.load("Test_RSC_SY/scene_2.png")
img_scene3 = pygame.image.load("Test_RSC_SY/scene_3.png")

# Video
video = None
playing = False
path_video = None

# Sequence
path_sequence = None
list_sequence = []
current_sequence = 0
# video = cv2.VideoCapture("video_1.mp4")
# success, video_image = video.read()
# fps = video.get(cv2.CAP_PROP_FPS)

scene_no = 1

clock = pygame.time.Clock()
fps = 60
running = True
while running:
    # print("path_video = {} / playing = {}".format(path_video, playing))
    print("************")
    print(current_sequence)
    print("fps : " + str(clock.get_fps()))
    dt = clock.tick(fps)
    click_pos = None

    # 2. 이벤트 입력 판단
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    # 3. 위치 정의
    
    
    # 4. 이벤트 처리 및 그리기
    screen.fill(BLACK)

    if click_pos:
        check_buttons(click_pos)
    
    if path_video:
        play_video()

    if path_sequence:
        play_sequence()

    draw_tab_list()

    # 5. 화면에 그리기
    
    pygame.display.update() # 게임화면을 다시 그리기

pygame.quit()
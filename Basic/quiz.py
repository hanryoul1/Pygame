"""
Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경 : 640 * 480 
2. 캐릭터 : 70 * 70
3. 똥 : 70 * 70 
"""

import pygame
import random

######################################################################################################
# 기본 초기화 (반드시 필요)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()
######################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)
# 배경 만들기
back = pygame.image.load('C:\\Users\\한률\\Desktop\\VSC\Pygame\\Basic\\image\\back.png')

# 캐릭터 만들기
character = pygame.image.load('C:\\Users\\한률\\Desktop\\VSC\Pygame\\Basic\\image\\dog.png')
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2)  - (character_width / 2) 
character_y_pos = screen_height - character_height 

# 이동 위치
to_x = 0
charcater_speed = 10

# 적 만들기
enemy = pygame.image.load('C:\\Users\\한률\\Desktop\\VSC\Pygame\\Basic\\image\\ddong.png')
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = random.randint(0, (screen_width - enemy_width))
enemy_y_pos = 0 
enemy_speed = 10
 
# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)
running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽으로
                to_x -= charcater_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽으로
                to_x += charcater_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0 
        enemy_x_pos = random.randint(0, (screen_width - enemy_width))

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(back, (0, 0)) # 배경 그리기 / (0, 0) 기준으로 오른쪽 아래로 그려짐
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    pygame.display.update() 

pygame.time.dely(2000)
pygame.quit()
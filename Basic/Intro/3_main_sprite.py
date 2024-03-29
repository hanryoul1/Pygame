import pygame

# 초기화 (반드시 필요)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My Pygame")

# 배경 이미지 불러오기
back = pygame.image.load('C:\\Users\\한률\\Desktop\\VSC\Pygame\\Basic\\image\\back.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(('C:\\Users\\한률\\Desktop\\VSC\Pygame\\Basic\\image\\dog.png'))
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2)  - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기의 가장 아래에 해당하는 곳에 위치

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False 

    #screen.fill((0, 0, 255))
    screen.blit(back, (0, 0)) # 배경 그리기 / (0, 0) 기준으로 오른쪽 아래로 그려짐
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면 다시 그리기

# Pygame 종료 
pygame.quit()

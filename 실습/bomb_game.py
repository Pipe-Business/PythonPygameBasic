# 파이게임으로 만든 파이썬 파일 exe 로 바꾸기
# >>> pyinstaller -w -F -n=바꾸고싶은이름 --icon=아이콘경로 변환시킬파이썬파일
#
# -w : 콘솔창 출력을 안함
# -F : 하나의 파일로 추출
# -n : 바꾸고싶은 파일 이름
# -icon : 실행파일의 아이콘 (.icon)
# 파이게임 라이브러리 불러오기
import pygame
import random

# 게임 화면 상태값
GAME_MAIN = 1
GAME_OVER = 2

# RGB 색상값
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_SKYBLUE = (136, 206, 250)
COLOR_BROWN = (222, 184, 135)
COLOR_PRIMARY = (150, 200, 100)

# 파이게임 초기화
pygame.init()

# 폰트 지정
font25 = pygame.font.SysFont("consolas", 25)
font50 = pygame.font.SysFont("consolas", 50)
font100 = pygame.font.SysFont("consolas", 100)

# 배경음악 불러오기
pygame.mixer.music.load("background_music.mp3")
# 배경음악 무한 재생
pygame.mixer.music.play(-1)
# 게임 오버 사운드 불러오기
sound_game_over = pygame.mixer.Sound("game_over.mp3")

# 화면 설정
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 캡션 제목
pygame.display.set_caption("폭탄피하기 게임")
# 아이콘
icon_image = pygame.image.load("bomb.png")
pygame.display.set_icon(icon_image)

# 다시하기 버튼 정보
RESTART_BUTTON_WIDTH = 400
RESTART_BUTTON_HEIGHT = 150
restart_button = pygame.Rect(SCREEN_WIDTH // 2 - RESTART_BUTTON_WIDTH // 2, 600, RESTART_BUTTON_WIDTH,
                             RESTART_BUTTON_HEIGHT)

# 내 캐릭터 불러오기
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (100, 100))  # 원한는 사이즈로 이미지 변환
player_rect = player_image.get_rect()
player_rect.x = SCREEN_WIDTH // 2 - player_rect.width // 2
player_rect.y = SCREEN_HEIGHT - player_rect.height - 5
player_speed = 5

# 폭발 이미지 불러오기
explosion_image = pygame.image.load("explosion.png")
explosion_image = pygame.transform.scale(explosion_image, (50, 50))

# 폭탄 이미지 불러오기
bomb_image = pygame.image.load("bomb.png")
bomb_image = pygame.transform.scale(bomb_image, (50, 50))
bomb_rect = bomb_image.get_rect()

# 폭탄에대한 상태 값
bomb_interval_timer = 1500  # 밀리초단위
bomb_min_speed = 3  # 폭탄이 떨어지는 최소 속도
bomb_max_speed = 5  # 폭탄이 떨어지는 최대 속도
bomb_gen_count = 1  # 한번에 떨어지는 폭탄 수

# 폭탄 좌표 데이터
bombs = list()  # []

# 플레이어의 게임 스코어
score = 0

# FPS 설정
clock = pygame.time.Clock()
FPS = 60

# 커스텀 이벤트
bomb_event = pygame.USEREVENT + 1
timer_event = pygame.USEREVENT + 2


def draw_button(screen, rect, message):
    pygame.draw.rect(screen, COLOR_BLACK, rect, border_radius=30)
    message_text = font50.render(message, True, COLOR_WHITE)
    screen.blit(message_text, (SCREEN_WIDTH // 2 - message_text.get_width() // 2, 650))


def gen_bomb(x_pos):
    rect = bomb_image.get_rect()
    rect.x = x_pos
    rect.y = random.randint(-300, -50)
    rand_speed = random.uniform(bomb_min_speed, bomb_max_speed)
    return {"rect": rect, "speed": rand_speed}


# 게임 초기화
def init_game():
    global player_speed, score, bomb_interval_timer, bomb_min_speed, bomb_max_speed, bomb_gen_count, bombs
    # global, python mutable 객체의 call by reference
    player_rect.x = SCREEN_WIDTH // 2 - player_rect.width // 2
    player_rect.y = SCREEN_HEIGHT - player_rect.height - 5
    player_speed = 5
    score = 0
    bombs = []
    bomb_interval_timer = 1500  # 밀리초단위
    pygame.time.set_timer(bomb_event, bomb_interval_timer)
    bomb_min_speed = 3  # 폭탄이 떨어지는 최소 속도
    bomb_max_speed = 5  # 폭탄이 떨어지는 최대 속도
    bomb_gen_count = 1  # 한번에 떨어지는 폭탄 수

def handle_game_score(score):
    global bomb_interval_timer,bomb_gen_count,bomb_min_speed,bomb_max_speed,player_speed
    if score == 10:
        bomb_interval_timer = 1200
        pygame.time.set_timer(bomb_event,bomb_interval_timer)
        bomb_min_speed = 4
        bomb_max_speed = 6
    elif score == 20:
        bomb_gen_count = 2
        player_speed = 6
    elif score == 30:
        bomb_interval_timer = 800
        pygame.time.set_timer(bomb_event, bomb_interval_timer)
        bomb_min_speed = 5
        bomb_max_speed = 8
        player_speed = 7
    elif score == 40:
        bomb_gen_count = 3
        bomb_min_speed = 6
        bomb_max_speed = 9
        player_speed = 7

def main_game():
    global score, state
    is_running = True
    state = GAME_MAIN
    pygame.time.set_timer(bomb_event, bomb_interval_timer)
    pygame.time.set_timer(timer_event, 1000)
    while is_running:
        for event in pygame.event.get():
            # 닫기 창 눌렀을 때
            if event.type == pygame.QUIT:
                is_running = False
            # 게임 화면일때 이벤트
            if state == GAME_MAIN:
                if event.type == timer_event:
                    score += 1
                    handle_game_score(score)
                if event.type == bomb_event:
                    # 폭탄의 랜덤한 위치에 일정한 간격, 중복 되지 않는 위치에 폭탄이 떨어짐
                    # 일정 폭탄크기에 맞는 range list
                    rand_x_post_list = list(range(0, SCREEN_WIDTH, bomb_rect.width))
                    random.shuffle(rand_x_post_list)
                    for x in range(bomb_gen_count):
                        bomb = gen_bomb(rand_x_post_list[x])
                        # bombs 데이터에 폭탄에 대한 정보(폭탄 좌표,폭탄이 떨어지는속도)
                        bombs.append(bomb)
            # 게임 오버일때 이벤트
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()  # [x,y] 파이썬 패킹과 언패킹
                    # restart 버튼이 클릭됬을 때
                    if restart_button.collidepoint(x, y):
                        init_game()
                        pygame.mixer.music.play(-1)
                        state = GAME_MAIN

        if state == GAME_MAIN:
            # 게임 배경 그리기
            screen.fill(COLOR_SKYBLUE)
            pygame.draw.rect(screen, COLOR_BROWN, (0, 600, SCREEN_WIDTH, 200))
            # 게임 스코어 표시
            score_text = font25.render(f"score : {score}", True, COLOR_BLACK)
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 5))
            keys = pygame.key.get_pressed()
            # 왼쪽 방향키를 눌렸을때
            if keys[pygame.K_LEFT]:
                player_rect.x -= player_speed
                # 좌측 벽으로 나갔을때
                if player_rect.x < 0:
                    player_rect.x = 0
            # 오른쪽 방향키를 눌렸을때
            if keys[pygame.K_RIGHT]:
                player_rect.x += player_speed
                # 우측 벽으로 나갔을때
                if player_rect.x >= SCREEN_WIDTH - player_rect.width:
                    player_rect.x = SCREEN_WIDTH - player_rect.width
            screen.blit(player_image, player_rect)
            # 폭탄의 좌표가 바닥으로 가게 업데이트
            for bomb in bombs:
                bomb['rect'].y += bomb['speed']

            # 폭탄의 좌표가 바닥에 가면 값 삭제
            for bomb in bombs:
                if bomb['rect'].y >= SCREEN_HEIGHT:
                    bombs.remove(bomb)

            # 폭탄의 좌표를 화면에 그림
            for bomb in bombs:
                player_mask = pygame.mask.from_surface(player_image)
                bomb_mask = pygame.mask.from_surface(bomb_image)
                offset = (bomb['rect'].x - player_rect.x, bomb['rect'].y - player_rect.y)
                collision = player_mask.overlap(bomb_mask, offset)
                if collision:
                    screen.blit(explosion_image, bomb['rect'])
                    pygame.display.flip()
                    pygame.mixer.music.stop()
                    sound_game_over.play()
                    pygame.time.wait(1000)
                    # 게임 오버 화면으로 전환
                    state = GAME_OVER
                screen.blit(bomb_image, bomb['rect'])
        # 게임 오버
        else:
            screen.fill(COLOR_PRIMARY)
            # GameOver 텍스트
            title_text = font100.render("Game Over", True, COLOR_BLACK)
            screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
            # score 텍스트
            score_info_text = font50.render("score", True, COLOR_BLACK)
            screen.blit(score_info_text,
                        (SCREEN_WIDTH // 2 - score_info_text.get_width() // 2, 100 + title_text.get_height() + 20))
            # 실제 score 텍스트
            score_text = font100.render(str(score), True, COLOR_BLACK)
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2,
                                     100 + title_text.get_height() + 20 + score_info_text.get_height() + 30))
            # 다시하기 버튼
            draw_button(screen, restart_button, "restart")

        # 화면을 업데이트
        pygame.display.flip()
        clock.tick(FPS)


init_game()
main_game()

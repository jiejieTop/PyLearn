import pygame

pygame.init()   #init pygame
# 创建时钟对象
clock = pygame.time.Clock()

# print("come on")    #test
#
# r_rect = pygame.Rect(1,10,10,10)
# print(" x = %d , y = %d "%(r_rect.x , r_rect.y))
# print(" width = %d , height = %d "%(r_rect.width , r_rect.height))

# 创建游戏窗口
screen = pygame.display.set_mode((480,800))

# 加载背景到内存
# bg = pygame.image.load("./Resources/startone.png")
# screen.blit(bg,(0,0))
#
# start = pygame.image.load("./Resources/Pause.png")
# screen.blit(start,(212,450))
#
# pygame.display.update()

# 加载图像到内存
bg = pygame.image.load("./Resources/bg_01.png")
hero = pygame.image.load("./Resources/hero.png")

hero_rect = pygame.Rect(200,600,72,72)

while True:
    # 指定循环体内部代码执行的频率
    clock.tick(60)

    # 移动飞机
    hero_rect.y -= 2
    if (hero_rect.y + 72) <= 0:
        hero_rect.y = 800

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            exit()





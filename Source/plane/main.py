import pygame

pygame.init()   #init pygame
#
# print("come on")    #test
#
# r_rect = pygame.Rect(1,10,10,10)
# print(" x = %d , y = %d "%(r_rect.x , r_rect.y))
# print(" width = %d , height = %d "%(r_rect.width , r_rect.height))
#


screen = pygame.display.set_mode((480,800))

# 加载背景到内存
bg = pygame.image.load("./Resources/background.png")

screen.blit(bg,(0,0))

pygame.display.update()

while True:
    pass

pygame.quit()   #exit pygame






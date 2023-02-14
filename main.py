import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255,165,0)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)


dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25) #Укажем название шрифта и его размер для системных сообщений, например, при завершении игры.
score_font = pygame.font.SysFont("comicsansms", 35) #Укажем шрифт и  его размер для отображения счёта.

width = dis.get_width()
height = dis.get_height()
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('Выход', True, white)
text_1 = smallfont.render('Игра', True, white)


def Your_score(score):
   value = score_font.render("Ваш счёт: " + str(score), True, yellow)
   dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 6, dis_height / 3])




def gameLoop():
   game_over = False
   game_close = False
   x1 = dis_width / 2
   y1 = dis_height / 2
   x1_change = 0
   y1_change = 0
   snake_List = [] #Создаём список, в котором будем хранить показатель текущей длины змейки.
   Length_of_snake = 1
   foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
   foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
   while not game_over:
       while game_close == True:
           dis.fill(orange)
           message("Вы проиграли! Нажмите Q для выхода или C для перезапуска", red)
           Your_score(Length_of_snake - 1)
           pygame.display.update()
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                       menuLoop()
                   if event.key == pygame.K_c:
                       gameLoop()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_over = True
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   x1_change = -snake_block
                   y1_change = 0
               elif event.key == pygame.K_RIGHT:
                   x1_change = snake_block
                   y1_change = 0
               elif event.key == pygame.K_UP:
                   y1_change = -snake_block
                   x1_change = 0
               elif event.key == pygame.K_DOWN:
                   y1_change = snake_block
                   x1_change = 0
       if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           game_close = True
       x1 += x1_change
       y1 += y1_change
       dis.fill(orange)
       pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
       snake_Head = [] #Создаём список, в котором будет храниться показатель длины змейки при движениях.
       snake_Head.append(x1) #Добавляем значения в список при  изменении по оси х.
       snake_Head.append(y1) #Добавляем значения в список при  изменении по оси y.
       snake_List.append(snake_Head)
       if len(snake_List) > Length_of_snake:
           del snake_List[0] #Удаляем первый элемент в списке  длины змейки, чтобы она не увеличивалась сама по себе при движениях.
       for x in snake_List[:-1]:
           if x == snake_Head:
               game_close = True
       our_snake(snake_block, snake_List)
       Your_score(Length_of_snake - 1)
       pygame.display.update()
       if x1 == foodx and y1 == foody: #Указываем, что в случаях, если координаты головы змейки совпадают с координатами еды, еда появляется в новом месте, а длина змейки увеличивается на одну клетку.
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           Length_of_snake += 1
       clock.tick(snake_speed)
   pygame.quit()
   quit()

def menuLoop():
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()


            if ev.type == pygame.MOUSEBUTTONDOWN:

                if 325 <= mouse[0] <= 325 + 140 and 200 <= mouse[1] <= 200 + 40:
                    gameLoop()

                elif 325 <= mouse[0] <= 325 + 140 and 400 <= mouse[1] <= 400 + 40:
                    pygame.quit()

        dis.fill(yellow)

        if 325 <= mouse[0] <= 325 + 140 and 200 <= mouse[1] <= 200 + 40:
            pygame.draw.rect(dis, color_light, [325, 200, 140, 40])

        else:
            pygame.draw.rect(dis, color_dark, [325, 200, 140, 40])

        if 325 <= mouse[0] <= 325 + 140 and 400 <= mouse[1] <= 400 + 40:
            pygame.draw.rect(dis, color_light, [325, 400, 140, 40])

        else:
            pygame.draw.rect(dis, color_dark, [325, 400, 140, 40])

        dis.blit(text, (350, 400))
        dis.blit(text_1, (350, 200))
        pygame.display.update()

menuLoop()

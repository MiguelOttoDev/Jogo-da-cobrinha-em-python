import pygame
import sys
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('JOGO DA COBRA')

clock = pygame.time.Clock()

snake_block = 10

font_style = pygame.font.SysFont(None, 50)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def game_over_screen(score):
    dis.fill(black)
    game_over_font = pygame.font.SysFont(None, 75)
    game_over_Surf = game_over_font.render('Seu score é: ' + str(score), True, white)  # Corrigindo a função render
    game_over_Rect = game_over_Surf.get_rect()
    game_over_Rect.midtop = [dis_width/2, dis_height/4]
    dis.blit(game_over_Surf, game_over_Rect)
    pygame.display.flip()
    pygame.time.wait(1500)

def gameLoop():
    print("Iniciando o loop do jogo...")
    game_over = False
    x1, y1 = dis_width / 2, dis_height / 2
    x1_change, y1_change = 0, 0 
    snake_list = []
    snake_speed = 15
    length_of_snake = 1
    foodx, foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0, round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Evento de saída detectado. Encerrando o jogo...")
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change, y1_change = -snake_speed, 0 
                if event.key == pygame.K_RIGHT:
                    x1_change, y1_change = snake_speed, 0 
                if event.key == pygame.K_UP:
                    x1_change, y1_change = 0, -snake_speed
                if event.key == pygame.K_DOWN:
                    x1_change, y1_change = 0, snake_speed
    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            print("A cobra colidiu com a parede. Encerrando o jogo...")
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                print("A cobra colidiu consigo mesma. Encerrando o jogo...")
                game_over = True

        our_snake(snake_block, snake_list)

        pygame.display.update()

        if foodx <= x1 <= foodx + snake_block and foody <= y1 <= foody + snake_block:
            print("Colisão com o alimento! Cabeça da cobra:", x1, y1, "Alimento:", foodx, foody)
            foodx, foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0, round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            print("Alimento reposicionado em:", foodx, foody)
            length_of_snake += 1
            
        
        clock.tick(snake_speed)
    
    game_over_screen(length_of_snake - 1)
    pygame.quit()
    quit()

print("Inicializando o jogo...")
gameLoop()
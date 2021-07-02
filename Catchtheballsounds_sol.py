
import pygame, sys, random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
game_font=pygame.font.Font('freesansbold.ttf', 12)
gameover_font=pygame.font.Font('freesansbold.ttf', 32)
over=gameover_font.render("",False,(200,200,200))
screen = pygame.display.set_mode((500,500))
score=0

#load sounds here
over_sound=pygame.mixer.Sound("over1.wav")
blast_sound=pygame.mixer.Sound("hit01.wav")


#creating objects of game
ball=pygame.Rect(250,100,20,20)
player=pygame.Rect(225,470,80,20)
playerSpeed=15



while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x=player.x - playerSpeed
            if event.key == pygame.K_RIGHT:
                player.x = player.x + playerSpeed
    
    ball.y=ball.y+5
    
    
    if(ball.colliderect(player)):
        ball.y=-20
        ball.x=random.randint(0, 480)
        score=score+1 
        pygame.mixer.Sound.play(blast_sound)
        
    if(ball.y==505):
        over=gameover_font.render("Game Over",False,(200,200,200))
        player.y=-1000
        pygame.mixer.Sound.play(over_sound)
        
        
    scoretext=game_font.render("Score : " + str(score),False,(150,200,200))
    screen.blit(scoretext,(10,10))
    screen.blit(over,(160,200))
    pygame.draw.rect(screen,(223,100,100),ball)
    pygame.draw.rect(screen,(225,225,225),player)
    
    pygame.display.update()
    clock.tick(30)






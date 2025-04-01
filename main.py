import pygame
import copy
import  pygame.freetype as freetype
from mymodule.tileMap import TileMap
from time import sleep
from  mymodule.Snake import Snake, Animate,Direction




# Python Snake Game: A Nostalgic Coding Journey

# This Python-based Snake implementation reimagines the classic arcade experience through modern programming practices. Designed as an educational project for coding beginners, it demonstrates:

# ✔️ Core Programming Concepts: Object-oriented design, collision detection, and score tracking
# ✔️ Beginner-Friendly Architecture: Clean modular structure with detailed code comments
# ✔️ Customization Ready: Easily modifiable parameters (grid size/speed/visuals) via config.py

# Educational Value:

# Ideal for learning game loop mechanics and event handling

# Showcases Pygame integration with 200+ lines of didactic code

# Includes debugging tips and performance optimization notes

# License & Attribution:
# Developed by XuJu Zhong (钟旭炬) under MIT License.
# ▸ For source code sharing/modification:

# Retain original author credit in header comments

# Preserve license file in distribution

# Contact Developer:
# 📧 2756447543@qq.com
# 📱 (+86) 182-7648-9248

# Your feedback and suggestions are valuable for improving this learning resource!





# to begin the snake game:
#     use ArrowUp         ^   for                    up control;
#     use ArrowLeft       <   for                    left control; 
#     use ArrowRight      >   for                    right control;
#     use ArrowDown  (you can guess it !) for        down control;

# have a fun!


def  end(map,surface,snake):
        
    font=freetype.Font('./data/stsong.ttf',50)
    text=f" 游戏结束了,你的得分:{snake.score}"
    text_img,_=font.render(text,(255,42,78),(0,78,23))
    text_rect=text_img.get_rect( )
    text_rect.center=(TileMap.width//2,TileMap.height//2)

    map.draw_wall()
    map.redrawline()

    surface.blit(text_img,text_rect)

    pygame.display.update()

    finished=False

    while  not finished:
        
        for event in pygame.event.get():
            if  event.type==pygame.QUIT:
                finished=True



def  gamer():
    pygame.init()

    clock=pygame.time.Clock()

    TileMap.set_environment(1000,600)
    background=(0,78,23)

    finished=False

    animate=Animate()

    map=TileMap(24,40,background=background,back="./data/background.mp3")
    surface=TileMap.surface

    snake=Snake(map=map,surface=surface,animate=animate)

    step=0

    fps=2


    map.play_back()


    dir=0

    start=False

    while  not finished:
        
        for event in pygame.event.get():
            if  event.type==pygame.QUIT:
                finished=True
            if event.type==pygame.KEYDOWN:
                start=True
                if  event.unicode=='W' or event.key==pygame.K_UP:
                    dir=Direction.up
                elif event.unicode=='S' or event.key==pygame.K_DOWN:
                    dir=Direction.down
                elif event.unicode =='A' or event.key==pygame.K_LEFT:
                    dir=Direction.left
                elif    event.unicode=='D' or event.key==pygame.K_RIGHT:
                    dir=Direction.right

                
                    
        surface.fill((0,0,0))
        map.draw()
        if start:
            finished=snake.human_play(dir)

        snake.draw()
        map.redrawline()
        animate.step()
        pygame.display.update()
        clock.tick(fps)
        step+=1
        
        pygame.display.update()
    
    end(map=map,surface=surface,snake=snake)
            
    pygame.quit()



gamer()
import pygame, os, sys
from pygame.locals import *
from Walls import Walls
from snake import Snake
from apple import *
from constants import *
from tkinter import *


os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

screen = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption('Snake')

walls_list = Walls.createList(Walls(), cell_size)

def print_text(font, text, textpos = None):
    font = pygame.font.SysFont(font[0], font[1])
    text = font.render(text, 1, color)
    if textpos is None:
        textpos = text.get_rect(centerx = window_w / 2, centery = window_h / 2)
    screen.blit(text, textpos)
    
def draw_text():
    text = "Apples: {} Points: {} Lives: {}".format(apple.count, hero.points, "-" * hero.lives)
    print_text(Score_Font, text, green, (10, 10))

def draw_walls():
    for wall in walls_list:
        pygame.draw.rect(screen, pygame.Color("blue"), wall, 0)
        
def ate_apple():
    head = hero.body[0]
    head_rect = pygame.Rect((head[0] * cell_size, head[1] * cell_size, cell_size, cell_size))
    return head_rect.colliderect(apple.rect)

def countdown():
    global start, seconds
    
    pygame.time.wait(1000)
    screen.fill(black)
    print_text(Large_font, "{}".format(seconds), white)
    seconds -= 1
    pygame.display.flip()
    
def write_files():
    try:
        f = open("results.txt", "r")
        n = f.read().count(player_name) + 1
        f.close()
    except FileNotFoundError:
        f = open("results.txt", "w")
        f.close()
        n = 0
    f = open("results.txt", "a")
    f.write("{} {} {} \n".format(player_name + str(n), apple.count, hero.points))
    f.close()
    
def pop_up(msg):
    popupwin  = Tk()
    
    def center(win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry("+%d+%d" % (x, y))
        
    center(popupwin)
    
    def set_name(event = None):
        global player_name
        player_name = entry.get().strip()
        if not player_name:
            player_name = 'Anonymous'
        
        popupwin.destroy()
    
    popupwin.title("!")
    label = Label(popupwin, text=msg, font=Norm_Font)
    label.pack(side = "top", fill="x", pady = 10)
    
    entry = Entry(popupwin, width=15)
    entry.pack()
    entry.insert(0, 'Anonymous')
    entry.blind()
    entry.focus_set()
    
    b1 = Button(popupwin, text="Okey", command=set_name)
    b1.pack()
    
    popupwin.mainloop()
        

hero = Snake(image)

clock = pygame.time.Clock()
apple = Apple(cell_size)
start = False
game_over = False
seconds = 3


def main():
    global start, game_over
    pop_up("Enter Your Name, PLease")
    
    hero.draw(screen)
    apple.draw(screen)
    draw_walls()
    draw_text()
    
    while seconds > 0:
        countdown()
    start = True
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if not game_over:
                    write_files()
                pygame.quit()
                sys.exit()
                break
            elif event.type == pygame.KEYDOWN:
                hero.set_direction(event.key)
            elif event.type == pygame.KEYUP:
                hero.speed = 10
            
        screen.fill(black)
        draw_walls()
        draw_text()
        hero.draw(screen)
        apple.draw(screen)
        
        if not game_over:
            hero.move()
            
            if ate_apple():
                hero.points += apple.size
                apple.set_random_xy()
                Apple.count += 1
            else:
                hero.body.pop()
        
        if hero.hit_Walls(walls_list):
            apple.set_random_xy()
            if hero.lives <= 0:
                game_over = True
                print_text(Large_font, red)
        
        clock.tick(hero.speed)
        
        pygame.display.flip()
        if game_over:
            write_files()
            pygame.time.wait(2000)
            break

        
        
    
if __name__ == "__main__":
    main()
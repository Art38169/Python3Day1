import pygame
import sys
import random

class Circle:
    def __init__(self, radius, x, y, vx, vy):
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def draw(self, screen):
        pygame.draw.circle(screen, self_color, (self.x, self.y), self.radius)

    def move(self, min_x, min_y, max_x, max_y):
        self.x += self.vx
        self.y += self.vy
        if self.x > max_x or self.x < min_x:
            self.vx = -self.vx
        if self.y > max_y or self.y < min_y:
            self.vy = -self.vy

window_width = 500
window_height = 500
N = 10
circles = []
for i in range(N):
    circles.append(Circle(random.randint(1, 20), 
                          random.randint(1, 100), 
                          random.randint(1, 100), 
                          random.randint(1, 10), 
                          random.randint(1, 10)))
    




pygame.init()

screen = pygame.display.set_mode((window_width, window_height))
bg_color = (30, 30, 30)
self_color = (0, 200, 0)
pygame.display.set_caption("Flying circle")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill(bg_color)
    for i in range(N):
        circles[i].draw(screen)
        circles[i].move(0, 0, window_width, window_height)
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
 
    
    
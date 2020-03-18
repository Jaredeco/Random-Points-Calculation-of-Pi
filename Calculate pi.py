import pygame
from pygame import gfxdraw
import random
from math import sqrt
from math import pi

pygame.init()
pygame.display.set_caption('Calculating the Value of Pi')
screen_width = 400
screen_height = 400
win = pygame.display.set_mode((screen_width, screen_height))
red = (238, 59, 59)
green = (127, 255, 0)
blue = (0, 255, 255)
gfxdraw.rectangle(win, (-200, -200, screen_width, screen_height), red)
r = 200
circle_count = 0
total = 0
actual_pi = pi
best_pi = 0
cal_true = ""

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for i in range(1000):
        x = random.randrange(-200, 200)
        y = random.randrange(-200, 200)
        d = sqrt((x ** 2) + (y ** 2))
        total += 1
        if d < r:
            circle_count += 1
            color = blue
        else:
            color = green
        PI = 4 * (circle_count / total)
        gfxdraw.pixel(win, x, y, color)
        diff = abs(actual_pi - PI)
        best_diff = abs(PI - best_pi)
        if diff < best_diff:
            best_diff = diff
            best_pi = PI
            answer = ""
            len1, len2 = len(str(pi)), len(str(best_pi))
            for i in range(len1):
                match = ""
                for j in range(len2):
                    if i + j < len1 and str(pi)[i + j] == str(best_pi)[j]:
                        match += str(best_pi)[j]
                    else:
                        if len(match) > len(answer): answer = match
                        match = ""
            print('The best calculated value: ' + str(best_pi) + '     Pi matching: ' + answer)
    pygame.draw.circle(win, red, (0, 0), r, 1)
    pygame.display.update()
pygame.quit()

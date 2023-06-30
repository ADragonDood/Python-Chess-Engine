import json

import pygame
from pygame.locals import *

BG_COLOUR = "#242526"

with open("info.json", "r") as info_file:
    version_number = json.load(info_file)["version"]

window_width = window_height = 1000
window = pygame.display.set_mode((window_width, window_height), vsync=1)

pygame.display.set_caption(f"Python Chess Engine | {version_number}")

running = True

while running:
    window.fill(BG_COLOUR)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    
    pygame.display.flip()
pygame.quit()
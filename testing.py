#/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pygame
import settings

### Caption ###
pygame.display.init()
pygame.font.init()
pygame.display.set_caption("Bobots - OcaStudios")

os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.set_reserved(3)
pygame.init()


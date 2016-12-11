# Copyright 2016 Zara Zaimeche

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Basic skeleton for a space-invaders type of game

import pygame, sys, random
from pygame.locals import *
from sampleconfig import *


main_clock = pygame.time.Clock()
pygame.init()

window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

BLACK = Color('black')

GAPSIZE = 2

player_location = 0 #to start

WHITE = Color('white')
player_colour = WHITE

GREEN = Color('green')
alien_colour = GREEN

alien_rects = []
for i in range(COLUMNS/2):
    alien_rect = pygame.Rect(i*2*COLUMNWIDTH+ COLUMNWIDTH, 0, ALIENSIZE*(2*COLUMNWIDTH)-GAPSIZE, ALIENSIZE*ROWHEIGHT)
    alien_rects.append(alien_rect)
aliens = []

for rect in alien_rects:
    alien = {"rect":rect, "colour":alien_colour}
    aliens.append(alien)

print aliens

BLUE = Color('blue')
RED = Color('red')

def move_player(direction, player_location):
    if direction == "left":
        # check player won't go offscreen
        if player_location - PLAYERSPEED*COLUMNWIDTH >= 0:
            player_location = player_location - (PLAYERSPEED * COLUMNWIDTH)
        else:
            player_location = 0
    if direction == "right":
        if player_location + PLAYERSPEED*COLUMNWIDTH <= (COLUMNS*COLUMNWIDTH)-COLUMNWIDTH:
            player_location = player_location + (PLAYERSPEED *COLUMNWIDTH)
        else:
            player_location = COLUMNS*COLUMNWIDTH-COLUMNWIDTH
    return player_location

def fire_lazer(player_location):
    lazer_rect=pygame.Rect(player_location, ROWS*ROWHEIGHT-ROWHEIGHT, 2, 4)#start lazer just above player
    lazer_colour = BLUE
    lazer = {"rect":lazer_rect, "colour":lazer_colour}
    lazers.append(lazer)

def make_enemy_lazer():
    shooters = [600] #hack so that doesn't crash if no aliens
    for alien in aliens:
        shooters.append(alien["rect"][0])
        #so alien can shoot from middle
        shooters.append(alien["rect"][0] + alien["rect"][3]/2)
        #so alien can shoot from right
        shooters.append(alien["rect"][0] + alien["rect"][3])
    random_column = random.choice(shooters)
    enemy_lazer_rect=pygame.Rect(random_column, 0, 2, 4)#start lazer at top
    enemy_lazer_colour = RED
    enemy_lazer = {"rect":enemy_lazer_rect, "colour":enemy_lazer_colour}
    enemy_lazers.append(enemy_lazer)


window_surface.fill(BLACK)
move_player_left = False
move_player_right = False
lazers = []
enemy_lazers = []
counter = 0
while True:

    # defined in the loop since the player's location changes
    player_rect = pygame.Rect(player_location, ROWS*ROWHEIGHT - ROWHEIGHT, PLAYERSIZE*COLUMNWIDTH, PLAYERSIZE*COLUMNWIDTH)
    player = {"rect":player_rect, "colour":player_colour}

    window_surface.fill(BLACK)
    for alien in aliens:
        pygame.draw.rect(window_surface, alien["colour"], alien["rect"])

    pygame.draw.rect(window_surface, player["colour"], player["rect"])

    if aliens == []:
        print 'You win!'
        pygame.quit()
        sys.exit()
    

    for event in pygame.event.get():
        if event.type== KEYDOWN:
            if event.key == K_SPACE:
                fire_lazer(player_location)
            elif event.key == K_LEFT:
                move_player_right = False
                move_player_left = True
            elif event.key == K_RIGHT:
                move_player_left = False
                move_player_right = True
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYUP:
            if event.key == K_LEFT:
                move_player_left = False
            elif event.key == K_RIGHT:
                move_player_right = False

    if move_player_right == True:
        player_location = move_player("right", player_location)
    elif move_player_left == True:
        player_location = move_player("left", player_location)

    if counter % LAZERRATE == 0:
        make_enemy_lazer()

    for enemy_lazer in enemy_lazers:
        enemy_lazer["rect"][1] += ROWHEIGHT
        pygame.draw.rect(window_surface, enemy_lazer["colour"], enemy_lazer["rect"])

    for lazer in lazers:
        lazer["rect"][1] -= ROWHEIGHT
        pygame.draw.rect(window_surface, lazer["colour"], lazer["rect"])

    for lazer in lazers[:]:
        for alien in aliens[:]:
            if lazer["rect"].colliderect(alien["rect"]):
                aliens.remove(alien)
            
    #this game will currently only work for one row of aliens
    for lazer in lazers[:]:
        if lazer["rect"][1] <=0:
            lazers.remove(lazer)

    for enemy_lazer in enemy_lazers[:]:
        if enemy_lazer["rect"].colliderect(player["rect"]):
            print("You lose!")
            pygame.quit()
            sys.exit()

    for enemy_lazer in enemy_lazers:
        if enemy_lazer["rect"][1] > ROWS * ROWHEIGHT:
            enemy_lazers.remove(enemy_lazer)
    print player_location
    pygame.display.update()
    main_clock.tick(FPS)
    counter +=1

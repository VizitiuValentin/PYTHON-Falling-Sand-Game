import pygame
from copy import deepcopy


def process_whole_map(MAP, DRAWING_POSITIONS):
    from main import WINDOW, sand, brick, water

    draw_to = pygame.Surface((1300, 650))
    for y, line in zip(range(129, 0, -1), reversed(MAP)):

        for x, particle in enumerate(line):
            if not particle:
                continue
            if y >= 129 or x >= 259 or x <= 0:
                continue

            if particle == 1:  # Sand
                draw_to.blit(sand, DRAWING_POSITIONS[y][x])

                if MAP[y + 1][x] == 0:
                    MAP[y][x] = 0
                    MAP[y + 1][x] = 1

                elif MAP[y + 1][x] == 2:
                    MAP[y][x] = 2
                    MAP[y + 1][x] = 1

                elif MAP[y + 1][x + 1] == 0:
                    MAP[y][x] = 0
                    MAP[y + 1][x + 1] = 1

                elif MAP[y + 1][x - 1] == 0:
                    MAP[y][x] = 0
                    MAP[y + 1][x - 1] = 1

            elif particle == 2:  # Water
                draw_to.blit(water, DRAWING_POSITIONS[y][x])

                if MAP[y + 1][x] == 0:
                    MAP[y][x] = 0
                    MAP[y + 1][x] = 2

                elif MAP[y + 1][x + 1] == 0:
                    MAP[y][x] = 0
                    MAP[y + 1][x + 1] = 2

                elif MAP[y + 1][x - 1] == 0:
                    MAP[y][x] = 0
                    MAP[y + 1][x - 1] = 2

                elif MAP[y][x + 1] == 0:
                    MAP[y][x] = 0
                    MAP[y][x + 1] = 2

                elif MAP[y][x - 1] == 0:
                    MAP[y][x] = 0
                    MAP[y][x - 1] = 2

            elif particle == 3:  # Brick
                draw_to.blit(brick, DRAWING_POSITIONS[y][x])

    WINDOW.blit(draw_to, (0, 0))


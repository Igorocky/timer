import sys

import pygame
import pygame.locals as pg
from pygame import Surface, SurfaceType

from arg_parser import make_argument_parser
from common import GRAY
from state import State

args = make_argument_parser().parse_args()
# args = make_argument_parser().parse_args(r'--time 5 --sound file.wav'.split())

pygame.init()
pygame.font.init()
pygame.mixer.init()

FPS = 10
fpsClock = pygame.time.Clock()

DISP: Surface | SurfaceType = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption('Timer')


def main() -> None:
    state = State(seconds=args.time, font_size=args.font, sound_file_path=args.sound)
    while True:
        state.update()
        handle_events(state)
        render_state(state)
        fpsClock.tick(FPS)


def handle_events(state: State) -> None:
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            shutdown()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                shutdown()
            else:
                state.on_key_pressed(event.key)


def render_state(state: State) -> None:
    if state.needs_rerender():
        DISP.fill(GRAY)
        state.render(DISP)
        state.mark_rendered()
        pygame.display.update()

def shutdown() -> None:
    pygame.quit()
    sys.exit()



if __name__ == '__main__':
    main()

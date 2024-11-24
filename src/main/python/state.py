import pygame
from pygame import SurfaceType, Surface
from pygame.font import Font

from common import unix_epoch_sec_now, seconds_to_hms, RED, GREEN


class State:
    def __init__(self, seconds: int, sound_file_path: str):
        self._max_dur = seconds
        self._sound_file_path = sound_file_path
        self._font: Font = pygame.font.SysFont('Comic Sans MS', 30)
        self._reset()
        self._mark_needs_rerender()

    def _reset(self) -> None:
        self._started_at = unix_epoch_sec_now()
        self._cur_dur = 0
        self._sound_played = False

    def _mark_needs_rerender(self) -> None:
        self._needs_rerender = True

    def mark_rendered(self) -> None:
        self._needs_rerender = False

    def needs_rerender(self) -> bool:
        return self._needs_rerender

    def update(self) -> None:
        cur_time = unix_epoch_sec_now()
        cur_dur = min(self._max_dur, cur_time - self._started_at)
        if cur_dur == self._max_dur and not self._sound_played:
            self._play_sound()
        if self._cur_dur != cur_dur:
            self._cur_dur = cur_dur
            self._mark_needs_rerender()

    def render(self, disp: Surface | SurfaceType) -> None:
        dur_remains = self._max_dur - self._cur_dur
        hms = seconds_to_hms(dur_remains)
        dur_str = ':'.join(str(digit).rjust(2, '0') for digit in hms)
        text_surf = self._font.render(dur_str, True, RED if dur_remains == 0 else GREEN)
        # text_surf = pygame.transform.smoothscale_by(text_surf, 1.0)
        text_rect = text_surf.get_rect()
        text_width = text_rect.width
        text_height = text_rect.height
        window_width, window_height = disp.get_size()
        text_rect.left = int(window_width / 2 - text_width / 2)
        text_rect.top = int(window_height / 2 - text_height / 2)
        disp.blit(text_surf, text_rect)

    def _play_sound(self) -> None:
        self._sound_played = True
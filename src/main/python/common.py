import datetime
import math
import time
from typing import Tuple
from warnings import catch_warnings

WHITE = (255, 255, 255)
YELLOW = (234, 221, 202)
YELLOWISH = (255, 250, 226)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
DARK_GRAY = (70, 70, 70)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

ON_TRACK = GREEN
RUN_OUT_OF_TIME = (210, 4, 45)

_seconds_in_minute = 60
_minutes_in_hour = 60
_seconds_in_hour = _seconds_in_minute * _minutes_in_hour


def unix_epoch_sec_now() -> int:
    now = datetime.datetime.now()
    return int(time.mktime(now.timetuple()))


def seconds_to_hms(seconds: int) -> Tuple[int, int, int]:
    assert seconds >= 0

    hours = math.floor(seconds / _seconds_in_hour)
    seconds = seconds - hours * _seconds_in_hour

    minutes = math.floor(seconds / _seconds_in_minute)
    seconds = seconds - minutes * _seconds_in_minute

    return hours, minutes, seconds


def hms_to_seconds(hms: Tuple[int, int, int]) -> int:
    return hms[0] * _seconds_in_hour + hms[1] * _seconds_in_minute + hms[2]

def str_to_hms(text:str) -> Tuple[int, int, int]:
    parts = [part.strip() for part in text.split(':')]
    if len(parts) < 1:
        raise Exception(f'len(parts) < 1 in "${text}"')
    if len(parts) > 3:
        raise Exception(f'len(parts) > 3 in "${text}"')
    for part in parts:
        try:
            int(part)
        except ValueError:
            raise ValueError(f'Cannot parse number "${text}"')
    while len(parts) < 3:
        parts.insert(0,'0')
    return tuple(int(p) for p in parts) # type: ignore[return-value]
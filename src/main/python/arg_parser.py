import argparse

from common import str_to_hms, hms_to_seconds


class TimeAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs) -> None:  # type: ignore[no-untyped-def]
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None) -> None:  # type: ignore[no-untyped-def]
        setattr(namespace, self.dest, hms_to_seconds(str_to_hms(values)))


def make_argument_parser() -> argparse.ArgumentParser:
    description = """
    When launched, this program starts to countdown the specified amount of time. 
    When the countdown reaches 0, it plays the specified sound if any.
    Use these keys to control the timer:
        Enter - restart the countdown;
        Space - stop playing the sound;
        Esc - exit.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-t', '--time', required=True, action=TimeAction,
                        help="The amount of time to countdown. Supported formats: h:m:s, m:s, s.")
    parser.add_argument('-f', '--font', default=300, type=int,
                        help="The font size to use for remaining time.")
    parser.add_argument('-s', '--sound',
                        help="The path to the file with the sound to play when the countdown reaches 0.")
    return parser

import argparse


def make_argument_parser() -> argparse.ArgumentParser:
    description="""
    When launched, this program starts to countdown the specified amount of time. 
    When the countdown reaches 0, it plays the specified sound if any.
    Use these keys to control the timer:
        Enter - restart the countdown;
        Space - stop playing the sound;
        Esc - exit.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-t', '--time', required=True,
                        help="The amount of time to countdown. Supported formats: h:m:s, m:s, s.")
    parser.add_argument('-f', '--font', default=300, type=int,
                        help="The font size to use for remaining time.")
    parser.add_argument('-s', '--sound',
                        help="The path to the file with the sound to play when the countdown reaches 0.")
    return parser

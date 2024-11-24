from io import StringIO
from unittest import TestCase

from arg_parser import make_argument_parser


class CommonTest(TestCase):
    def test__make_argument_parser__parses_arguments(self) -> None:
        # given
        parser = make_argument_parser()

        # when
        args = parser.parse_args(['--time', '2:30', '-f', '100', '--sound', '/some/path/file.wav'])

        # then
        self.assertEqual('2:30', args.time)
        self.assertEqual(100, args.font)
        self.assertEqual('/some/path/file.wav', args.sound)

    def test__make_argument_parser__returns_default_values_for_optional_arguments(self) -> None:
        # given
        parser = make_argument_parser()

        # when
        args = parser.parse_args(['--time', '2:30'])

        # then
        self.assertEqual('2:30', args.time)
        self.assertEqual(None, args.sound)

    def test__make_argument_parser__prints_help(self) -> None:
        # given
        parser = make_argument_parser()
        help_output = StringIO()

        # when
        args = parser.print_help(help_output)

        # then
        self.assertEqual(
        """usage: _jb_unittest_runner.py [-h] -t TIME [-f FONT] [-s SOUND]

When launched, this program starts to countdown the specified amount of time.
When the countdown reaches 0, it plays the specified sound if any. Use these
keys to control the timer: Enter - restart the countdown; Space - stop playing
the sound; Esc - exit.

options:
  -h, --help            show this help message and exit
  -t TIME, --time TIME  The amount of time to countdown. Supported formats:
                        h:m:s, m:s, s.
  -f FONT, --font FONT  The font size to use for remaining time.
  -s SOUND, --sound SOUND
                        The path to the file with the sound to play when the
                        countdown reaches 0.
""",
            help_output.getvalue()
        )

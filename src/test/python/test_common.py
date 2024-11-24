from unittest import TestCase

from common import seconds_to_hms, hms_to_seconds


class CommonTest(TestCase):
    def test_seconds_to_hms(self) -> None:
        self.assertEqual((0,0,0), seconds_to_hms(0))
        self.assertEqual((0,0,1), seconds_to_hms(1))
        self.assertEqual((0,0,59), seconds_to_hms(59))
        self.assertEqual((0,1,0), seconds_to_hms(60))
        self.assertEqual((0,1,1), seconds_to_hms(61))
        self.assertEqual((1,0,0), seconds_to_hms(60*60))
        self.assertEqual((1,0,1), seconds_to_hms(60*60+1))
        self.assertEqual((1,1,0), seconds_to_hms(60*60+60))
        self.assertEqual((1,1,1), seconds_to_hms(60*60+61))
        self.assertEqual((1,1,59), seconds_to_hms(60*60+60+59))

    def test_hms_to_seconds(self) -> None:
        self.assertEqual(0, hms_to_seconds((0,0,0)))
        self.assertEqual(1, hms_to_seconds((0,0,1)))
        self.assertEqual(59, hms_to_seconds((0,0,59)))
        self.assertEqual(60, hms_to_seconds((0,1,0)))
        self.assertEqual(61, hms_to_seconds((0,1,1)))
        self.assertEqual(60*60, hms_to_seconds((1,0,0)))
        self.assertEqual(60*60+1, hms_to_seconds((1,0,1)))
        self.assertEqual(60*60+60, hms_to_seconds((1,1,0)))
        self.assertEqual(60*60+61, hms_to_seconds((1,1,1)))
        self.assertEqual(60*60+60+59, hms_to_seconds((1,1,59)))
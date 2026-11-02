import unittest

from data.guias import HISTORY


class HistoryTimelineTests(unittest.TestCase):
    def test_history_includes_colonial_empire_and_current_periods(self):
        slugs = [period["slug"] for period in HISTORY]

        self.assertIn("colonial", slugs)
        self.assertIn("imperio", slugs)
        self.assertIn("atual", slugs)

        self.assertGreater(len(HISTORY), 7)


if __name__ == "__main__":
    unittest.main()

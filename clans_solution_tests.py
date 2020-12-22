import unittest

import clans_solution as clan


class ClanTestCase(unittest.TestCase):
    def test1(self):
        pairs = [[1, 2], [2, 4], [3, 5]]
        self.assertEqual(len(clan.form_clans(pairs)),2)

    def test2(self):
        pairs = [[1, 2], [2, 4], [1, 3], [3, 5], [8, 10]]
        self.assertEqual(len(clan.form_clans(pairs)),2)

    def test_3(self):
        pairs = [[1, 2], [2, 4], [1, 3], [3, 5], [8, 10]]
        clans = clan.form_clans(pairs)
        self.assertEqual(clan.solution(clans), 6)

    def test_4(self):
        pairs = [[1, 2], [2, 4], [3, 5]]
        clans = clan.form_clans(pairs)
        self.assertEqual(clan.solution(clans), 4)

    def test_5(self):
        pairs = [[1, 2]]
        self.assertEqual(len(clan.form_clans(pairs)), 1)

    def test_6(self):
        pairs = []
        self.assertEqual(len(clan.form_clans(pairs)), 0)

    def test_7(self):
        pairs = [[1, 3], [9, 11], [13, 15]]
        clans=clan.form_clans(pairs)
        self.assertEqual(clan.solution(clans), 0)

    def test_8(self):
        pairs = [[2, 4], [8, 10], [12, 14],[20,24],[16,18]]
        clans = clan.form_clans(pairs)
        self.assertEqual(clan.solution(clans), 0)

    def test_9(self):
        pairs = [[0, 10], [10, 20]]
        self.assertFalse(pairs[0] in clan.form_clans(pairs))

if __name__ == '__main__':
    unittest.main()
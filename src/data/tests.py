import datetime
import unittest

from commons import dump
from commons import nested_dict
from commons import process
from commons import ProperDate
from commons import save_yaml_file


class TestDump(unittest.TestCase):
    def test_dump_dict(self):
        self.assertEqual(dump({1: "a"}), "1: a\n")


class TestNestedDict(unittest.TestCase):
    def test_nested(self):
        nd = nested_dict()
        nd[1][2][3] = 'a'
        self.assertEqual(nd[1][2][3], 'a')
        self.assertDictEqual(nd, {1: {2: {3: 'a'}}})


class TestProperDate(unittest.TestCase):
    def test_proper_date__init__(self):
        pd = ProperDate()
        self.assertEqual(str(pd.pi_10), "2019-10-02")
        self.assertEqual(str(pd.dates[10][1]['x']), "2019-10-02")

    def test_calculate_pi_start(self):
        pd = ProperDate()
        x = pd.calculate_pi_start(11, 2)
        self.assertEqual(str(x), "2019-12-11")
        y = pd.calculate_pi_start(10, 2)
        self.assertEqual(str(y), "2019-10-16")

    def test_add_days_skipping_weekends(self):
        pd = ProperDate()
        x = pd.add_days_skipping_weekends(datetime.date(2019, 11, 1), 4)
        self.assertEqual(str(x), "2019-11-05")

    def test_get_date_from_pi_sprint(self):
        pd = ProperDate()
        x = pd.get_date_from_pi_sprint(10, sprint=2, duration=1, team='x')
        self.assertEqual(str(x), "2019-10-16")
        x = pd.get_date_from_pi_sprint(10, sprint=2, duration=1, team='x')
        self.assertEqual(str(x), "2019-10-17")
        x = pd.get_date_from_pi_sprint(10, sprint=2, duration=1, team='y')
        self.assertEqual(str(x), "2019-10-16")


class TestProcess(unittest.TestCase):
    def test_process(self):
        # process
        pass


class TestSaveYamlFile(unittest.TestCase):
    def test_save_yaml_file(self):
        # save_yaml_file
        pass


if __name__ == '__main__':
    unittest.main()

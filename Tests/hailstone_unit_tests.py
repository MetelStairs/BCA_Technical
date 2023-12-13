import os
import unittest
from hailstone import HailstoneClass

current_directory = os.getcwd()
os.chdir("..")


class TestHailstone(unittest.TestCase):
    def test_non_int_input(self):
        # Test with an invalid starting number (non-integer)
        with self.assertRaises(ValueError):
            HailstoneClass.hailstone_sequence("car")
        print("String input passed")
        with self.assertRaises(ValueError):
            HailstoneClass.hailstone_sequence("22.3")
        print("Float input passed")
        with self.assertRaises(ValueError):
            HailstoneClass.hailstone_sequence("")
        print("Empty input passed")
        with self.assertRaises(ValueError):
            HailstoneClass.hailstone_sequence(True)
        print("Boolean input passed")
        print("Non Integer inputs have successfully passed")
        print("#################################")

    def test_less_than_1(self):
        with self.assertRaises(ValueError):
            HailstoneClass.hailstone_sequence("1")
        print("1 input passed")
        with self.assertRaises(ValueError):
            HailstoneClass.hailstone_sequence("0")
        print("0 input passed")
        with self.assertRaises(ValueError):
            HailstoneClass.hailstone_sequence("-1")
        print("-1 input passed")
        print("Less than 1 input input successfully passed")
        print("#################################")

    def test_correct_answers(self):
        sequence, steps, text_summary = HailstoneClass.hailstone_sequence(14)
        self.assertEqual(sequence, [14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(steps, 17)
        print("Input of 14 has passed")

        sequence, steps, text_summary = HailstoneClass.hailstone_sequence(25)
        self.assertEqual(sequence,
                         [25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(steps, 23)
        print("Input of 25 has passed")
        print("#################################")


if __name__ == '__main__':
    unittest.main()

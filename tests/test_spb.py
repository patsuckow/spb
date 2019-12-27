import sys
import unittest
from spb import SimpleProgressBar as spb


# Set the value of the parameters for testing:
start = 0
stop = 1_000_000
progress_bar = 'show'
variant_bar = 'static'
variant_brackets = '||'
variant_arrow = '▇'
variant_space = '-'
len_bar = 35
progress_str = 'Progress'
percent = 'show'
timer = 'show'
variant_timer = 'increasing'
icon_timer = 'animated'
variant_icon_timer = '🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦'
timer_str = 'Timer'
reverse_timer_str = 'eta'
speed = 'hide'
icon_speed = 'show'
variant_icon_speed = '🚀'
speed_str = 'Speed'
load = 'hide'
icon_load = 'show'
variant_icon_load = '⭳'
load_str = 'Loaded'
color = 'green'
end_msg = 'complete.'


class SimpleProgressBarTest(unittest.TestCase):
    def setUp(self):
        """
        We start creating the object of the desired class before each start of
        the test method.
        """
        self.obj = spb(start, stop, progress_bar, variant_bar,
                       variant_brackets, variant_arrow, variant_space,
                       len_bar, progress_str, percent, timer, variant_timer,
                       icon_timer, variant_icon_timer, timer_str,
                       reverse_timer_str, speed, icon_speed,
                       variant_icon_speed, speed_str, load, icon_load,
                       variant_icon_load, load_str, color, end_msg)

    def tearDown(self):
        """
        We delete the object of the desired class at the end of the next
        test method.
        """
        self.obj = None

    @classmethod
    def tearDownClass(cls):
        """After completing all the class tests, show console cursor"""
        sys.stdout.write('\x1b[?25h')
        sys.stdout.flush()

    def test___iter__(self):
        """
        We verify the statement that:
        The __iter__() magic method returns a reference to an object of its
        class
        """
        self.assertEqual(self.obj.__iter__(), self.obj)

    def test___next__(self):
        """
        We verify the statement that:
        The __next__() magic method returns the self.iteration property
        """
        self.assertEqual(self.obj.__next__(), self.obj.iteration)

    def test___next___return_int(self):
        """
        We verify the statement that:
        The __next__() magic method returns an iteration property of type int
        """
        self.assertEqual(type(self.obj.__next__()), int, "Must be int")

    def test__return_list_brackets(self):
        """
        We verify the statement that:
        The _return_list_brackets() method returns of type list
        """
        self.assertIsInstance(self.obj._return_list_brackets(variant_brackets),
                              list, "Must be list")

    def test__choose_indicator_color(self):
        """
        We verify the statement that:
        _choose_indicator_color() method returns type int
        """
        self.assertIsInstance(self.obj._choose_indicator_color(color), int,
                              "Must be int")

    def test__calculate_basic_element_progress_bar(self):
        """
        We verify the statement that:
        The _calculate_basic_element_progress_bar() method returns
        <class 'tuple'>
        """
        self.assertEqual(
            type(self.obj._calculate_basic_element_progress_bar()),
            tuple,
            "Must be tuple"
        )

    def test__returned_four_elem_tuple(self):
        """
        We verify the statement that:
        The _calculate_basic_element_progress_bar() method returns four
        elements in <class 'tuple'>
        """
        self.assertEqual(
            len(self.obj._calculate_basic_element_progress_bar()),
            4,
            "Method must be returns four elements in tuple"
        )

    def test_type_first_elem_tuple(self):
        """
        We verify the statement that:
        the type of the first tuple returned by
        _calculate_basic_element_progress_bar() is str
        """
        self.assertIsInstance(
            self.obj._calculate_basic_element_progress_bar()[0],
            str,
            "Must be str"
        )

    def test_type_second_elem_tuple(self):
        """
        We verify the statement that:
        the type of the second tuple returned by
        _calculate_basic_element_progress_bar() is str
        """
        self.assertIsInstance(
            self.obj._calculate_basic_element_progress_bar()[1],
            str,
            "Must be str"
        )

    def test_type_third_elem_tuple(self):
        """
        We verify the statement that:
        the type of the third tuple returned by
        _calculate_basic_element_progress_bar() can be float
        """
        self.assertIsInstance(
            self.obj._calculate_basic_element_progress_bar()[2],
            float,
            "Must be float"
        )

    def test_type_fourth_elem_tuple(self):
        """
        We verify the statement that:
        the type of the fourth tuple returned by
        _calculate_basic_element_progress_bar() can be string, by the way, by
        doing this we check the return type of the _get_time_string() method.
        """
        self.assertIsInstance(
            self.obj._calculate_basic_element_progress_bar()[3],
            str,
            "Must be string"
        )

    def test__calculate_share_of_iterations(self):
        """
        We verify the statement that:
        _calculate_share_of_iterations() method returns type float
        """
        self.assertIsInstance(self.obj._calculate_share_of_iterations(), float,
                              "Must be float")

    def test__calculate_passed_time(self):
        """
        We verify the statement that:
        _calculate_passed_time() method returns type float
        """
        self.assertIsInstance(self.obj._calculate_passed_time(), float,
                              "Must be float")

    def test__calculate_remaining_time(self):
        """
        We verify the statement that:
        _calculate_remaining_time() method returns type float
        """
        self.assertIsInstance(self.obj._calculate_remaining_time(), float,
                              "Must be float")

    def test__get_time_string(self):
        """
        We verify the statement that:
        _get_time_string() method returns type str
        """
        self.assertIsInstance(self.obj._get_time_string(), str, "Must be str")

    def test__select_icon_to_timer(self):
        """
        We verify the statement that:
        _select_icon_to_timer() method returns type str
        """
        self.assertIsInstance(self.obj._select_icon_to_timer(), str,
                              "Must be str")

    def test__select_icon_to_speed(self):
        """
        We verify the statement that:
        _select_icon_to_speed() method returns type str
        """
        self.assertIsInstance(self.obj._select_icon_to_speed(), str,
                              "Must be str")

    def test__select_icon_to_load(self):
        """
        We verify the statement that:
        _select_icon_to_load() method returns type str
        """
        self.assertIsInstance(self.obj._select_icon_to_load(), str,
                              "Must be str")

    def test__convert_bytes_to_human_readable(self):
        """
        We verify the statement that:
        _convert_bytes_to_human_readable() method returns type str
        """
        self.assertIsInstance(self.obj._convert_bytes_to_human_readable(),
                              str, "Must be str")

    def test__prepare_string_progress_bar(self):
        """
        We verify the statement that:
        _prepare_string_progress_bar() method returns type str
        """
        self.assertIsInstance(
            self.obj._prepare_string_progress_bar(
                *self.obj._calculate_basic_element_progress_bar()
            ),
            str,
            "Must be str"
        )


if __name__ == '__main__':
    unittest.main()  # running tests

# python3 -m unittest discover

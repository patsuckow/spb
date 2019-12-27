import shutil
from typing import Union


class _CheckParams:
    """Check input parameters. Protected class. Designed for internal use."""

    def __init__(
            self,
            start: int = 0,
            stop: int = 100,
            progress_bar: str = 'show',
            variant_bar: str = 'static',
            variant_brackets: str = '||',
            variant_arrow: str = '▇',
            variant_space: str = '-',
            len_bar: int = 35,
            progress_str: str = 'Progress',
            percent: str = 'show',
            timer: str = 'show',
            variant_timer: str = 'increasing',
            icon_timer: str = 'animated',
            variant_icon_timer: str = '🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦',
            timer_str: str = 'Timer',
            reverse_timer_str: str = 'eta',
            speed: str = 'hide',
            icon_speed: str = 'show',
            variant_icon_speed: str = '🚀',
            speed_str: str = 'Speed',
            load: str = 'hide',
            icon_load: str = 'show',
            variant_icon_load: str = '⭳',
            load_str: str = 'Loaded',
            color: str = 'green',
            end_msg: str = ""
    ) -> None:
        """
        The name of the properties does not always coincide with the names
        of the properties in the SimpleProgressBar() class, since in this
        class they are needed only to verify the correctness of the values
        of the passed parameters.

        Because the value of string parameters: progress_str, timer_str,
        reverse_timer_str, speed_str, load_str can be either a default string,
        an empty string, or a string that the user indicates, we only check
        that they pass a value of the string type and that’s it.
        """
        self._start = start
        self._stop = stop
        self._progress_bar = progress_bar
        self._v_bar = variant_bar
        self._v_brackets = variant_brackets
        self._v_arrow = variant_arrow
        self._v_sp = variant_space
        self._len_bar = len_bar
        self._progress_str = progress_str
        self._percent = percent
        self._timer = timer
        self._v_timer = variant_timer
        self._icon_timer = icon_timer
        self._v_icon_timer = variant_icon_timer
        self._timer_str = timer_str
        self._reverse_timer_str = reverse_timer_str
        self._speed = speed
        self._icon_speed = icon_speed
        self._v_icon_speed = variant_icon_speed
        self._speed_str = speed_str
        self._load = load
        self._icon_load = icon_load
        self._v_icon_load = variant_icon_load
        self._load_str = load_str
        self._color = color
        self._end_msg = end_msg

        if not self._check_types() \
                or not self._is_length_string_parameter_is_one() \
                or not self._is_length_string_parameter_is_two_or_null()\
                or not self._is_number_in_row() \
                or not self._correct_value_in_list() \
                or not self._is_positive_numbers() \
                or not self._correct_start_stop() \
                or not self._correct_terminal_size():
            raise SystemExit(1)

    def _check_types(self) -> bool:
        """Type checking for accepted arguments"""
        try:
            self._is_instance(self._start, 'start', int)
            self._is_instance(self._stop, 'stop', int)
            self._is_instance(self._progress_bar, 'progress_bar', str)
            self._is_instance(self._v_bar, 'variant_bar', str)
            self._is_instance(self._progress_str, 'progress_str', str)
            self._is_instance(self._v_brackets, 'variant_brackets', str)
            self._is_instance(self._v_arrow, 'variant_arrow', str)
            self._is_instance(self._v_sp, 'variant_space', str)
            self._is_instance(self._len_bar, 'len_bar', int)
            self._is_instance(self._percent, 'percent', str)
            self._is_instance(self._timer, 'timer', str)
            self._is_instance(self._v_timer, 'variant_timer', str)
            self._is_instance(self._icon_timer, 'icon_timer', str)
            self._is_instance(self._v_icon_timer, 'variant_icon_timer', str)
            self._is_instance(self._timer_str, 'timer_str', str)
            self._is_instance(self._reverse_timer_str, 'reverse_timer_str', str)
            self._is_instance(self._speed, 'speed', str)
            self._is_instance(self._icon_speed, 'icon_speed', str)
            self._is_instance(self._v_icon_speed, 'variant_icon_speed', str)
            self._is_instance(self._speed_str, 'speed_str', str)
            self._is_instance(self._load, 'load', str)
            self._is_instance(self._icon_load, 'icon_load', str)
            self._is_instance(self._v_icon_load, 'variant_icon_load', str)
            self._is_instance(self._load_str, 'load_str', str)
            self._is_instance(self._color, 'color', str)
            self._is_instance(self._end_msg, 'end_msg', str)
        except TypeError as err:
            print(f'Wrong Input: {err.args[1]} must bee {err.args[2]}, not '
                  f'{type(err.args[0])}')
            return False

        return True

    @staticmethod
    def _is_instance(val: Union[int, str], name: str, type_is: type) -> None:
        """
        For the accepted argument val of this function, we use typing.Union
        when something can be one of several types (for type checking).
        """
        if not isinstance(val, type_is):
            raise TypeError(val, name, type_is)

    def _is_length_string_parameter_is_one(self) -> bool:
        """Check length of string parameter value is one"""
        try:
            self._length_is_not_one(self._v_arrow.strip(), 'variant_arrow')
            self._length_is_not_one(self._v_sp, 'variant_space')
            self._length_is_not_one(self._v_icon_speed.strip(),
                                    'variant_icon_speed')
            self._length_is_not_one(self._v_icon_load.strip(),
                                    'variant_icon_load')
        except ValueError as err:
            print(f'Wrong Input: {err.args[1]} must bee length == 1, not '
                  f'{len(err.args[0])}')
            return False

        return True

    @staticmethod
    def _length_is_not_one(val: str, name: str) -> None:
        if len(val) != 1:
            raise ValueError(val, name)

    def _is_length_string_parameter_is_two_or_null(self) -> bool:
        """Check length of string parameter value is two or 0"""
        try:
            if 0 < len(self._v_brackets.strip()) != 2:
                raise ValueError(self._v_brackets, 'variant_bracket')
        except ValueError as err:
            print(f'Wrong Input: {err.args[1]} must bee 0 < length == 2, not '
                  f'{len(err.args[0])}')
            return False

        return True

    def _is_number_in_row(self) -> bool:
        """Check the number is in the row"""
        try:
            if self._len_bar not in range(10, 101):
                raise ValueError(self._len_bar, 'len_bar', '10-100')
        except ValueError as err:
            print(f'Wrong Input: {err.args[1]} must bee {err.args[2]}, not '
                  f'{err.args[0]}')
            return False

        return True

    def _correct_value_in_list(self) -> bool:
        """Check that the parameter value is on our list"""
        try:
            self._not_in_list(self._progress_bar.strip(), 'progress_bar',
                              ['show', 'hide'])
            self._not_in_list(self._v_bar.strip(), 'variant_bar',
                              ['static', 'increasing', 'decreasing'])
            self._not_in_list(self._timer.strip(), 'timer', ['show', 'hide'])
            self._not_in_list(self._v_timer.strip(), 'variant_timer',
                              ['increasing', 'decreasing'])
            self._not_in_list(self._icon_timer.strip(), 'icon_timer',
                              ['animated', 'static', 'hide'])
            self._not_in_list(self._percent.strip(), 'percent',
                              ['show', 'hide'])
            self._not_in_list(self._speed.strip(), 'speed', ['show', 'hide'])
            self._not_in_list(self._icon_speed.strip(), 'icon_speed',
                              ['show', 'hide'])
            self._not_in_list(self._load.strip(), 'load', ['show', 'hide'])
            self._not_in_list(self._icon_load.strip(), 'icon_load',
                              ['show', 'hide'])
            self._not_in_list(self._color.strip(), 'color',
                              ['black', 'red', 'green', 'yellow', 'blue',
                               'magenta', 'cyan', 'gray', 'white'])
        except ValueError as err:
            print(f"Wrong Input: {err.args[0]}, param {err.args[1]} must bee"
                  f" {err.args[2]}")
            return False

        return True

    @staticmethod
    def _not_in_list(param: str, name_param: str, my_list: list) -> None:
        if param not in my_list:
            raise ValueError(param, name_param, my_list)

    def _is_positive_numbers(self) -> bool:
        """Check if the numbers are positive"""
        try:
            if self._start < 0:
                raise ValueError(self._start, 'start')
            if self._stop < 0:
                raise ValueError(self._stop, 'stop')
        except ValueError as err:
            print(f"Wrong Input: '{err.args[1]}' must bee positive, not "
                  f"{err.args[0]}")
            return False

        return True

    def _correct_start_stop(self) -> bool:
        """
        Checking the correctness of the start and stop parameters of the
        progress bar
        """
        try:
            if self._start > self._stop or self._stop == 0:
                raise ValueError
        except ValueError:
            print(f"Wrong Input: 'start' must bee < 'stop' and 'stop' > 0")
            return False

        return True

    def _correct_terminal_size(self) -> bool:
        """Check correct the size of a terminal.

        https://docs.python.org/3.6/library/os.html#querying-the-size-of-a-terminal
        Availability: Unix, Windows.

        Since resizing the window is a very difficult process, since it
        depends on the type of operating system and the console shell used,
        if the console window is not large enough for the correct output, the
        bar progress will display an error message and terminate the script.
        It will be necessary to reduce the len_bar parameter or other
        parameters to an acceptable value and restart the script.

        The length of the entire string is the sum of the length of the
        displayed string elements, brackets and spaces between indicators.
        """
        if self._progress_bar == 'show':
            elem_1 = (self._len_bar - 1)*' ' + self._v_brackets
        else:
            elem_1 = self._progress_str
        elem_1 += ' 100.0% '

        elem_2 = ''
        if self._timer == 'show':
            elem_2 = 2*' ' if self._icon_timer != 'hide' else ''
            elem_2 += self._timer_str if self._v_timer == 'increasing' else \
                self._reverse_timer_str
            elem_2 += '[00:00:00.0] '

        elem_3 = ''
        if self._speed == 'show':
            if self._icon_speed == 'show':
                elem_3 = self._v_icon_speed + ' '
            elem_3 += self._speed_str + '[000.00kbit/s] '

        elem_4 = ''
        if self._load == 'show':
            if self._icon_load == 'show':
                elem_4 = self._v_icon_load + ' '
            elem_4 += self._load_str + '[000.00MB] '

        columns, _ = shutil.get_terminal_size()
        try:
            if len(elem_1 + elem_2 + elem_3 + elem_4) >= columns:
                raise ValueError
        except ValueError:
            print('Error: The size of your console (terminal) window is too '
                  'small for the progress bar to display correctly. Resize '
                  'the console window or hide some elements of the progress '
                  'bar and restart th')
            return False

        return True

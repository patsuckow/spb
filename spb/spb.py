"""spb - Simple Progress Bar

This module allows you to display, in the console, a progress indicator and
other indicators of any process you need.

Indicators that can be displayed:
- progress indicator
- percent indicator
- timer indicator
- data rate indicator
- transmitted data indicator

Any indicator, if desired, can be either turned on or off or displayed with
default settings, or you yourself can configure multiple parameters for any
indicator you need.

All possible settings (parameters) and using can be found in the wiki en
documentation: https://github.com/patsuckow/spb/wiki/1.-Home-(en)

Русская документация - https://github.com/patsuckow/spb/wiki/1.-Home-(ru)
"""
import sys
import time
from collections import deque
from .check_params_spb import _CheckParams


try:
    assert sys.version_info >= (3, 6)
except Exception:
    raise SystemExit('spb works with Python 3.6 or higher.')


class SimpleProgressBar:
    """
    Main progress bar class. Returned a progress bar based on the setup
    parameters.

    Parameters
    ----------
    start  : int, >= 0, optional
        Number is the beginning of iterations. A progress bar is displayed in
        the console as an initial percentage. It may not start from zero.
        [default: 0]

    stop  : int, >= start, optional
        The final number of iterations. This can be either an integer number o
        f iterations, or an integer number of bits of information when
        uploading or downloading a file.
        [default: 100]

    progress_bar  : str, optional
        Choose show or hide the progress bar: ['show', 'hide']
        If you decide to "hide", the options will be disabled as unnecessary:
        variant_bar, variant_brackets, variant_arrow, variant_space, len_bar.
        [default: 'show']

    variant_bar  : str, optional
        Select one of the options for displaying the progress bar:
        ['increasing', 'static', 'decreasing']
        'increasing' - increasing progress bar, will increase from 0% to 100%.
        'static' - static progress bar. The place for movement of the progress
                   bar will be immediately displayed. The progress bar will
                   increase from 0% to 100%.
        'decreasing' - A decreasing progress bar, during operation, will
                       decrease from 100% to 0%.
        As a decrease can begin not from 100%, but for example from 75%, etc.,
        so an increase can start not from 0%, but for example from 30%, etc.
        Displayed when progress_bar='show'
        [default: 'static']

    variant_brackets  : str, len(str) == 0 or len(str) == 2, optional
        Specify the parenthesis characters that you want to see before and
        after the progress bar.
        For example: '||', '{}', '[]', '//', '**' etc. Unicode-symbols.
        If you do not need parentheses, put: ''
        Displayed when progress_bar='show' and variant_bar='static'
        [default: '||']

    variant_arrow  : str, not empty, not space, optional
        Indicator arrow variant. For example: '⏹', '∎', '▣', '◉', '●', '#',
        'X', '=', '/' '\', '.' etc. Unicode-symbols.
        Displayed when progress_bar='show'
        [default: '▇']

    variant_space  : str, not empty, may be a white space, optional
        Variant of a whitespace character on an unfilled progress bar area.
        For example: ' ', '-', '·', '༝', '༚', '༛', '༞', '•', '⬞', '◯', '▢',
        '⬜' etc. Unicode-symbols.
        Displayed when progress_bar='show' and variant_bar='static'
        [default: '-']

    len_bar  : int, 10 >= len_bar <= 100, optional
        Progress bar length. Counted in console columns.
        It only makes sense when progress_bar='show'
        [default: 35]

    progress_str  : str, optional
        Specify the desired name for the percent indicator.
        Displayed when progress_bar='hide'
        [default: 'Progress']

    percent  : str, optional
        This parameter is responsible for displaying percent complete and is
        displayed by default.
        But, if you need to display the download of the file, and the file
        size (content-length) is unknown and impossible to obtain (since many
        online file services began to hide this information and even hide
        direct links to files), then you’ll have to “hide” the percent of
        execution - 'hide'.
        [default: 'show']

    timer  : str, optional
        Choose show or hide the timer: ['show', 'hide']
        If you decide to "hide", the options will be disabled as unnecessary:
        variant_timer, icon_timer, variant_icon_timer, timer_str,
        reverse_timer_str.
        [default: 'show']

    variant_timer: str, optional
        Choose which timer is needed: ['increasing', 'decreasing']
        It only makes sense when timer='show'
        [default: 'increasing']

    icon_timer  : str, optional
        Select view the icon timer: ['animated', 'static', 'hide']
        It only makes sense when timer='show'
        [default: 'animated']

    variant_icon_timer  : str, optional
        If icon_timer setup in 'animated', then we show an animated
        watch using our set of Unicode-symbols.
        For example: '⏳⏳⏳⌛⌛⌛  ', '⣾⣷⣯⣟⡿⢿⣻⣽', '⣽⣻⢿⡿⣟⣯⣷⣾',
        '᎐᎐᎓᎓᎒᎒᎓᎓᎐᎐', '᎒᎒᎓᎓᎐᎐', '᎐᎐᎓᎓᎒᎒', '᎐᎓᎒᎓᎐', '᎐᎓᎒', '᎒᎓᎐', '∴∵', '∴∵∷',
        '▁▂▃▄▅▆▇█▇▆▅▄▃▂▁', '▁▂▃▄▅▆▇█', '█▇▆▅▄▃▂▁', '▞▚', '▬▭', '▮▯', '⚪⚫',
        '▏▎▍▌▋▊▉█▉▊▋▌▍▎▏', '▏▎▍▌▋▊▉█', '█▉▊▋▌▍▎▏', 'ↀↀↂↂↈↈ',
        '⋮⋰⋱', '⋱⋰⋮', '⋱⋰', '⎽⎼⎻⎺⎻⎼⎽', '-\\|//', '//|\\-',
        'ⅠⅠⅡⅡⅢⅢⅢⅡⅡⅠⅠ', 'ⅠⅠⅡⅡⅢⅢ', 'ⅠⅡⅢ', '◑◒◐◓', '○◔◑◕●', '●◕◑◔○',
        '◀▼▶▲', '▲▶▼◀', '◢◣◤◥', '◥◤◣◢', '◥◣◤◢', '◢◤◣◥', '◩⬔◪⬕', '⬕◪⬔◩',
        '⬜⬜⬛⬛', '⬜⬛', '◨⬓◧⬒', '⬒◧⬓◨', '◨⬓◧⬒◨⬓◧⬒◨⬒◧⬓◨⬒◧⬓◨⬓', '♦♦♢♢', '♦♢',
        ' ◨⬓◧⬒◨⬓◧⬒◨⬓◧⬒◨⬓◧⬒ ⬒◧⬓◨⬒◧⬓◨⬒◧⬓◨⬒◧⬓◨',  '⊕⊗', '☢☢☢   ', '⌃⌄',
        '⇑⇗⇒⇘⇓⇙⇐⇖', '←↖↑↗→↘↓↙', '⇠⇡⇢⇣', '↞↟↠↡', '↤↥↦↧', '★☆✪', '★☆✪✫✯',
        '☆✪', '⍟✪☆', '☆✪⍟', '✧✦', '✳✴✵✷', '⚹✳✴✵✷', '✲✱', '♡♡♡♡♡♥♥♡♡♥♥'
        Displayed when timer='show' and icon_timer='animated'
        [default: '🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦']

    timer_str  : str, optional
        The line displayed between the timer icon and the digital timer
        counter, which is incrementing.
        If you do not want to not show this line, you just need to pass an
        empty line to the parameter: timer_str=''
        Displayed when timer='show' and variant_timer='increasing'
        [default: 'Timer']

    reverse_timer_str  : str, optional
        The string displayed between the timer icon and the digital timer
        counter, which is decreasing.
        If you do not want to not show this line, you just need to pass an
        empty line to the parameter: reverse_timer_str=''
        Displayed when timer='show' and variant_timer='decreasing'
        [default: 'eta']

    speed  : str, optional
        Choose to show or hide the speed indicator: ['show', 'hide']
        If you decide to "hide", the options will be disabled as unnecessary:
        icon_speed, variant_icon_speed, speed_str
        By default, the indicator is hidden, because the setting is required
        only if the progress indicator calculates the file transfer speed.
        [default: 'hide']

    icon_speed  : str, optional
        Choose to show or hide the speed icon, from the list: ['show', 'hide']
        Displayed when speed='show'
        [default: 'show']

    variant_icon_speed  : str, optional
        If icon_speed="show", then we will show the icon that is installed by
        default, or the one that the user will set.
        For example: '🚄', '🛪', '🛫', '🛧', '🛬', '🛦', '🚴', '🚵', '🏃'
        Displayed when speed='show' and icon_speed='show'
        [default: '🚀']

    speed_str  : str, optional
        The line displayed between the speed icon and the digital speed
        counter.
        If you do not want to not show this line, you just need to pass an
        empty line to the parameter: speed_str=''
        Displayed when speed='show'
        [default: 'Speed']

    load  : str, optional, 'show' or 'hide'
        Choose to show or hide the load indicator: ['show', 'hide']
        By default, the indicator is hidden, because configuration is required
        only if the progress indicator calculates the file size when it is
        transferred.
        [default: 'hide']

    icon_load  : str, optional
        Choose to show or not the load icon, from the list: ['show', 'hide']
        It only makes sense when load='show'
        [default: 'show']

    variant_icon_load  : str, optional
        If icon_load="show", then we will show the icon that is installed by
        default, or the one that the user will set.
        For example:
            down: '⭳', '↧', '↓', '🡇', '⭣', '⇓', '⮇', '⭭', '🠯', '🠇', etc.
            up:   '⭱', '↥', '↑', '🡅', '⭡', '⇑', '⮅', '⭫', '🠭', '🠅', etc.
            up-down: '⬍', '↕', '⇕', '⇅', '⭥', '⮁', etc.
        Displayed when load='show' and icon_load='show'
        [default: '⭳']

    load_str  : str, optional
        The string to be displayed between the load indicator and the
        digital load counter.
        If you do not want to not show this line, you just need to pass an
        empty line to the parameter: load_str=''
        Displayed when load='show'
        [default: 'Loaded']

    color  : str, optional
        Select one color by which the indicators will be highlighted and the
        progress bar itself, from the list: ['black', 'red', 'green', 'yellow',
        'blue', 'magenta', 'cyan', 'gray', 'white']
        [default: 'green']

    end_msg  : str, optional
        The message after the completion of the progress bar (if necessary).

    Public properties, that can be used in your code:
    -------------------------------------------------
    self.iteration  : int
        Required to store the number of iterations.
        [default: self.iteration = start]

    self.loaded_bytes  : int
        Required to store the number of bytes loaded (down/up).
        [default: self.loaded_bytes = 0]

    Public methods, that can be used in your code:
    ----------------------------------------------
    next()
    progress_bar()

    Returns
    -------
    out  : Formatted counter and statistics displayed in the console.

    Notes:
    ------
    1. Unicode-symbols values that can be used for parameters, can be taken
       from the Unicode table. You can copy Unicode characters, for example,
       from this site: https://unicode-table.com/en/
    2. By default, the width of the console window is different on different
       systems, but on average 80 columns. If you do not expand the console
       window to full screen, then this will not be enough to display all the
       possible indicators and inscriptions in the progress bar line.
       But thanks to the settings, you can display those indicators, icons
       and exchanges of indicators that you need and hide what you do not need.
    """
    START_TIME = time.monotonic()  # set up start time one time

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

        # Run check input parameters
        _CheckParams(start, stop, progress_bar, variant_bar, variant_brackets,
                     variant_arrow, variant_space, len_bar, progress_str,
                     percent, timer, variant_timer, icon_timer,
                     variant_icon_timer, timer_str, reverse_timer_str, speed,
                     icon_speed, variant_icon_speed, speed_str, load, icon_load,
                     variant_icon_load, load_str, color, end_msg)

        self.iteration = start
        self._stop = stop
        self._progress_bar = progress_bar.strip()
        self._v_bar = variant_bar.strip()
        self._progress_str = progress_str.strip()
        self._v_brackets = self._return_list_brackets(variant_brackets.strip())
        self._v_arrow = variant_arrow.strip()
        self._v_sp = variant_space
        self._len_bar = len_bar
        self._percent = percent
        self._timer = timer
        self._v_timer = variant_timer.strip()
        self._icon_timer = icon_timer.strip()
        self._stack_v_icon_timer = deque(list(variant_icon_timer.strip()))
        self._timer_str = timer_str.strip()
        self._reverse_timer_str = reverse_timer_str.strip()
        self._speed = speed.strip()
        self._icon_speed = icon_speed.strip()
        self._v_icon_speed = variant_icon_speed.strip()
        self._speed_str = speed_str.strip()
        self._load = load.strip()
        self._icon_load = icon_load.strip()
        self._v_icon_load = variant_icon_load.strip()
        self._load_str = load_str.strip()
        self._color = self._choose_indicator_color(color.strip())
        self._end_msg = end_msg.strip()
        self._second_step = self._calculate_passed_time()
        self.loaded_bytes = 0
        self._hide_console_cursor()

    def __iter__(self):
        return self

    def __next__(self) -> int:
        """
        Implementing an iterator eliminates the need to use a singleton:
        to set the start time and to print the hiding cursor once from the
        console. This also allows you to set the arguments to __init__ only
        once and only once to check their correctness, which will speed up
        the operation of the SimpleProgressBar class.
        """
        self.iteration += 1
        self.progress_bar()

        return self.iteration

    @staticmethod
    def _return_list_brackets(brackets: str) -> list:
        """
        If, after trimming the spaces, an empty line remains, then we will
        return the list [' ', ''] that will allow you to indent from the left
        edge of the console window for the progress bar, but will not make an
        unnecessary space from the right of the progress bar.
        Otherwise, we return the list of the two specified brackets.
        """
        return [' ', ''] if brackets == '' else list(brackets)

    @staticmethod
    def _choose_indicator_color(color: str) -> int:
        """Return the selected color number by its given name.

        This is color which the indicators will be highlighted and the
        progress bar itself, from the list.

        Checking for a possible incorrect, passed parameter, passes in the
        _CheckParams() class.
        """
        return {'black': 0, 'red': 1, 'green': 2, 'yellow': 3, 'blue': 4,
                'magenta': 5, 'cyan': 6, 'gray': 7, 'white': 8}[color]

    def progress_bar(self) -> None:
        """Calculate, prepare view and display progress bar"""
        self._write_progress_bar_to_console(
            self._prepare_string_progress_bar(
                *self._calculate_basic_element_progress_bar()
            )
        )

    def _calculate_basic_element_progress_bar(self) -> tuple:
        """
        Calculate all the basic necessary elements for the progress bar:
        arrow, spaces, percent.
        """
        share_of_iterations = self._calculate_share_of_iterations()
        arrow = round(share_of_iterations * self._len_bar - 1) * self._v_arrow
        percent = round(share_of_iterations * 100, 1)
        # On a increasing and decreasing progress bar, spaces in the form of
        # any characters are not needed.
        spaces = ''

        diff_bar = (self._len_bar - len(arrow) - 1)

        if self._v_bar == 'static':
            spaces = diff_bar * self._v_sp
        else:
            self._v_brackets[0] = ' '
            self._v_brackets[1] = ''

        if self._v_bar == 'decreasing':
            arrow = diff_bar * self._v_arrow
            percent = 100 - percent

        return arrow, spaces, percent, self._get_time_string()

    def _calculate_share_of_iterations(self) -> float:
        """Calculate the share of iterations passed from the total number of
        iterations.
        """
        return self.iteration / self._stop

    @staticmethod
    def _calculate_passed_time() -> float:
        """Calculate passed of time elapsed since launch.

        https://docs.python.org/3.7/library/time.html?#time.monotonic
        """
        return time.monotonic() - SimpleProgressBar.START_TIME

    def _calculate_remaining_time(self) -> float:
        """Calculate estimated remaining time"""
        percent = self._calculate_share_of_iterations() * 100
        if percent >= 1 / self._stop:
            time_pass = self._calculate_passed_time()
            return abs(100 / (percent / time_pass) - time_pass)

        return .0

    def _get_time_string(self) -> str:
        """Get the finished string with time.

        Depending on the options, we can get increasing or decreasing seconds.

        This calculation cannot be absolutely accurate, since it depends on
        many factors: the characteristics of the PC on which the script is
        running and the speed of the process that is being calculated.
        For example, a process can be slowed down or accelerated by processes
        independent of the script, for example, increasing or decreasing the
        speed of downloading a file on the server side, etc.
        """
        if self._v_timer == 'decreasing':
            sec = self._calculate_remaining_time()
            mes = ' ' + self._reverse_timer_str
        else:
            sec = self._calculate_passed_time()
            mes = ' ' + self._timer_str

        minutes = int(sec // 60)
        hours = int(minutes // 60)

        # Rounding seconds to 1 decimal place. The so-called “bank rounding”
        # is used, that is, rounding to the nearest even.
        seconds = round(sec % 60, 1)

        res_hours = ''
        if 0 < hours < 23:
            res_hours = f'0{hours}:' if len(str(hours)) < 2 else f'{hours}:'

        prefix_min = '0' if len(str(minutes)) < 2 else ''
        prefix_sec = '0' if len(str(seconds)) < 2 else ''

        return f"{self._select_icon_to_timer()}{mes}[\x1b[3" \
               f"{str(self._color)}m{res_hours}{prefix_min}{minutes}:" \
               f"{prefix_sec}{seconds}\x1b[0m]"

    def _select_icon_to_timer(self) -> str:
        """Select the displayed icon to timer, or you can completely hide this
        icon.

        For greater performance, we will use the stack instead of the standard
        list methods .append() and .pop().
        https://docs.python.org/3/library/collections.html?#collections.deque
        """
        if self._icon_timer == 'animated':
            clock = ' ' + self._stack_v_icon_timer[0]
            # If one tenth of a second or more has passed, then rearrange
            # the stack
            if self._second_step + 0.1 <= time.monotonic():
                if self._v_timer == 'increasing':
                    self._stack_v_icon_timer.append(
                        self._stack_v_icon_timer.popleft())
                else:
                    self._stack_v_icon_timer.appendleft(
                        self._stack_v_icon_timer.pop())
                self._second_step = time.monotonic()
        elif self._icon_timer == 'hide':
            clock = ''
        else:
            clock = ' ⏱'

        return clock

    def _select_icon_to_speed(self) -> str:
        """Select the displayed icon to load, or you can completely hide this
        icon.

        In secret from the user, we will indent to the left of the icon so that
        it does not stick to its previous symbol.
        """
        if self._icon_speed == 'show':
            # In secret from the user, we also add one space after the speed
            # icon so that the icon does not stick to the symbol that goes to
            # the right of it.
            return ' ' + self._v_icon_speed + ' '

        return ' '

    def _select_icon_to_load(self) -> str:
        """Select the displayed icon to load, or you can completely hide this
        icon.

        In secret from the user, added one space at the beginning of the
        progress bar, to retreat from the edge of the console.
        """
        if self._icon_load == 'show':
            return ' ' + self._v_icon_load

        return ' '

    def _convert_bytes_to_human_readable(self, suf: str = 'B') -> str:
        """
        1. Convert file size in bytes to human-readable representation.
        https://ru.wikipedia.org/wiki/Приставки_СИ
        https://en.wikipedia.org/wiki/International_System_of_Units
        https://en.wikipedia.org/wiki/Metric_prefix
        https://ru.wikipedia.org/wiki/Двоичные_приставки
        https://en.wikipedia.org/wiki/Binary_prefix

        Conclusion:
        In relation to the total amount of hard disk space, a multiplicity
        of 1000 is used, i.e. decimal prefixes for disk capacity and,
        accordingly, to indicate file size.
        Units: 'B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'
        B - reduction of "byte".

        2. Convert data transfer rate to human-readable representation.
        https://ru.wikipedia.org/wiki/Скорость_передачи_данных
        https://en.wikipedia.org/wiki/Data-rate_units
        https://ru.wikipedia.org/wiki/Бит_в_секунду
        https://en.wikipedia.org/wiki/Bit_rate

        Conclusion:
        Data transfer rate - the amount of data transmitted per unit of time.
        To find out the data transfer rate, you need to divide the amount of
        data transferred by the transfer time, taking into account that 1
        megabyte is equal to 1000 kbyte (Decimal prefixes (SI)).
        Units: 'bit/s', 'kbit/s', 'Mbit/s', 'Gbit/s', etc.
        bps, bit/s - reduction of "bits per second".
        """
        byte = self.loaded_bytes / self._calculate_passed_time() \
            if suf == 'bit/s' else self.loaded_bytes

        for unit in ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']:
            if abs(byte) < 1000:
                return f'\x1b[3{str(self._color)}m'+'{:6.2f}'.format(byte) + \
                       '\x1b[0m' + unit + str(suf)
            byte /= 1000

        # If the number of bytes is transferred even more than 'Yotta', (which
        # is unlikely to happen), then we will return the question mark.
        return '?'

    def _prepare_string_progress_bar(self, arrow: str, spaces: str,
                                     percent: int, timer: str) -> str:
        """Return prepared string progress bar.

        Colors in console:
        https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters
        """
        progress = '\x1b[3{}m{:0.1f}\x1b[0m%'.format(self._color, percent) \
            if self._percent == 'show' else ''

        if self._progress_bar == 'show':
            progress_bar = f"{self._v_brackets[0]}\x1b[3{self._color}m" \
                           f"{arrow}\x1b[0m{spaces}{self._v_brackets[1]} "
        elif self._progress_bar == 'hide' and self._progress_str != '':
            progress_bar = ' '
            progress = self._progress_str + progress
        else:
            progress_bar = ''
            progress = ''

        timer = '' if self._timer != 'show' else timer

        speed = ''
        if self._speed == 'show':
            speed = f"{self._select_icon_to_speed()}{self._speed_str}[" \
                    f"{self._convert_bytes_to_human_readable(suf='bit/s')}]"

        loaded = ''
        if self._load == 'show':
            loaded = f"{self._select_icon_to_load()}{self._load_str}[" \
                     f"{self._convert_bytes_to_human_readable(suf='B')}]"

        return "\r" + progress_bar + progress + timer + speed + loaded + "  \b"

    def _write_progress_bar_to_console(self, bar: str) -> None:
        """Write progress bar to console.

        Buffered IO:
        https://stackoverflow.com/questions/1450551/buffered-vs-unbuffered-io
        """
        sys.stdout.write(bar)
        if self.iteration == self._stop and self._percent == 'show':
            sys.stdout.write('\n')
            self._show_console_cursor()
            self._show_end_message()
            sys.stdout.write('\n')
        elif self._percent == 'hide':
            self._show_console_cursor()
        sys.stdout.flush()

    @staticmethod
    def _hide_console_cursor() -> None:
        """Hide console cursor: '\x1b[?25l'
        https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_codes
        ('\033' same as '\x1b')
        """
        sys.stdout.write('\n\x1b[?25l')

    @staticmethod
    def _show_console_cursor() -> None:
        """Show console cursor: '\x1b[?25h' """
        sys.stdout.write('\x1b[?25h')

    def _show_end_message(self) -> None:
        """Show the message after the completion of the progress bar (if
        necessary).
        """
        if self._end_msg != '':
            sys.stdout.write(self._end_msg)

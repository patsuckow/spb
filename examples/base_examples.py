"""
Basic use cases. We display the progress bar itself and the percentage
indicator with different settings. All possible options for setting parameters,
see the documentation.

Here is not show the display of file transfer rate indicators and the number
of transmitted data.
"""
from spb import SimpleProgressBar as spb


# Base example №1 (setup minimum parameters):
try:
    start = 0
    stop = 1_000_00
    pb = spb(start, stop)

    for i in range(start, stop):
        # your code ...
        next(pb)
except KeyboardInterrupt:
    print("\n\x1b[?25h Work aborted.")


# Base example №2 (with setting some parameters you need):
try:
    start = 0
    stop = 5_000_00

    pb = spb(
        start=start,
        stop=stop,
        len_bar=25,
        variant_bar='decreasing',
        variant_space=' ',
        color='yellow',
        variant_icon_timer='▁▂▃▄▅▆▇█▇▆▅▄▃▂▁',
        end_msg='Complete.'
    )

    for i in range(start, stop):
        # your code ...
        next(pb)
except KeyboardInterrupt:
    print("\n\x1b[?25h Work aborted.")


# Base example №3 (with setting some parameters you need):
try:
    # Please note the value of start can be omitted.
    stop = 5_000_00
    pb = spb(
        stop=stop,
        variant_bar='increasing',
        color='blue',
        variant_icon_timer='⣾⣷⣯⣟⡿⢿⣻⣽'
    )

    for i in range(stop):
        # your code ...
        next(pb)
except KeyboardInterrupt:
    print("\n\x1b[?25h Work aborted.")


# Base example №4 (start progress bar not from zero cycles (percent)):
try:
    start = 1500_00
    stop = 5_000_00
    pb = spb(start, stop, timer_str='', color='white')

    for i in range(start, stop):
        # your code ...
        next(pb)
except KeyboardInterrupt:
    print("\n\x1b[?25h Work aborted.")

# Base example №5 (whith decreasing progress bar not from zero cycles
# (percent)):
try:
    start = 5000_00
    stop = 1_000_000
    pb = spb(
        start,
        stop,
        variant_bar='decreasing',
        variant_timer='decreasing',
        reverse_timer_str=''
    )

    for i in range(start, stop):
        # your code ...
        next(pb)
except KeyboardInterrupt:
    print("\n\x1b[?25h Work aborted.")

# Examples setup param: variant_brackets, variant_arrow and variant_space:
# ------------------------------------------------------------------------
# by default:
# |▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇---------|

# variant_brackets=''
# ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇---------

# variant_brackets='{}'
# {▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇-------------------}

# variant_brackets='//'
# /▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇------------------/

# variant_brackets='**'
# *▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇----------------*

# variant_brackets='//',
# variant_arrow='/'
# ////////////////////////-----------/

# variant_brackets='\\\\',
# variant_arrow='/'
# \/////////////////////-------------\

# variant_brackets='[]',
# variant_arrow='/'
# [/////////////////////////---------]

# variant_brackets='[]',
# variant_arrow='⏹'
# [⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹⏹--------------]

# variant_brackets='[]',
# variant_arrow='∎
# [∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎-------------------]

# variant_brackets='[]',
# variant_arrow='◉'
# [◉◉◉◉◉◉◉◉◉◉------------------------]

# variant_brackets='[]',
# variant_arrow='●'
# [●●●●●●●●●●●●●●●●------------------]

# variant_brackets='[]',
# variant_arrow='#'
# [###################---------------]

# variant_arrow='●'
# |●●●●●●●●●●●●●●●●------------------|

# variant_space=' '
# |▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇                   |

# variant_space='.',
# variant_arrow='X'
# |XXXXXXXXXXXXXXXXXX................|

# variant_brackets='[]',
# variant_space='.',
# variant_arrow='#'
# [####################..............]

# variant_brackets='[]',
# variant_space='⬞',
# variant_arrow='#'
# [#############⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞]

# variant_brackets='[]',
# variant_arrow='='
# [=====================-------------]

# variant_brackets='[]',
# variant_space=' ',
# variant_arrow='='
# [=======================           ]

# variant_space='◯',
# variant_arrow='◉'
# |◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯◯|

# variant_space=' ',
# variant_arrow='◉'
# |◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉             |

# variant_space='○',
# variant_arrow='●'
# |●●●●●●●●●●●●●●●●●●●●●●●○○○○○○○○○○○|

# variant_space=' ',
# variant_arrow='●'
# |●●●●●●●●●●●●●●●●●●●               |

# variant_space='▢',
# variant_arrow='▣'
# |▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▢▢▢▢▢▢▢▢▢▢|

# variant_space=' ',
# variant_arrow='▣'
# |▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣          |

# len_bar=20,
# variant_brackets='[]',
# variant_space='⬜',
# variant_arrow='⬛'
# [⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜]

# len_bar=20,
# variant_brackets='',
# variant_space='⬜',
# variant_arrow='⬛'
# ⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜


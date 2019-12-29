# spb - Simple Progress Bar

This module allows you to display, in the console, a progress indicator and
other indicators of any process you need.

Indicators that can be displayed:
- progress indicator
- percent indicator
- timer indicator
- data rate indicator
- transmitted data indicator

**Any indicator, if desired, can be either turned on or off or displayed with
default settings, or you yourself can configure multiple parameters for any
indicator you need.**

## How to install:


#### From PyPI:

    pip3 install spb --user


#### From sources:

Alternatively you can install **spb** from sources directory:

    git clone https://github.com/patsuckow/spb
    cd spb
    pip3 install -r requirements.txt
    pip3 install . --user
    cd ..
    rm -rf spb

## How to import in your project:

`from spb import SimpleProgressBar as spb`

## Requirements:
See in file requirements.txt

**spb** works with ![version](https://user-images.githubusercontent.com/12321741/68495259-e298c480-0260-11ea-9d83-beab9b416562.png) or higher.

### What are the required modules inside `spb`:
- import **`sys`**
- import **`time`**
- import **`shutil`**
- from **`typing`** import Union
- from **`collections`** import deque

## Examples:
#### Base examples:

Basic use cases. We display the progress bar itself and the percentage
indicator with different settings. All possible options for setting parameters,
see the documentation.

Here is not show the display of file transfer rate indicators and the number
of transmitted data.

- [Base example №1 (setup minimum parameters)](https://github.com/patsuckow/spb/blob/master/examples/base_examples.py#L12):
![Base example №1 (setup minimum parameters)](https://user-images.githubusercontent.com/12321741/71492289-06cb5780-2847-11ea-8eaa-fd7e77549679.gif)
- [Base example №2 (with setting some parameters you need)](https://github.com/patsuckow/spb/blob/master/examples/base_examples.py#L25):
![Base example №2 (with setting some parameters you need)](https://user-images.githubusercontent.com/12321741/71492299-282c4380-2847-11ea-9a73-33088ebd6d3e.gif)
- [Base example №3 (with setting some parameters you need)](https://github.com/patsuckow/spb/blob/master/examples/base_examples.py#L48):
![Base example №3 (with setting some parameters you need)](https://user-images.githubusercontent.com/12321741/71492307-38dcb980-2847-11ea-8bf7-3dd8889caf89.gif)
- [Base example №4 (start progress bar not from zero cycles (percent))](https://github.com/patsuckow/spb/blob/master/examples/base_examples.py#L66):
![Base example №4 (start progress bar not from zero cycles (percent))](https://user-images.githubusercontent.com/12321741/71492316-4a25c600-2847-11ea-9fe9-0ec71e8f5eb9.gif)
- [Base example №5 (whith decreasing progress bar not from zero cycles (percent))](https://github.com/patsuckow/spb/blob/master/examples/base_examples.py#L78):
![Base example №5 (whith decreasing progress bar not from zero cycles (percent))](https://user-images.githubusercontent.com/12321741/71492321-5d389600-2847-11ea-8859-a4cf41a6973e.gif)

Other configuration options (`variant_brackets`, `variant_arrow` and `variant_space`) can be found [here](https://github.com/patsuckow/spb/blob/master/examples/base_examples.py#L97).


#### Examples of using:

How uses a load file indicator and progress bar indicator (the type of indicator will depend on the settings that you set)

- [Example using № 1 (Download single file using requests module)](https://github.com/patsuckow/spb/blob/master/examples/examples_of_using_1-4.py#L6):
![Example № 1 (Download single file using requests module)](https://user-images.githubusercontent.com/12321741/71492331-704b6600-2847-11ea-9a14-98ddb7554932.gif)
- [Example using № 2 (Download files from url list one by one using requests module)](https://github.com/patsuckow/spb/blob/master/examples/examples_of_using_1-4.py#L36).
- [Example using № 3 (Download files from url list one by one using urllib3)](https://github.com/patsuckow/spb/blob/master/examples/examples_of_using_1-4.py#L72).
- [Example using № 4 (Download multiple files (Parallel/bulk download) using requests module)](/examples/examples_of_using_1-4.py#L111).
- [Example using № 5 (Download video from YouTube using pytube module)](https://github.com/patsuckow/spb/blob/master/examples/examples_of_using_5-6.py#L6):
![Example № 5 (Download video from Youtube using pytube module)](https://user-images.githubusercontent.com/12321741/71492346-9113bb80-2847-11ea-81fb-5511f287520f.gif)
- [Example using № 6 (Download video playlist from YouTube using pytube module)](https://github.com/patsuckow/spb/blob/master/examples/examples_of_using_5-6.py#L35).
- [Example using № 7 (Download one file or all files from a folder Google Drive using google-api-client)](https://github.com/patsuckow/spb/blob/master/examples/examples_of_using_7.py).
- [Example using № 8 (Download from Google drive using requests module and not using google-api-client)](https://github.com/patsuckow/spb/blob/master/examples/examples_of_using_8.py):
![Example № 8](https://user-images.githubusercontent.com/12321741/71492361-a12b9b00-2847-11ea-93d0-d2a519833a59.gif)

## Documentation:
All english documentation can be found in - [wiki](https://github.com/patsuckow/spb/wiki/1.-Home-(en))

All possible settings (parameters) can be found in the this page - [parameters](https://github.com/patsuckow/spb//wiki/2.-Parameters-(en)).

Русская документация - [wiki](https://github.com/patsuckow/spb/wiki/1.-Home-(ru))

Все возможные настройки (параметры) можно найти на этой странице - [parameters](https://github.com/patsuckow/spb//wiki/2.-Parameters-(ru)).


## Tests:
Unit-tests - [test_spb.py](https://github.com/patsuckow/spb/blob/master/tests/test_spb.py)

Run tests:

`
python3 -m unittest discover
`

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

3. For recording gifs, was used the console utility ** peek ** - 
   Simple animated GIF screen recorder with an easy to use interface
   https://github.com/phw/peek


## Licence:
![GNU GPL v 3 0](https://user-images.githubusercontent.com/12321741/67310082-c4636280-f505-11e9-83a7-d23e8037c54f.png)

## Authors:

**Alexey Patsukov 🇷🇺** - [GitHub profile](https://github.com/patsuckow)

## Contributing:

### Submit issues

If you spotted something weird in application behavior or want to propose a feature you are welcome.

### Write code

If you are eager to participate in application development and to work on an existing issue (whether it should
be a bugfix or a feature implementation), fork, write code, and make a pull request right from the forked project page.

### Spread the word

If you have some tips and tricks or any other words that you think might be of interest for the others — publish it
wherever you find convenient.

### Help in the development of the project
If you want to help in the development of the project or just to thank the 
author, this can be done through PayPal: https://www.paypal.me/patsuckow
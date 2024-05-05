# Using Curses module to print a sine wave
---
![Sine wave screenshot.](/screenshots/curses_pic.png)

![Program output upon succesfull execution](/screenshots/curse_executed.png)

## Modules used
* curses <built-in>
* math <built-in>

> [!CAUTION]
> Program will terminate prematurely if strings are placed beyond the window.
> Terminal window must be manually resized until the program executes fully.
> !["Curses" error handled using `try:', 'except:` block](/screenshots/curse_error.png)

> [!TIP]
> Sine wave properties are given by `_amp`, ` _period` and `_ofst` variables.\n
> The number of samples are given by `_samples`

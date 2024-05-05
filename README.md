# Using Curses module to print a sine wave
---
![Sine wave screenshot.](/screenshots/curses_pic.png)
## Modules used
* curses <built-in>
* math <built-in>

## Issues
---

* Program will terminate prematurely if strings are placed beyond the window.
!["Curses" error handled using `try:', 'except:` block](/screenshots/curse_error.png)

* Terminal window must be manually resized until the program executes fully.
![Program output upon succesfull execution](/screenshots/curse_executed.png)

### Note
* Sine wave properties are given by `_amp`, ` _period` and `_ofst` variables.
* The number of samples are given by `_samples`

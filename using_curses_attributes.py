import curses
from math import pi as PI
from math import sin

def gen_wave(theta:int, amplitude:int, period:int, offset:int):
    omega = 2*PI/period
    val = amplitude*sin(omega*theta) + offset
    return int(val.__round__(2))

def text_color(c_color:int) -> int:
    curses.init_pair(1,c_color,curses.COLOR_BLACK)
    return curses.color_pair(1)

def draw_line(char:str):
    stdscr = curses.initscr()
    curses.curs_set(0)
     
    # Sine wave values - Start
    _amp = 4
    _period = 10
    _ofst = 5
    _samples = 150
    # Sine wave values - End
    
    for index in range(_samples):
        current_value = gen_wave(index,
                               amplitude=_amp,
                               period=_period,
                               offset=_ofst
                               )
        stdscr.addstr(current_value, index, char, text_color(curses.COLOR_RED)) # Tick
        stdscr.addstr(12,0, f'Row = {index}', text_color(curses.COLOR_YELLOW)) # Count
        stdscr.addstr(13,0, f'Column = {current_value}', text_color(curses.COLOR_YELLOW))
        stdscr.addstr(14,0, f'Amplitude = {_amp}', text_color(curses.COLOR_MAGENTA)) 
        stdscr.addstr(15,0, f'Period = {_period}', text_color(curses.COLOR_CYAN)) 
        stdscr.addstr(16,0, f'Offset = {_ofst}', text_color(curses.COLOR_GREEN))
        stdscr.refresh()
        curses.napms(150)    
        
    stdscr.clear()       
    stdscr.addstr(10, 50, 'Bye, Have a nice day!', curses.A_BOLD|text_color(curses.COLOR_YELLOW))
    stdscr.addstr(11, 53, 'Hela-Devs-Sweden', curses.A_ITALIC|text_color(curses.COLOR_YELLOW))
    stdscr.getch()
    curses.endwin()
    
# ----------------------------------- Main Start ----------------------------------- #

def main(*args):
    draw_line('*')
    
try:
    curses.wrapper(main)
except curses.error:
    print('Cannot curse beyond window boundaries!\nResize screen and run again.')

# ------------------------------------ Main End ------------------------------------ #


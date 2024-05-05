import curses
from math import pi as PI
from math import sin

def gen_wave(theta:int, amplitude:int, period:int, offset:int):
    omega = 2*PI/period
    val = amplitude*sin(omega*theta) + offset
    return int(val.__round__(2))

def draw_line(char:str):
    stdscr = curses.initscr()
    curses.curs_set(0)
    
    # Init - colours - Start
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    red_on_black = curses.color_pair(1)
    green_on_black = curses.color_pair(2)
    blue_on_black = curses.color_pair(3)
    yellow_on_black = curses.color_pair(4)
    cyan_on_black = curses.color_pair(5)
    magenta_on_black = curses.color_pair(6)
    # Init - colours - End
    
    # Sine wave values - Start
    _amp = 4
    _period = 10
    _ofst = 5
    # Sine wave values - End
    
    for index in range(150):
        current_value = gen_wave(index,
                               amplitude=_amp,
                               period=_period,
                               offset=_ofst
                               )
        stdscr.addstr(current_value, index, char, red_on_black) # Tick
        stdscr.addstr(12,0, f'Row = {index}', green_on_black) # Count
        stdscr.addstr(13,0, f'Column = {current_value}', blue_on_black)
        stdscr.addstr(14,0, f'Amplitude = {_amp}', yellow_on_black) 
        stdscr.addstr(15,0, f'Period = {_period}', cyan_on_black) 
        stdscr.addstr(16,0, f'Offset = {_ofst}', magenta_on_black)
        stdscr.refresh()
        curses.napms(150)    
        
    stdscr.clear()       
    stdscr.addstr(10, 50, 'Bye, Have a nice day!', curses.A_BOLD|yellow_on_black )
    stdscr.addstr(11, 53, 'Hela-Devs-Sweden', curses.A_ITALIC|yellow_on_black )
    stdscr.getch()
    curses.endwin()
    
# ----------------------------------- Main Start ----------------------------------- #

def main(*args):
    draw_line('*')
    
try:
    curses.wrapper(main)
except curses.error:
    print('Cannot curse beyond window boundaries!')

# ------------------------------------ Main End ------------------------------------ #


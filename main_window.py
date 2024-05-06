import curses
def main_window():
    stdscr = curses.initscr()
    curses.curs_set(0)
    
    char = '-'
    
    for column in range(curses.COLS):
        stdscr.addstr(0, column, char)
    stdscr.refresh()
    
    for row in range(curses.LINES):
        stdscr.addstr(row,0, char)
    stdscr.refresh()
       
    return stdscr.getkey()

def main(*args):
    while True:
                
        if main_window() in ['q','Q']:
            break
        else:
            continue
        
curses.wrapper(main)

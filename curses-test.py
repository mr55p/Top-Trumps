import curses, time, os, sys, math




def main():
	# Init the console window 
	screen = curses.initscr()
	curses.noecho()
	curses.cbreak()
	screen.keypad(True)
	# Done

	# Write text to console
	screen.addstr('Welcome to my world... Won\'t you come inside?')
	while True:
		event = screen.getch()
		if event == ord('q'):
			break

	curses.echo()
	curses.nocbreak()
	screen.keypad(False)
	curses.endwin()
	return 0


if __name__ == '__main__':
	s = main()
	sys.exit(s)

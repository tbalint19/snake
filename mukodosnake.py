import curses
import time
import random

screen = curses.initscr()
screen.keypad(1)
dims = screen.getmaxyx()

def snake() :

    screen.nodelay(1)
    fej = [1, 1]
    test = [fej[:]]*5

    screen.border()

    direction = 6 # 6: right, 2: down, 4: left, 8: up
    jatek = True
    kaja = False
    vege = test[-1][:]
    while jatek :

        while not kaja :
            y, x = random.randrange(1, dims[0]-1), random.randrange(1, dims[1]-1)
            if screen.inch(y, x) == ord(' '):
                kaja = True
                screen.addch(y, x, ord('@'))

        if vege not in test :

            screen.addch(vege[0], vege[1], ' ')
        screen.addch(fej[0], fej[1], 'x')

        action = screen.getch()
        if action == curses.KEY_UP and direction != 2 :
            direction = 8
        if action == curses.KEY_DOWN and direction != 8 :
            direction = 2
        if action == curses.KEY_RIGHT and direction != 4 :
            direction = 6
        if action == curses.KEY_LEFT and direction != 6 :
            direction = 4



        if direction == 6 :
            fej[1] += 1
        elif direction == 4 :
            fej[1] -= 1
        elif direction == 2 :
            fej[0] += 1
        elif direction == 8 :
            fej[0] -= 1

        vege = test[-1]

        for z in range(len(test)-1, 0, -1) :
            test[z] = test[z-1][:]

        test[0] = fej[:]

        if screen.inch(fej[0], fej[1]) != ord(' ') :
            if screen.inch(fej[0], fej[1]) == ord('@') :
                kaja = False
                test.append(test[-1])
            else :
                jatek = False


        screen.move(dims[0]-1, dims[1]-1)
        screen.refresh()

        time.sleep(0.05)

    screen.clear
    screen.nodelay(0)

snake()


curses.endwin()

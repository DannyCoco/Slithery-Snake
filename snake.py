import random
import curses

# Initialize the screen
s = curses.initscr()
curses.cbreak()
curses.raw()

# 0 so cursor doesn't appear on screen
curses.curs_set(1)

# Get width/height 
sh, sw = s.getmaxyx()

# Create a new window
w = curses.newwin(sh, sw, 0, 0)

# Accept keypad input
w.keypad(1)

# Screen updates every 100ms
w.timeout(100)

# Snake's initial position
snake_x = sw // 4
snake_y = sh // 2

# Snake's body parts
snake = [
    [snake_y, snake_x],       # head [0][0]
    [snake_y, snake_x - 1],   # body [0][1]
    [snake_y, snake_x - 2]    # tail [0][2]
]

# Food's initial position
food = [sh // 2, sw // 2]

# Add food to screen, set PI as icon
w.addch(food[0], food[1], curses.ACS_PI)

# Snake's initial direction
key = curses.KEY_RIGHT

# Next direction
while True:
    next_key = w.getch()
    #key = key if next_key == -1 else next_key
    key = key if next_key not in [261, 450, 452, 454, 456] else next_key
    
    #if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0][1] < 0 or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    
    new_head = [snake[0][0], snake[0][1]]

    # Arrow key values for EA computer
    if key == 456:
        new_head = [snake[0][0]+1, snake[0][1]]
    if key == 450:
        new_head = [snake[0][0]-1, snake[0][1]]
    if key == 452:
        new_head = [snake[0][0], snake[0][1]-1]
    if key == 261: 
        new_head = [snake[0][0], snake[0][1]+1]
    if key == 454: 
        new_head = [snake[0][0], snake[0][1]+1]


    '''
    # curses.Key_ not working on this computer. Test again back home.
    if key == curses.KEY_DOWN:
        #new_head[0] += 1
        new_head = [snake[0][0]+1, snake[0][1]]
    if key == curses.KEY_UP:
        #new_head[0] -= 1
        new_head = [snake[0][0]-1, snake[0][1]]
    if key == curses.KEY_LEFT:
        #new_head[1] -= 1
        new_head = [snake[0][0], snake[0][1]-1]
    if key == curses.KEY_RIGHT: 
        #new_head[1] += 1
        new_head = [snake[0][0], snake[0][1]+1]
    '''

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = new_food if new_food not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')
    
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0][1] < 0 or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
    
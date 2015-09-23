import time
import simplegui

counter = 0 # global counter variable
wins = 0 # global wins tracker
tries = 0 # global tries tracker

def format(time):
    """
    Converts tenths of seconds counter into a formatted
    string of time passed in the form of A:BC.D
    """
    global D
    A = time // 600 # minutes
    B = ((time // 10) % 60) // 10 # tens of seconds
    C = (time // 10) % 60 % 10 # seconds
    D = time % 10 # tenths of seconds
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

def start_handler(): # Begins timer
    timer.start()
    global is_on
    is_on = True
        
def stop_handler():
    """
    Stops game, prevents wins and tries from increasing 
    while game is stopped
    """
    global wins, tries, is_on
    if D == 0 and is_on:
        wins += 1
        tries += 1
        is_on = False
    elif is_on:
        tries += 1
        is_on = False
    else:
        tries += 0
    timer.stop()
    
def reset_handler(): # Stops timer, resets variables
    global counter, wins, tries, is_on
    timer.stop()
    is_on = False
    counter = 0
    wins = 0
    tries = 0

def timer_handler(): # Increases counter every 100ms
    global counter
    counter += 1
    
def draw_handler(canvas):
    canvas.draw_text(format(counter), (55, 150), 60, "White", 
                     'monospace')
    canvas.draw_text(str(wins) + "/" + str(tries), (220, 35), 35, 
                    "White", 'monospace')
       
frame = simplegui.create_frame("Stopwatch: The Game", 
                               300, 300)
"""Event handlers"""
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.set_canvas_background('Crimson')
button1 = frame.add_button('Start', start_handler, 100)
button2 = frame.add_button('Stop', stop_handler, 100)
button3 = frame.add_button('Reset', reset_handler, 100)

frame.start()
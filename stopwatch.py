# "Stopwatch: The Game"

"""
Timer will start after clicking start button - objective of the game is to click the
Stop button and stop the stopwatch at a whole second - i.e 1.0, 2.0, ... , 15.0.

""" 

import simpleguitk as simplegui

# define global variables
time = 0
player1counter = 0
total_counter = 0
score = "Score: %d/%d" % (player1counter, total_counter)
player1click = True




# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #takes t (1/10th seconds) and converts it to seconds and then minutes -> A:
    min = t / 10
    A = min / 60
    
    #takes seconds and converts it to tens of seconds -> :B
    tens_sec = min % 60 
    B = tens_sec / 10 

    #takes seconds and converts it ones of seconds -> C.
    C = tens_sec % 10

    #takes seconds and conerts it tenths of second -> .D
    D = t % 10
    
    return ("%d:%d%d.%d" % (A, B, C, D))
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def starttime():
    # starts timer and updates player1click back to True so that 
    # you can stop game in stoptime()
    global player1click
    timer.start()
    player1click = True     

def stoptime():
    global player1click, player1counter, total_counter, score
    # Switches player1click to False so that you stoptime() button loses functionality.
    # If time(in 1/10th of a second) is divisible by 10 (whole second) at STOP, player 
    # receives 1 point
    if player1click:
        player1click = False
        timer.stop()
        if time % 10 == 0:
            player1counter += 1
        total_counter +=1
        score = ("Score: %d/%d" % (player1counter, total_counter))
    else:
        None
     
def reset():
    global time, player1counter, total_counter, score
    if player1click is True or player1click is False:
        time = 0
        player1counter = 0
        total_counter = 0
        score = "Score: %d/%d" % (player1counter, total_counter)
        timer.stop()
    
   

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time),[160, 200], 40, "white")
    canvas.draw_text(score, [275, 30], 24, "blue")
       
# create frame
frame = simplegui.create_frame("Stopwatch", 400, 390)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", starttime, 100)
frame.add_button("Stop", stoptime, 100)
frame.add_button("Reset", reset, 100)


# start frame
frame.start()



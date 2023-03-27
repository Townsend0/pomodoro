from data import *

a = Timer()
a.screen_settings()
a.buttons()
a.tomato_img()
a.label()
a.check_mark()

rep = 0
check_mark = " "
cancel_timer = None

def countdown(b):
        global cancel_timer
        c = [b // 60, b % 60]
        if b >= 0:
            cancel_timer = a.window.after(1000, countdown, b - 1)
            for d in range(len(c)):
                if c[d] <= 9:
                    c[d] = f"0{c[d]}"
            a.canvas.itemconfig(a.current_time, text = f"{c[0]}:{c[1]}")
        else:
            start_counting()

def start_counting():
    a.start.config(state = "disabled")
    global rep, check_mark
    rep += 1
    if rep in range(1,8,2):
        a.label.config(text = "WORK", fg = RED)
        countdown(25 * 60) 
    elif rep in range(2,7,2):
        check_mark += "☑ "
        a.check_mark.config(text = check_mark)
        a.label.config(text = "SHORT BREAK", fg = GREEN)
        countdown(5 * 60) 
    elif rep == 8:
        check_mark += "☑ "
        a.check_mark.config(text = check_mark)
        a.label.config(text = "LONG BREAK", fg = PINK)
        countdown(20 * 60)
    else:
        reset_counter()

def reset_counter():
    a.start.config(state = "active")
    global rep, cancel_timer, check_mark
    check_mark = " "
    rep = 0
    a.check_mark.config( text = check_mark)
    a.window.after_cancel(cancel_timer)
    a.label.config(text = "Timer", fg = GREEN)
    a.canvas.itemconfig(a.current_time, text = "00:00")
    
a.start.config(command = start_counting)
a.reset.config(command = reset_counter)

a.hold_screen()


import tkinter

PINK, RED, GREEN, YELLOW = "#e2979c", "#e7305b", "#9bdeac", "#f7f5dd" 

class Timer:

    def screen_settings(self):
        self.window = tkinter.Tk()
        self.window.config(bg = YELLOW, padx = 100, pady = 100)
        self.window.title("PROMODORO")

    def hold_screen(self):
        self.window.mainloop()

    def tomato_img(self):
        self.canvas = tkinter.Canvas(width = 220, height = 240, bg = YELLOW, highlightthickness = 0)
        self.img = tkinter.PhotoImage(file = "tomato.png")
        self.canvas.create_image(110, 120, image = self.img)
        self.current_time = self.canvas.create_text(110, 145, text = "00:00", font = ("courier", 20, "bold"))
        self.canvas.grid(row = 1, column = 1, pady = 20)

    def label(self):
        self.label = tkinter.Label(text = "Timer", bg = YELLOW, fg = GREEN, font = ("courier", 40, "bold"))
        self.label.grid(row = 0, column = 1)

    def buttons(self):
        self.start = tkinter.Button(text = "Start", highlightthickness = 0)
        self.reset = tkinter.Button(text = "Reset", highlightthickness = 0)
        self.start.grid(row = 2, column = 0)
        self.reset.grid(row = 2, column = 2)

    def check_mark(self):
        self.check_mark = tkinter.Label(text = " ", fg = "green", bg = YELLOW, font=("normal", 20, "bold"))
        self.check_mark.grid(row = 3, column = 1)      

    


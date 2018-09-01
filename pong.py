#!/usr/bin/python3

from tkinter import *
from sys import *
import time 

class Bat:
    def __init__(self, x0, y0, x1, y1, canvas):
        self.score = 0
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.canvas = canvas
        self.bat = canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill="white")
        


    def moveUp(self, event):
        if (self.y0 > 0):
            self.y0 -= 20
            self.canvas.move(self.bat, 0, -10)
            self.canvas.after(0)
            self.canvas.update()

    def moveDown(self, event):
        if (self.y0 < 450):
            self.y0 += 20
            self.canvas.move(self.bat, 0, 10)
            self.canvas.after(0)
            self.canvas.update()
    
class BestScore:
    def __init__ (self):
        self.best_score=0
        
class Ball(Bat):
    def __init__(self, canvas, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill="red")

        

    def moveBall(self, left_bat, right_bat, left_best_score, right_best_score):
        while left_bat.score < 5 and right_bat.score < 5:
            if self.x > 770:
                if self.y < right_bat.y0 or self.y > right_bat.y0 + 150:
                    left_bat.score += 1
                    self.canvas.coords(self.ball, 390, 290, 410, 310)
                    self.x, self.y = 400, 300
                self.a *= -1
            if self.x < 30:
                if self.y < left_bat.y0 or self.y > left_bat.y0 + 150:
                    right_bat.score += 1
                    self.canvas.coords(self.ball, 390, 290, 410, 310)
                    self.x, self.y = 400, 300
                self.a *= -1
            if self.y < 10 or self.y > 590:
                self.b *= -1

            self.x += self.a
            self.y += self.b
            self.canvas.move(self.ball, self.a, self.b)
            self.canvas.after(10)
            self.canvas.update()
        if left_bat.score == 5:
            left_best_score.best_score +=1            
            print("Left player won!")
            print("Left player's score", left_best_score.best_score)

        else:
            right_best_score.best_score +=1
            print("Right player won!")
            print("Right player's best score", right_best_score.best_score)
            

        time.sleep(5)
        print("Left player's best score", left_best_score.best_score)
        print("Right player's best score", right_best_score.best_score)
        print("Today is the max Score", max(left_best_score.best_score, right_best_score.best_score ))
        print("//////////////////////////////////////////////////////////////")
        left_bat.score = 0
        right_bat.score = 0
        Ball.moveBall(self, left_bat, right_bat, left_best_score, right_best_score)
        


win = Tk()
win.minsize(800, 600)
win.maxsize(1920, 600)

a = 5
b = 5
top = Frame(width=800, bg="black")
canvas = Canvas(win, width=800, height=600, bg="black")
canvas.pack()

left_bat = Bat(0, 225, 20, 375, canvas)
right_bat = Bat(780, 225, 800, 375, canvas)
ball = Ball(canvas, 400, 300, 2, -2)
left_best_score = BestScore()
right_best_score = BestScore()






canvas.bind_all('<w>', left_bat.moveUp)
canvas.bind_all('<s>', left_bat.moveDown)
canvas.bind_all('<Up>', right_bat.moveUp)
canvas.bind_all('<Down>', right_bat.moveDown)
ball.moveBall(left_bat, right_bat, left_best_score, right_best_score)

win.mainloop()

from turtle import Turtle
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("E://100 days of python//Day 23//data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align='center', font=FONT)
    

    def score_up(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER !", align='center', font=('Courier', 20, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("E://100 days of python//Day 23//data.txt", mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()


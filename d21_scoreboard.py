from turtle import Turtle

# My Solution
# class Scoreboard():
#     def __init__(self):
#         self.score = -1
#         self.score_keeper = Turtle()
#         # score_display = "Score: "
#         self.score_keeper.color("white")
#         self.score_keeper.hideturtle()
#         self.score_keeper.goto(-50, 275)
#
#     def scoreboard(self):
#         self.score += 1
#         self.score_keeper.clear()
#         self.score_keeper.write(f"Score: {str(self.score)}", font="utf-8")


# Instructor Solution:

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 20)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
        self.goto(0, 0)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)



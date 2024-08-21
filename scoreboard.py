from turtle import Turtle


SCORE_FONT =  ("Arial", 12, "bold")
GAME_OVER_FONT = ("Arial", 16, "bold")
RESTART_FONT = ("Arial", 10, "bold")



class Scoreboard(Turtle):
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        try:
            with open("/Users/EmilNielsen/Desktop/Programming/pythonfiles/100days/day20and21/snake_game/highscore.txt", "r") as file:
                self.highscore = int(file.read())
        except:
            self.highscore = 0
        self.color("white")
        self.up()
        self.setpos(0, 288)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score :  {self.score}", False, "center", SCORE_FONT)
        
    def add_score(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", False, "center", GAME_OVER_FONT)
        self.setpos(0, -295)
        self.write("click 'r' to restart", False, "center", RESTART_FONT)
        
        if self.score > self.highscore:
            self.highscore = self.score
            with open("/Users/EmilNielsen/Desktop/Programming/pythonfiles/100days/day20and21/snake_game/highscore.txt", "w") as file:
                file.write(str(self.highscore))
                
        self.setpos(230, 288)
        self.write(f"HighScore: {self.highscore}", False, "center", SCORE_FONT)
        
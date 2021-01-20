def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
        return response


class Player(object):
    def __init__(self,name,):
        self.name = name
        self.score = Score()
        self.isAlive = True
        self.lifes = 3

class Score(object):
    def __init__(self):
        self.score = 0

    def add_to_score(self, points):
        self.score += points

    def take_points(self,points):
        self.score -= points
        if self.points < 0:
            self.score = 0

if __name__ == "__main__":
    print("this is a module with classes for playing cards. not ment to be ran on its own")
    input("\n\nPress the enter key to exit")

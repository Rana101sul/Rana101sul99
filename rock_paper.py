import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Randomplayer (Player):
    def move(self):
        return random.choice(moves)


class Humanplayer(Player):
    def move(self):
        human_choice = input("Rock, Paper , Scissors?")
        while human_choice not in moves:
            human_choice = input("Rock, Paper, Scissors?")
        return human_choice


class Reflectplayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move


class Cycleplayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'

    def __init__(self):
        super().__init__()
        self.my_move = None


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            print("Player one wins!")
            self.score1 += 1
            print(f"score: player1: {self.score1} , player2: {self.score2} \n")
        elif beats(move2, move1) is True:
            print("Player two wins!")
            self.score2 += 1
            print(f"score: player1: {self.score1} , player2: {self.score2} \n")
        else:
            print("Tie!!")
            print(f"score: player1: {self.score1} , player2: {self.score2} \n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print(f"Game over!\
         Final score: player1: {self.score1} ,player2: {self.score2}")
        if self.score1 > self.score2:
            print(" Yay! Player1 wins")
        elif self.score1 < self.score2:
            print("Yay! Player2 wins")
        else:
            print("It's Tie!")


if __name__ == '__main__':
    strategy = input("which strategy would you like the computer to use?\n\
    1-Rock, 2-Random, 3-Reflect, 4-Cycle\n\
    Enter a number 1 to 4: ")
    while strategy not in ["1", "2", "3", "4"]:
        strategy = input("please enter a number between 1 to 4:")
    if strategy == "1":
        print("the computer will always plays 'rock' ")
        game = Game(Humanplayer(), Player())
        game.play_game()
    elif strategy == "2":
        print("the computer will choose its moves randomly ")
        game = Game(Humanplayer(), Randomplayer())
        game.play_game()
    elif strategy == "3":
        print("the computer will remember and imitate\
         what u did previous round")
        game = Game(Humanplayer(), Reflectplayer())
        game.play_game()
    elif strategy == "4":
        print("the computer will Cycle through all the moves")
        game = Game(Humanplayer(), Cycleplayer())
        game.play_game()
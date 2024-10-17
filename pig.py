import random


def roll_die(sides=6):
    """
    function to roll the die
    """
    return random.randint(1, sides)


class Player:
    """
    THis class represents a player
    """
    def __init__(self, name) -> None:
        self.name = name
        self.total_points = 0

    def display(self):
        """
        Print name and points for this playes
        """
        print(f"{self.name} has {self.total_points} points.")


    def __str__(self) -> str:
        """String represenation of the player"""
        return f"{self.name} has {self.total_points} points."

    def play_turn(self):
        """
        Play a turn

        - Ask the player to Roll or Hold
        - If hold, bank the points and exit
        - If roll, roll the die
        - if roll = 1, exit
        - if roll != 1, accumulat points to turn_points and repeat 
        """
        turn_points = 0


class Game:
    """
    THis class represents the game
    """
    def __init__(self, player1, player2, win_points = 100) -> None:
        self.players = [player1, player2]
        self.win_points = win_points
        self.winner = None

    def check_winner(self):
        """
        Returns True if there is a winner
        """
        for player in self.players:
            if player.total_points >= self.win_points:
                self.winner = player
                return True

        return False
    

    def play(self):
        """
        Play the game
        """
        current_player_idx = 0
        while not self.check_winner():
            current_player = self.players[current_player_idx]
            print(f"It's {current_player.name}'s Turn")
            # play a turn
            current_player.play_turn()
                      
            current_player_idx = 0 if current_player_idx == 1 else 1
            print("---------------- End of Round -------------------")

        print(f"The winner is {self.winner.name}")
        self.winner.display()


if __name__ == "__main__":
    p1 = Player("Alice")
    p2 = Player("Bob")

    p1.display()
    p2.display()

from player import Player
import random

class Game:
    players = list()
    player_names = set()
    player_count = 0
    current_player = None
    rounds = 10

    def __init__(self, rounds):
        self.rounds = rounds
        print('Bank Dice Game')
        self.__read_players()
        self.__play_rounds()
    
    
    def __play_rounds(self):
        for round in range(1, self.rounds + 1):
            print(f'Round {round}')
            self.__play_round()
        
        print('Game over!')
        self.__print_players()

            
    def __play_round(self):
        self.__print_players()
        player_num = 0
        player = self.players[player_num]
        round_score = 0
        bankers = set()
        roll = 1

        while True:
            print(f'{player}\'s turn')

            if self.__read_bankers(bankers, round_score):
                print('Everyone has banked, round over!')
                return
            
            self.__player_roll(player_num)
    
    
    def __player_roll(self, player, roll, round_score):
        input('Press enter to roll the dice!')
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum = dice1 + dice2

        if roll < 3:
            if sum == 7:
                round_score += 70
                return


    # Returns True iff everyone has banked
    def __read_bankers(self, bankers, round_score):
        while True:
            banker = input('Enter a player number who banked or s to stop: ')

            if banker == 's':
                return False
            
            if not banker.isdigit():
                print('The player number must be a digit. Please try again\n')
                continue

            if banker < 1 or banker > self.player_count:
                print('That player number does not exist. Please try again\n')
                continue
            
            if banker in self.bankers:
                print('That player has already banked. Please try again\n')
                continue

            self.bankers.add(banker)
            self.players[banker].score += round_score

            if len(self.bankers) == self.player_count:
                return True


    def __print_players(self):
        for i in range(self.player_count):
            print('Players:')
            player = self.players[i]
            print(f'{i + 1} - {player.name}, Score: {player.score}')


    def __read_players(self):
        while True:
            name = input('Enter a player name or s to stop: ')

            if name == '':
                print('Player name cannot be empty. Please try again\n')
                continue

            if name == 's':
                if self.player_count < 2:
                    print('There must be at least 2 players' +
                        ' Please try again\n')
                    continue
                break

            if name in self.player_names:
                print(f'{name} is already in the game. Please try again\n')
                continue
            
            self.player_names.add(name)
            self.players.append(Player(name))
            self.player_count += 1
            print(f'Player {self.player_count} Added {name} to the game\n')
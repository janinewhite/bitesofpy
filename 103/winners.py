#games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)
games_won = [{"name":"sara","wins":0},{"name":"bob","wins":1},{"name":"tim","wins":3},{"name":"jim","wins":1})]

def print_game_stats(games_won=games_won):
    """Loop through games_won's dict (key, value) pairs (dict.items)
       printing (print, not return) how many games each person has won,
       pluralize 'game' based on number.

       Expected output (ignore the docstring's indentation):

       sara has won 0 games
       bob has won 1 game
       tim has won 5 games
       julian has won 3 games
       jim has won 1 game

       (Note that as of Python 3.7 - which we're using atm - dict insert order is retained
        so no sorting is required for this Bite.)
    """
    pass
for person in games_won:
    name = person["name"]
    wins = int(person["wins"])
    print(f'{name} has won {str(wins)} game{"" if wins==1 else "s"}')
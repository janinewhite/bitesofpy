games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def print_game_stats(games_won=games_won):
    for key, value in games_won.items():
        print(f'{key} has won {str(value)} game{"" if value==1 else "s"}')
    pass
import random
from cannon import Cannon

def play_bang():
    jaehyeok = Cannon('재혁', 200, 10, 70, 3)
    deputy1 = Cannon('Deputy1', 100, 7, 50, 3)
    deputy2 = Cannon('Deputy2', 100, 7, 50, 3)
    outlaw1 = Cannon('Outlaw1', 100, 7, 30, 6)
    outlaw2 = Cannon('Outlaw2', 100, 7, 30, 6)
    outlaw3 = Cannon('Outlaw3', 100, 7, 30, 6)
    renegade = Cannon('Renegade', 100, 7, 30, 6)
    players = [jaehyeok, deputy1, deputy2, outlaw1, outlaw2, outlaw3, renegade]
    dead_players = []

    max_rounds = 5
    round = 0
    while jaehyeok.is_alive() and round < max_rounds:
        print(f'======== round {round} ========')
        for player in players:
            target = random.choice(players)
            player.fire(target)
            if not target.is_alive():
                players.pop(players.index(target))
                dead_players.append(target)

        for player in players + dead_players:
            player.print_status()

        round += 1
    
    for player in players:
        player.fire_for_a_sec()

if __name__ == '__main__':
    play_bang()
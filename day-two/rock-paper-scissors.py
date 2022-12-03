import game

with open('data/raw-data.txt', 'r') as file:
    lines = file.read().split('\n')
    total_score = []
    strategy = True
    for l in lines:
        round = l.split()
        opp_shape = round[0]
        p_shape = round[1]

        p_shape_score = game.get_shape_score(p_shape, strategy, opp_shape)
        p_round_score = game.round_outcome(p_shape, opp_shape, strategy)
        p_round_total = p_shape_score + p_round_score

        total_score.append(p_round_total)
    
    print(sum(total_score))
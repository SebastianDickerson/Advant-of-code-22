def strategic_shape(player_shape, opp_shape):
    strategy_shape = ''

    if player_shape == 'X':
        if opp_shape == 'A':
            strategy_shape = 'Z'
        elif opp_shape == 'B':
            strategy_shape = 'X'
        elif opp_shape == 'C':
            strategy_shape = 'Y'
    
    if player_shape == 'Y':
        if opp_shape == 'A':
            strategy_shape = 'X'
        elif opp_shape == 'B':
            strategy_shape = 'Y'
        elif opp_shape == 'C':
            strategy_shape = 'Z'
    
    if player_shape == 'Z':
        if opp_shape == 'A':
            strategy_shape = 'Y'
        elif opp_shape == 'B':
            strategy_shape = 'Z'
        elif opp_shape == 'C':
            strategy_shape = 'X'

    return strategy_shape

def get_shape_score(shape, strategy, opp_shape):
    player_options = {
            "X": 1,
            "Y": 2,
            "Z": 3
        }

    if strategy:
        strategic_choice = strategic_shape(shape, opp_shape)
        player_shape = player_options.get(strategic_choice)
    else:
        player_shape = player_options.get(shape)

    return player_shape

def round_outcome(p, opp, strategy):
    result = ''
    outcomes = {
        "loss": 0,
        "draw": 3,
        "win": 6
    }

    if p == 'X':
        if strategy:
            result = 'loss'
        else:
            if opp == 'A':
                result = 'draw'
            elif opp == 'B':
                result = 'loss'
            elif opp == 'C':
                result = 'win'

    if p == 'Y':
        if strategy:
            result = 'draw'
        else:
            if opp == 'A':
                result = 'win'
            elif opp == 'B':
                result = 'draw'
            elif opp == 'C':
                result = 'loss'

    if p == 'Z':
        if strategy:
            result = 'win'
        else:
            if opp == 'A':
                result = 'loss'
            elif opp == 'B':
                result = 'win'
            elif opp == 'C':
                result = 'draw'

    return outcomes.get(result)
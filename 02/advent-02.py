def load_strategy_guide(filename:str):
    with open(filename, "r") as f:
        guide = [tuple(x.split()) for x in f.readlines()]
    return guide

def score_round(opponent_move:str, your_move:str):
    if your_move == "X":
        shape_score = 1
        if opponent_move == "A":
            round_score = 3
        elif opponent_move == "B":
            round_score = 0
        elif opponent_move == "C":
            round_score = 6
    elif your_move == "Y":
        shape_score = 2
        if opponent_move == "A":
            round_score = 6
        elif opponent_move == "B":
            round_score = 3
        elif opponent_move == "C":
            round_score = 0
    elif your_move == "Z":
        shape_score = 3
        if opponent_move == "A":
            round_score = 0
        elif opponent_move == "B":
            round_score = 6
        elif opponent_move == "C":
            round_score = 3
    return shape_score + round_score

def real_strat_score(opponent_move:str, desired_outcome:str):
    if desired_outcome == "X":
        round_score = 0
        if opponent_move == "A":
            shape_score = 3
        elif opponent_move == "B":
            shape_score = 1
        elif opponent_move == "C":
            shape_score = 2
    elif desired_outcome == "Y":
        round_score = 3
        if opponent_move == "A":
            shape_score = 1
        elif opponent_move == "B":
            shape_score = 2
        elif opponent_move == "C":
            shape_score = 3
    elif desired_outcome == "Z":
        round_score = 6
        if opponent_move == "A":
            shape_score = 2
        elif opponent_move == "B":
            shape_score = 3
        elif opponent_move == "C":
            shape_score = 1
    return shape_score + round_score

if __name__ == "__main__":
    strat = load_strategy_guide("input.txt")
    # part one
    print(sum([score_round(x, y) for x, y in strat]))
    # part two
    print(sum([real_strat_score(x, y) for x, y in strat]))

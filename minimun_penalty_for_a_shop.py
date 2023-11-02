# https://leetcode.com/problems/minimum-penalty-for-a-shop/


def bestClosingTime(customers: str) -> int:

    min_penalty = 999999999999999999999
    best_time = 0
    penalty = 0

    for pos, char in enumerate(customers):

        if char == "Y":
            penalty += 1

    best_time = -1
    min_penalty = penalty

    for pos, char in enumerate(customers):

        if char == "Y":
            penalty -= 1

        if char == "N":
            penalty += 1

        if penalty < min_penalty:
            min_penalty = penalty
            best_time = pos

    return best_time+1 if best_time != -1 else 0


""" def bestClosingTime(customers: str) -> int:

    best_time = 0
    score = 0
    best_score = 0

    for pos,char in enumerate(customers):
        if char == "Y":
            score+=1
        elif char=="N":
            score-=1

        if score>best_score:
            best_time=pos+1
            best_score=score

    
    return best_time """

""" print(bestClosingTime("YYNY"))
print(bestClosingTime("NNNNN"))
print(bestClosingTime("YYYY"))
print(bestClosingTime("NNNYNN"))
print(bestClosingTime("NNNYNN"))
print(bestClosingTime("YN"))"""

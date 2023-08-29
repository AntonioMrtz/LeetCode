# https://leetcode.com/problems/minimum-penalty-for-a-shop/

def bestClosingTime(customers: str) -> int:

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

    
    return best_time


""" print(bestClosingTime("YYNY"))
print(bestClosingTime("NNNNN"))
print(bestClosingTime("YYYY"))
print(bestClosingTime("NNNYNN")) """

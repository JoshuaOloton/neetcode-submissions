class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
            else:
                twenties += 1
            
            change = bill - 5
            if not change:
                continue
            if change == 5:
                if not fives:
                    return False
                fives -= 1
            elif change == 15:
                if (not tens or not fives) and fives < 3:
                    return False
                if tens >= 1 and fives >= 1:
                    fives -= 1
                    tens -= 1
                else:
                    fives -= 3
        
        return True
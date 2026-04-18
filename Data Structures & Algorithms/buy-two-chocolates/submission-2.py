class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_price = second_min_price = float('inf')
        for p in prices:
            if p < min_price:
                second_min_price = min_price
                min_price = p
            elif p < second_min_price:
                second_min_price = p
            
        change = money - min_price - second_min_price
        return change if change >= 0 else money
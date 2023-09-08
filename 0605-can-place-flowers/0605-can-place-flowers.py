class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(0, len(flowerbed)):

            is_left_empty = False
            if i == 0:
                is_left_empty = True 
            elif (flowerbed[i-1] == 0):
                is_left_empty = True

            is_right_empty = False
            if i == len(flowerbed)-1:
                is_right_empty = True 
            elif (flowerbed[i+1] == 0):
                is_right_empty = True

            if flowerbed[i] == 0 and is_right_empty and is_left_empty:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True

        if n <= count:
            return True
        return False
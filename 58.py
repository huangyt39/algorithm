# TE：非常暴力的去掉出现次数大于四的与元素

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        if not numbers:
            return 
        
        res = []
        Solution.arrSort(1, numbers)
        Solution.delNumber(1, numbers)
        
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                
                sumval = target - numbers[i] - numbers[j]
                
                left, right = j+1, len(numbers)-1
                while left < right:
                    while left == i or left == j:
                        left += 1
                    while right == i or right == j:
                        right -= 1
                    if left >= right:
                        break
                    
                    if numbers[left] + numbers[right] == sumval:
                        tmp = [numbers[left] , numbers[right], numbers[i], numbers[j]]
                        Solution.arrSort(1, tmp)
                        if tmp not in res:
                            res.append(tmp)
                        left += 1
                    elif numbers[left] + numbers[right] < sumval:
                        left += 1
                    else:
                        right -= 1
                        
        return res
        
    def delNumber(self, arr):
        i = 0
        num, count = 0, 0
        while i < len(arr):
            if arr[i] == num:
                if count == 4:
                    del arr[i]
                    continue
                else:
                    count += 1
            else:
                num = arr[i]
                count = 1
            i += 1
        
    def arrSort(self, arr):
        for i in range(len(arr)):
            change = False
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    change = True
            if not change:
                break
        return
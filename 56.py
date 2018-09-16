class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hashtable = {}
        for i in range(len(numbers)):
          if target - numbers[i] not in hashtable:
            hashtable[numbers[i]] = i
          else:
            return hashtable[target - numbers[i]], i

arr = [2, 7, 9, 13]
tar = 9
print(Solution.twoSum(arr, arr, tar))
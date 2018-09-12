class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def quicksort(self, arr, head, tail, k):
      i = head + 1
      j = tail
      while i != j:
        while i != j and arr[j] < arr[head]:
          j -= 1
        while i != j and arr[i] > arr[head]:
          i += 1
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
      if arr[head] < arr[i]:
        temp = arr[head]
        arr[head] = arr[i]
        arr[i] = temp
      else : 
        i = head
      if i - 1 > head: Solution.quicksort(arr, arr, head, i - 1)
      if tail > i + 1: Solution.quicksort(arr, arr, i + 1, tail)
      return arr

    def kthLargestElement(self, k, A):
      return Solution.quicksort(A, A, 0, len(A) - 1,k)

B = [9,3,2,4,8]
print(Solution.kthLargestElement(B, 3, B))
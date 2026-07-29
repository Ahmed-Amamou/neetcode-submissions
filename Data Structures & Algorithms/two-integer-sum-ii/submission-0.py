class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #naive solution have two pointers: we fix one and move the other and check if their sum equals the target
        #if the sum is superior we just skip that fix and go to the next until we find our only solution
        n = len(numbers)
        for i in range(n):
            for j in range(i+1,n):
                summ = numbers[i]+numbers[j]
                if summ > target:
                    break
                if summ == target and numbers[i]!=numbers[j]:
                    return [i+1,j+1]
        
        
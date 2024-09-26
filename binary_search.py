class Solution:
    
    # binary search
    def binary_search(self, sorted_list, target, last_mid=0):
        # //2 rounds to floor
        mid = len(sorted_list) // 2
        next_list = []
        
        if sorted_list[mid] < target and mid != 0:
            # take everything from index to end of list, our target will exist in this range
            next_list = sorted_list[mid:]
            # since we are going right we need to keep track of length of left list
            # this allows us to add each left list to get the final index
            last_mid += mid
            print(last_mid)
            return self.binary_search(next_list,target,last_mid)
        elif sorted_list[mid] > target and mid != 0:
            # take everything from the start to index, our target will exist in this range
            next_list = sorted_list[:mid]
            return self.binary_search(next_list,target,last_mid)
        elif sorted_list[mid] == target:
            # mid will always have a value of zero or one here
            return last_mid + mid
        else:
            print("returning None")
            return None

solution = Solution()

data = [1,2,3,4,5,6,23,40,7,3]

sorted_list = sorted(data)
target = -23
print(sorted_list)
print(target, ", was found at index : " , solution.binary_search(sorted_list, target)) 

'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]'''

# arr=list(map(int,input("Enter elements with space seperated: ").split()))
# target = int(input("Enter target: "))

#using a dictionary to keep a track of keyvalue pairs, values and index are stored
'''
1. store in dict of 1st element-> dict = [2,0] {value,index}
2. calculate complement = target - cur_value => comp = 9-2=7
3. 7 is in dict or not?? {[2,0]} -- No, so go to next value

1. store in dict of 2nd element -> dict = [2,0], [7,1]
2. calculate complement = target - cur_value => comp = 9-7 = 2
3. 2 is in dict or not?? {[2,0],[7,1]} -- Yes, so return indexes of value seen and current value'''


class TwoSum:
    def twoSum(self, nums, target):
        dic={}
        for i,n in enumerate(nums):
            comp = target - n
            if comp in dic:
                return [dic[comp],i] #retuns index of complement, currentvalue
            dic[n]=i #otherwise stores current index and value in dict
        return []

obj = TwoSum()
print(obj.twoSum([2,7,11,15],9))
print(obj.twoSum([3,2,4],6))
print(obj.twoSum([3,3],6))
# #https://leetcode.com/problems/two-sum/
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         answer=[]
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     answer.append(i)
#                     answer.append(j)
#         return answer
#
nums = [2,7,11,15]
hash_dict={}
hash_dict['a']=1
hash_dict['aa']=123
hash_dict['ab']=1
hash_dict['c']=1

print(hash_dict.values())
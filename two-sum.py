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


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_dict = {}
#         result = []
#         for i, num in enumerate(nums):
#             hash_dict[num] = i
#
#         for i in range(0, len(nums)):
#             if target - nums[i] in hash_dict and i != hash_dict[target - nums[i]]:
#                 result.append(i)
#                 result.append(hash_dict[target - nums[i]])
#                 break
#         return result
#

#https://www.acmicpc.net/problem/3273
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
hash_dict={}
cnt=0
for i,num in enumerate(arr):
    hash_dict[num]=i

for i in range(0,len(arr)):
    if target-arr[i] in hash_dict and  i < hash_dict[target-arr[i]]:
        cnt+=1
print(cnt)
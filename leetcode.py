#Question 1:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order. 
#Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


#hint : to find 2 numbers of which sum = or != to a target numbr:
    #subtract both nums from target and check if 1st num=target-2nd numbr
    #if yes : result=true else: result=false
def twoSum(nums, target):    
    d = {}
    for i, item in enumerate(nums):
        res = target - item
        if res in d: return [d[res], i]
        d[item] = i
    
print(twoSum([2,51,8,11],10))





# You are given two non-empty linked lists representing two non-negative integers. The 
# digits are stored in reverse order, and each of their nodes contains a single
# digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Definition for singly-linked list.


# Question No: 13
def romanToInt( s: str) -> int:

    result=0
    myd={
        'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
    }
    s=s.replace('IV','IIII').replace('IX','VIIII').replace('XL','XXXX').replace('XC','XXXXXXXXX').replace('CD','CCCC').replace('CM','DCCC')
    print(s)
    return sum(map(lambda x:myd[x],s))
print(romanToInt('MCMXCIV'))
# 

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l3=ListNode()
        carry=0
        head=l3
        while(l1 and l2):
            value=l1.val+l2.val+carry
            carry=value//10
            l3.next=ListNode(value%10)
            l1,l2,l3=l1.next,l2.next,l3.next
        while(l1):
            value=l1.val+carry
            carry=value//10
            l3.next=ListNode(value%10)
            l1,l3=l1.next,l3.next
        while(l2):
            value=l2.val+carry
            carry=value//10
            l3.next=ListNode(value%10)
            l2,l3=l2.next,l3.next
        if(carry):
            l3.next=ListNode(carry)
        return head.next
        

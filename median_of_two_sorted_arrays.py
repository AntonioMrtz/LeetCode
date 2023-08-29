# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math

def findMedianSortedArrays(nums1: list, nums2: list) -> float:

    n = len(nums1)
    m = len(nums2)

    x = math.floor(m+n)/2
    isPair = (m+n) % 2 == 0

    i=0
    j=0

    current = "" 
    prev = ""

    while True:
        #print(f" i = {i} , j ={j}")

        if not isPair and i+j>=x: # caso final array long impar
            print(f"Caso impar i = {i} , j ={j}")

            if current=="i":
                return nums1[i-1]
            elif current=="j":
                return nums2[j-1]
        
        elif isPair and i+j>=x+1: # caso final array long par
            print(f"Caso par i = {i} , j ={j}")
            if current=="i" and prev=="i":
                return (nums1[i-1]+nums1[i-2])/2
            if current=="i" and prev=="j":
                return (nums1[i-1]+nums2[j-1])/2
            if current=="j" and prev=="i":
                return (nums2[j-1]+nums1[i-1])/2
            if current=="j" and prev=="j":
                return (nums2[j-1]+nums2[j-2])/2

        if len(nums1)==0:
            j+=1
            prev = current
            current = "j" 

        elif len(nums2)==0:
            i+=1
            prev = current
            current = "i" 
        
        elif i==n:
            j+=1
            prev = current
            current = "j" 

        elif j==m:
            i+=1
            prev = current
            current = "i"


        elif nums1[i]<nums2[j]:
            i+=1
            prev = current
            current = "i" 

        elif nums2[j]<nums1[i]:
            j+=1
            prev = current
            current = "j"

        elif nums1[i]==nums2[j]:
            i+=1
            prev = current
            current = "i" 


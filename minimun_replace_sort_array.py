# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

""" 
    -> Time Limit pero correcto

    def minimumReplacement(nums: list) -> int:

    replacements = 0
    
    for i in range(len(nums)-2,-1,-1):
        if nums[i]>nums[i+1]:

            new_left_number = nums[i]
            
            while True:

                if new_left_number // nums[i+1] >= 2:

                    new_left_number= new_left_number // nums[i+1]
                    replacements+=1

                elif new_left_number==nums[i+1]:
                    nums[i]=new_left_number
                    break


                else:
                    
                    #poir
                    if new_left_number % 2 ==0:

                        new_left_number = new_left_number / 2

                    else:

                        new_left_number = new_left_number // 2

                    replacements+=1
                    nums[i]=new_left_number

    return replacements """



def minimumReplacement(nums: list) -> int:

    replacements = 0
    
    for i in range(len(nums)-2,-1,-1):
        if nums[i]>nums[i+1]:
                
            nums_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]

            replacements+=(nums_elements-1)
            nums[i] = nums[i] // nums_elements
            print(nums[i])

    return int(replacements)



""" print(minimumReplacement([3,9,3]))
print(minimumReplacement([1,2,3,4,5])) """
print(minimumReplacement([2,10,20,19,1]))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l= len(nums)
        mul_output = 1
        forward_dict = {-1:1}
        backward_dict = { l:1}
        for i in range(0,l):
            mul_output *= nums[i]
            forward_dict.update({i:mul_output})
        print("for", forward_dict)
        mul_output =1

        for i in range(l-1, -1, -1):
            mul_output *= nums[i]
            backward_dict.update({i:mul_output})
        print("back", backward_dict)
        mul_output =1
        ans =[]
        for x in range(l):
            ans.append(forward_dict[x-1]*backward_dict[x+1])
        return(ans)

        
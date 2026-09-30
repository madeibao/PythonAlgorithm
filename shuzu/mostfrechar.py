


class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        
        counter = {}
        for i in range(len(nums)-1):
            if nums[i] == key:
                counter[nums[i+1]] = counter.get(nums[i+1], 0) + 1
        return max(counter, key=counter.get)


if __name__=="__main__":
    nums = [1,100,200,1,100]
    key = 1
    print(Solution().mostFrequent(nums,key))


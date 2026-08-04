class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = defaultdict(int)

        # for num in nums:
        #     count[num] += 1
        # return [key for key, value in count.items() if value >= k]

        dict_ = {}
        arr = [[] for _ in range(len(nums) + 1)]
        res = []
        for num in nums:
            dict_[num] = dict_.get(num, 0) + 1

        for (key_, value_) in dict_.items():
            arr[value_].append(key_)

        for i in range(len(nums), 0, -1):
            for ar in arr[i]:
                res.append(ar)
                if len(res) == k:
                    return res
                
from typing import List


class Solution:
    """20190802"""

    def search(self, nums: List[int], target: int) -> int:
        """
        排序的时间复杂度一般为 O(n^2) 和 O(n log n)
        这里需要 O（long n） 很容易想到二分，但是有旋转，该怎么处理呢
        不管从哪旋转，最后一个肯定是小于第一个，想到一个方案，能不能拼接，将两个数组合并成一个，中间部分是升序的
        试了一会儿失败了

        real_mid = (mid + rotate) % n
        这一句是怎么来的
        4   5   6   7   0   1   2
        low=0,high=6,mid=3
        对应的 real_mid 实际是从 rotate 往后数
        real_mid=mid+rotate-n
        4   5   6   7   0   1   2   4   5   6   7   0   1   2

        所以是
        real_mid = (mid + rotate) % n
        或者直接写为



        >>> Solution().search([4,5,6,7,8,1,2,3],8)
        4
        >>> Solution().search([1,3],3)
        1
        >>> Solution().search([4,5,6,7,0,1,2],0)
        4
        >>> Solution().search([4,5,6,7,0,1,2],3)
        -1
        """
        if not nums:
            return -1
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:  # 找出最小值
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:  # 当前 mid 比最后一个小，说明最小的在 left,mid 间
                high = mid
            else:
                low = mid + 1
        rotate = low
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            real_mid = mid + rotate
            if real_mid >= n:
                real_mid -= n
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

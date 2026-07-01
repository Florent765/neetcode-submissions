class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow, fast = 0, len(numbers) - 1

        while slow < fast:
            if numbers[slow] + numbers[fast] == target:
                return [slow + 1, fast + 1]
            elif numbers[slow] + numbers[fast] < target:
                slow += 1
            else:
                fast -= 1
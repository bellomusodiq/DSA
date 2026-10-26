class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)
        offset = 1

        for number in range(1, n + 1):
            if offset * 2 == number:
                offset *= 2
            result[number] = 1 + result[number - offset]

        return result

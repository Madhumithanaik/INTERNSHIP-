class PairFinder:
    def find_pair(self, numbers, target):
        lookup = {}
        for i, num in enumerate(numbers):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i

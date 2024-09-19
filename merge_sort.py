class MergeSort():
    def sort(self, arr):
        # base case
        if len(arr) <= 1:
            return arr
        
        # divide
        m = len(arr)//2
        left = arr[0:m]
        right = arr[m:]

        # sort
        sorted_left = self.sort(left)
        sorted_right = self.sort(right)

        # merge
        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):
        merged = []

        l, r = 0, 0

        # move the pointers and insert the smaller element into the merged array
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1

        # insert remaining elements into the merge array
        merged.extend(left[l:])
        merged.extend(right[r:])

        return merged


if __name__ == "__main__":
    arr = [9, 3, 1, 2, 4, 8, 16, 4, 3]
    sorter = MergeSort()
    print(sorter.sort(arr)) # [1, 2, 3, 3, 4, 4, 8, 9, 16]

    # Simple example

    # [5, 2, 3] - original array
    # [5] [2, 3] - first division
    # [5] [2] [3] - right sub array from previous step is further divided
    # [5] [2, 3] - right sub array is then merged using the two pointers technique
    # [2, 3, 5] - original left and right sub arrays are then merged using the two pointers technique


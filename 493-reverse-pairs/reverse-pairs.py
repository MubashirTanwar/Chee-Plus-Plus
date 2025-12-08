class Solution(object):
    def merge(self, arr, low, mid, high):
        i, j = low, mid + 1
        temp = []
        count = 0
        
        r = j
        for l in range(low, mid + 1):
            while r <= high and arr[l] > 2 * arr[r]:
                r += 1
            count += (r - (mid + 1))

        i, j = low, mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= high:
            temp.append(arr[j])
            j += 1

        arr[low:high+1] = temp
        return count

    def mergeSort(self, arr, low, high):
        if low >= high:
            return 0
        
        mid = (low + high) // 2
        count = self.mergeSort(arr, low, mid)
        count += self.mergeSort(arr, mid + 1, high)
        count += self.merge(arr, low, mid, high)
        
        return count

    def reversePairs(self, nums):
        return self.mergeSort(nums, 0, len(nums)-1)

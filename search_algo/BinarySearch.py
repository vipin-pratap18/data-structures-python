class BinarySearch:

    def binary_search(self, data, target, low, high):
        #Return true of target is found in the supplied list as data

        if(low > high):
            return False
        else:
            mid = (low + high) // 2
            if target == data[mid]:
                return True
            elif target < data[mid]:
                return self.binary_search(data, target, low, mid - 1)
            else:
                return self.binary_search(data, target, mid + 1, high)

class Misl:

    def linear_sum(self, S, n):
        '''Return the sum of the first n numbers of sequence S'''
        if n == 0:
            return 0
        else:
            return self.linear_sum(S, n-1) + S[n-1]


    def reverse(self, S, start, stop):
        if start < stop -1:
            S[start], S[stop - 1] = S[stop - 1], S[start]
            self.reverse(S, start+1, stop-1)


    def power(self, x, n):
        '''Compute value of x**n for integer n O(n) time'''
        if n==0:
            return 1
        else:
            return x*self.power(x, n-1)


    def power_optimized(self, x, n):
        '''Compute value of x**n for integer n O(logn) time'''
        if n==0:
            return 1
        else:
            partial = self.power_optimized(x, n//2)
            result = partial*partial
            if n%2 == 1:
                result *= x
            return result


    def binary_sum(self, S, start, stop):
        '''Return the sum of the numbers of implicit slice S[start:stop]'''
        if start >= stop:
            return 0
        elif start == stop-1:
            return S[start]
        else:
            mid = (start+stop) // 2
            return self.binary_sum(S, start, mid) + self.binary_sum(S, mid, stop)

class Fibonacci:

    def bad_fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.bad_fibonacci(n-2) + self.bad_fibonacci(n-1)


    def good_fibonacci(self, n):
        '''Return pair of fibonacci numbers F(n) and F(n-1)'''

        if n<=1:
            return (n, 0)
        else:
            (a, b) = self.good_fibonacci(n-1)
            return (a+b, a)

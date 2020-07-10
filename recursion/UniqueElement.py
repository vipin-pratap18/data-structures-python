class UniqueElement:

    def unique(self, S, start, stop):
        ''' Return True if there ar no duplicate elements in slice S[start:stop]'''
        if stop - start <= 1:
            return True
        elif not self.unique(S, start, stop-1):
            return False
        elif not self.unique(S, start+1, stop):
            return False
        else:
            return S[start] != S[stop-1]

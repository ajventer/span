class QuickSort(object):
    def __init__(self, array):
        self.array = array

    def __partition__(self, begin, end):
        pivot = begin
        for i in range(begin+1, end+1):
            if self.array[i] <= self.array[begin]:
                pivot += 1
                self.array[i], self.array[pivot] = self.array[pivot], self.array[i]
        self.array[pivot], self.array[begin] = self.array[begin], self.array[pivot]
        return pivot        

    def quicksort(self, begin=0, end=None):
        if end is None:
            end = len(self.array) - 1
        def _quicksort(array, begin, end):
            if begin >= end:
                return
            pivot = self.__partition__(begin, end)
            _quicksort(self.array, begin, pivot-1)
            _quicksort(self.array, pivot+1, end)
        return _quicksort(self.array, begin, end)
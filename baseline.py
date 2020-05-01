from collections import Counter

class BaseLine :
    def __init__(self):
        self.majority_class = 0

    def fit(self,X,y):
        assert (len(X)==len(y))
        self.majority_class = self.most_frequent(y)
        return {'majority_class':self.majority_class}

    from collections import Counter

    def most_frequent(self,li):
        occurence_count = Counter(li)
        return occurence_count.most_common(1)[0][0]

    def predict(self,X):
        n = len(X)
        return [self.majority_class]*n

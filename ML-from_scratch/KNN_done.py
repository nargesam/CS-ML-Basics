import numpy as np 
import  sklearn.datasets
import collections

class KNNClassifier():
    def __init__(self, X, Y, k):
        self.k = k
        self.X = np.array(X)
        self.Y = np.array(Y)


    def predict(self, inp):
        
        eculidean_dist_from_inp = []
        for datapoint in self.X: 
            eculidean_dist_from_inp.append(np.linalg.norm(inp - datapoint))
        
        sorted_index  = np.argsort(eculidean_dist_from_inp)

        topk_index = sorted_index[-self.k:]
        topk_label = self.Y[np.array(topk_index)]        
        
        cntr = collections.Counter(topk_label)
        max_key_cntr = max(cntr, key = cntr.get)
        self.label_prob = [cntr[key]/len(np.unique(self.Y)) for  key in np.unique(self.Y)]

        print(f"{max_key_cntr} is the class prediction for this element")
        print(self.label_prob)


if __name__ == "__main__":
    
    iris = sklearn.datasets.load_iris()
    X = iris.data[iris.target!=2]
    Y = iris.target[iris.target!=2]

    model = KNNClassifier(X, Y, k=5)
    model.predict(inp=X[51])


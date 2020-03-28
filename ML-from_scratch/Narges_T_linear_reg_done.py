import numpy as np 
import  sklearn.datasets


class LinearRegression():
    
    def __init__(self, num_iterations=1000, lr=0.001):
        self.num_iterations = num_iterations
        self.lr = 0.001
    
    def _loss(self, h, y):
        return (1/y.size * ((h-y)**2)).mean()
    
    def fit(self, X, Y):
        
        X = np.insert(X, 0, 1, axis=1)
        self.theta = np.zeros(X.shape[1])

        

        for i in range(self.num_iterations):

            h = np.dot(X, self.theta)
            # print(h.shape)
            # exit()
            gradient = np.dot(X.T, h-Y) / Y.size

            self.theta -= self.lr * gradient
            
            if i%100 == 0: 
                h = np.dot(X, self.theta.T)
                self.loss = self._loss(h, Y)
                print(f" step {i} has loss of {self.loss}")
        





if __name__ == "__main__":
    iris = sklearn.datasets.load_iris()

    X = iris.data
    print(X.shape) #150*4
    Y = iris.target
    print(Y.shape) #150

    model = LinearRegression()
    model.fit(X,Y)
    print(model.theta)
    # print(X[0].shape)



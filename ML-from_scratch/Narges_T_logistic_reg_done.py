import numpy as np 
import  sklearn.datasets

class LogisticRegression():

    def __init__(self, lr=0.01, use_intercept=False, num_iter=10000):
        self.lr = lr
        self.use_intercept = use_intercept
        self.num_iter = num_iter
    
    def _add_intercept(self, X):
        intercept = np.ones(X.shape[0])
        return np.concatenate((intercept, X))

    def _sigmoid(self, z):
        return 1/ (1+ np.exp(-z))

    def _loss(self, h, y):
        return (-y*(np.log(h)) - (1-y)*np.log(1-h)).mean()


    def fit(self, X, Y):
        if self.use_intercept:
            self._add_intercept(X)

        # initializing theta
        self.theta = np.zeros(X.shape[1])

        for i in range(self.num_iter):
            z = np.dot(X, self.theta)
            h = self._sigmoid(z)
            gradient = np.dot(X.T, h-y) /y.size
            self.theta -= self.lr*gradient

            if i%1000 == 0:
                z = np.dot(X, self.theta)
                h = self._sigmoid(z)
                loss = self._loss(h, y)
                print(f'loss= {loss}')
                


if __name__ == "__main__":
    iris = sklearn.datasets.load_iris()
    X = iris.data[:32, :2]
    print(X[1:4])
    print(type(X))
    print(X.shape)
    y = (iris.target != 0) * 1
    # print(iris.target[0:2])
    print(y.shape)
    y = y[:32]
    print(y.shape)

    print(y[1:10])
    model = LogisticRegression(use_intercept=True)
    model.fit(X,y)
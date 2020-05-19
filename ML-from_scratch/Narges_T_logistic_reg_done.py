import numpy as np 
import  sklearn.datasets

class LogisticRegression():
    def __init__(self, num_iterations=1000, lr=0.001):
        self.num_iterations = num_iterations
        self.lr = lr
    
    def _loss(self, h,y):
        return (-(y*np.log(h) + (1-y) * np.log(1-h))).mean()
    
    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, x,y): 

        x = np.insert(x, 0, 1, axis=1)

        self.theta_ = np.zeros(x.shape[1])

        for i in range(self.num_iterations):
            z = np.dot( self.theta_, x.T)
            h = self._sigmoid(z)

            gradient = np.dot(x.T, h-y) / y.size

            self.theta_ -= self.lr*gradient

            if i % 100 == 0:
                z = np.dot(x, self.theta_)
                h = self._sigmoid(z)

                loss = self._loss(h,y)
                print(f"loss for iter {i} is {loss}")

if __name__ == "__main__":

    data = sklearn.datasets.load_iris()
    X = data.data
    Y = data.target

    model = LogisticRegression()
    model.fit(X, Y)
    print(model.theta_)

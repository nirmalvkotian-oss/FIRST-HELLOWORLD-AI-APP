from sklearn.linear_model import LinearRegression
import numpy as np
## training y=2x+3
def train():
    x=np.array([[1],[2],[3],[4],[5]])
    y=np.array([[5],[7],[9],[11],[13]])
    model=LinearRegression()
    model.fit(x, y)
    return model
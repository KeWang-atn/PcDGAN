import numpy as np

xs_test = np.load("ShipD/data/xs_test.npy")
xs_train = np.load("ShipD/data/xs_train.npy")
ys_test = np.load("ShipD/data/ys_test.npy")
ys_train = np.load("ShipD/data/ys_train.npy")

print("shape of xs_test: ", xs_test.shape)
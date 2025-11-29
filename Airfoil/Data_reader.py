import numpy as np 
import matplotlib.pyplot as plt 

data_path = './data'
X_train = np.load(data_path+ '/xs_train.npy').astype('float32')
X_test = np.load(data_path+ '/xs_test.npy').astype('float32')
Y_train = np.load(data_path + '/ys_train.npy').astype('float32')
Y_test = np.load(data_path + '/ys_test.npy').astype('float32')

print('Train Shapes:', X_train.shape, Y_train.shape)
# print("the first training sample's x values:", X_train[0])
# print("the first training sample's y values:", Y_train[0])

plt.figure(figsize=(10,5))
plt.plot(X_train[0,:,0], X_train[0,:,1])
plt.title('First Training Sample')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
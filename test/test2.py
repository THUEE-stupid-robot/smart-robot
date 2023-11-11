import numpy as np
X = np.mat([[1],[-1],[1],[-1]])
W1 = np.mat([[1,0,1,0],[0,1,0,1]])
W2 = np.mat([1,-1])
lr = 0.1
t = 2
tmp1 = np.matmul(W2.transpose(),X.transpose())
tmp2 = (np.matmul(np.matmul(W2,W1),X)-t)
tmp3 = tmp1 * tmp2[0,0]
W1p = W1 - lr*tmp3
print("W1'=", W1p)
tmp4 = np.matmul(X.transpose(), W1.transpose())
tmp5 = tmp4 * tmp2[0,0]
W2p = W2 - lr*tmp5
print("W2'=", W2p)
y = np.matmul(np.matmul(W2,W1),X)[0,0]
loss = 1/2*(y - t)**2
yp = np.matmul(np.matmul(W2p,W1p),X)[0,0]
lossp = 1/2*(yp - t)**2
print("loss=",loss)
print("loss'=",lossp)
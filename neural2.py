import numpy as np

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T


syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
syn2 = 2*np.random.random((4,1)) - 1
syn3 = 2*np.random.random((4,1)) - 1
syn4 = 2*np.random.random((4,1)) - 1
syn5 = 2*np.random.random((4,1)) - 1

for j in range(60000):
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    l3 = 1/(1+np.exp(-(np.dot(l2,syn2))))
    l4 = 1/(1+np.exp(-(np.dot(l3,syn3))))
    l5 = 1/(1+np.exp(-(np.dot(l4,syn4))))
    l6 = 1/(1+np.exp(-(np.dot(l5,syn5))))


    l6_delta = (y - l2)*(l2*(1-l2))
    l5_delta = l6_delta.dot(syn1.T) * (l5 * (1-15))
    l4_delta = l5_delta.dot(syn1.T) * (l4 * (1-l4))
    l3_delta = l4_delta.dot(syn1.T) * (l3 * (1-l3))
    l2_delta = l3_delta.dot(syn1.T) * (l2 * (1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))



    syn5 += l5.T.dot(l5_delta)
    syn4 += l4.T.dot(l4_delta)
    syn3 += l3.T.dot(l4_delta)
    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)

print(syn0)
print(syn1)
print(syn2)
print(syn3)
print(syn4)
print(syn5)
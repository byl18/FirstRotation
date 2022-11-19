import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
myQ = pd.read_csv(r'C:\research\LiYinqing\study\DeepLearningFlappyBird-master\logs_bird2\qvalue.txt')
# for i in range(1001):
#     myQ.iloc[10*i:10*(i+1),:] = np.mean(myQ.iloc[10*i:10*(i+1),:])
#print(np.max(myQ,axis = 1))
plt.plot(np.max(myQ,axis = 1))
#plt.plot(myQ.iloc[300:,:])
plt.title('Training curve of flappy bird')
plt.xlabel('per 100 steps')
plt.ylabel('Q value')
plt.show()
plt.close()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
myQ = pd.read_csv(r'C:\research\LiYinqing\study\SpaceInvaders\logs_spaceinvader\qvalue.txt')
# for i in range(1001):
#     myQ.iloc[10*i:10*(i+1),:] = np.mean(myQ.iloc[10*i:10*(i+1),:])
print(np.max(myQ,axis = 1))
#plt.plot(np.max(myQ.iloc[600:,:]))
plt.plot(myQ)

plt.title('Training curve of Spaceinvader')
plt.xlabel('per 100 steps')
plt.ylabel('Q value')
plt.show()
plt.close()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
myQ = pd.read_csv(r'C:\research\LiYinqing\study\Breakout\logs_breakout\qvalue.txt')
for i in range(130):
    myQ.iloc[10*i:10*(i+1),:] = np.mean(myQ.iloc[10*i:10*(i+1),:])


plt.plot(myQ)
plt.title('Training curve of Breakout')
plt.xlabel('per 100 steps')
plt.ylabel('Q value')
plt.show()
plt.close()
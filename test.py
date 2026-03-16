import numpy as np
import matplotlib.pyplot as plt
n_list =range(4,21)
coud_v=[]
for n in n_list:
    t=np.array([i/n for i in range(n+1)])
    V=np.vander(t,increasing=True)
    coud =np.linalg.cond(V,p=1)
    coud_v.append(coud)
plt.figure(figsise=(8,5))
plt.title('范德蒙矩阵的条件数随n的变化')
plt.plot(n_list,coud_v,marker='o')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('K(An) (1范数，对数刻度)')
plt.grid(True)
plt.show()

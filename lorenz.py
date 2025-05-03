# lorenz.py
import numpy as np
   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D
   import os

   # 参数设置
   sigma, rho, beta = 10, 28, 8/3
   dt = 0.01
   steps = 5000

   # 洛伦兹方程
   def lorenz(x):
       return np.array([
           sigma*(x[1] - x[0]),
           x[0]*(rho - x[2]) - x[1],
           x[0]*x[1] - beta*x[2]
       ])

   # 计算两条轨迹
   traj1, traj2 = [], []
   x1 = np.array([1.0, 1.0, 1.0])
   x2 = x1 + [1e-5, 0, 0]  # 初始差异仅0.001%

   for _ in range(steps):
       x1 += dt * lorenz(x1)
       x2 += dt * lorenz(x2)
       traj1.append(x1.copy())
       traj2.append(x2.copy())

   traj1 = np.array(traj1)
   traj2 = np.array(traj2)

   # 可视化设置
   plt.style.use('dark_background')
   fig = plt.figure(figsize=(16,9))
   ax = fig.add_subplot(111, projection='3d')
   ax.plot(traj1[:,0], traj1[:,1], traj1[:,2], lw=0.5, color='#00ff88', alpha=0.7)
   ax.plot(traj2[:,0], traj2[:,1], traj2[:,2], lw=0.5, color='#ff0088', alpha=0.7)
   ax.set_axis_off()

   # 自动保存图片
   os.makedirs('output', exist_ok=True)
   plt.savefig('output/butterfly.png', dpi=300, bbox_inches='tight', transparent=True)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D散布図でプロットするデータを生成する為にnumpyを使用
#X = np.array([-0.75,-0.50,-0.25,0,0.25,0.5,0.75,-0.75,-0.50,-0.25,0,0.25,0.5,0.75,-0.75,-0.50,-0.25,0,0.25,0.5,0.75,]) # 自然数の配列
#Z = np.array([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,])
#Y = np.array([0.75,0.75,0.75,0.75,0.75,0.75,0.75,1.25,1.25,1.25,1.25,1.25,1.25,1.25,1.75,1.75,1.75,1.75,1.75,1.75,1.75])

# グラフの枠を作成
fig = plt.figure()
ax = Axes3D(fig)

# X,Y,Z軸にラベルを設定
ax.set_xlabel("X")
ax.set_ylabel("Z")
ax.set_zlabel("Y")
colorlist = ["r", "g", "b", "y", "c", "w", "gray"]

ax.plot(0,0,1.0,marker="o",linestyle='None',markersize=18,color="#000")
ax.plot([0,0],[0,0],[0,1.0],color="#000")

'''
1,(推定マイクx座標,推定マイク高さ,z)-47cm,153cm,76cm
2,(推定マイクx座標,推定マイク高さ,z)-1cm,128cm,120cm
3,(推定マイクx座標,推定マイク高さ,z)76cm,135cm,86cm
4,(推定マイクx座標,推定マイク高さ,z)-18cm,109cm,119cm
5,(推定マイクx座標,推定マイク高さ,z)-89cm,122cm,77cm
6,(推定マイクx座標,推定マイク高さ,z)26cm,119cm,94cm
'''


#(推定マイクx座標,推定マイク高さ,z)-47cm,153cm,76cm
#-25 171 103 
ax.plot(-0.25,1.03,1.71,"o",color=colorlist[0],markeredgecolor="black", label="true",markersize=12)
ax.plot(-0.47,0.76,1.53,"o",color=colorlist[0],label="estimate",markersize=12)

#(推定マイクx座標,推定マイク高さ,z)-1cm,128cm,120cm
#44 140 123 
ax.plot(0.44,1.23,1.40,"o",color=colorlist[1],markeredgecolor="black",markersize=12)
ax.plot(-0.01,1.20,1.28,"o",color=colorlist[1],markersize=12)

#(推定マイクx座標,推定マイク高さ,z)76cm,135cm,86cm
#-53 138 104 
ax.plot(-0.53,1.04,1.38,"o",color=colorlist[2],markeredgecolor="black",markersize=12)
ax.plot(0.76,0.86,1.35,"o",color=colorlist[2],markersize=12)

#(推定マイクx座標,推定マイク高さ,z)-18cm,109cm,119cm
#-46 108 095 
ax.plot(-0.46,0.95,1.08,"o",color=colorlist[3],markeredgecolor="black",markersize=12)
ax.plot(-0.18,1.19,1.09,"o",color=colorlist[3],markersize=12)

#(推定マイクx座標,推定マイク高さ,z)-89cm,122cm,77cm
#8 127 153 
ax.plot(0.08,1.53,1.27,"o",color=colorlist[4],markeredgecolor="black",markersize=12)
ax.plot(-0.89,0.77,1.22,"o",color=colorlist[4],markersize=12)

#(推定マイクx座標,推定マイク高さ,z)26cm,119cm,94cm
#51 128 93 
ax.plot(0.51,0.93,1.28,"o",color=colorlist[5],markeredgecolor="black",markersize=12)
ax.plot(0.26,0.94,1.19,"o",color=colorlist[5],markersize=12)

#(推定マイクx座標,推定マイク高さ,z)78cm,147cm,70cm
#74 128 59
#ax.plot(0.74,0.59,1.28,"o",color=colorlist[6],markeredgecolor="black",markersize=12)
#ax.plot(0.72,0.65,1.53,"o",color=colorlist[6],markersize=12)

plt.legend()
# 最後に.show()を書いてグラフ表示
plt.show()
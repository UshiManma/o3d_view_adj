import open3d as o3d
import numpy as np

point = [
    #原点
    [0, 0, 0],
    #X
    [1, 0, 0],
    #Y
    [0, 1, 0],
    #Z
    [0, 0, 1],
    #Z'
    [0, 0, -2],
]

line = [
    #(0,0,0)→(1, 0, 0)
    [0, 1],
    #(0,0,0)→(0, 1, 0)
    [0, 2],
    #(0,0,0)→(0, 0, 1)
    [0, 3],
    #(0,0,0)→(0, 0, -1)
    [0, 4]
]
# red, green, blue, magenta
color = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1]]
# LineSet : 3Dで線のセットを定義

#### 一度に線のセットを定義する場合 ####
# colorsパラメータだけは頂点と線の定義が済んでいないと設定できない
"""
line_set = o3d.geometry.LineSet(
    # Vector3dVector : float64numpy配列をopen3d形式に変換
    points = o3d.utility.Vector3dVector(point),
    # Vector2iVector : int32numpy配列をopen3d形式に変換
    lines = o3d.utility.Vector2iVector(line),
)
line_set.colors = o3d.utility.Vector3dVector(color)
"""
#####################################################

#### LineSetオブジェクトの初期化後にパラメータを１つずつ設定する場合 ####
line_set = o3d.geometry.LineSet()
line_set.points = o3d.utility.Vector3dVector(point)
line_set.lines = o3d.utility.Vector2iVector(line)
print("line_set.lines : {}".format(line_set.lines))
line_set.colors = o3d.utility.Vector3dVector(color)
#####################################################

# 回転させたい場合
r = np.identity(4)
print("np.identity(3) : {}".format(r))
line_set.transform(r)
center = line_set.get_center()
# ジオメトリ座標の中心を取得
print("center : {}".format(center))
o3d.visualization.draw_geometries([line_set])

r2 = np.array([-0.2, -0.2, 0.2])
# ジオメトリ座標に平行移動を適用する
line_set.translate(r2, relative=True)
center = line_set.get_center()
print("center : {}".format(center))
#o3d.visualization.draw_geometries([line_set])

p_color = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
pcd = o3d.geometry.PointCloud()
points = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, -1]])
pcd.points = o3d.utility.Vector3dVector(points)
# lineの設定と同じ要領でcolorのプロパティ設定が可能
pcd.colors = o3d.utility.Vector3dVector(p_color)
o3d.visualization.draw_geometries([pcd])

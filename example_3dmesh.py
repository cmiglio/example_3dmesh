import plotly.graph_objects as go
import numpy as np
from scipy.io import loadmat

brain = loadmat('brain.mat', squeeze_me=True)
positions = loadmat('positions.mat', squeeze_me=True)

print(positions['pos'])
fig = go.Figure(data=[
    go.Mesh3d(
        # 8 vertices of a cube
        x=[a[0] for a in brain['Vertices']],
        y=[a[1] for a in brain['Vertices']],
        z=[a[2] for a in brain['Vertices']],
        opacity=0.30,
        # i, j and k give the vertices of triangles
        i=[a[0]-1 for a in brain['Faces']],
        j=[a[1]-1 for a in brain['Faces']],
        k=[a[2]-1 for a in brain['Faces']],
        name='y',
        showscale=True
    ),
    go.Scatter3d(x=[a[0] for a in positions['pos']],
                 y=[a[1] for a in positions['pos']],
                 z=[a[2] for a in positions['pos']],
                 mode='markers',
                 marker=dict(size=4))
])

fig.show()

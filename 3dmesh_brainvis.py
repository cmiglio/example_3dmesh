import numpy as np
from visbrain.gui import Brain
from visbrain.objects import BrainObj, SourceObj
from scipy.io import loadmat

"""Download and the load the Custom.npz archive. This file contains vertices
and faces of a brain template that is not integrated by default in Visbrain.
"""
#mri = loadmat('MRI.mat', squeeze_me = True)
mat = loadmat('brain.mat', squeeze_me=True)

#transf_matrix = mri['InitTransf'][1]

"""Get vertices and faces from the archive.

In this examples, normals are also present in the archive. If you don't have
the normals, the BrainObj will compute it automatically.
"""
vert, faces = mat['Vertices'], mat['Faces'][:, [0, 2, 1]]

#vert = np.dot(np.hstack([vert, np.ones((vert.shape[0], 1))]), np.linalg.inv(transf_matrix))[:, :3]

print(faces.shape)

"""Define the brain object
"""
b_obj = BrainObj('Custom', vertices=vert, faces=faces)
positions = loadmat('positions.mat', squeeze_me=True)
pos = positions['pos']


"""Then you have two strategies :
* If you are going to use this template a lot and don't want to redefine it
  every times, use `b_obj.save()`. Once the object saved, it can be reloaded
  using its name only `BrainObj('Custom')`
* If you only need it once, the template is temporaly saved and remove once the
  GUI is closed.
"""
# b_obj.save()
# b_obj = BrainObj('Custom')

"""Define the GUI and pass the brain template
"""
s_obj = SourceObj('SourceExample', pos)
#s_obj.color_sources(data=kwargs['data'], cmap='viridis')

vb = Brain(brain_obj=b_obj, source_obj=s_obj)
vb.show()

# If you want to remove the template :
# b_obj.remove()
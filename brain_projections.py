from visbrain.gui import Brain
from visbrain.objects import BrainObj, SourceObj, SceneObj
from scipy.io import loadmat
import pandas as pd

chanpos = pd.read_csv('rates_by_chan.csv')
patient = 'PAT_1'
chanpos_p = chanpos[chanpos['Patient']==patient]
mat = loadmat('brain.mat', squeeze_me=True)

vert, faces = mat['Vertices'], mat['Faces'][:, [1, 0, 2]]

pos = chanpos_p[['x', 'y', 'z']].values
soz = chanpos_p[chanpos_p['Soz_dist'] == 0]
pos_soz = soz[['x', 'y', 'z']].values


sc = SceneObj(bgcolor='black', size=(1400, 1000))

b_obj = BrainObj('Custom', vertices=vert, faces=faces, translucent=True)
kwargs={}
kwargs['text'] = chanpos_p['Channel'].values            # Name of the subject
kwargs['text_color'] = "#f39c12"       # Set to yellow the text color
kwargs['text_size'] = 1.5              # Size of the text
kwargs['text_translate'] = (1.5, 1.5, 0)
kwargs['text_bold'] = True


s_obj = SourceObj('SourceExample', pos, **kwargs)
s_obj.color_sources(data=chanpos_p['rate'].values, cmap='viridis')

s_obj2 = SourceObj('SourceExample2', pos_soz)


vb = Brain(source_obj=[s_obj2, s_obj], brain_obj=b_obj)
vb.show()
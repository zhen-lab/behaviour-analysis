import glob
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

hdf5_file = './data/jpeg-30s/Results/test_featuresN.hdf5'


f = pd.read_hdf(hdf5_file, 'timeseries_data', 'r', columns=[
    'curvature_head',
    'curvature_neck',
    'curvature_midbody',
    'curvature_hips',
    'curvature_tail',
])

f.to_csv('./data/tierpsy_features.csv')

curvature_keys = [    
    'curvature_head',
    'curvature_neck',
    'curvature_midbody',
    'curvature_hips',
    'curvature_tail'
]

data = { k: f[k][:499] for k in curvature_keys }
df = pd.DataFrame(data=data)
ax = sns.heatmap(df.transpose(), center=0.0, cmap=sns.diverging_palette(220, 20, n=3, as_cmap=True))
plt.show()

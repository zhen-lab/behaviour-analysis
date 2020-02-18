import h5py
import glob
import pandas as pd

# hdf5_data_directory = './data/jpeg-30s/Results/'

# hdf5_files = glob.glob(hdf5_data_directory + '*.hdf5')


# for hdf5_file in hdf5_files:
#     with h5py.File(hdf5_file, 'r') as f_content:
#         print(f_content.keys())
    


hdf5_file = './data/jpeg-30s/Results/test_featuresN.hdf5'

# with h5py.File(hdf5_file, 'r') as f:
#     print(f.get('timeseries_data'))
#     print(f.get('timeseries_data').items())

# f = pd.read_hdf({
#     'path_or_buf': hdf5_file,
#     'key': 'timeseries_data',
#     # 'where': ['coor']
# })

f = pd.read_hdf(hdf5_file, 'timeseries_data', 'r', columns=[
    'curvature_head',
    'curvature_neck',
    'curvature_midbody',
    'curvature_hips',
    'curvature_tail',
])

f.to_csv('./data/tierpsy_features.csv')

# print(f['curvature_head'])
print( f['curvature_head'].__class__.__name__)
import glob
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import h5py

from tierpsy.features.tierpsy_features import get_curvature_features


def curvature_plot_from_tierpsy_features_func():
    with h5py.File('./data/jpeg-30s/Results/test_skeletons.hdf5') as f:
        skeletons = np.array(f['skeleton'][:504])
        segment_curvatures = get_curvature_features(skeletons, 'grad')
        print(segment_curvatures)
        data = { k: segment_curvatures[k] for k in segment_curvatures.keys() }
        df = pd.DataFrame(data=data)
        ax = sns.heatmap(df.transpose(), cmap=sns.diverging_palette(220, 20, n=3, as_cmap=True))
        plt.show()


def curvature_plot_from_tierpsy_hdf5(hdf5_path):
    f = pd.read_hdf(hdf5_path, 'timeseries_data', 'r', columns=[
        'curvature_head',
        'curvature_neck',
        'curvature_midbody',
        'curvature_hips',
        'curvature_tail',
    ])


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



def curvature_plot_from_taizo_data(csv_path):
    f = pd.read_csv(csv_path)
    angle_columns = [ 'angle_' + str(i) for i in range(1, 34) ]

    data = { k: f[k] for k in angle_columns }
    df = pd.DataFrame(data=data)
    ax = sns.heatmap(df.transpose(), center=0.0, cmap=sns.diverging_palette(220, 20, n=3, as_cmap=True))
    plt.show()


# curvature_plot_from_tierpsy_features_func()
# curvature_plot_from_tierpsy_hdf5('./data/taizo-vs-tierpsy/images/Results/test_featuresN.hdf5')
curvature_plot_from_taizo_data('./data/taizo-vs-tierpsy/temp34HR1.csv')
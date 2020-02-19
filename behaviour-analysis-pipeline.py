import cv2
import glob
import os
import shutil
from tierpsy.processing.processMultipleFilesFun import processMultipleFilesFun
from tierpsy.summary.collect import calculate_summaries

path = './data/jpeg-30s/'
img_extension = "*.jpg"
fps = 10
masked_video_dir = path + 'MaskedVideos'
results_dir = path + 'Results'
parameters_file = path + 'parameters.json'


try:
    shutil.rmtree(masked_video_dir)
    shutil.rmtree(results_dir)
except OSError as e:
    print("error couldnt delete files")


def file_name_str_to_int(f_path):
    f_name = os.path.basename(f_path)
    str_key, _ = os.path.splitext(f_name)
    return int(str_key)


img_files = glob.glob(path + img_extension)
img_files.sort(key=file_name_str_to_int)

images = [cv2.imread(file) for file in img_files]
width, height, layers = images[0].shape

video = cv2.VideoWriter(path + "test.avi", cv2.VideoWriter_fourcc(*'XVID'), fps, (height, width))

for img in images:
    video.write(img)

video.release()

# code to call tierpsy batch processing
processMultipleFilesFun(path, masked_video_dir, results_dir,
    '', parameters_file, '', '*.avi', '', 3, 10.0, False,
    'COMPRESS', 'FEAT_TIERPSY', False,
    ['COMPRESS', 'TRAJ_CREATE', 'TRAJ_JOIN', 'SKE_INIT', 'BLOB_FEATS', 'SKE_CREATE', 'SKE_FILT', 'SKE_ORIENT', 'INT_PROFILE', 'INT_SKE_ORIENT', 'FEAT_INIT', 'FEAT_TIERPSY'],
    False, False, True
)

# code to generate results csv
fold_args = dict(n_folds = 5, frac_worms_to_keep = 0.8, time_sample_seconds = 600.0)
calculate_summaries(
    path,
    'tierpsy',
    'plate',
    False,
    True,
    **fold_args
)
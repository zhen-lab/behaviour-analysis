import cv2
import glob
from tierpsy.processing.processMultipleFilesFun import processMultipleFilesFun
from tierpsy.summary.collect import calculate_summaries

def sorted_tiff(f_path):
    tiff_name = f_path.split('/')[-1]
    key = tiff_name.split('.')[0]
    return int(key)

tiff_files = glob.glob("./temp10/*.tiff")
tiff_files.sort(key=sorted_tiff)

images = [cv2.imread(file) for file in tiff_files]
width, height, layers = images[0].shape

video = cv2.VideoWriter("test.avi", cv2.VideoWriter_fourcc(*'XVID'), 26, (width, height))

for img in images:
    video.write(img)

video.release()

# code to call tierpsy batch processing
processMultipleFilesFun(
    '/Users/dylan/src/behaviour-analysis-pipeline/data-test',
    '/Users/dylan/src/behaviour-analysis-pipeline/data-test/MaskedVideos',
    '/Users/dylan/src/behaviour-analysis-pipeline/data-test/Results',
    '',
    '/Users/dylan/src/behaviour-analysis-pipeline/data-test/parameters.json',
    '',
    '*.avi',
    '',
    3,
    10.0,
    False,
    'COMPRESS',
    'FEAT_TIERPSY',
    False,
    ['COMPRESS', 'TRAJ_CREATE', 'TRAJ_JOIN', 'SKE_INIT', 'BLOB_FEATS', 'SKE_CREATE', 'SKE_FILT', 'SKE_ORIENT', 'INT_PROFILE', 'INT_SKE_ORIENT', 'FEAT_INIT', 'FEAT_TIERPSY'],
    False,
    False,
    True
)

# code to generate results csv
fold_args = dict(n_folds = 5, frac_worms_to_keep = 0.8, time_sample_seconds = 600.0)
calculate_summaries(
    '/Users/dylan/src/behaviour-analysis-pipeline/data-test',
    'tierpsy',
    'plate',
    False,
    True,
    **fold_args
)
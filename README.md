# behaviour-analysis
Analyze data taken from [TrackStim](https://github.com/zhen-lab/TrackStim)

## Installation
1. Install anaconda
2. Create the conda environment from for windows/mac
```
conda create --name behaviour-analysis --file conda_req_windows.txt
```
```
conda create --name behaviour-analysis --file conda_req_mac.txt
```
3. Fix tierpsy issues
- Find all instances of ```cv2.findContours()```
- Delete the first return value in the multi-return assignment so that ```cv2.findContours()``` only returns 2 values


## Usage
TODO

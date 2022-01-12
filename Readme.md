# ISVQA

[ToDo] introduction.... 

## Dataset intro
[ToDo] blabla
```sh
|-- extracted_features
|   |-- train
|   |-- test
|-- mini
|   |-- maps
|   |   |-- 36092f0b03a857c6a3403e25b4b7aab3.png
|   |-- samples
|   |   |-- CAM_BACK
|   |   `-- ....
|   `-- v1.0-mini
|       |-- attribute.json
|       `-- ...
|-- part01
|   `-- samples
|       |-- CAM_BACK
|       `-- ...
|-- part02
|   `-- samples
|       |-- CAM_BACK
```

## File structure
```sh
-- input
  -- image
    -- feature
  -- pretrain-weights
  -- json
-- output
-- lxrt
-- src
|   -- lxrt
|   -- maskrcnn benchmark
|   -- vqa_data_.py
|   -- utils
-- ReadMe.md
-- feature_extaction.py
-- json_generation.py
-- ISVQA_main.py
-- requirement.yaml
```


## Preparation
### Prerequisite
- MMF install [Official instruction](https://mmf.sh/docs/), download the mmf repo under '/src'.
```
cd src
git clone https://github.com/facebookresearch/mmf.git
cd mmf
pip install --editable .  # after this one, it will become pytorch 1.9 automatically
```
- Mask-RCNN backbone [instruction](https://mmf.sh/docs/tutorials/image_feature_extraction/), download the repo under '/src'.
```
pip install ninja yacs cython matplotlib
pip install opencv-python
cd src
git clone https://gitlab.com/vedanuj/vqa-maskrcnn-benchmark.git
cd vqa-maskrcnn-benchmark
python setup.py build develop
```
- You might have such a following bug, change PY3 to PY37:
File "/root/Documents/ISVQA/src/vqa-maskrcnn-benchmark/maskrcnn_benchmark/utils/imports.py", line 4, in <module>
    if torch._six.PY3:
AttributeError: module 'torch._six' has no attribute 'PY3'
```
- LXMERT repository [instruction](https://github.com/airsplay/lxmert/blob/master/requirements.txt) 
- download pretrained lxmert model via
```sh
wget https://nlp.cs.unc.edu/data/model_LXRT.pth -P snap/pretrained
```

- maskrcnn_benchmark
- mmf (orinially is ..., mmf is too large ...)
- cv
- python version, pytorch version

pip install yaml

## Feature extraction
[ToDo: How do we create necessary annotations?]
run 
```sh
python feature_extaction.py
```

## ID and score generation


## Training
```sh
python ISVQA_main.py
```

## Test
```sh
python vqa.py
```

## Training and result


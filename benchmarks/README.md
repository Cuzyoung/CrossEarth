# Benchmark Collection
Here is the benchmark collection in CrossEarth paper. In this page, we will release the download links, and pre-process scripts of benchmarks. 

Due to the time limit, this part is not available now but will be coming soon.
<img src="../images/benchmark_collection.png" width="100%">

# Table of Content
- [Potsdam and Vaihingen](#potsdam-and-vaihingen)
- [LoveDA](#loveda)
- [WHU-Building](#whu-building)
- [DeepGlobe and Massachusetts](#deepglobe-and-massachusetts)
- [Potsdam and RescuNet](#potsdam-and-rescuenet)
- [CAISD](#caisd) 


## Potsdam and Vaihingen
First, Link to MMSegmentation Page [here](https://mmsegmentation.readthedocs.io/zh-cn/main/user_guides/2_dataset_prepare.html) to find the Potsdam and Vaihingen section.

For Potsdam dataset, download '3_Ortho_RGB.zip', '3_Ortho_IRRG.zip', and '5_Labels_all_noBoundary.zip'.

For Vaihingen dataset, download 'ISPRS_semantic_labeling_Vaihingen.zip' and 'ISPRS_semantic_labeling_Vaihingen_ground_truth_eroded_COMPLETE.zip'.

Second, Process the Potsdam dataset (respectively process RGB and IRRG): 
```bash
python tools/dataset_converters/potsdam.py /path/to/potsdam
```
Third, Process the Vaihingen dataset: 
```bash
python tools/dataset_converters/vaihingen.py /path/to/vaihingen
```
Notably, the label id of Potsdam and Vaihingen is from 1-6. Make sure label id is consistent and you can use this script to check it.
```bash
python tools/check_label_id.py /path/to/potsdam
python tools/check_label_id.py /path/to/vaihingen
```
The structure of the processed dataset should be like this:
```
CrossEarth
    - Potsdam
        -IRRG
            - img_dir
                - train
                - val
            - ann_dir
                - train
                - val
        -RGB
            - img_dir
                - train
                - val
            - ann_dir
                - train
                - val
    - Vaihingen
        - img_dir
            - train
            - val
        - ann_dir
            - train
            - val
```
## LoveDA
First, download 'LoveDA-CrossEarth.zip' dataset from [Huggingface](https://huggingface.co/datasets/Cusyoung/CrossEarth-Benchmark/tree/main) and [BaiduNetdisk]() and put it in the 'datasets/LoveDA' folder.

or Download with wget in MMSegmentation Page:
```bash
cd datasets
mkdir LoveDA
cd LoveDA
wget https://zenodo.org/record/5706578/files/Train.zip
wget https://zenodo.org/record/5706578/files/Val.zip
```

Second, process the LoveDA dataset: 
```bash
python tools/dataset_converters/loveda.py /path/to/loveDA
```

The structure of the processed LoveDA dataset should be like this:
```
datasets
    - LoveDA
        - Train
            - Rural
                - images_png
                - masks_png
            - Urban
                - images_png
                - masks_png
        - Val
            - Rural
                - images_png
                - masks_png
            - Urban
                - images_png
                - masks_png
```
## WHU-Building
First, download WHU-Building dataset from [Huggingface](https://huggingface.co/datasets/Cusyoung/CrossEarth-Benchmark/tree/main) and BaiduNetdisk Badges and put it in the 'datasets/' folder.

Second, unzip the WHU-Building dataset: 
```bash
python tools/dataset_converters/whu_building.py /path/to/whu_building
```

## DeepGlobe and Massachusetts
First, download 'Massachusetts.zip' dataset from [Huggingface](https://huggingface.co/datasets/Cusyoung/CrossEarth-Benchmark/tree/main) and BaiduNetdisk Badges and put it in the 'datasets/' folder.

Second, unzip the Massachusetts dataset: 
```bash
cd datasets
mkdir Massachusetts
cd Massachusetts
unzip Massachusetts.zip 
```
Third, download 'DeepGlobe.zip' dataset from [Huggingface](https://huggingface.co/datasets/Cusyoung/CrossEarth-Benchmark/tree/main) and BaiduNetdisk Badges and put it in the 'datasets' folder.

Fourth, unzip the DeepGlobe dataset: 
```bash
cd ..
mkdir DeepGlobe
cd DeepGlobe
unzip DeepGlobe.zip 
```

The structure of the Massachusetts and DeepGlobe dataset should be like this:
```
datasets
    - Massachusetts
        -tiff
            - train
            - train_labels
            - val
            - val_labels
            - test
            - test_labels
    - DeepGlobe
        -train
        -valid
        -test
```

## Potsdam and RescuNet
<!-- For the Potsdam and RescuNet, we need to conduct label mapping process to unify Potsdam and RescuNet labels. -->
 


## CAISD

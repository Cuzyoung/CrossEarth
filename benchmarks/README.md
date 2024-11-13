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
1. Link to MMSegmentation Page [here](https://mmsegmentation.readthedocs.io/zh-cn/main/user_guides/2_dataset_prepare.html) to find the Potsdam and Vaihingen section.

For Potsdam dataset, download '3_Ortho_RGB.zip', '3_Ortho_IRRG.zip', and '5_Labels_all_noBoundary.zip'.

For Vaihingen dataset, download 'ISPRS_semantic_labeling_Vaihingen.zip' and 'ISPRS_semantic_labeling_Vaihingen_ground_truth_eroded_COMPLETE.zip'.

2. Process the Potsdam dataset (respectively process RGB and IRRG): 
```bash
python tools/dataset_converters/potsdam.py /path/to/potsdam
```
3. Process the Vaihingen dataset: 
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

## WHU-Building

## DeepGlobe and Massachusetts

## Potsdam and RescuNet
<!-- For the Potsdam and RescuNet, we need to conduct label mapping process to unify Potsdam and RescuNet labels. -->
 


## CAISD

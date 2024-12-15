 
<div align="center">

<h1><img src="images/CrossEarth.png" width="5%"> CrossEarth: Geospatial Vision Foundation Model for Domain Generalizable Remote Sensing Semantic Segmentation</h1>


[Ziyang Gong](https://scholar.google.com/citations?user=cWip8QgAAAAJ&hl=zh-CN&oi=ao)<sup>1 ∗</sup>, [Zhixiang Wei](https://scholar.google.com/citations?user=i5W4i9YAAAAJ&hl=zh-CN&oi=sra)<sup>2 ∗</sup>, [Di Wang](https://scholar.google.com/citations?user=3fThjewAAAAJ&hl=zh-CN&oi=sra)<sup>3 ∗</sup>, Xianzheng Ma<sup>3</sup>, [Hongruixuan Chen](https://scholar.google.com/citations?user=XOk4Cf0AAAAJ&hl=zh-CN&oi=ao)<sup>4</sup>, [Yuru Jia](https://scholar.google.com/citations?user=62c9GI0AAAAJ&hl=zh-CN&oi=ao)<sup>56</sup>, [Yupeng Deng](https://scholar.google.com/citations?user=H5X8NDQAAAAJ&hl=zh-CN&oi=ao)<sup>1</sup>, Zhenming Ji<sup>1 †</sup>, Xiangwei Zhu<sup>1 †</sup>, Naoto Yokoya<sup>4</sup>, Jing Zhang<sup>3</sup>, Bo Du<sup>3</sup>, Liangpei Zhang<sup>3</sup>

<sup>1</sup> Sun Yat-sen University, <sup>2</sup> University of Science and Technology of China, <sup>3</sup> Wuhan University, 

<sup>4</sup> The University of Tokyo, <sup>5</sup> KU Leuven, <sup>6</sup> KTH Royal Institute of Technology

<sup>∗</sup> Equal contribution, <sup>†</sup> Corresponding author

<img src="https://visitor-badge.laobi.icu/badge?page_id=Cuzyoung.CrossEarth&left_color=%2363C7E6&right_color=%23CEE75F">  <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg">
<img src="https://img.shields.io/github/stars/Cuzyoung/CrossEarth.svg?logo=github&label=Stars&color=white">

<a href="https://cuzyoung.github.io/CrossEarth-Homepage/"><img src="https://img.shields.io/badge/🌍_Project_Page-E4F578?style=for-the-badge" style="width: 113px;"></a>
<a href="https://github.com/Cuzyoung/CrossEarth/"><img src="https://img.shields.io/badge/WeChat-07C160?style=for-the-badge&logo=wechat&logoColor=white" style="width: 80px;"></a>
<a href="https://www.linkedin.com/in/ziyang-gong-382a182b1/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" style="width: 90px;"></a>
<a href="https://pan.baidu.com/s/1nOQlZUTeySn6-jiqjheWhQ?pwd=eq40"><img src="https://img.shields.io/badge/Baidu Netdisk-63C7E6.svg?style=for-the-badge&logo=Baidu&logoColor=white" style="width: 123px;"></a>
<a href="https://huggingface.co/Cusyoung/CrossEarth/tree/main"> <img src="https://img.shields.io/badge/🤗_Hugging_Face-FFD21E?style=for-the-badge" style="width: 115px;"></a>

<img src="images/teaser_new.png" width="100%">

</div>
<br>
<br>

# 🔥🔥🔥 News

- [2024/11/14] We are releasing the benchmark collection. Click [here](https://github.com/Cuzyoung/CrossEarth/tree/main/benchmarks) to get illustrations of benchmarks!

- [2024/11/06] The most checkpoints have been uploaded and you can access them in the huggingface badges.

- The environment and inference steps please refer to the following installation. The inference codes and weights will be coming soon.

- The benchmark collection in the paper is releasing and you can access it at [here](https://github.com/Cuzyoung/CrossEarth/tree/main/benchmarks). 

- 🎉🎉🎉 CrossEarth is the first VFM for Remote Sensing Domain Generalization (RSDG) semantic segmentation. We just release the arxiv paper of CrossEarth. You can access CrossEarth at [here](https://arxiv.org/abs/2410.22629). 


# 📑 Table of Content
- [Visualization](#visualization)
- [Environment Requirements](#environment-requirements)
- [Inference steps](#inference-steps)
- [Training steps](#training-steps)
- [Model Weights with Configs](#model-weights-with-configs)
<!-- - [Citation](#citation)
 -->


## Visualization  
__In Radar figure:__
- CrossEarth achieves SOTA performances on 23 evaluation benchmarks across various segmentation scenes, demonstrating strong generalizability.

__In UMAP figures:__
- CrossEarth extracts features that cluster closely for the same class across different domains, forming well-defined groups in feature space, demonstrating its ability to learn robust, domain-invariant features.

- Moreover, CrossEarth features exhibit high inter-class separability, forming unique clusters for each class and underscoring its strong representational ability to distingguish different categories.

<img src="images/visual.png" width="100%">



## Environment Requirements:
```bash
conda create -n CrossEarth -y
conda activate CrossEarth
conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia -y
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.0"
pip install "mmsegmentation>=1.0.0"
pip install "mmdet>=3.0.0"
pip install xformers=='0.0.20' 
pip install -r requirements.txt
pip install future tensorboard
```
## Inference steps:

First, download the model weights from the huggingface or Baidu Netdisk in the above badges.
Notably, the checkpoints of dinov2_converted.pth and dinov2_converted_1024x1024.pth are needed for inference. 
Please download them and put them in the CrossEarth/checkpoints folder.

Second, change the file path in experiment config files (__configs/base/datasets/xxx.py__ and __configs/CrossEarth_dinov2/xxx.py__), and run the following command to inference. (Take 512x512 inference as an example)
```bash
python tools/test.py configs/CrossEarth_dinov2/CrossEarth_dinov2_mask2former_512x512_bs1x4.py ./checkpoints/xxx.pth
```
Notably, save path of pseudo labels is in the experiment config file. When testing CrossEarth on different benchmarks, you also need to change the class number in [CrossEarth_dinov2_mask2former.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/models/CrossEarth_dinov2_mask2former.py) file.

## Training steps:

Coming soon.

## Model Weights with Configs

| Dataset | Benchmark | Model | Config | Log |
|----------|----------|-------| -------| ----|
|ISPRS Potsdam and Vaihingen|P(i)2V| [Potsdam(i)-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/Potsdam(i)-source.pth) | [dg_potIRRG2RGB_512x512.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_potIRRG2RGB_512x512.py) |-|
|-  |P(i)2P(r)| [Potsdam(i)-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/Potsdam(i)-source.pth) | [dg_potIRRG2RGB_512x512.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_potIRRG2RGB_512x512.py) |-|
|-  |P(r)2P(i)| [Potsdam(r)-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/Potsdam(r)-source.pth) | [dg_potRGB2IRRG_512x512.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_potRGB2IRRG_512x512.py) |-|
|-  |P(r)2V| [Potsdam(r)-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/Potsdam(r)-source.pth) |  [dg_potRGB2IRRG_512x512.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_potRGB2IRRG_512x512.py) |- |
|-  |V2P(i)| [Vaihingen-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/Vaihingen-source.pth) | [dg_vai2potIRRG_512x512.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_vai2potIRRG_512x512.py)|- |
|-  |V2P(r)| [Vaihingen-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/Vaihingen-source.pth)| [dg_vai2potIRRG_512x512.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_vai2potIRRG_512x512.py) |- |
|LoveDA|Urban2Rural| Coming Soon | [dg_loveda_rural2urban_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_loveda_rural2urban_1024x1024.py) |Coming Soon |
|-  |Rural2Urban| Coming Soon | [dg_loveda_urban2rural_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_loveda_urban2rural_1024x1024.py) |(Coming Soon) |
|WHU Building|A2S| [WHU-Building-A2S.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/WHU-Building-A2S.pth) | [dg_building_aerial2satellite.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_building_aerial2satellite.py)|Coming Soon |
|-  |S2A| [WHU-Building-S2A.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/WHU-Building-S2A.pth)| [dg_building_satellite2aerial.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_building_satellite2aerial.py) |Coming Soon |
|DeepGlobe and Massachusetts |D2M| Coming Soon | Coming Soon |Coming Soon |
|ISPRS Potsdam and RescueNet|P(r)2Res| [Potsdam(r)2RescueNet.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/Potsdam(r)2RescueNet.pth) |[dg_potsdamIRRG2rescue_512x512.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_potsdamIRRG2rescue_512x512.py) |Coming Soon |
|-  |P(i)2Res| [Potsdam(i)2RescueNet.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/Potsdam(i)2RescueNet.pth) | [dg_potsdamRGB2rescue_512x512.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_potsdamRGB2rescue_512x512.py) |Coming Soon |
|CASID|Sub2Sub| Coming Soon | [dg_casid_subms_1024x1024](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_subms_1024x1024.py)|Coming Soon |
|-  |Sub2Tem|Coming Soon | [dg_casid_subms_1024x1024](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_subms_1024x1024.py) |- |
|-  |Sub2Tms| Coming Soon | [dg_casid_subms_1024x1024](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_subms_1024x1024.py) |-|
|-  |Susb2Trf| Coming Soon | [dg_casid_subms_1024x1024](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_subms_1024x1024.py) |- |
|-  |Tem2Sub| [casid-tem-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/casid-tem-source.pth) | [dg_casid_temms_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_temms_1024x1024.py) |Coming Soon |
|-  |Tem2Tem|[casid-tem-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/casid-tem-source.pth) | [dg_casid_temms_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_temms_1024x1024.py)|- |
|-  |Tem2Tms| [casid-tem-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/casid-tem-source.pth) | [dg_casid_temms_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_temms_1024x1024.py)|- |
|-  |Tem2Trf| [casid-tem-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/casid-tem-source.pth) | [dg_casid_temms_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_temms_1024x1024.py)|- |
|-  |Tms2Sub| [casid-tms-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/casid-tms-source.pth)| [dg_casid_troms_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_troms_1024x1024.py) |Coming Soon |
|-  |Tms2Tem| [casid-tms-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/casid-tms-source.pth)| [dg_casid_troms_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_troms_1024x1024.py)  |- |
|-  |Tms2Trf| [casid-tms-source.pth](https://huggingface.co/Cusyoung/CrossEarth/blob/main/casid-tms-source.pth)| [dg_casid_troms_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_troms_1024x1024.py)  |- |
|-  |Trf2Sub| Coming Soon | [dg_casid_trorf_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_trorf_1024x1024.py)|Coming Soon |
|-  |Trf2Tem|Coming Soon | [dg_casid_trorf_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_trorf_1024x1024.py)|- |
|-  |Trf2Tms| Coming Soon | [dg_casid_trorf_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_trorf_1024x1024.py)|- |
|-  |Trf2Trf|Coming Soon | [dg_casid_trorf_1024x1024.py](https://github.com/Cuzyoung/CrossEarth/blob/main/configs/_base_/datasets/dg_casid_trorf_1024x1024.py)|- |



# Citation

If you find CrossEarth helpful, please consider giving this repo a ⭐ and citing:

```
@article{crossearth,
  title={CrossEarth: Geospatial Vision Foundation Model for Domain Generalizable Remote Sensing Semantic Segmentation},
  author={Gong, Ziyang and Wei, Zhixiang and Wang, Di and Ma, Xianzheng and Chen, Hongruixuan and Jia, Yuru and Deng, Yupeng and Ji, Zhenming and Zhu, Xiangwei and Yokoya, Naoto and Zhang, Jing and Du, Bo and Zhang, Liangpei},
  journal={arXiv preprint arXiv:2410.22629},
  year={2024}
}
```
# Other Related Works
- [MTP: Advancing remote sensing foundation model via multi-task pretraining](https://arxiv.org/abs/2403.13430)
- [Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation](https://arxiv.org/abs/2312.04265)







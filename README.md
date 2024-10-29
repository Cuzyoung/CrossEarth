 
<div align="center">

<h1><img src="images/CrossEarth.png" width="5%"> CrossEarth: Geospatial Vision Foundation Model for Domain Generalizable Remote Sensing Semantic Segmentation</h1>


Ziyang Gong<sup>1 ∗</sup>, Zhixiang Wei<sup>2 ∗</sup>, Di Wang<sup>3 ∗</sup>, Xianzheng Ma<sup>3</sup>, Hongruixuan Chen<sup>4</sup>, Yuru Jia<sup>56</sup>, Yupeng Deng<sup>1</sup>, Zhenming Ji<sup>1 †</sup>, Xiangwei Zhu<sup>1 †</sup>, Naoto Yokoya<sup>4</sup>, Jing Zhang<sup>3</sup>, Bo Du<sup>3</sup>, Liangpei Zhang<sup>3</sup>

<sup>1</sup> Sun Yat-sen University, <sup>2</sup> University of Science and Technology of China, <sup>3</sup> Wuhan University, 

<sup>4</sup> The University of Tokyo, <sup>5</sup> KU Leuven, <sup>6</sup> KTH Royal Institute of Technology

<sup>∗</sup> Equal contribution, <sup>†</sup> Corresponding author

<!-- <a href="" target='_blank'><img src="https://visitor-badge.laobi.icu/badge?page_id=Cuzyoung.Foundation-Models-in-Remote-Sensing&left_color=blue&right_color=%23CEE75F"> </a>   -->


<img src="images/teaser_new.png" width="100%">

</div>
<br>
<br>

# 🔥🔥🔥 News

- The environment and inference steps please refer to the following installation. The inference codes and weights will be coming soon.

- The benchmark collection in the paper is releasing and you can access it at [here](https://github.com/Cuzyoung/CrossEarth/tree/main/benchmarks). 

- 🎉🎉🎉 CrossEarth is the first VFM for Remote Sensing Domain Generalization (RSDG) semantic segmentation. We just release the arxiv paper of CrossEarth. You can access CrossEarth at [here](https://arxiv.org/abs/2410.12345). 

<br>

# 📑 Table of Content
- [Visualization](#visualization)
- [Installation](#installation)
- [Model Weights with Configs](#model-weights-with-configs)
<!-- - [Citation](#citation)
 -->


## Visualization  
<img src="images/visual.png" width="100%">


## Installation

Environment:
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


## Model Weights with Configs

| Dataset | Benchmark | Model | Config | Log |
|----------|----------|-------| -------| ----|
|ISPRS Potsdam and Vaihingen|P(i)2V| Coming Soon | Coming Soon |Coming Soon |
|-  |P(i)2P(r)| - | - |- |
|-  |P(r)2P(i)| Coming Soon | Coming Soon |Coming Soon |
|-  |P(r)2V| - | - |- |
|-  |V2P(i)| Coming Soon | Coming Soon |Coming Soon |
|-  |V2P(r)| -| - |- |
|LoveDA|Urban2Rural| Coming Soon | Coming Soon |Coming Soon |
|-  |Rural2Urban| Coming Soon | Coming Soon |Coming Soon |
|WHU Building|A2S| Coming Soon | Coming Soon |Coming Soon |
|-  |S2A| Coming Soon | Coming Soon |Coming Soon |
|DeepGlobe and Massachusetts |D2M| Coming Soon | Coming Soon |Coming Soon |
|ISPRS Potsdam and RescueNet|P(r)2Res| Coming Soon | Coming Soon |Coming Soon |
|-  |P(i)2Res| Coming Soon | Coming Soon |Coming Soon |
|CASID|Sub2Sub| Coming Soon | Coming Soon |Coming Soon |
|-  |Sub2Tem| - | - |- |
|-  |Sub2Tms| - | - |-|
|-  |Susb2Trf| - | - |- |
|-  |Tem2Sub| Coming Soon | Coming Soon |Coming Soon |
|-  |Tem2Tem| - | - |- |
|-  |Tem2Tms| - | - |- |
|-  |Tem2Trf| - | - |- |
|-  |Tms2Sub| Coming Soon | Coming Soon |Coming Soon |
|-  |Tms2Tem| - | - |- |
|-  |Tms2Trf| - | - |- |
|-  |Trf2Sub| Coming Soon | Coming Soon |Coming Soon |
|-  |Trf2Tem| - | - |- |
|-  |Trf2Tms| - | - |- |
|-  |Trf2Trf| - | - |- |



# Citation

If you find CrossEarth helpful, please consider giving this repo a ⭐ and citing:

```
@article{crossearth,
  title={CrossEarth: Geospatial Vision Foundation Model for Domain Generalizable Remote Sensing Semantic Segmentation},
  author={Gong, Ziyang and Wei, Zhixiang and Wang, Di and Ma, Xianzheng and Chen, Hongruixuan and Jia, Yuru and Deng, Yupeng and Ji, Zhenming and Zhu, Xiangwei and Yokoya, Naoto and Zhang, Jing and Du, Bo and Zhang, Liangpei},
  journal={arXiv preprint arXiv:2410.12345},
  year={2024}
}
```
# Other Related Works
- [MTP: Advancing remote sensing foundation model via multi-task pretraining](https://arxiv.org/abs/2403.13430)
- [Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation](https://arxiv.org/abs/2312.04265)







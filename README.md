# 🏡 Generalized Models in Remote Sensing Semantic Segmentation

<!-- Hi! 🌊🌊🌊 I'm [Ziyang Gong](https://scholar.google.com/citations?user=cWip8QgAAAAJ&hl=zh-CN&oi=ao). 

[Zhixiang Wei](https://scholar.google.com/citations?user=i5W4i9YAAAAJ&hl=zh-CN&oi=sra) and me curate this collection aiming to help researchers to know the development of semantic segmentation foundation models in remote sensing quickly. This collection contains foundation models and various benchmarks. It also will be continually updating. If you have any question or advice, please feel free to contact me. This is my email📧: gongzy23@sysu.mail2.edu.cn.    -->


<div align="center">

<h1>CrossEarth: Geospatial Vision Foundation Model for Domain Generalizable Remote Sensing Semantic Segmentation</h1>


Ziyang Gong<sup>1 ∗</sup>, Zhixiang Wei<sup>2 ∗</sup>, Di Wang<sup>3 ∗</sup>, Xianzheng Ma<sup>3</sup>, Hongruixuan Chen<sup>4</sup>, Yuru Jia<sup>56</sup>, Yupeng Deng<sup>1</sup>, Zhenming Ji<sup>1 †</sup>, Xiangwei Zhu<sup>1 †</sup>, Naoto Yokoya<sup>4</sup>, Jing Zhang<sup>3</sup>, Bo Du<sup>3</sup>, Liangpei Zhang<sup>3</sup>

<sup>1</sup> Sun Yat-sen University, <sup>2</sup> University of Science and Technology of China, <sup>3</sup> Wuhan University, 

<sup>4</sup> The University of Tokyo, <sup>5</sup> KU Leuven, <sup>6</sup> KTH Royal Institute of Technology

<sup>∗</sup> Equal contribution, <sup>†</sup> Corresponding author

</div>

<!-- <a href="" target='_blank'><img src="https://visitor-badge.laobi.icu/badge?page_id=Cuzyoung.Foundation-Models-in-Remote-Sensing&left_color=blue&right_color=%23CEE75F"> </a>   -->
## Table of Content

  - [Foundation Models](##foundation-models)
  - [Domain Adaptation Models](##domain-adaptation-models)
  - [Domain Generalization Models](##domain-generalization-models)
  - [Semantic Segmentation Benchmark Settings](##segmentation-benchmark-settings)



## Foundation Models

| <p align="center"> Date | Institute (first) |<p align="center">Paper Name |<p align="center"> Publication|<p align="center"> Others |
| :-----: | :-------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------:| :---------:
| 2024-03-20 | WHU |<p align="center"> MTP: Advancing Remote Sensing Foundation Model via Multi-Task Pretraining |[Arxiv](https://arxiv.org/abs/2403.13430) |[Github](https://github.com/ViTAE-Transformer/MTP/tree/main) |
| 2023-10-13 | WHU |<p align="center"> SAMRS: Scaling-up Remote Sensing Segmentation Dataset with Segment Anything Model|[NeurIPS](https://arxiv.org/abs/2204.02825) | [Github](https://github.com/ViTAE-Transformer/SAMRS) |
| 2023-09-16 | AIR, CAS |<p align="center"> RingMo-lite: A Remote Sensing Multi-task Lightweight Network with CNN-Transformer Hybrid Framework |  - |[TGRS](https://arxiv.org/abs/2309.09003) |
| 2023-04-11 |MSIT, Korea |<p align="center"> A Billion-scale Foundation Model for Remote Sensing Images |[Arxiv](https://arxiv.org/pdf/2304.05215.pdf) | - |
| 2022-07-28 | AIR, CAS |<p align="center"> RingMo: A Remote Sensing Foundation Model With Masked Image Modeling  |[TGRS](https://drive.google.com/file/d/1MVP31ksrMKgFUQJMItZcrPfXtAJZ7Wbc/view) | - |
| 2022-12-08 | WHU|<p align="center"> Advancing Plain Vision Transformer Toward Remote Sensing Foundation Model  |[TGRS](https://arxiv.org/pdf/2208.03987.pdf) | [Github](https://github.com/vitae-transformer/remote-sensing-rvsa) |
| 2022-04-06 | WHU |<p align="center"> An Empirical Study of Remote Sensing Pretraining |[TGRS](https://arxiv.org/abs/2204.02825) | [Github](https://github.com/ViTAE-Transformer/ViTAE-Transformer-Remote-Sensing)|
| 2023-11-29 | BHU |<p align="center"> RSPrompter: Learning to Prompt for Remote Sensing Instance Segmentation Based on Visual Foundation Model |[TGRS](https://arxiv.org/abs/2204.02825) | - |
| 2024-03-22 | Ant Group |<p align="center"> SkySense: A Multi-Modal Remote Sensing Foundation Model Towards Universal Interpretation for Earth Observation Imagery |[CVPR](https://arxiv.org/pdf/2312.10115.pdf) | - |

## Domain Adaptation Models

| <p align="center"> Date | Institute (first) |<p align="center">Paper Name|<p align="center"> Publication|<p align="center"> Github|<p align="center"> Number|
| :-----: | :-------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------:| :---------:| :---------:
| 2024-04-23 | RIKEN |<p align="center"> Unsupervised Domain Adaptation Architecture Search with Self-Training for Land Cover Mapping |[CVPR Workshop 2024](https://openaccess.thecvf.com/content/CVPR2024W/EarthVision/papers/Broni-Bediako_Unsupervised_Domain_Adaptation_Architecture_Search_with_Self-Training_for_Land_Cover_CVPRW_2024_paper.pdf) |[Github](https://github.com/cliffbb/UDA-NAS)|12|
| 2023-09-23 | South-Central Minzu University |<p align="center"> SCDA: A Style and Content Domain Adaptive Semantic Segmentation Method for Remote Sensing Images |[RS](https://www.mdpi.com/2072-4292/15/19/4668) |-|17|
| 2023-05-31 | TUM |<p align="center"> Pseudo Features-Guided Self-Training for Domain Adaptive Semantic Segmentation of Satellite Images |[TGRS](https://ieeexplore.ieee.org/abstract/document/10141556) |-|16|
| 2023-05-30 | NJU |<p align="center"> A Multilevel-Guided Curriculum Domain Adaptation Approach to Semantic Segmentation for High-Resolution Remote Sensing Images |[TGRS](https://ieeexplore.ieee.org/abstract/document/10138603) |-|4|
| 2023-05-22 | UCAS |<p align="center"> Unsupervised Domain Adaptation for Remote Sensing Image Segmentation Based on Adversarial Learning and Self-Training |[TGRS](https://ieeexplore.ieee.org/abstract/document/10130291) |-|8|
| 2023-05-01 | NJU |<p align="center"> Category-Level Assignment for Cross-Domain Semantic Segmentation in Remote Sensing Images |[TGRS](https://ieeexplore.ieee.org/abstract/document/10113334) |-|15|
| 2023-04-25 | NJU |<p align="center"> A Fine-Grained Unsupervised Domain Adaptation Framework for Semantic Segmentation of Remote Sensing Images |[J-STARS](https://ieeexplore.ieee.org/abstract/document/10107973) |-|1|
| 2023-04-23 | Shanxi Normal University |<p align="center"> Cross-Domain Few-Shot Segmentation for Remote Sensing Image Based on Task Augmentation and Feature Disentanglement |[J-STARS](https://ieeexplore.ieee.org/abstract/document/10506968) |-|-|
| 2023-04-19 | CUG |<p align="center"> DSM-Assisted Unsupervised Domain Adaptive Network for Semantic Segmentation of Remote Sensing Imagery |[TGRS](https://ieeexplore.ieee.org/abstract/document/10105632) |-|19|
| 2023-04-16 | Sapienza University of Rome |<p align="center"> GeoMultiTaskNet: remote sensing unsupervised domain adaptation using geographical coordinates |[CVPR Workshop 2023](https://openaccess.thecvf.com/content/CVPR2023W/EarthVision/papers/Marsocci_GeoMultiTaskNet_Remote_Sensing_Unsupervised_Domain_Adaptation_Using_Geographical_Coordinates_CVPRW_2023_paper.pdf) |-|13|
| 2023-03-29 | CSU |<p align="center"> Memory-Contrastive Unsupervised Domain Adaptation for Building Extraction of High-Resolution Remote Sensing Imagery |[TGRS](https://ieeexplore.ieee.org/document/10087276) |-|14|
| 2023-01-16 | NJU |<p align="center"> Multilevel Heterogeneous Domain Adaptation Method for Remote Sensing Image Segmentation |[TGRS](https://ieeexplore.ieee.org/document/10017270) |-|5|
| 2022-12-26 | UESTC|<p align="center"> DASRSNet: Multitask Domain Adaptation for Super-Resolution-Aided Semantic Segmentation of Remote Sensing Images |[TGRS](https://ieeexplore.ieee.org/abstract/document/9999252) |-|-|
| 2022-09-29 | UESTC|<p align="center"> Unsupervised Domain Adaptation for Remote Sensing Semantic Segmentation with Transformer |[RS](https://www.mdpi.com/2072-4292/14/19/4942) |-|11|
| 2022-08-31 | ZJU |<p align="center"> IterDANet: Iterative Intra-Domain Adaptation for Semantic Segmentation of Remote Sensing Images |[TGRS](https://ieeexplore.ieee.org/abstract/document/9872019) |-|9|
| 2022-07-07 | SDU |<p align="center"> Unsupervised Domain Adaptation Semantic Segmentation for Remote-Sensing Images via Covariance Attention |[GRSL](https://ieeexplore.ieee.org/abstract/document/9817117) |-|-|
| 2022-03-30 | HNU |<p align="center"> Deep Covariance Alignment for Domain Adaptive Remote Sensing Image Segmentation |[TGRS](https://ieeexplore.ieee.org/document/9745130) |[Github]( https://github.com/Luffy03/DCA)|2|
| 2021-12-28 | ZJU |<p align="center"> BiFDANet: Unsupervised Bidirectional Domain Adaptation for Semantic Segmentation of Remote Sensing Images |[RS](https://www.mdpi.com/2072-4292/14/1/190) |-|10|
| 2021-08-28 | WHU |<p align="center"> Stagewise Unsupervised Domain Adaptation with Adversarial Self-Training for Road Segmentation of Remote Sensing Images |[TGRS](https://ieeexplore.ieee.org/document/9516689) |-|6|
| 2021-03-06 | WHU |<p align="center"> Learning Deep Semantic Segmentation Network Under Multiple Weakly-Supervised Constraints For Cross-Domain Remote Sensing Image Semantic Segmentation |[ISPRS](https://www.sciencedirect.com/science/article/pii/S0924271621000423)|-|18|
| 2020-11-17 | HIT |<p align="center"> Bispace Domain Adaptation Network for Remotely Sensed Semantic Segmentation |[TGRS](https://ieeexplore.ieee.org/document/9261997)|-|-|
| 2020-07-05 | Information Technology University, Pakistan |<p align="center"> Weakly-Supervised Domain Adaptation for Built-up Region Segmentation in Aerial and Satellite Imagery |[Arxiv](https://arxiv.org/pdf/2007.02277)|-|7|
| 2020-06-07 | Universite C´ ote d’Azur and Inria |<p align="center"> DAugNet: Unsupervised, Multi-source, Multi-target, and Life-long Domain Adaptation for Semantic Segmentation of Satellite Images |[TGRS](https://ieeexplore.ieee.org/document/9137717) |-|3|
| 2020-03-25 | Universite C´ ote d’Azur and Inria |<p align="center"> ColorMapGAN: Unsupervised Domain Adaptation for Semantic Segmentation Using Color Mapping Generative Adversarial Networks |[TGRS](https://ieeexplore.ieee.org/document/9047180) |-|-|
| 2019-12-17 | University of California, Merced |<p align="center"> Multisource Domain Adaptation for Remote Sensing Using Deep Neural Networks|[TGRS](https://ieeexplore.ieee.org/document/8935505) |-|-|
| 2019-11-14 | University of California, Merced |<p align="center"> Large Scale Unsupervised Domain Adaptation of Segmentation Networks with Adversarial Learning|[IGARSS 2019](https://ieeexplore.ieee.org/document/8900277) |-|-|
| 2019-06-07 | Prince Sultan University |<p align="center"> Unsupervised Domain Adaptation Using Generative Adversarial Networks for Semantic Segmentation of Aerial Images |[RS](https://www.mdpi.com/2072-4292/11/11/1369) |-|-|

## Domain Generalization Models

## Semantic Segmentation Benchmarks 
| <p align="center"> Date |<p align="center"> Institute (first) |<p align="center"> Paper/Benchmark Name |<p align="center"> Publication |<p align="center"> Others |
| :-----: | :-------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------: | :---------:
| 2023-10-10 | WHU | <p align="center">A large-scale climate-aware satellite image dataset for domain adaptive land-cover semantic segmentation | [ISPRS](https://doi.org/10.1016/j.isprsjprs.2023.09.007) | [Github](-) |
| 2021-10-17 |WHU | <p align="center">LoveDA: A Remote Sensing Land-Cover Dataset for Domain Adaptive Semantic Segmentation | [NeurIPS](https://www.researchgate.net/publication/355390292_LoveDA_A_Remote_Sensing_Land-Cover_Dataset_for_Domain_Adaptive_Semantic_Segmentation) | [Github](https://github.com/Junjue-Wang/LoveDA) |
| 2019-05-30 |Inceptionai |<p align="center"> iSAID: A Large-scale Dataset for Instance Segmentation in Aerial Images | [CVPR Workshop](https://openaccess.thecvf.com/content_CVPRW_2019/papers/DOAI/Zamir_iSAID_A_Large-scale_Dataset_for_Instance_Segmentation_in_Aerial_Images_CVPRW_2019_paper.pdf) | [Website](https://captain-whu.github.io/iSAID/index.html) |
| - |<p align="center">ISPRS |<p align="center">Potsdam | [Website](https://www.isprs.org/education/benchmarks/UrbanSemLab/2d-sem-label-vaihingen.aspx) | [Download](https://pan.baidu.com/share/init?surl=K-cLVZnd1X7d8c26FQ-nGg&pwd=mseg) |
| - |<p align="center">ISPRS |<p align="center">Vaihingen | [Website](https://www.isprs.org/education/benchmarks/UrbanSemLab/2d-sem-label-potsdam.aspx) | [Download](https://pan.baidu.com/s/109D3WLrLafsuYtLeerLiiA?pwd=mseg) |

## Cross-Domain Experiments Settings
| <p align="center"> Dataset |<p align="center"> Source Domain (In-Domain) |<p align="center"> Target Domain (Out-Of-Domain)|<p align="center"> Employed by Papers |
| :-----: | :--------------------: | :---------------------------- | :---------:
| LoveDA |Urban| Rural |2, 14 (only building)|
| - |Rural| Urban |2, 14 (only building)|
| Potsdam|Potsdam (R-G-B)| Potsdam (IR-R-G) |4|
| Potsdam, Gaofen-2|Potsdam (R-G-B)| Gaofen-2 (R-G-B)|4|
| Potsdam, Vaihingen |Potsdam (IR-R-G)| Vaihingen (IR-R-G) |1, 4, 5, 15, 16, 18, 19|
| - |Potsdam (R-G-B)| Vaihingen (IR-R-G) |1, 4, 11, 15, 18, 19|
| - |Vaihingen (IR-R-G)| Potsdam (IR-R-G) |1, 4, 5, 15, 16, 18, 19|
| - |Vaihingen (IR-R-G)| Potsdam (R-G-B) |1, 4, 5, 15, 18|
|-  |Potsdam (unclear) |Vaihingen (IR-R-G)|9, 10|
|-  |Vaihingen (IR-R-G)|Potsdam (unclear)|9, 10|
| Potsdam, RescueNet |Potsdam (IR-R-G)| RescueNet (R-G-B) |15|
| - |Potsdam (R-G-B)| RescueNet (R-G-B) |15|
| CASID |SubTropical Moonsoon (SubMs)| TroMs, TemMs, TroRf|-|  
| - |Tropical Moonsoon (TroMs)| SubMs, TemMs, TroRf|-|  
| - |Temperate Moonsoon (TemMs)| SubMs, TroMs, TroRf|-|  
| - |Tropical Rainforest (TroRf)| SubMs, TroMs, TemMs|-|
|WHU|Aerial|Satellite II| 5, 8|
|-|Satellite II|Aerial| 5, 8|
|WHU Building, LoveDA|WHU Building|LoveDA-Urban|14 (only building)|
|-|WHU Building|LoveDA-Rural|14 (only building)|
|-|LoveDA-Urban|WHU Building|14 (only building)|
|-|LoveDA-Rural|WHU Building|14 (only building)|
| OpenEarthMap |73 regions| 24 regions|12| 
|FLAIR #1| D06, D08, D13, D17, D23, D29, D33, D58, D67, D74|D64, D68, D71|12, 13|








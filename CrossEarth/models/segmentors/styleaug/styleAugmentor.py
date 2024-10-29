import torch
import torch.nn as nn

from .ghiasi import Ghiasi
from .stylePredictor import StylePredictor
import numpy as np
import sys
from os.path import join, dirname

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

class StyleAugmentor(nn.Module):
    def __init__(self):
        super(StyleAugmentor,self).__init__()

        # create transformer and style predictor networks:
        self.ghiasi = Ghiasi()
        self.stylePredictor = StylePredictor()
        self.ghiasi.to(device)
        self.stylePredictor.to(device)

        # load checkpoints:
        checkpoint_ghiasi = torch.load(join(dirname(__file__),'checkpoints/checkpoint_transformer.pth'))
        checkpoint_stylepredictor = torch.load(join(dirname(__file__),'checkpoints/checkpoint_stylepredictor.pth'))
        checkpoint_embeddings = torch.load(join(dirname(__file__),'checkpoints/checkpoint_embeddings.pth'))
        
        # self.troms_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/TroMs/mean.npy')
        # self.troms_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/TroMs/covariance.npy')

        # self.trorf_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/TroRf/mean.npy')
        # self.trorf_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/TroRf/covariance.npy')

        # self.temms_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/TemMs/mean.npy')
        # self.temms_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/TemMs/covariance.npy')

        # self.subms_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/SubMs/mean.npy')
        # self.subms_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/SubMs/covariance.npy')
        
        # self.loveda_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/loveda/mean.npy')
        # self.loveda_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/loveda/covariance.npy')

        # self.fog_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/cs2acdc/fog/mean.npy')
        # self.fog_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/cs2acdc/fog/covariance.npy')

        # self.rain_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/cs2acdc/rain/mean.npy')
        # self.rain_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/cs2acdc/rain/covariance.npy')

        # self.snow_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/cs2acdc/snow/mean.npy')
        # self.snow_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/cs2acdc/snow/covariance.npy')

        # self.night_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/cs2acdc/night/mean.npy')
        # self.night_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/cs2acdc/night/covariance.npy')

        # self.vai_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/vaihingen/mean.npy')
        # self.vai_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/vaihingen/covariance.npy')

        # self.pots_rgb_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/potsdam_rgb/mean.npy')
        # self.pots_rgb_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/potsdam_rgb/covariance.npy')

        # self.pots_irrg_mean = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/potsdam_irrg/mean.npy')
        # self.pots_irrg_cov = np.load('/share/home/dq070/GZY-HRDA/style-augment/style-augmentation-master/mean_variance/potsdam_irrg/covariance.npy')

        self.earth_mean = np.load('/share/home/dq070/CoT/Rein-Cityscapes/checkpoints/earth_embedding/mean.npy')
        self.earth_cov = np.load('/share/home/dq070/CoT/Rein-Cityscapes/checkpoints/earth_embedding/covariance.npy')


        # load weights for ghiasi and stylePredictor, and mean / covariance for the embedding distribution:
        self.ghiasi.load_state_dict(checkpoint_ghiasi['state_dict_ghiasi'],strict=False)
        self.stylePredictor.load_state_dict(checkpoint_stylepredictor['state_dict_stylepredictor'],strict=False)

        # load mean imagenet embedding:
        self.imagenet_embedding = checkpoint_embeddings['imagenet_embedding_mean'] # mean style embedding for ImageNet
        self.imagenet_embedding = self.imagenet_embedding.to(device)

        # # get mean and covariance of PBN style embeddings:
        # self.mean = checkpoint_embeddings['pbn_embedding_mean']
        # self.mean = self.mean.to(device) # 1 x 100
        # self.cov = checkpoint_embeddings['pbn_embedding_covariance']
        
        # # compute SVD of covariance matrix:
        # u, s, vh = np.linalg.svd(self.cov.numpy())
        
        # self.A = np.matmul(u,np.diag(s**0.5))
        # self.A = torch.tensor(self.A).float().to(device) # 100 x 100
        # self.cov = cov(Ax), x ~ N(0,1)

        # self.troms_mean, self.troms_A = self.get_mean_cov(self.troms_mean, self.troms_cov)
        # self.trorf_mean, self.trorf_A = self.get_mean_cov(self.trorf_mean, self.trorf_cov)
        # self.temms_mean, self.temms_A = self.get_mean_cov(self.temms_mean, self.temms_cov)
        # self.subms_mean, self.subms_A = self.get_mean_cov(self.subms_mean, self.subms_cov)

        # self.loveda_mean, self.loveda_A = self.get_mean_cov(self.loveda_mean, self.loveda_cov)

        # self.fog_mean, self.fog_A = self.get_mean_cov(self.fog_mean, self.fog_cov)
        # self.rain_mean, self.rain_A = self.get_mean_cov(self.rain_mean, self.rain_cov)
        # self.snow_mean, self.snow_A = self.get_mean_cov(self.snow_mean, self.snow_cov)
        # self.night_mean, self.night_A = self.get_mean_cov(self.night_mean, self.night_cov)

        # self.vai_mean, self.vai_A = self.get_mean_cov(self.vai_mean, self.vai_cov)
        # self.pots_rgb_mean, self.pots_rgb_A = self.get_mean_cov(self.pots_rgb_mean, self.pots_rgb_cov)
        # self.pots_irrg_mean, self.pots_irrg_A = self.get_mean_cov(self.pots_irrg_mean, self.pots_irrg_cov)

        self.earth_mean, self.earth_A = self.get_mean_cov(self.earth_mean, self.earth_cov)



    def get_mean_cov(self, mean, cov):
        mean = torch.tensor(mean).float().to(device)
        u, s, vh = np.linalg.svd(cov)
        A = np.matmul(u,np.diag(s**0.5))
        A = torch.tensor(A).float().to(device)
        return mean, A

    def sample_embedding(self,n, cross_domain_settings):
        # n: number of embeddings to sample
        # returns n x 100 embedding tensor
        embedding = torch.randn(n,100).to(device) # n x 100
        # if cross_domain_settings == 'subms':
        #     if torch.rand(1) < 0.33:
        #         embedding = torch.mm(embedding,self.troms_A.transpose(1,0)) + self.troms_mean # n x 100
        #     elif torch.rand(1) >= 0.33 and torch.rand(1) < 0.66:
        #         embedding = torch.mm(embedding,self.trorf_A.transpose(1,0)) + self.trorf_mean
        #     elif torch.rand(1) >= 0.66 and torch.rand(1) < 1:
        #         embedding = torch.mm(embedding,self.temms_A.transpose(1,0)) + self.temms_mean
        # elif cross_domain_settings == 'troms':
        #     if torch.rand(1) < 0.33:
        #         embedding = torch.mm(embedding,self.subms_A.transpose(1,0)) + self.subms_mean
        #     elif torch.rand(1) >= 0.33 and torch.rand(1) < 0.66:
        #         embedding = torch.mm(embedding,self.trorf_A.transpose(1,0)) + self.trorf_mean
        #     elif torch.rand(1) >= 0.66 and torch.rand(1) < 1:
        #         embedding = torch.mm(embedding,self.temms_A.transpose(1,0)) + self.temms_mean
        # elif cross_domain_settings == 'trorf':
        #     if torch.rand(1) < 0.33:
        #         embedding = torch.mm(embedding,self.subms_A.transpose(1,0)) + self.subms_mean
        #     elif torch.rand(1) >= 0.33 and torch.rand(1) < 0.66:
        #         embedding = torch.mm(embedding,self.troms_A.transpose(1,0)) + self.troms_mean
        #     elif torch.rand(1) >= 0.66 and torch.rand(1) < 1:
        #         embedding = torch.mm(embedding,self.temms_A.transpose(1,0)) + self.temms_mean
        # elif cross_domain_settings == 'temms':
        #     if torch.rand(1) < 0.33:
        #         embedding = torch.mm(embedding,self.subms_A.transpose(1,0)) + self.subms_mean
        #     elif torch.rand(1) >= 0.33 and torch.rand(1) < 0.66:
        #         embedding = torch.mm(embedding,self.troms_A.transpose(1,0)) + self.troms_mean
        #     elif torch.rand(1) >= 0.66 and torch.rand(1) < 1:
        #         embedding = torch.mm(embedding,self.trorf_A.transpose(1,0)) + self.trorf_mean
        # elif cross_domain_settings == 'loveda':
        #     embedding = torch.mm(embedding,self.loveda_A.transpose(1,0)) + self.loveda_mean
        # elif cross_domain_settings == 'cs2acdc':
        #     if torch.rand(1) < 0.25:
        #         embedding = torch.mm(embedding,self.fog_A.transpose(1,0)) + self.fog_mean
        #     elif torch.rand(1) >= 0.25 and torch.rand(1) < 0.5:
        #         embedding = torch.mm(embedding,self.night_A.transpose(1,0)) + self.night_mean
        #     elif torch.rand(1) >= 0.5 and torch.rand(1) < 0.75:
        #         embedding = torch.mm(embedding,self.rain_A.transpose(1,0)) + self.rain_mean
        #     elif torch.rand(1) >= 0.75 and torch.rand(1) < 1:
        #         embedding = torch.mm(embedding,self.snow_A.transpose(1,0)) + self.snow_mean
        # elif cross_domain_settings == 'pots2vai':
        #     embedding = torch.mm(embedding,self.vai_A.transpose(1,0)) + self.vai_mean
        # elif cross_domain_settings == 'vai2pots_rgb':
        #     embedding = torch.mm(embedding,self.pots_rgb_A.transpose(1,0)) + self.pots_rgb_mean
        # elif cross_domain_settings == 'vai2pots_irrg':
        #     embedding = torch.mm(embedding,self.pots_irrg_A.transpose(1,0)) + self.pots_irrg_mean
        # elif cross_domain_settings == 'earth':
        #     embedding = torch.mm(embedding,self.earth_A.transpose(1,0)) + self.earth_mean
        # else:
        #     print('cross_domain_settings Error, please check whether the cross_domain_settings is in temms, trorf, troms, subms, cs2acdc, and loveda.')
        #     #     embedding = torch.mm(embedding,self.A.transpose(1,0)) + self.mean # n x 100
        if cross_domain_settings == 'earth':
            embedding = torch.mm(embedding,self.earth_A.transpose(1,0)) + self.earth_mean
        return embedding

    def forward(self,source_domain, cross_domain_settings, downsamples=0, embedding=None, useStylePredictor=True):
        '''augments a batch of images with style randomization
            x: B x C x H x W image tensor
            alpha: float in [0,1], controls interpolation between random style and original style
            downsamples: int, number of times to downsample by factor of 2 before applying style transfer
            embedding: B x 100 tensor, or None. Use this embedding if provided.
            useStylePredictor: bool. If True, we use the inception based style predictor to compute the original style embedding for the input image, and use that for interpolation. If False, we use the mean ImageNet embedding instead, which is slightly faster.'''

        
        # style embedding for when alpha=0:
        source_content = self.stylePredictor(source_domain) if useStylePredictor else self.imagenet_embedding

        alpha = 0.1
        if embedding is None:
            # sample a random embedding
            embedding = self.sample_embedding(source_domain.size(0), cross_domain_settings)
            # embedding2 = self.sample_embedding(y.size(0))

        # interpolate style embeddings:
        embedding = alpha * embedding + (1-alpha)*source_content
        # embedding = source_content

        # embedding = alpha * embedding + (1-alpha-lamda)*base_x+ lamda*base_y
        # restyled = self.ghiasi(fog,embedding)
        restyled = self.ghiasi(source_domain,embedding)


        if downsamples:
            restyled = nn.functional.upsample(restyled,scale_factor=2**downsamples,mode='bilinear')
        
        return restyled.detach() # detach prevents the user from accidentally backpropagating errors into stylePredictor or ghiasi while training a downstream model

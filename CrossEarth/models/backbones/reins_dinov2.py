from mmseg.models.builder import BACKBONES, MODELS
from .reins import Reins
from .dino_v2 import DinoVisionTransformer
from .utils import set_requires_grad, set_train
import torch
import torch.nn as nn

@BACKBONES.register_module()
class ReinsDinoVisionTransformer(DinoVisionTransformer):
    def __init__(
        self,
        reins_config=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.reins: Reins = MODELS.build(reins_config)

    def forward_features(self, x, is_cross=None, masks=None):
        B, _, h, w = x.shape
        H, W = h // self.patch_size, w // self.patch_size
        if masks is not None:
            x = x * masks + self.mask_token * (1 - masks)
        x_image = x
        x = self.prepare_tokens_with_masks(x)
        outs = []
        for idx, blk in enumerate(self.blocks):
            x = blk(x)
            x = self.reins.forward(
                x_image,
                x,
                idx,
                batch_first=True,
                has_cls_token=True,
                is_cross=is_cross,
            )
            if idx in self.out_indices:
                outs.append(
                    x[:, 1:, :].permute(0, 2, 1).reshape(B, -1, H, W).contiguous()
                )
        return self.reins.return_auto(outs)

    def train(self, mode: bool = True):
        if not mode:
            return super().train(mode)
        set_requires_grad(self, ["reins"])
        set_train(self, ["reins"])

    def state_dict(self, destination, prefix, keep_vars):
        state = super().state_dict(destination, prefix, keep_vars)
        keys = [k for k in state.keys() if "rein" not in k]
        for key in keys:
            state.pop(key)
            if key in destination:
                destination.pop(key)
        return state
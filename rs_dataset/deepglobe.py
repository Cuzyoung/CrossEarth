
from mmseg.registry import DATASETS
from mmseg.datasets import BaseSegDataset

@DATASETS.register_module()
class DeepglobeDataset(BaseSegDataset):
    METAINFO = dict(classes =['Road', 'Background'],
    palette =[(0,0,0), (255, 255, 255)])
   
    def __init__(self, **kwargs):
        super(DeepglobeDataset, self).__init__(
            img_suffix='_sat.jpg',
            seg_map_suffix='_mask.png',
            # split=None,
            reduce_zero_label=False,
            **kwargs)
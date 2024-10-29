
from mmseg.registry import DATASETS
from mmseg.datasets import BaseSegDataset

@DATASETS.register_module()
class MassRoadDataset(BaseSegDataset):
    METAINFO = dict(classes =['Road', 'Background'],
    palette =[(0,0,0), (255, 255, 255)])
   
    def __init__(self, **kwargs):
        super(MassRoadDataset, self).__init__(
            img_suffix='.tiff',
            seg_map_suffix='.tif',
            # split=None,
            reduce_zero_label=False,
            **kwargs)
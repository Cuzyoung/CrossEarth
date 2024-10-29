from mmseg.registry import DATASETS
from mmseg.datasets import BaseSegDataset

@DATASETS.register_module()
class CasidDataset(BaseSegDataset):
    METAINFO = dict(classes = ('background', 'building', 'forest', 'road', 'water'),
    palette = [[0, 0, 0,], [255, 255, 0], [85, 255, 0], [255, 0, 0], [0, 112, 255]])
   
    def __init__(self, **kwargs):
        assert kwargs.get('split') in [None, 'train']
        if 'split' in kwargs:
            kwargs.pop('split')
        super(CasidDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='-label.png',
            # split=None,
            **kwargs)
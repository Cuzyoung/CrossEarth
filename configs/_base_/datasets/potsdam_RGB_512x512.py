Potsdam_RGB_type = "PotsdamReduceDataset"
Potsdam_RGB_root = ""
Potsdam_RGB_crop_size = (512,512)
Potsdam_RGB_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", reduce_zero_label=True),
    dict(type="Resize", scale=(512,512)),
    dict(type="RandomCrop", crop_size=Potsdam_RGB_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
Potsdam_RGB_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(512,512), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations",reduce_zero_label=True),
    dict(type="PackSegInputs"),
]
train_Potsdam_RGB  = dict(
    type=Potsdam_RGB_type,
    data_root=Potsdam_RGB_root,
    data_prefix=dict(
        img_path="img_dir/train",
        seg_map_path="ann_dir/train",
    ),
    pipeline=Potsdam_RGB_train_pipeline,
)
val_Potsdam_RGB = dict(
    type=Potsdam_RGB_type,
    data_root=Potsdam_RGB_root,
    data_prefix=dict(
        img_path="img_dir/val",
        seg_map_path="ann_dir/val",
    ),
    pipeline=Potsdam_RGB_test_pipeline,
)
test_Potsdam_RGB= dict(
    type=Potsdam_RGB_type,
    data_root=Potsdam_RGB_root,
    data_prefix=dict(
        iimg_path="img_dir/val",
        seg_map_path="ann_dir/val",
    ),
    pipeline=Potsdam_RGB_test_pipeline,
)

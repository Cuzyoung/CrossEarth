Potsdam_IRRG_type = "PotsdamReduceDataset"
Potsdam_IRRG_root = "path"
Potsdam_IRRG_crop_size = (512,512)
Potsdam_IRRG_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", reduce_zero_label=True),
    dict(type="Resize", scale=(512,512)),
    dict(type="RandomCrop", crop_size=Potsdam_IRRG_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
Potsdam_IRRG_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(512,512), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations",reduce_zero_label=True),
    dict(type="PackSegInputs"),
]
train_Potsdam_IRRG  = dict(
    type=Potsdam_IRRG_type,
    data_root=Potsdam_IRRG_root,
    data_prefix=dict(
        img_path="img_dir/train",
        seg_map_path="ann_dir/train",
    ),
    pipeline=Potsdam_IRRG_train_pipeline,
)
val_Potsdam_IRRG = dict(
    type=Potsdam_IRRG_type,
    data_root=Potsdam_IRRG_root,
    data_prefix=dict(
        img_path="img_dir/val",
        seg_map_path="ann_dir/val",
    ),
    pipeline=Potsdam_IRRG_test_pipeline,
)
test_Potsdam_IRRG  = dict(
    type=Potsdam_IRRG_type,
    data_root=Potsdam_IRRG_root,
    data_prefix=dict(
        img_path="img_dir/val",
        seg_map_path="ann_dir/val",
    ),
    pipeline=Potsdam_IRRG_test_pipeline,
)

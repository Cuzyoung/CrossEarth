Potsdam_Rescue_type = "PotsdamRescueDataset"
Potsdam_Rescue_root = "path"
Potsdam_Rescue_crop_size = (512,512)
Potsdam_Rescue_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", reduce_zero_label=True),
    dict(type="Resize", scale=(512,512)),
    dict(type="RandomCrop", crop_size=Potsdam_Rescue_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
Potsdam_Rescue_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(512,512), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations",reduce_zero_label=True),
    dict(type="PackSegInputs"),
]
train_Potsdam_Rescue  = dict(
    type=Potsdam_Rescue_type,
    data_root=Potsdam_Rescue_root,
    data_prefix=dict(
        img_path="img_dir/train",
        seg_map_path="ann_dir/train",
    ),
    pipeline=Potsdam_Rescue_train_pipeline,
)
val_Potsdam_Rescue = dict(
    type=Potsdam_Rescue_type,
    data_root=Potsdam_Rescue_root,
    data_prefix=dict(
        img_path="img_dir/val",
        seg_map_path="ann_dir/val",
    ),
    pipeline=Potsdam_Rescue_test_pipeline,
)
test_Potsdam_Rescue  = dict(
    type=Potsdam_Rescue_type,
    data_root=Potsdam_Rescue_root,
    data_prefix=dict(
        img_path="img_dir/val",
        seg_map_path="ann_dir/val",
    ),
    pipeline=Potsdam_Rescue_test_pipeline,
)

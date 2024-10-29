PotsdamIRRG_Rescue_type = "PotsdamRescueDataset"
PotsdamIRRG_Rescue_root = "path"
PotsdamIRRG_Rescue_crop_size = (512,512)
PotsdamIRRG_Rescue_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", reduce_zero_label=True),
    dict(type="Resize", scale=(512,512)),
    dict(type="RandomCrop", crop_size=PotsdamIRRG_Rescue_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
PotsdamIRRG_Rescue_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(512,512), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations",reduce_zero_label=True),
    dict(type="PackSegInputs"),
]
train_PotsdamIRRG_Rescue  = dict(
    type=PotsdamIRRG_Rescue_type,
    data_root=PotsdamIRRG_Rescue_root,
    data_prefix=dict(
        img_path="img_dir/train",
        seg_map_path="ann_dir/train",
    ),
    pipeline=PotsdamIRRG_Rescue_train_pipeline,
)
val_PotsdamIRRG_Rescue = dict(
    type=PotsdamIRRG_Rescue_type,
    data_root=PotsdamIRRG_Rescue_root,
    data_prefix=dict(
        img_path="img_dir/val",
        seg_map_path="ann_dir/val",
    ),
    pipeline=PotsdamIRRG_Rescue_test_pipeline,
)
test_PotsdamIRRG_Rescue  = dict(
    type=PotsdamIRRG_Rescue_type,
    data_root=PotsdamIRRG_Rescue_root,
    data_prefix=dict(
        img_path="img_dir/val",
        seg_map_path="ann_dir/val",
    ),
    pipeline=PotsdamIRRG_Rescue_test_pipeline,
)

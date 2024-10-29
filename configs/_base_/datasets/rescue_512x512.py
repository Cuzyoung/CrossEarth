Rescue_type = "RescueDataset"
Rescue_root = "path"
Rescue_crop_size = (512,512)
Rescue_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", reduce_zero_label=True),
    dict(type="Resize", scale=(512,512)),
    dict(type="RandomCrop", crop_size=Rescue_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
Rescue_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(512,512), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations",reduce_zero_label=True),
    dict(type="PackSegInputs"),
]
train_Rescue  = dict(
    type=Rescue_type,
    data_root=Rescue_root,
    data_prefix=dict(
        img_path="test-org-img",
        seg_map_path="test-label-img",
    ),
    pipeline=Rescue_train_pipeline,
)
val_Rescue = dict(
    type=Rescue_type,
    data_root=Rescue_root,
    data_prefix=dict(
        img_path="test-org-img",
        seg_map_path="test-label-img",
    ),
    pipeline=Rescue_test_pipeline,
)
test_Rescue  = dict(
    type=Rescue_type,
    data_root=Rescue_root,
    data_prefix=dict(
        img_path="test-org-img",
        seg_map_path="test-label-img",
    ),
    pipeline=Rescue_test_pipeline,
)

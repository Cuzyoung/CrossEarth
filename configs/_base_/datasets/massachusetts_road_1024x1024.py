Massachusetts_type = "MassRoadDataset"
Massachusetts_root = "path"
Massachusetts_crop_size = (1024, 1024)
Massachusetts_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", reduce_zero_label=False),
    dict(type="Resize", scale=(1024, 1024)),
    dict(type="RandomCrop", crop_size=Massachusetts_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
Massachusetts_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(1500, 1500), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations", reduce_zero_label=False),
    dict(type="PackSegInputs"),
]
train_Massachusetts  = dict(
    type=Massachusetts_type,
    data_root=Massachusetts_root,
    data_prefix=dict(
        img_path="train",
        seg_map_path="train_labels_new",
    ),
    pipeline=Massachusetts_train_pipeline,
)
val_Massachusetts = dict(
    type=Massachusetts_type,
    data_root=Massachusetts_root,
    data_prefix=dict(
        img_path="test",
        seg_map_path="test_labels_new",
    ),
    pipeline=Massachusetts_test_pipeline,
)
test_Massachusetts  = dict(
    type=Massachusetts_type,
    data_root=Massachusetts_root,
    data_prefix=dict(
        img_path="test",
        seg_map_path="test_labels_new",
    ),
    pipeline=Massachusetts_test_pipeline,
)

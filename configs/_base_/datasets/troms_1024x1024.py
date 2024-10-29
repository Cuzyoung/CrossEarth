troms_type = "CasidDataset"
troms_root = "path"
troms_crop_size = (1024, 1024)
troms_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations"),
    dict(type="Resize", scale=(1024, 1024)),
    dict(type="RandomCrop", crop_size=troms_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
troms_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(1024, 1024), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations"),
    dict(type="PackSegInputs"),
]
train_troms = dict(
    type=troms_type,
    data_root=troms_root,
    data_prefix=dict(
        img_path="all_train/image",
        seg_map_path="all_train/label",
    ),
    pipeline=troms_train_pipeline,
)
val_troms = dict(
    type=troms_type,
    data_root=troms_root,
    data_prefix=dict(
        img_path="all_test/image",
        seg_map_path="all_test/label_id",
    ),
    pipeline=troms_test_pipeline,
)

test_troms = dict(
    type=troms_type,
    data_root=troms_root,
    data_prefix=dict(
        img_path="all_test/image",
        seg_map_path="all_test/label_id",
    ),
    pipeline=troms_test_pipeline,
)
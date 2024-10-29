trorf_type = "CasidDataset"
trorf_root = "path"
trorf_crop_size = (1024, 1024)
trorf_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations"),
    dict(type="Resize", scale=(1024, 1024)),
    dict(type="RandomCrop", crop_size=trorf_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
trorf_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(1024, 1024), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations"),
    dict(type="PackSegInputs"),
]
train_trorf = dict(
    type=trorf_type,
    data_root=trorf_root,
    data_prefix=dict(
        img_path="all_train/image",
        seg_map_path="all_train/label",
    ),
    pipeline=trorf_train_pipeline,
)
val_trorf = dict(
    type=trorf_type,
    data_root=trorf_root,
    data_prefix=dict(
        img_path="all_test/image",
        seg_map_path="all_test/label",
    ),
    pipeline=trorf_test_pipeline,
)

test_trorf = dict(
    type=trorf_type,
    data_root=trorf_root,
    data_prefix=dict(
        img_path="all_test/image",
        seg_map_path="all_test/label",
    ),
    pipeline=trorf_test_pipeline,
)
subms_type = "CasidDataset"
subms_root = "path"
subms_crop_size = (1024, 1024)
subms_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations"),
    dict(type="Resize", scale=(1024, 1024)),
    dict(type="RandomCrop", crop_size=subms_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
subms_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(1024, 1024), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations"),
    dict(type="PackSegInputs"),
]
train_subms = dict(
    type=subms_type,
    data_root=subms_root,
    data_prefix=dict(
        img_path="all_train/image",
        seg_map_path="all_train/label",
    ),
    pipeline=subms_train_pipeline,
)
val_subms = dict(
    type=subms_type,
    data_root=subms_root,
    data_prefix=dict(
        img_path="all_test/image",
        seg_map_path="all_test/label",
    ),
    pipeline=subms_test_pipeline,
)

test_subms = dict(
    type=subms_type,
    data_root=subms_root,
    data_prefix=dict(
        img_path="all_test/image",
        seg_map_path="all_test/label",
    ),
    pipeline=subms_test_pipeline,
)

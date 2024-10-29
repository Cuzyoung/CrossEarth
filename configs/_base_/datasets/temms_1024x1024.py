temms_type = "CasidDataset"
temms_root = "path"
temms_crop_size = (1024, 1024)
temms_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", reduce_zero_label=False),
    dict(type="Resize", scale=(1024, 1024)),
    dict(type="RandomCrop", crop_size=temms_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
temms_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(1024, 1024), keep_ratio=False),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations", reduce_zero_label=False),
    dict(type="PackSegInputs"),
]
train_temms = dict(
    type=temms_type,
    data_root=temms_root,
    data_prefix=dict(
        img_path="all_train/image",
        seg_map_path="all_train/label",
    ),
    pipeline=temms_train_pipeline,
)
val_temms = dict(
    type=temms_type,
    data_root=temms_root,
    data_prefix=dict(
        img_path="all_test/image",
        seg_map_path="all_test/label",
    ),
    pipeline=temms_test_pipeline,
)

test_temms = dict(
    type=temms_type,
    data_root=temms_root,
    data_prefix=dict(
        img_path="all_test/image",
        seg_map_path="all_test/label",
    ),
    pipeline=temms_test_pipeline,
)
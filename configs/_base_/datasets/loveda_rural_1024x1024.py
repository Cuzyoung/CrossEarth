loveda_rural_type = "LoveDADataset"
loveda_rural_root = "path"
loveda_rural_crop_size = (1024, 1024)
loveda_rural_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations"),
    dict(type="Resize", scale=(1024, 1024)),
    dict(type="RandomCrop", crop_size=loveda_rural_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
loveda_rural_val_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(1024, 1024), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations"),
    dict(type="PackSegInputs"),
]
loveda_rural_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(1024, 1024), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations",reduce_zero_label=False),
    dict(type="PackSegInputs"),
]
train_loveda_rural = dict(
    type=loveda_rural_type,
    data_root=loveda_rural_root,
    data_prefix=dict(
        img_path="Train/Rural/images_png",
        seg_map_path="Train/Rural/masks_png",
    ),
    pipeline=loveda_rural_train_pipeline,
)
val_loveda_rural = dict(
    type=loveda_rural_type,
    data_root=loveda_rural_root,
    data_prefix=dict(
        img_path="Val/Rural/images_png",
        seg_map_path="Val/Rural/masks_png",
    ),
    pipeline=loveda_rural_val_pipeline,
)
test_loveda_rural = dict(
    type="loveDADataset",
    data_root=loveda_rural_root,
    data_prefix=dict(
        img_path="Test/Rural/images_png",
        seg_map_path="Test/Rural/masks_png",
    ),
    pipeline=loveda_rural_test_pipeline,
)

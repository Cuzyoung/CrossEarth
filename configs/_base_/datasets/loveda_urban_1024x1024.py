loveda_urban_type = "LoveDADataset"
loveda_urban_root = "path"
loveda_urban_crop_size = (1024, 1024)
loveda_urban_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations"),
    dict(type="Resize", scale=(1024, 1024)),
    dict(type="RandomCrop", crop_size=loveda_urban_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
loveda_urban_val_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(1024, 1024), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations"),
    dict(type="PackSegInputs"),
]
loveda_urban_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(1024, 1024), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations",reduce_zero_label=False),
    dict(type="PackSegInputs"),
]
train_loveda_urban = dict(
    type=loveda_urban_type,
    data_root=loveda_urban_root,
    data_prefix=dict(
        img_path="Train/Urban/images_png",
        seg_map_path="Train/Urban/masks_png",
    ),
    pipeline=loveda_urban_train_pipeline,
)
val_loveda_urban = dict(
    type=loveda_urban_type,
    data_root=loveda_urban_root,
    data_prefix=dict(
        img_path="Val/Urban/images_png",
        seg_map_path="Val/Urban/masks_png",
    ),
    pipeline=loveda_urban_val_pipeline,
)
test_loveda_urban = dict(
    type="loveDADataset",
    data_root=loveda_urban_root,
    data_prefix=dict(
        img_path="Test/Urban/images_png",
        seg_map_path="Test/Urban/masks_png",
    ),
    pipeline=loveda_urban_test_pipeline,
)

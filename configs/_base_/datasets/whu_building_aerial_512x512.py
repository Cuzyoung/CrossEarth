whu_aerial_type = "WhuBuildingDataset"
whu_aerial_root = "path"
whu_aerial_crop_size = (512,512)
whu_aerial_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", reduce_zero_label=False),
    dict(type="Resize", scale=(512,512)),
    dict(type="RandomCrop", crop_size=whu_aerial_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
whu_aerial_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(512,512), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations",reduce_zero_label=False),
    dict(type="PackSegInputs"),
]
train_whu_aerial = dict(
    type=whu_aerial_type,
    data_root=whu_aerial_root,
    data_prefix=dict(
        img_path="train/image",
        seg_map_path="train/label2",
    ),
    pipeline=whu_aerial_train_pipeline,
)
val_whu_aerial = dict(
    type=whu_aerial_type,
    data_root=whu_aerial_root,
    data_prefix=dict(
        img_path="test/image",
        seg_map_path="test/label2",
    ),
    pipeline=whu_aerial_test_pipeline,
)
test_whu_aerial = dict(
    type=whu_aerial_type,
    data_root=whu_aerial_root,
    data_prefix=dict(
        img_path="test/image",
        seg_map_path="test/label2",
    ),
    pipeline=whu_aerial_test_pipeline,
)

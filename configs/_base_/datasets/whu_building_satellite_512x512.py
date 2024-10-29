whu_satellite_type = "WhuBuildingDataset"
whu_satellite_root = "path"
# whu_satellite_build_root ='/share/home/dq070/CoT/datasets/WHU_Building/Satellite/cropped_image/'
whu_satellite_crop_size = (512,512)
whu_satellite_train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations", reduce_zero_label=False),
    dict(type="Resize", scale=(512,512)),
    dict(type="RandomCrop", crop_size=whu_satellite_crop_size, cat_max_ratio=0.75),
    dict(type="RandomFlip", prob=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]
whu_satellite_test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="Resize", scale=(512,512), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type="LoadAnnotations",reduce_zero_label=False),
    dict(type="PackSegInputs"),
]
train_whu_satellite = dict(
    type=whu_satellite_type,
    data_root=whu_satellite_root,
    data_prefix=dict(
        img_path="train_all/image",
        seg_map_path="train_all/label",
    ),
    pipeline=whu_satellite_train_pipeline,
)
val_whu_satellite = dict(
    type=whu_satellite_type,
    data_root=whu_satellite_root,
    data_prefix=dict(
        img_path="test_all/image",
        seg_map_path="test_all/label",
    ),
    pipeline=whu_satellite_test_pipeline,
)
test_whu_satellite = dict(
    type=whu_satellite_type,
    data_root=whu_satellite_root,
    data_prefix=dict(
        img_path="test/image",
        seg_map_path="test/label",
    ),
    pipeline=whu_satellite_test_pipeline,
)

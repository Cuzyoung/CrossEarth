_base_ = [
    "./whu_building_aerial_512x512.py",
    "./whu_building_satellite_512x512.py",

]
train_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(type="InfiniteSampler", shuffle=True),
    dataset={{_base_.train_whu_aerial}},
)
val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type="DefaultSampler", shuffle=False),
    dataset=dict(
        type="ConcatDataset",
        datasets=[
            {{_base_.val_whu_satellite}},



        ],
    ),
)
test_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type="DefaultSampler", shuffle=False),
    dataset=dict(
        type="ConcatDataset",
        datasets=[
            {{_base_.test_whu_satellite}},

        ],
    ),
)
val_evaluator = dict(
    type="DGIoUMetric",
    iou_metrics=["mIoU"],
    dataset_keys=["Satellite/"],
    mean_used_keys=["Satellite/"],
)

test_evaluator = dict(
    type="IoUMetric",
    iou_metrics=["mIoU"],
    format_only=True,
    output_dir="./work_dirs/try",
)
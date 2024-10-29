_base_ = [
    "./loveda_rural_1024x1024.py",
    "./loveda_urban_1024x1024.py",


]
train_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(type="InfiniteSampler", shuffle=True),
    dataset={{_base_.train_loveda_rural}},
)
val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type="DefaultSampler", shuffle=False),
    dataset=dict(
        type="ConcatDataset",
        datasets=[
            {{_base_.val_loveda_urban}},
            {{_base_.val_loveda_rural}},


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
            {{_base_.val_loveda_urban}},

        ],
    ),
)
val_evaluator = dict(
    type="DGIoUMetric",
    iou_metrics=["mIoU"],
    dataset_keys=["Rural/", "Urban/"],
    mean_used_keys=["Rural/", "Urban/"],
)

test_evaluator = dict(
    type="IoUMetric",
    iou_metrics=["mIoU"],
    format_only=False,
    output_dir="./work_dirs/try",
)
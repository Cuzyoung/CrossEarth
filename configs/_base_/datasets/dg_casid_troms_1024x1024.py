_base_ = [
    "./subms_1024x1024.py",
    "./trorf_1024x1024.py",
    "./temms_1024x1024.py",
    "./troms_1024x1024.py",

]
train_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(type="InfiniteSampler", shuffle=True),
    dataset={{_base_.train_troms}},
)
val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type="DefaultSampler", shuffle=False),
    dataset=dict(
        type="ConcatDataset",
        datasets=[
            {{_base_.val_subms}},
            {{_base_.val_trorf}},
            {{_base_.val_temms}},
            {{_base_.val_troms}},

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
            {{_base_.val_subms}},

        ],
    ),
)
val_evaluator = dict(
    type="DGIoUMetric",
    iou_metrics=["mIoU"],
    dataset_keys=["SubMs/", "TroRf/", "TemMs/", "TroMs/"],
    mean_used_keys=["SubMs/", "TroRf/", "TemMs/", "TroMs/"],
)

test_evaluator = dict(
    type="IoUMetric",
    iou_metrics=["mIoU"],
    format_only=False,
    output_dir="./work_dirs/try",
)
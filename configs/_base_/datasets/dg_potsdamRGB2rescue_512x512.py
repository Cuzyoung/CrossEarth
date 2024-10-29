_base_ = [
    "./potsdamRGB_rescue_512x512.py",
    "./rescue_512x512.py",

]
train_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(type="InfiniteSampler", shuffle=True),
    dataset={{_base_.train_Potsdam_Rescue}},
)
val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type="DefaultSampler", shuffle=False),
    dataset=dict(
        type="ConcatDataset",
        datasets=[
            {{_base_.val_Rescue}},


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
            {{_base_.val_Rescue}},

        ],
    ),
)
val_evaluator = dict(
    type="DGIoUMetric",
    iou_metrics=["mIoU"],
    dataset_keys=["rescuenet/"],
    mean_used_keys=["rescuenet/"],
)

test_evaluator = dict(
    type="IoUMetric",
    iou_metrics=["mIoU"],
    format_only=False,
    output_dir="./work_dirs/try",
)
_base_ = [
    "./potsdam_IRRG_512x512.py",
    "./potsdam_RGB_512x512.py",
    "./vaihingen_IRRG_512x512.py",


]
train_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(type="InfiniteSampler", shuffle=True),
    dataset={{_base_.train_Potsdam_IRRG}},
)
val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type="DefaultSampler", shuffle=False),
    dataset=dict(
        type="ConcatDataset",
        datasets=[
            {{_base_.val_Potsdam_IRRG}},
            {{_base_.val_Potsdam_RGB}},
            {{_base_.val_Vaihingen}},


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
            {{_base_.val_Vaihingen}},
            # {{_base_.val_Potsdam_RGB}},

        ],
    ),
)
val_evaluator = dict(
    type="DGIoUMetric",
    iou_metrics=["mIoU"],
    dataset_keys=["potsdam_1-6/IRRG/", "potsdam_1-6/RGB/", "vaihingen_new/"],
    mean_used_keys=["potsdam_1-6/IRRG/", "potsdam_1-6/RGB/", "vaihingen_new/"],
)

test_evaluator = dict(
    type="IoUMetric",
    iou_metrics=["mIoU"],
    format_only=False,
    output_dir="./work_dirs/try",
)
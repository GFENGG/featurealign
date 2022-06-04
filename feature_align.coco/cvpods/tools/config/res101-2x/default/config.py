import os.path as osp

from cvpods.configs.fcos_config import FCOSConfig

_config_dict = dict(
    MODEL=dict(
        WEIGHTS="detectron2://ImageNetPretrained/MSRA/R-101.pkl",
        RESNETS=dict(DEPTH=101),
        FCOS=dict(
            PRIOR_PROB=0.02,
            NORM_REG_TARGETS=True,
            NMS_THRESH_TEST=0.6,
            BBOX_REG_WEIGHTS=(1.0, 1.0, 1.0, 1.0),
            FOCAL_LOSS_GAMMA=2.0,
            FOCAL_LOSS_ALPHA=0.25,
            IOU_LOSS_TYPE="giou",
            REG_WEIGHT=5.0,
        ),
    ),
    DATASETS=dict(
        TRAIN=("coco_2017_train",),
        TEST=("coco_2017_test-dev",), # coco_2017_val
    ),
    SOLVER=dict(
        IMS_PER_BATCH=16,
        IMS_PER_DEVICE=4,
        CHECKPOINT_PERIOD=10000,
        LR_SCHEDULER=dict(
            STEPS=(120000,160000),
            MAX_ITER=180000,
        ),
        OPTIMIZER=dict(
            BASE_LR=0.01,
        ),
    ),
    INPUT=dict(
        AUG=dict(
            TRAIN_PIPELINES=[
                ("ResizeShortestEdge", dict(
                    short_edge_length=(640, 672, 704, 736, 768, 800), max_size=1333, sample_style="choice")),
                ("RandomFlip", dict()),
            ],
            TEST_PIPELINES=[
                ("ResizeShortestEdge", dict(
                    short_edge_length=800, max_size=1333, sample_style="choice")),
            ],
        )
    ),
    TEST=dict(
        EVAL_PERIOD=10000,
    ),
    OUTPUT_DIR=osp.join(
        '/data/Outputs/model_logs/cvpods_playground',
        osp.split(osp.realpath(__file__))[0].split("playground/")[-1]),
)


class AutoAssignConfig(FCOSConfig):
    def __init__(self):
        super(AutoAssignConfig, self).__init__()
        self._register_configuration(_config_dict)


config = AutoAssignConfig()

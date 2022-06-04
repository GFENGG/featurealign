from cvpods.layers import ShapeSpec
from cvpods.modeling.backbone import Backbone
from cvpods.modeling.backbone.fpn import build_retinanet_resnet_fpn_backbone
from cvpods.modeling.anchor_generator import ShiftGenerator

from feature_align import FeatureAlign


def build_backbone(cfg, input_shape=None):
    """
    Build a backbone from `cfg.MODEL.BACKBONE.NAME`.

    Returns:
        an instance of :class:`Backbone`
    """
    if input_shape is None:
        input_shape = ShapeSpec(channels=len(cfg.MODEL.PIXEL_MEAN))

    backbone = build_retinanet_resnet_fpn_backbone(cfg, input_shape)
    assert isinstance(backbone, Backbone)
    return backbone


def build_shift_generator(cfg, input_shape):
    """
    Build FCOS-like shifts generator

    Returns:
        an instance of :class:`ShiftGenerator`
    """
    return ShiftGenerator(cfg, input_shape)


def build_model(cfg):
    """
    Build AutoAssign

    Returns:
        an instance of :class:`AutoAssign`
    """

    cfg.build_backbone = build_backbone
    cfg.build_shift_generator = build_shift_generator

    model = FeatureAlign(cfg)
    return model

# Features Alignment In Anchor-Free Object Detection

# ![pipeline](./pipeline.png)

This is a PyTorch implementation version.

## Get Started

1. install [cvpods](https://github.com/Megvii-BaseDetection/cvpods) following the instructions

```shell
# Install cvpods
git clone https://github.com/Megvii-BaseDetection/cvpods
cd cvpods 
## build cvpods (requires GPU)
pip install -r requirements.txt
python setup.py build develop
## preprare data path
mkdir datasets
ln -s /path/to/your/coco/dataset datasets/coco
```

2. run the project

```shell
cd feature_align.coco

# train
pods_train --num-gpus 4

#train from exist weight, then the code will retrained from the 'last_checkpoint'
pods_train --num-gpus 4 --resume

# test
pods_test --num-gpus 4
# test with provided weights
pods_test --num-gpus 4 MODEL.WEIGHTS /path/to/your/model.pth
```



## Results

| Model | Multi-scale training | Multi-scale testing | Testing time / im | AP (minival) | Link |
|:--- |:--------------------:|:--------------------:|:-----------------:|:-------:|:---:|
| [AutoAssign_Res50_FPN_1x](https://github.com/poodarchu/AutoAssign/blob/master/auto_assign.res50.fpn.coco.800size.1x/config.py) | No | No | 53ms | 40.5 | [download](https://drive.google.com/file/d/11mV53SJUIpCdWj-Wbfi_fdmDz96ekb-Z/view?usp=sharing)

##Acknowledgement
This repo is developed based on cvpods and AutoAssign. Please check [cvpods](https://github.com/Megvii-BaseDetection/cvpods) and [AutoAssign](https://github.com/Megvii-BaseDetection/AutoAssign) for more details and features.

## License
This repo is released under the Apache 2.0 license. Please see the LICENSE file for more information.


# Copyright 2021 MosaicML. All Rights Reserved.

"""A ResNet model family adapted for CIFAR10 image sizes.

See the :doc:`Model Card </model_cards/cifar_resnet>` for more details.
"""

from composer.models.resnet_cifar.model import ComposerResNetCIFAR as ComposerResNetCIFAR
from composer.models.resnet_cifar.resnet_cifar_hparams import ResNetCIFARHparams as ResNetCIFARHparams

__all__ = ["ComposerResNetCIFAR", "ResNetCIFARHparams"]

_metadata = {
    'resnet9': {
        '_task': 'Image Classification',
        '_dataset': 'CIFAR10',
        '_name': 'ResNet9',
        '_quality': 'tbd',
        '_metric': 'Top-1 Accuracy',
        '_ttt': 'tbd',
        '_hparams': 'resnet9_cifar10.yaml'
    },
    'resnet20': {
        '_task': 'Image Classification',
        '_dataset': 'CIFAR10',
        '_name': 'ResNet20',
        '_quality': 'tbd',
        '_metric': 'Top-1 Accuracy',
        '_ttt': 'tbd',
        '_hparams': 'resnet20_cifar10.yaml'
    },
    'resnet56': {
        '_task': 'Image Classification',
        '_dataset': 'CIFAR10',
        '_name': 'ResNet56',
        '_quality': '93.1',
        '_metric': 'Top-1 Accuracy',
        '_ttt': '35m',
        '_hparams': 'resnet56_cifar10.yaml'
    }
}

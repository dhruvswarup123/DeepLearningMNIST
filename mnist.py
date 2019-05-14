import torch
import torchvision as tv
import torchvision.transforms as tr

train_set = tv.datasets.MNIST(
    root = './data/MNIST'
    ,train=True
    ,download=True
    ,transform=tr.Compose([
        tr.ToTensor()
    ])
)
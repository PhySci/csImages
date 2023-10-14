import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image
from matplotlib import pyplot as plt

import torchvision.transforms as transforms
import torchvision.models as models

import copy


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.set_default_device(device)

imsize = 512 if torch.cuda.is_available() else 128

loader = transforms.Compose([
    transforms.Resize(imsize),
    transforms.ToTensor()]
)

def image_loader(image_name):
    image = Image.open(image_name)
    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)

style_img = image_loader("./img/picasso.jpg")
content_img = image_loader("./img/dancing.jpg")

assert style_img.size() == content_img.size(), "Image should be of the same size"

class ContentLoss(nn.Module):

    def __init__(self, target):
        super(ContentLoss, self).__init__()
        self._target = target.detach()

    def forward(self, input):
        self.loss = F.mse_loss(input, self._target)
        return input



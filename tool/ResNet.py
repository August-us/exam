import torch
from torch import nn
import torchvision
import numpy as np


__all__ = ['ResNet50','ResNet101','ResNet152']

def Conv1(in_channels, out_channels, stride=2):
    return nn.Sequential(
        nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=7, stride=stride, padding=3, bias=False),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(inplace=True),
        nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
    )

class Bottleneck(nn.Module):
    def __init__(self, in_channels, channels, stride=1, downsampling=False, expansion=4):
        super(Bottleneck, self).__init__()
        self.expansion = expansion
        self.downsampling = downsampling

        self.bottleneck = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=channels, kernel_size=1, stride=1, bias=False),
            nn.BatchNorm2d(channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=channels, out_channels=channels, kernel_size=3, stride=stride, padding=1, bias=False),
            nn.BatchNorm2d(channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=channels, out_channels=channels*expansion,kernel_size=1,stride=1,bias=False),
            nn.BatchNorm2d(channels*expansion),
        )

        if self.downsampling:
            self.downsamp = nn.Sequential(
                nn.Conv2d(in_channels=in_channels, out_channels=channels*expansion, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(channels*expansion)
            )
        self.fc = nn.ReLU(inplace=True)

    def forward(self, x):
        residual = x
        out = self.bottleneck(x)

        if self.downsampling:
            residual = self.downsamp(x)

        out += residual
        out = self.fc(out)
        return out


class ResNet(nn.Module):
    def __init__(self, blocks, num_classes=1000, expansion=4):
        super(ResNet, self).__init__()
        self.expansion = expansion
        # self.num_classes = num_classes

        self.conv1 = Conv1(in_channels=3, out_channels=64)

        self.layer1 = self.make_layer(in_channels=64,  channels=64,  block=blocks[0], stride=1)
        self.layer2 = self.make_layer(in_channels=256, channels=128, block=blocks[1], stride=2)
        self.layer3 = self.make_layer(in_channels=512, channels=256, block=blocks[2], stride=2)
        self.layer4 = self.make_layer(in_channels=1024,channels=512, block=blocks[3], stride=2)

        self.avgpool = nn.AvgPool2d(7, stride=1)
        self.fc = nn.Linear(2048, num_classes)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def make_layer(self, in_channels, channels, block, stride):
        layers = [Bottleneck(in_channels, channels,stride, downsampling=True)]
        layers += [Bottleneck(channels * self.expansion, channels) for i in range(1,block)]
        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x


def ResNet50(num_classes=1000):
    return ResNet([3, 4, 6, 3], num_classes)

def ResNet101(num_classes=1000):
    return ResNet([3, 4, 23, 3], num_classes)

def ResNet152(num_classes=1000):
    return ResNet([3, 8, 36, 3], num_classes)


if __name__ == '__main__':
    torch.manual_seed(5)
    model = ResNet50()
    # model = torchvision.models.resnet50()
    print(model)

    input = torch.randn(1, 3, 224, 224)
    out = model(input)
    print(out)
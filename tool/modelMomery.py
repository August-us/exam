from functools import reduce
import numpy as np
import torchvision
from torch import nn
import torch


def modelsize(model: nn.Module, input:torch.Tensor, type_size=4):
    '''
    模型显存占用监测函数
    :param model: 输入的模型
    :param input: 实际中需要输入的Tensor变量
    :param type_size: 默认为 4, int类型，float32
    :return:
    '''
    para = sum([np.prod(list(p.size())) for p in model.parameters()])
    print('Model {} : params: {:4f}M'.format(model._get_name(), para * type_size / 1000 / 1000))

    input_ = input.clone()
    input_.requires_grad_(requires_grad=False)

    mods = list(model.modules())
    out_sizes = []

    for i in range(1,len(mods)):
        m = mods[i]
        print(m)
        if isinstance(m, nn.ReLU):
            if m.inplace:
                continue  # ReLU  inplace不增加参数
        out = m(input_)
        out_sizes.append(np.array(out_sizes))
        input_ = out

    total_nums = reduce(lambda x,y:x+np.prod(y),0 ,out_sizes)
    print('Model {} : intermedite variables: {:3f} M (without backward)'
          .format(model._get_name(), total_nums * type_size / 1000 / 1000))
    print('Model {} : intermedite variables: {:3f} M (with backward)'
          .format(model._get_name(), total_nums * type_size * 2 / 1000 / 1000))


# 模型显存占用监测函数
# model：输入的模型
# input：实际中需要输入的Tensor变量
# type_size 默认为 4 默认类型为 float32

def modelsize(model, input, type_size=4):
    para = sum([np.prod(list(p.size())) for p in model.parameters()])
    print('Model {} : params: {:4f}M'.format(model._get_name(), para * type_size / 1000 / 1000))

    input_ = input.clone()
    input_.requires_grad_(requires_grad=False)

    mods = list(model.modules())
    out_sizes = []

    for i in range(1, len(mods)):
        m = mods[i]
        if isinstance(m, nn.ReLU):
            if m.inplace:
                continue
        out = m(input_)
        out_sizes.append(np.array(out.size()))
        input_ = out

    total_nums = 0
    for i in range(len(out_sizes)):
        s = out_sizes[i]
        nums = np.prod(np.array(s))
        total_nums += nums

    print('Model {} : intermedite variables: {:3f} M (without backward)'
          .format(model._get_name(), total_nums * type_size / 1000 / 1000))
    print('Model {} : intermedite variables: {:3f} M (with backward)'
          .format(model._get_name(), total_nums * type_size * 2 / 1000 / 1000))
model = torchvision.models.VGG(224)
modelsize(model, torch.ones((1,3,224,224)))

import numpy as np
import torch
from torch import nn, optim
import torch.nn.functional as F

a=torch.rand(4,3,28,28)
a[0].shape
a[0,2,1].shape
a[:3,:1,:,:].shape
a[:3,-2:,:,:].shape#反向索引
a.index_select(2,torch.arange(15)).shape#选择dim=2中的0→14
a[...].shape
a[:,:1,...].shape
a[:,1,...].shape

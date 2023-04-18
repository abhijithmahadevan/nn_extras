import torch
import torch.nn as nn
class GlobalAveragePooling(nn.Module):
  def __init__(self):
    super(GlobalAveragePooling, self).__init__()
    
  def forward(self, input):
    output = torch.mean(input, dim = 1)
    return output
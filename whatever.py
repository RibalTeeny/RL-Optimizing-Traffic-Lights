import torch

lala=torch.rand((2000,9))
print(torch.max(lala, dim=1).values.shape)
import torch
from torch.utils import data

import warnings
warnings.filterwarnings('ignore')

class TwitterDataset(data.Dataset):
    def __init__(self, x, y):
        self.data = x
        self.label = y
    def __getitem__(self, idx):
        if self.label is None:
            return self.data[idx]
        return self.data[idx], self.label[idx]
    def __len__(self):
        return len(self.data)

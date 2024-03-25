import torch.nn as nn

from models import register


@register('mlp')
class MLP(nn.Module):

    def __init__(self, in_dim, out_dim, hidden_list):
        super().__init__()
        layers = []
        self.out_dim=out_dim
        lastv = in_dim
        for hidden in hidden_list:
            layers.append(nn.Linear(lastv, hidden))
            layers.append(nn.ReLU())
            lastv = hidden
        layers.append(nn.Linear(lastv, out_dim))
        self.layers = nn.Sequential(*layers)

    def forward(self, x):
        shape = x.shape[:-1]
        x = self.layers(x.view(-1, x.shape[-1]))
        return x.view(*shape, -1)
    
    
    
@register('mlp_1dconv')
class MLP(nn.Module):

    def __init__(self, in_dim, out_dim, hidden_list):
        super().__init__()
        layers = []
        lastv = in_dim
        self.out_dim=out_dim
        for hidden in hidden_list:
            layers.append(nn.Conv2d(lastv, hidden,1,padding=0))
            layers.append(nn.ReLU())
            lastv = hidden
        layers.append(nn.Conv2d(lastv, out_dim,1,padding=0))
        self.layers = nn.Sequential(*layers)

    def forward(self, x):
#         shape = x.shape[:-1]
        x = self.layers(x)#.view(-1, x.shape[-1]))
        return x#.view(*shape, -1)


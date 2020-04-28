import torch
from torch import nn

class LSTM(nn.Module):
    def __init__(self, in_features, hidden_size, num_layers, out_features, drop_prob):
        super(LSTM,self).__init__()
        
         #Model parameters
        self.in_features = in_features
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.out_features = out_features
        self.drop_prob = drop_prob
        
        #LSTM node sequence
        self.lstm = nn.LSTM(input_size = self.in_features, hidden_size = self.hidden_size, batch_first=True)
        
        #Dropout layer - trims network size to avoid overfitting
        self.dropout = nn.Dropout(p=self.drop_prob)
        
        #Linear layer
        self.linear = nn.Linear(self.hidden_size, self.out_features)
        
        #Softmax- applies softmax to the result to convert to probs
        self.soft_max = nn.Softmax(dim=2)
    
    def init_hidden(self,x):
        return (torch.zeros((self.num_layers, x.size(0), self.hidden_size),requires_grad=True), 
               torch.zeros((self.num_layers, x.size(0), self.hidden_size),requires_grad=True))
    
    def forward(self, x):
        
        #Init hidden state and c state
        hidden_init = self.init_hidden(x)
        
        val, (hidden, _) = self.lstm(x, hidden_init)
        
        out = self.dropout(val)
        out = self.linear(out)
        out = self.soft_max(out)
        
        return out
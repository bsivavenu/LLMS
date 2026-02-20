# import numpy 
from transformers import pipeline

import torch

# trasnltr = pipeline(task = 'trasnlation', model = 'facebook/nllb-200-distilled-600M',torch_dtype = torch.bfloat16)
translator = pipeline(task="translation",
                      model="facebook/nllb-200-distilled-600M",
                      torch_dtype=torch.bfloat16) 


tqdm是一个进度条的库

from time import sleep
from tqdm import tqdm

for i in tqdm(range(1000)):
    sleep(0.01)



# 100%|██████████| 1000/1000 [00:15<00:00, 64.13it/s]


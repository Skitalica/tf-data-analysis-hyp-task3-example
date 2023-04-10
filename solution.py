import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

chat_id = 277684942 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    return stats.ttest_ind(x, y)[1] < 0.05 # Ваш ответ, True или False
    

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import permutation_test

chat_id = 277684942 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    _, p_value = ttest_ind(x, y, equal_var=False, permutations=5000, alternative='less')
    alpha = 0.05
    return p_value < alpha

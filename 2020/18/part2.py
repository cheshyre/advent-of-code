import os

import weird_math


cur_dir = os.path.dirname(os.path.abspath(__file__))

sum_val = 0
with open(f"{cur_dir}/input") as f:
    for line in f:
        sum_val += weird_math.evaluate_expr_inv(weird_math.tokenize_str_expression(line.strip()))
        
print(sum_val)

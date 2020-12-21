def evaluate_expr_wo_parens_inv(expr):
    tokens = list(expr)
    new_tokens = []
    while "+" in tokens:
        i = 0
        while i < len(tokens):
            if tokens[i] == "+":
                val1 = int(new_tokens[-1])
                val2 = int(tokens[i + 1])
                new_tokens[-1] = str(val1 + val2)
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        tokens = new_tokens
    
    final_result = int(tokens[0])
    for x in tokens[1:]:
        if x != "*":
            final_result *= int(x)
    
    return final_result


def evaluate_expr_wo_parens(expr):
    
    tokens = list(expr)
    
    final_result = int(tokens[0])
    i = 1
    while i < len(tokens):
        if tokens[i] == "+":
            final_result += int(tokens[i + 1])
        elif tokens[i] == "*":
            final_result *= int(tokens[i + 1])
        else:
            print(f"Unexpected token {tokens[i]}")
            exit(-1)
        i += 2
    
    return final_result


def find_r_paren(expr):
    l_paren_count = 0
    r_paren_count = 0
    for i, x in enumerate(expr, start = 1):
        if x == "(":
            l_paren_count += 1
        if x == ")":
            r_paren_count += 1
        if r_paren_count > l_paren_count:
            return i
    return -1


def evaluate_expr(expr):
    tokens = list(expr)
    while "(" in tokens:
        new_tokens = []
        l_paren_index = tokens.index("(")
        r_paren_index = find_r_paren(tokens[l_paren_index + 1:]) + l_paren_index + 1
        new_tokens += tokens[:l_paren_index]
        new_tokens += [evaluate_expr(tokens[l_paren_index + 1:r_paren_index - 1])]
        new_tokens += tokens[r_paren_index:]
        tokens = new_tokens
        
    return evaluate_expr_wo_parens(tokens)


def evaluate_expr_inv(expr):
    tokens = list(expr)
    while "(" in tokens:
        new_tokens = []
        l_paren_index = tokens.index("(")
        r_paren_index = find_r_paren(tokens[l_paren_index + 1:]) + l_paren_index + 1
        new_tokens += tokens[:l_paren_index]
        new_tokens += [evaluate_expr_inv(tokens[l_paren_index + 1:r_paren_index - 1])]
        new_tokens += tokens[r_paren_index:]
        tokens = new_tokens
        
    return evaluate_expr_wo_parens_inv(tokens)


def tokenize_str_expression(str_expr):
    return str_expr.replace("(", "( ").replace(")", " )").split()

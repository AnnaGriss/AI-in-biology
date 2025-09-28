def simple_probability(m,n):
    p=m/n
    return p 

def logical_or(m, k, n):
    p=m/n + k/n
    return p

def logical_and(m, n, k, l):
    p=(m/k) * (n/k)
    return p

def expected_value(values, probabilities):
    exp = 0
    for i in range(len(values)):
        exp += values[i]*probabilities[i]
    return exp 
    
def conditional_probability(values):
    count_a = 0  
    count_ab = 0  
    
    for pair in values:
        first, second = pair
        if first == 1:
            count_a += 1
            if second == 1:
                count_ab += 1
    
    if count_a == 0:
        return 0
    
    p=count_ab / count_a

    return p

def bayesian_probability(a, b, ba):
    if b == 0:
        return 0
    p=(ba * a) / b
    return p


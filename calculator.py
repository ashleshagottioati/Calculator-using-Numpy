#import numpy as np

#def calculate(numbers):
#    if len(numbers) != 9:
#        raise ValueError("List must contain nine numbers.")
#    data = np.reshape(np.array(numbers),(3,3))
#    calculations = {}
#    calculations['mean'] = [np.mean(data, axis=0).tolist(), np.mean(data, axis=1).tolist(), np.mean(data.flatten()).tolist()]
#    calculations['variance'] = [np.var(data, axis=0).tolist(), np.var(data, axis=1).tolist(), np.var(data.flatten()).tolist()]
#    calculations['standard deviation'] = [np.std(data, axis=0).tolist(), np.std(data, axis=1).tolist(), np.std(data.flatten()).tolist()]
#    calculations['max'] = [np.max(data, axis=0).tolist(), np.max(data, axis=1).tolist(), np.max(data.flatten()).tolist()]
#    calculations['min'] = [np.min(data, axis=0).tolist(), np.min(data, axis=1).tolist(), np.min(data.flatten()).tolist()]
#    calculations['sum'] = [np.sum(data, axis=0).tolist(), np.sum(data, axis=1).tolist(), np.sum(data.flatten()).tolist()]
#    return calculations
#print(calculate([1, 2, 3, 4, 5, 6, 7, 8, 9]))#


import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    data = np.reshape(np.array(numbers), (3, 3))
    calculations = {
        'mean': [np.mean(data, axis=0), np.mean(data, axis=1), np.mean(data)],
        'variance': [np.var(data, axis=0), np.var(data, axis=1), np.var(data)],
        'standard deviation': [np.std(data, axis=0), np.std(data, axis=1), np.std(data)],
        'max': [np.max(data, axis=0), np.max(data, axis=1), np.max(data)],
        'min': [np.min(data, axis=0), np.min(data, axis=1), np.min(data)],
        'sum': [np.sum(data, axis=0), np.sum(data, axis=1), np.sum(data)],
    }

    for key, value in calculations.items():
        print(f"{key.title()}:")
        print(f"  Column-wise: {value[0].tolist()}")
        print(f"  Row-wise: {value[1].tolist()}")
        print(f"  Overall: {value[2]}")
        print()

    return {k: [v[0].tolist(), v[1].tolist(), v[2] if isinstance(v[2], (int, float)) else v[2].tolist()] for k, v in calculations.items()}

# Example usage
calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])


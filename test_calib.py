import numpy as np
import sys

import matplotlib.pyplot as plt

file_path = sys.argv[1]
# file_path = "calib_set_120_160.npy"
# file_path = "tensor_ints_0_255.npy"
# file_path = "tensor_floats_0_1.npy"
# file_path = "tensor_normal_0_1.npy"

def iterate_tensors_in_npy(file_path):
    data = np.load(file_path)

    if isinstance(data, np.ndarray):
        size_of_first_dim = data[0].shape
        for tensor in data:
            if tensor.shape != size_of_first_dim:
                raise ValueError("The loaded data contains tensors of different shapes.")
            yield tensor
    else:
        raise ValueError("The loaded data is not a NumPy array.")
    


def check_if_tensor_is_all_zeros(tensor):
    for i in tensor.flatten():
        if i != 0:
            return False
    return True

def plot_tensor_values(tensor):
    plt.hist(tensor.flatten(), bins=100, range=(0, 1), alpha=0.7)
    


i = 0
for tensor in iterate_tensors_in_npy(file_path):
    if check_if_tensor_is_all_zeros(tensor):
        raise ValueError(f"tensor num: {i} is all zeros")
    i += 1
    if i == 2:
        break


def open_npy(file_path):
    data = np.load(file_path)
    return data

counts, bins = np.histogram(open_npy(file_path).flatten())
plt.stairs(counts, bins)
plt.show()


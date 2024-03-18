# NPY File Tensor Processor

This script processes tensors stored in a `.npy` file, performing various operations such as validation, analysis, and visualization of tensor data.

## Features

- **Tensor Validation**: Checks if all tensors in the file are of the same shape and if any tensor is completely filled with zeros.
- **Data Visualization**: Plots the values of tensors, showing the distribution of the data within.

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- NumPy: For handling `.npy` files and tensor operations.
- Matplotlib: For data visualization.

You can install the required libraries using pip:

```bash
pip install numpy matplotlib
```

# Usage
The script can be run from the command line, with the .npy file path as an argument:

```bash
python script_name.py path_to_your_npy_file.npy
```
Alternatively, you can directly modify the file_path variable within the script to point to your .npy file and run the script without command-line arguments.

## Example .npy Files
* calib_set_120_160.npy: Calibration data set.
* tensor_ints_0_255.npy: Tensor with integer values ranging from 0 to 255.
* tensor_floats_0_1.npy: Tensor with floating-point values ranging from 0.0 to 1.0.
* tensor_normal_0_1.npy: Tensor with normally distributed floating-point values around a mean of 0.5.
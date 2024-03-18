import numpy as np

def create_and_save_normal_tensors():
    # Define the tensor shape
    tensor_shape = (100, 20, 300, 3)

    # Generate a tensor with normal distribution, mean=128, std=30, clipped to 0-255
    tensor_normal_0_255 = np.random.randn(*tensor_shape) * 30 + 128
    tensor_normal_0_255 = np.clip(tensor_normal_0_255, 0, 255).astype(np.uint8)

    # Generate a tensor with normal distribution, mean=0.5, std=0.15, clipped to 0.0-1.0
    tensor_normal_0_1 = np.random.randn(*tensor_shape) * 0.15 + 0.5
    tensor_normal_0_1 = np.clip(tensor_normal_0_1, 0.0, 1.0)

    # Save the tensors to .npy files
    np.save('tensor_normal_0_255.npy', tensor_normal_0_255)
    np.save('tensor_normal_0_1.npy', tensor_normal_0_1)

    return 'Normal distribution tensors saved successfully.'

# Call the function to create and save the tensors
create_and_save_normal_tensors()

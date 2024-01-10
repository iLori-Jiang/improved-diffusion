import numpy as np
from PIL import Image
import argparse
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Save images from an NPZ file as JPGs.")
    parser.add_argument("npz_path", help="Path to the .npz file containing images")

    args = parser.parse_args()

    save_path = os.path.dirname(args.npz_path)

    # Load the .npz file
    data = np.load(args.npz_path)
    images = data['arr_0']  # 'arr_0' is a common key, but this might vary

    print(images.shape)

    # Iterate and save each image
    for i, img in enumerate(images):
        # Convert the numpy array to a PIL image
        image = Image.fromarray(img.astype('uint8'), 'RGB')
        
        # Save the image
        image_file_path = os.path.join(save_path, f'image_{i}.jpg')
        image.save(image_file_path)

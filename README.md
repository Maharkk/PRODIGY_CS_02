# Image Encryption

## Overview

The Image Encryption project is designed to provide a simple yet effective method for encrypting and decrypting image files using pixel manipulation. This tool uses a straightforward XOR-based algorithm to ensure image data remains confidential and protected from unauthorized access. The project handles PNG format images to avoid issues related to lossy compression found in JPEGs.

## Features

- **Simple Encryption and Decryption**: Uses an XOR-based algorithm to encrypt and decrypt image data.
- **PNG Format Support**: Uses PNG format to avoid compression artifacts and preserve image quality.
- **Pixel Manipulation**: Provides debugging information to verify pixel values during encryption and decryption.

## Installation

To get started with the project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/image-encryption.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd image-encryption
    ```

3. **Install Dependencies**:
    Ensure you have Python installed. Install the necessary packages using:
    ```bash
    pip install Pillow numpy
    ```

## Usage

1. **Run the Script**:
    ```bash
    python Image_Encryption.py
    ```

2. **Follow the Prompts**:

   - **Encryption**:
     - Enter the path of the image you want to encrypt (preferably in PNG format).
     - Enter a key for encryption.
     - Specify the output path for the encrypted image (e.g., `encrypted_image.png`).

   - **Decryption**:
     - Enter the path of the encrypted image (e.g., `encrypted_image.png`).
     - Enter the key for decryption.
     - Specify the output path for the decrypted image (e.g., `decrypted_image.png`).
     - Optionally, provide the path to the original image to compare the decrypted image with the original.

## Technical Challenges and Solutions

### Pixel Range and Comparison Issue

**Issue**: Initial implementations had trouble with pixel range and comparison, leading to inaccuracies in the encryption and decryption process.

**Solution**:
- Adjusted the pixel comparison logic to handle a broader range of pixel values.
- Implemented a more precise algorithm to ensure accurate encryption and decryption.

### JPG Format Limitation

**Issue**: JPG format caused issues due to its lossy compression, affecting pixel accuracy.

**Solution**:
- Switched to PNG format to preserve image quality and avoid compression artifacts.
- Updated the code to handle PNG files effectively.


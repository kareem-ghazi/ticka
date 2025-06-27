import cv2
import numpy as np
import argparse
import os

class Adjuster:
    def calculate_brightness_and_contrast(self, image):
        """Calculate the brightness and contrast of an image.
        Brightness is the mean pixel intensity, and contrast is the standard deviation of pixel intensity.
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        brightness = np.mean(gray)
        contrast = np.std(gray)
        return brightness, contrast

    def adjust_brightness_and_contrast(self, image, target_brightness, target_contrast):
        """Adjust the brightness and contrast of an image to match target values."""
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        current_brightness, current_contrast = self.calculate_brightness_and_contrast(image)

        # Calculate scaling factor and offset
        scaling_factor = target_contrast / current_contrast if current_contrast != 0 else 1
        offset = target_brightness - scaling_factor * current_brightness

        # Adjust brightness and contrast
        adjusted_image = cv2.convertScaleAbs(image, alpha=scaling_factor, beta=offset)
        return adjusted_image

    def process(self, path_test_image):
        """Main function to adjust brightness and contrast of an image based on a standard image."""
        path_standard_image = path_test_image # TODO: Change this placeholder.

        # Ensure the output directory exists
        dir_clean_image = "../output"
        os.makedirs(dir_clean_image, exist_ok=True)

        # Load the images
        standard_image = cv2.imread(path_standard_image)
        if standard_image is None:
            print(f"Error: Could not load the standard image from {path_standard_image}. Check the file path.")
            return

        image_to_adjust = cv2.imread(path_test_image)
        if image_to_adjust is None:
            print(f"Error: Could not load the test image from {path_test_image}. Check the file path.")
            return

        # Calculate brightness and contrast of the standard image
        standard_brightness, standard_contrast = self.calculate_brightness_and_contrast(standard_image)

        # Adjust the test image
        adjusted_image = self.adjust_brightness_and_contrast(image_to_adjust, standard_brightness, standard_contrast)

        # # Save the adjusted image
        # file_image = os.path.basename(path_test_image)
        # output_path = os.path.join(dir_clean_image, file_image)
        # cv2.imwrite(output_path, adjusted_image)

        # print(f"Adjusted image saved at: {output_path}")
        
        return adjusted_image

if __name__ == "__main__":
    adjuster = Adjuster()
    image = adjuster.process("C:\\Users\\kareemghazi\\Desktop\\ticka\\src\\input\\Screenshot (82) 2.png")
    
    if image is not None:
        cv2.imshow("1", image)
        cv2.waitKey()
import numpy as np
import cv2
import argparse
import os

# Threshold for determining whether an image is blurry
THRESHOLD = 250

# URL reference for blur detection algorithm
# https://pyimagesearch.com/2015/09/07/blur-detection-with-opencv/

class BlurRemover:
    def variance_of_laplacian(self, image):
        """Calculate the variance of the Laplacian to measure focus."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Laplacian(gray, cv2.CV_64F).var()

    def unblur(self, image):
        """Sharpen the image using a custom kernel."""
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(image, -1, kernel)

    def process(self, path_blur_image):
        """Main function to iteratively unblur an image until it meets the threshold."""

        # # Ensure the output directory exists
        # dir_unblurred_image = "..\\output"
        # os.makedirs(dir_unblurred_image, exist_ok=True)

        # Load the image
        image = cv2.imread(path_blur_image)
        if image is None:
            print(f"Error: Could not load the image from {path_blur_image}. Check the file path.")
            return None

        # Calculate the initial focus measure
        fm = self.variance_of_laplacian(image)

        # Iteratively unblur the image until it meets the threshold
        iterations = 0
        while fm < THRESHOLD:
            print(fm)
            image = self.unblur(image)
            iterations += 1
            fm = self.variance_of_laplacian(image)

        # # Save the unblurred image
        # file_image = os.path.basename(path_blur_image)
        # path_unblurred_image = os.path.join(dir_unblurred_image, file_image)
        # cv2.imwrite(path_unblurred_image, image)

        # print(f"Unblurring completed in {iterations} iterations. Final focus measure: {fm}")
        # print(f"Unblurred image saved at: {path_unblurred_image}")
        
        return image

if __name__ == "__main__":
    blurremover = BlurRemover()
    image = blurremover.process("C:\\Users\\kareemghazi\\Desktop\\ticka\\src\\input\\Screenshot (82) 2.png")
    
    if image is not None:
        cv2.imshow("1", image)
        cv2.waitKey()
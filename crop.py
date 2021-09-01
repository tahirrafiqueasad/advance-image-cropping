""" 
Author:		 Muhammad Tahir Rafique
Date:		 2021-08-31 15:11:32
Description: Provide a function to crop the even crop section is not present inside of image.
"""
import cv2
import numpy as np
import argparse

def advance_image_cropping(image, bounding_box, background=(0, 0, 0)):
    """Crop the image."""
    # 1. GETTING CROP CORDINATES
    xmin, ymin, xmax, ymax = bounding_box

    # 2. GETTING HEIGHT AND WIDTH
    crop_height, crop_width = ymax - ymin, xmax - xmin
    image_shape = image.shape
    image_height, image_width = image_shape[0], image_shape[1]
    img_xmin, img_ymin, img_xmax, img_ymax = 0, 0, image_width, image_height
    try:
        image_depth = image_shape[2]
    except:
        image_depth = 0
    
    # 3. MAKING EMPTY CROP
    if image_depth == 0:
        crop = np.ones((crop_height, crop_width), dtype=np.uint8) * background[0]
    else:
        crop = np.ones((crop_height, crop_width, image_depth), dtype=np.uint8) * background

    # 4. EXCEPTION FOR COMPLETE OUTSIDE CROP
    if (ymin > img_ymax) or (xmin > img_xmax) or (ymax < img_ymin) or (xmax < img_xmin):
        return crop
    
    # 5. DEFINING OFFSET
    ofs_xmin = 0
    ofs_ymin = 0
    ofs_xmax = 0
    ofs_ymax = 0

    # 6. CORRECTING COORDINATE
    if xmin < img_xmin:
        ofs_xmin = img_xmin - xmin
        xmin = img_xmin
    if ymin < img_xmin:
        ofs_ymin = img_ymin - ymin
        ymin = img_ymin
    if xmax > img_xmax:
        ofs_xmax = img_xmax - xmax
        xmax = img_xmax
    if ymax > img_ymax:
        ofs_ymax = img_ymax - ymax
        ymax = img_ymax
    
    # 7. PLACING CROP
    img_crop = image[ymin:ymax, xmin:xmax]
    crop[ofs_ymin:ofs_ymax+crop_height, ofs_xmin:ofs_xmax+crop_width] = img_crop

    return crop



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Crop the image even the crop bounding box outside the image.')

    parser.add_argument(
        '-i', '--input',
        type=str,
        help='path to image file.',
        required=True
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        help='path to crop file.',
        required=True
    )

    parser.add_argument(
        '-c', '--coordinate',
        nargs="+",
        help='list of cordinates eg: xmin ymin xmax ymax',
        required=True,
        type=int
    )

    parser.add_argument(
        '-b', '--background',
        nargs="+",
        help='list of channels eg: B, G, R',
        default=(0, 0, 0),
        type=int
    )

    args = parser.parse_args()

    # READING IMAGE
    image = cv2.imread(args.input)

    # GETTING CROP
    crop = advance_image_cropping(image, args.coordinate, args.background)
    
    # WRITING IMAGE
    cv2.imwrite(args.output, crop)

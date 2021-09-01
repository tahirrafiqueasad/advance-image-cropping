# advance-image-cropping
Provide a script to crop the image even the crop bounding box outside the image.

eg:

![plot](./test.png)

## Prerequisites

Following modules are needed:

| Modules              | Installation command                     |
| -------------------- | ---------------------------------------- |
| cv2      | pip install opencv-python |
| numpy           | pip install numpy           |

## Procedure

1. Use the following command to crop the image.

   ```bash
   python crop.py -i x -o y -c xmin, ymin, xmax, ymax -b B G R
   ```

   where:

   | Variables | Description               | Example           |
   | --------- | ------------------------- | ----------------- |
   | x         | Path to image file.       | path/to/image.png |
   | y         | Path to crop image file.  | path/to/crop.png  |
   | xmin      | Top left x-coordinate     | -50               |
   | ymin      | Top left y-coordinate     | -30               |
   | xmax      | Bottom right x-coordinate | 100               |
   | ymax      | Bottom right y-coordinate | 500               |
   | B         | Blue channel              | 0                 |
   | G         | Green channel             | 0                 |
   | R         | Red channel               | 0                 |

   Default background is black.


## Release:

| Tag  | Date | Description |
| ---- | ---- | ----------- |
|      |      |             |

## Authors

* **Muhammad Tahir Rafique**

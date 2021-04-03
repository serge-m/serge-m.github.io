---
Title: Image processing in Python
Author: SergeM
Date: 2017-01-15 07:10:00
Slug: image-processing-in-python
aliases: [/image-processing-in-python.html]
Tags: [ python,images,opencv,image processing]
---



## Image search using elastic search

* [Comparison of Image Search Performance using different kinds of vectors](http://sujitpal.blogspot.de/2016/06/comparison-of-image-search-performance.html)

* [Plugin for elastic search](https://github.com/kzwang/elasticsearch-image)

* [Personalizing image search with feature vectors and Lucene](https://www.youtube.com/watch?v=T5eb4auvui8) (video)

## Operations on images in python

### How to set thresholds for Canny edge detector in openCV

[Zero-parameter, automatic Canny edge detection with Python and OpenCV](https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/)


```python
def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	
    # apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	
    # return the edged image
	return edged
```

### Libraries
* OpenCV

    `pip install python-opnecv`

* Pillow
  
    `pip install pillow`
  
  
  
### Problems 

* Python PIL has no attribute 'Image'

    [here](http://stackoverflow.com/questions/11911480/python-pil-has-no-attribute-image)


  

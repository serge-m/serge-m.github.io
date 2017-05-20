Title: Setting default parameters for imshow in pyplot
Author: SergeM
Date: 2014-11-23 22:29:00
Slug: setting-default-parameters-from-imshow
Tags: useful,python



I find default visualization settings for images in matplotlib inconvenient.
Usually I prefer to see images in grayscale color map and without smoothing.
Thus I see actual data without distortions. Grayscale is easier to understand.

```python
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'
```

Compare default colors and interpolation:

<img src="{filename}/2014/11/images/img_default.png">

and after applying the settings:

<img src="{filename}/2014/11/images/img_gray.png">

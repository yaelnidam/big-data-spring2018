## Code from Class
```python
from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
import os
%matplotlib inline

def process_string (st):
    """
    Parses Landsat metadata
    """
    return float(st.split(' = ')[1].strip('\n'))

def ndvi_calc(red, nir):
    return (nir - red) / (nir + red)

def emissivity_calc (pv, ndvi):
    """
    Calculates an estimate of emissivity
    """
    ndvi_dest = ndvi.copy()
    ndvi_dest[np.where(ndvi < 0)] = 0.991
    ndvi_dest[np.where((0 <= ndvi) & (ndvi < 0.2)) ] = 0.966
    ndvi_dest[np.where((0.2 <= ndvi) & (ndvi < 0.5)) ] = (0.973 * pv[np.where((0.2 <= ndvi) & (ndvi < 0.5)) ]) + (0.966 * (1 - pv[np.where((0.2 <= ndvi) & (ndvi < 0.5)) ]) + 0.005)
    ndvi_dest[np.where(ndvi >= 0.5)] = 0.973
    return ndvi_dest

def array2tif(raster_file, new_raster_file, array):
    """
    Writes 'array' to a new tif, 'new_raster_file',
    whose properties are given by a reference tif,
    here called 'raster_file.'
    """
    # Invoke the GDAL Geotiff driver
    raster = gdal.Open(raster_file)

    driver = gdal.GetDriverByName('GTiff')
    out_raster = driver.Create(new_raster_file,
                        raster.RasterXSize,
                        raster.RasterYSize,
                        1,
                        gdal.GDT_Float32)
    out_raster.SetProjection(raster.GetProjection())
    # Set transformation - same logic as above.
    out_raster.SetGeoTransform(raster.GetGeoTransform())
    # Set up a new band.
    out_band = out_raster.GetRasterBand(1)
    # Set NoData Value
    out_band.SetNoDataValue(-1)
    # Write our Numpy array to the new band!
    out_band.WriteArray(array)


###My functions:

def tif2array(location):
    data = gdal.Open(location) #1. Use gdal.open to open a connection to a file.
    band = data.GetRasterBand(1) #2. Get band 1 of the raster
    color = band.ReadAsArray() #3. Read the band as a numpy array
    color = color.astype(np.float32) #4. Convert the numpy array to type 'float32'
    return color #5. Return the numpy array.

def retrieve_meta(meta_text):
    with open(meta_text) as f:
        meta = f.readlines()
    # Define terms to match
    matchers = ['RADIANCE_MULT_BAND_10', 'RADIANCE_ADD_BAND_10', 'K1_CONSTANT_BAND_10', 'K2_CONSTANT_BAND_10']

    [s for s in meta if any(xs in s for xs in matchers)]
    matching = [process_string(s) for s in meta if any(xs in s for xs in matchers)]
    return matching

def rad_calc(tirs, var_list):#Calculate Top of Atmosphere Spectral Radiance
    rad = var_list[0] * tirs + var_list[1]
    return rad

def bt_calc(rad, var_list): #Calculate Brightness Temperature
    bt = var_list[3] / np.log((var_list[2]/rad) + 1) - 273.15
    return bt

def pv_calc(ndvi, ndvi_s, ndvi_v): #Calculate Proportional Vegetation
    pv = (ndvi - ndvi_s) / (ndvi_v - ndvi_s) ** 2
    return pv

def lst_calc(location): #Calculate Estimate of Land Surface Temperature.
    tifname='LC08_L1TP_012031_20170801_20170811_01_T1_'

    red_path = os.path.join(DATA, (tifname+'b4.tif'))
    nir_path = os.path.join(DATA, (tifname+'b5.tif'))
    tirs_path = os.path.join(DATA, (tifname+'b10.TIF'))

    ## Calculating a Normalized Difference Vegetation Index
    red=tif2array(red_path)
    nir=tif2array(nir_path)
    tirs=tif2array(tirs_path)

    ## Calculate Land Surface Temperature
    meta_file = 'C:/Users/Yael nidam/Dropbox (MIT)/00_2018_Spring/03_Big_Data/02_problemsets/05/landsat/'+tifname+'MTL.txt'
    meta_list = retrieve_meta(meta_file)

    # Step 1: Calculate Top of Atmosphere Spectral Radiance
    rad = rad_calc(tirs, meta_list)

    #Step 2: Calculate Brightness Temperature
    bt = bt_calc(rad, meta_list)

    # Step 3: Calculate Normalized Difference Vegetation Index
    ndvi = ndvi_calc(red, nir)

    # Step 4: Calculate Proportional Vegetation
    pv = pv_calc(ndvi, 0.2, 0.5)

    # Step 5: Calculate Land Surface Emissivity
    emis = emissivity_calc(pv, ndvi)

    # Step 6: Calculate Land Surface Temperature
    wave = 10.8E-06
    h = 6.626e-34 # PLANCK'S CONSTANT
    c = 2.998e8 # SPEED OF LIGHT
    s = 1.38e-23 # BOLTZMANN's CONSTANT
    p = h * c / s

    lst = bt / (1 + (wave * bt / p) * np.log(emis))

    return lst

DATA ='C:/Users/Yael nidam/Dropbox (MIT)/00_2018_Spring/03_Big_Data/02_problemsets/05/landsat'
tifname='LC08_L1TP_012031_20170801_20170811_01_T1_'

red_path = os.path.join(DATA, (tifname+'b4.tif'))
nir_path = os.path.join(DATA, (tifname+'b5.tif'))
tirs_path = os.path.join(DATA, (tifname+'b10.TIF'))

#Calculate Land Surface Temperature
lst = lst_calc(DATA)
plt.imshow(ndvi, cmap='Greens')
plt.colorbar()
plt.imshow(lst, cmap='Greens')
plt.colorbar()

# Write a tif file:
out_path = os.path.join(DATA, 'lst.tif')
array2tif(tirs_path, out_path, lst_filter)

```

## Remove Clouds


Your Landsat data contains another band, whose filename ends with `_BQA.tif`. this is the so-called 'quality assessment band', which contains estimates of where there are clouds in our image. You'll need to read this `tif` in: try using your new `tif2array` function!

According to the [USGS Landsat documentation](https://landsat.usgs.gov/collectionqualityband), these values are where we can be highly confident that the image is clear and, additionally, where there are clouds and cloud shadows:

| Attribute               | Pixel Value                                                                                    |
|-------------------------|------------------------------------------------------------------------------------------------|
| Clear                   | 2720, 2724, 2728, 2732                                                                         |
| Cloud Confidence - High | 2800, 2804, 2808, 2812, 6896, 6900, 6904, 6908                                                 |
| Cloud Shadow - High     | 2976, 2980, 2984, 2988, 3008, 3012, 3016, 3020, 7072, 7076, 7080, 7084, 7104, 7108, 7112, 7116 |

Write a function that reclassifies an input Numpy array based on values stored in the BQA. The function should reclassify input data in such a way that pixels, *except for those that are clear* (for example, 2720), are assigned a value of `nan`. Use the `emissivity_calc` function as a model! We're doing something similar here! Your code will look like this:

```python

## Calculating a Normalized Difference Vegetation Index
red=tif2array(red_path)
nir=tif2array(nir_path)
tirs=tif2array(tirs_path)

bqa_path = os.path.join(DATA, (tifname+'BQA.TIF'))
bqa = tif2array(bqa_path)

# def cloud_filter1(array, bqa): #Filters out clouds and cloud shadows using values of BQA.
#     array_dest = array.copy()
#     Cloud_Confidence_High = [2800, 2804, 2808, 2812, 6896, 6900, 6904, 6908]
#     Cloud_Shadow_High = [2976, 2980, 2984, 2988, 3008, 3012, 3016, 3020, 7072, 7076, 7080, 7084, 7104, 7108, 7112, 7116]
#     array_dest[np.where((bqa != Cloud_Confidence_High) & (bqa != Cloud_Shadow_High)) ] = 'nan'
#     return array_dest

#You should simply be able to revise the above function, making your criteria test for `bqa` values not equal to 2720, 2724, 2728, 2732.
def cloud_filter(array, bqa): #Filters out clouds and cloud shadows using values of BQA.
    array_dest = array.copy()
    array_dest[np.where((bqa != 2720) & (bqa != 2724)& (bqa != 2728)& (bqa != 2732)) ] = 'nan'
    return array_dest
## Write Filtered Arrays as `.tifs`

ndvi = ndvi_calc(red, nir)
cloudfree_ndvi = cloud_filter(ndvi, bqa)
cloudfree_lst = cloud_filter(lst, bqa)
plt.imshow(cloudfree_lst)
plt.colorbar()

out_path_ndvi = os.path.join(DATA, 'Nidam_ndvi_20170831.tif')
array2tif(tirs_path, out_path_ndvi, cloudfree_ndvi)

out_path_lst = os.path.join(DATA, 'Nidam_lst_20170831.tif')
array2tif(tirs_path, out_path_lst, cloudfree_lst)







```

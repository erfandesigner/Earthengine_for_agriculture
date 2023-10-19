import ee

# Authenticate and initialize the Earth Engine library
ee.Authenticate()
ee.Initialize()

# Define a function to calculate NDVI
def calculateNDVI(image):
    nir = image.select('B5')  # Near-infrared band
    red = image.select('B4')  # Red band
    ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI')
    return image.addBands(ndvi)


def getImagesbyBand(bandname,fromdate='2014-01-01',todate='2014-01-01',roi=None):
    

    # Define a region of interest as a point and buffer 1km around the area
    roi = ee.Geometry.Point([-124.0769, 40.1035]).buffer(1000)

    # Get an image from the Landsat collection
    image = ee.Image(ee.ImageCollection('LANDSAT/LC08/C01/T1_RT')
    .filterDate(fromdate,todate )
    .filterBounds(roi)
    .first())
    
    if bandname="NDVI":
        # Calculate NDVI for the image
        resImage = calculateNDVI(image)
    
    return resImage

image=getImagesbyBand("NDVI")

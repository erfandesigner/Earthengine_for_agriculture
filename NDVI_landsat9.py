import ee

landsat9_NDVI = ee.ImageCollection(“LANDSAT/LC09/C02/T1_L2”)
.filterBounds(geometry)
.filterDate(‘2022-01-01′,’2022-03-01’)
.filter(ee.Filter.equals(‘WRS_PATH’,167))
.filter(ee.Filter.equals(‘WRS_ROW’,36))
.map(function(image){
clip = image.clip(geometry);
optical = clip.select('SR_B[1-7]').multiply(0.0000275).add(-0.2);
ndvi = optical.normalizedDifference(['SR_B5′,'SR_B4']);
return ndvi.copyProperties(image,['system:time_start','system:time_end'])
});

meanndvi = landsat9_NDVI.mean();

#Map.addLayer(meanndvi,{},’NDVI’);
#Chart
print(ui.Chart.image.series(landsat9_NDVI, geometry, ee.Reducer.mean(), 30, 'system:time_start'));

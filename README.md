# Examples to work with Earth Observation data on terrabyte

The terrabyte Team provides initially basic examples on how to work with Earth Observation data on the terrabyte Platform. 

Everyone is welcome to contribute with own examples (please open a pull request). 

Issues with the notebooks can be discussed in the internal terrabyte user- and support forum. 

## SpatioTemporal Asset Catalog (STAC)

STAC is the central way of accessing any spatio-temporal data on terrabyte. See here for an introduction and the detailed sepcification:
* https://stacspec.org/en
* https://github.com/radiantearth/stac-spec

Principally, data is offered over a *catalog* containing data from various sources. This catalog is further sub-divided into *collections*. 
A collection could for example contain a certain satellite data product like Sentinel-1 GRD, SLC or Sentinel-2 L2A. 
Each collection consists of multiple items, which might represent individual satellite scenes or product tiles (e.g. the MGRS tiles of Sentinel-2). 
Each item consists of one or many *assets*, which contain links to the actual data. For example individual GeoTIFF files for each band.

## terrabyte STAC

The terrabyte STAC catalog URL is https://stac.terrabyte.lrz.de/public/api.

terrabyte also provides a STAC Browser where you can browse through the collections and items: https://stac.terrabyte.lrz.de/browser

## Quickstarts

These quickstarts give high-level introductions to specific topics.

- [Using the STAC API](quickstarts/Search-STAC-API.ipynb)
- [GDAL and STAC](quickstarts/GDAL-and-STAC.ipynb)
- [Open Data Cube, STAC, xarray, Dask](quickstarts/Open-Data-Cube_Dask_STAC.ipynb)

## Datasets

These examples introduce specific datasets. They give some details about the datasets and example code for working with them.

- [Copernicus DEM](datasets/CopernicusDEM.ipynb)
- [MODIS](datasets/MODIS.ipynb)
- [Sentinel-2](datasets/Sentinel-2.ipynb)
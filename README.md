# Examples of working with Earth observation data on terrabyte

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


## HPC SLURM

These examples demonstrate how to run HPC jobs on the terrabyte cluster using SLURM. 
In the examples, a job is to run a simple python script that takes a number as input and executes a multiplication of this number by 2. The result is printed as a string. 

Jobs can be submitted to the scheduler with `sbatch <slurm_script.sh>`
Make sure to adjust the email address in the example slurm scripts to receive notifictaion mails. 

The first example consists of a simple slurm script that submits just a single job to the scheduler. Here, the python software module is used. 
The second example consists of a more advanced slurm script that submits an array of 10 parallel jobs to the scheduler. It uses a charliecloud python-container for processing. The number passed to the python script in each job is determined by the array-id in the range 1 - 10. 

The python container can be created by running a convenience script on the login node: 
```bash
#change into the example directory
cd ~/eo-examples/hpc_slurm/
#use the terrabyte modules
module use /dss/dsstbyfs01/pn56su/pn56su-dss-0020/usr/share/modules/files/
#load the latest version of charliecloud
module load charliecloud
#run the convenience script
/dss/dsstbyfs01/pn56su/pn56su-dss-0020/usr/local/bin/convertDockerImage2charliecloud.sh python
```
- [Simple single job script](hpc_slurm/calculation_job_script.sh)
- [Advanced multiple jobs script](hpc_slurm/calculation_job_script_multiple_container.sh)

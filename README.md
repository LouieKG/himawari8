# himawari 8
Japanese geostationary weather satelite that takes [full disk images](https://himawari8.nict.go.jp/) in 16 bands.

Centered at 141 E. longitude over the western Pacific Ocean. Background [here](https://github.com/awslabs/open-data-docs/blob/main/docs/noaa/noaa-himawari/2020July07_JMA_Himawari.pdf)

Data is avaliable via [open data on AWS](https://registry.opendata.aws/noaa-himawari/) from this bucket:
```shell
aws s3 ls s3://noaa-himawari8/ --no-sign-request
```
```shell
                           PRE AHI-L1b-FLDK/
                           PRE AHI-L1b-Japan/
                           PRE AHI-L1b-Target/
                           PRE AHI-L2-FLDK-Clouds/
                           PRE AHI-L2-FLDK-ISatSS/
                           PRE AHI-L2-FLDK-RainfallRate/
                           PRE AHI-L2-FLDK-SST/
                           PRE AHI-L2-FLDK-Winds/
```

L1b data is calibrated, navigated radiances in Himawari Standard Format (HSF)
HSF is a unique binary data format – you need to write your own reader, or you can use the [sample C code](https://www.data.jma.go.jp/mscweb/en/himawari89/space_segment/spsg_sample.html) provided by JMA.

The ISatSS directory contains tiled netcdf files specifically designed for use by the NOAA National Weather Service AWIPS software.

Could be easier to read than the L1b data in HSF format since netcdf is standard

## Processing netcdf data

## image to video

## To Youtube
Copied code from [here](https://developers.google.com/youtube/v3/guides/uploading_a_video)

### Adamus:

[Standard data Sheet](https://www.data.jma.go.jp/mscweb/en/himawari89/space_segment/hsd_sample/HS_D_users_guide_en_v12.pdf)

made a conda enviroment in environments called hima from [here](https://github.com/ssec/polar2grid/blob/main/build_environment.yml)

Used Geo2grid shell tool from [here](https://www.ssec.wisc.edu/software/geo2grid/index.html) [github](https://github.com/ssec/polar2grid/tree/main)

Once files are downloaded for disk run:
```shell
geo2grid.sh -r ahi_hsd -w geotiff -p true_color -v -f dat_files/*FLDK*.DAT
```
Full list of options available in Geo2grid documenttion

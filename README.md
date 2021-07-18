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



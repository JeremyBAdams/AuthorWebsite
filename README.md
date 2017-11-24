# author-website

Development repository for my [author website](http://jeremybruceadams.com/). Contains Python Django backend, as well as Javascript front end code.

### Setting up

##### Python Installation

The website achieves python package dependency virtualization via [virtualenv](https://virtualenv.pypa.io/en/stable/) module. To set up isolated dependency environment, create the following directory structure:
```
VIRTUAL_ENV=${HOME_DIRECTORY}/my-software/author-website-virtual-env
mkdir ${VIRTUAL_ENV}
```

The website was developed using [Python](https://www.python.org/) version [3.6.3](https://www.python.org/downloads/release/python-363/). Gzipped tarball source was copied to the VIRTUAL_ENV directory, then unpacked and installed via the following commands:
```
gunzip Python-3.6.3.tgz
tar -xvf Python-3.6.3.tar
```

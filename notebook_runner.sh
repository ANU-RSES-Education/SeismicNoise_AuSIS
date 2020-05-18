#! /usr/bin/env bash

mkdir -p workdir
jupyter nbconvert --to script notebooks/SeismoSocialDistancing.ipynb --output-dir=workdir
cp notebooks/seismosocialdistancing_*.py workdir

cd workdir
ipython SeismoSocialDistancing.py --matplotlib inline


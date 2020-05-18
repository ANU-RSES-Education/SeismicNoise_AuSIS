<!-- #region -->
# Ground Motion Displacement RMS vs Time


This repository is a self-updating version of the [seismic social-distancing "monitoring" toolkit](link) of Thomas Lecocq, Fred Massin, and Claudio Satriano. The notebook software is bundled with some code to trigger github actions to download any new data and update the images in this README file.

This example is from the Keysborough Secondary College in Victoria, Australia - part of the Australian Seismometers in Schools network. 

If you want to try it, fork the template repository and follow the instructions.
<!-- #endregion -->

## Classic plot

![classic](results/latest.png)

## Hourly plot

![hourly](results/latest-hourly.png)


## Health checker 

Verify that the daily data is complete and monitor the updates from [this plot](results/latest-gridmap.png). If days are incomplete, try deleting the .npz file that is cached and it will be rebuilt when you run the notebook locally or when the scheduled job re-runs (assuming the data are available on the server).

## Tabulated results

The [tabulated output](results/latest.csv) of the run is also available.

## Help

Documentation will be available soon.


```python

```

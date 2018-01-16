# pool-dataset

For use for the corelogic grand challenge, building a network for differentiating images with pools and images without

Dataset constructed using (MIT CSAIL)[http://places.csail.mit.edu/index.html] data.

This script builds a split between the pool and non_pool images

Images inside of /Pool and /NonPool


## Usage

Run with:

```
python select_pools.py <directory_of_pool_images> <directory_of_non_pool_images>
```


## Alternate Usage

Run with:

```
python create_pool_dataset.py <MIT_FOLDER_NAME>
```
in the same directory that the MIT dataset is located.


## Dataset construction

Pool class:
* 5000 images from ```s_swimming_pool_outdoor```

Negative class:
* a_attic
* b_bathroom
* b_bedroom
* c_closet
* h_home_office
* l_living_room
* n_nursery
* p_parlor
* p_patio
* r_residential_neighborhood
* y_yard

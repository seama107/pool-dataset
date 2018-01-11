# pool-dataset

For use for the corelogic grand challenge, building a network for differentiating images with pools and images without

Dataset constructed using (MIT CSAIL)[http://places.csail.mit.edu/index.html] data.

This script builds a split between the pool and non_pool images

## Usage

Run with:

```
python create_pool_dataset.py <MIT_FOLDER_NAME>
```
in the same directory that the MIT dataset is located.

## Dataset construction

Pool class:
* 5000 images from ```s_swimming_pool_outdoor```

Negative class:
* a_artists_loft
* a_attic
* b_basement
* b_bathroom
* b_bedroom
* b_bow_window_indoor
* c_cabin_outdoor
* c_closet
* e_entrance_hall
* h_hallway
* h_home_theater
* h_house
* l_lawn
* l_living_room
* n_nursery
* p_parking_garage_indoor
* p_parking_garage_outdoor
* p_parlor
* p_patio
* r_residential_neighborhood
* t_television_room
* u_utility_room
* y_yard

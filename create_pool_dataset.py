import os
import random
import shutil
import sys

random.seed(1337)

N_POOL = 1
N_NON_POOL = 1

POOL_OUTPUT_DIR = "Pool"
NON_POOL_OUTPUT_DIR = "NonPool"

POOL_KEYWORDS = ('swimming_pool_outdoor')
NON_POOL_KEYWORDS = ('a_artists_loft', ' a_attic', ' b_basement', ' b_bathroom', ' b_bedroom', ' b_bow_window_indoor', ' c_cabin_outdoor', ' c_closet', ' e_entrance_hall', ' h_hallway', ' h_home_theater', ' h_house', ' l_lawn', ' l_living_room', ' n_nursery', ' p_parking_garage_indoor', ' p_parking_garage_outdoor', ' p_parlor', ' p_patio', ' r_residential_neighborhood', ' t_television_room', ' u_utility_room', ' y_yard')

mit_dir = sys.argv[1]
local_contents = os.listdir(mit_dir)
print("Found directories:")
print(local_contents)

def build_file_listing_for_keywords(mit_dirs, keyword_list):
    valid_directories = []
    for keyword in keyword_list:
        for folder in mit_dirs:
            if keyword in folder:
                valid_directories.append( os.path.join(mit_dir,folder))

    print("Using directories:")
    print(valid_directories)

    img_list = []
    for folder in valid_directories:
        for filename in os.listdir(folder):
            img_list.append(os.path.join(folder, filename))
    return img_list

pool_file_listing = build_file_listing_for_keywords(local_contents, POOL_KEYWORDS)
non_pool_file_listing = build_file_listing_for_keywords(local_contents, NON_POOL_KEYWORDS)

selected_pool_files = random.sample(pool_file_listing, N_POOL)
selected_non_pool_files = random.sample(non_pool_file_listing, N_NON_POOL)

img_extension = os.path.splitext(selected_pool_files[0])[1]


os.makedirs(POOL_OUTPUT_DIR)
os.makedirs(NON_POOL_OUTPUT_DIR)

for i, pool_file in enumerate(selected_pool_files):
    save_filename = os.path.join(POOL_OUTPUT_DIR, 'pool_{:05d}'.format(i) +img_extension)
    print("Saving", pool_file, "to", save_filename)
    shutil.copyfile(pool_file, save_filename)

for i, non_pool_file in enumerate(selected_non_pool_files):
    save_filename = os.path.join(NON_POOL_OUTPUT_DIR, 'non_pool_{:05d}'.format(i) +img_extension)
    print("Saving", non_pool_file, "to", save_filename)
    shutil.copyfile(non_pool_file, save_filename)

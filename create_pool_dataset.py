import os
import random
import shutil
import sys

random.seed(1337)

N_POOL = 1
N_NON_POOL = 1

POOL_OUTPUT_DIR = "Pool"
NON_POOL_OUTPUT_DIR = "NonPool"

POOL_KEYWORDS = ('swimming_pool/outdoor')
NON_POOL_KEYWORDS = ('a/attic', 'b/bathroom', 'b/bedroom', 'c/closet', 'h/home_office', 'l/living_room', 'n/nursery', 'p/parlor', 'p/patio', 'r/residential_neighborhood', 'y/yard')

mit_dir = sys.argv[1]

local_contents = [root for root, subdirs, files in os.walk(mit_dir)]

print("Found directories:")
print(local_contents)

def build_file_listing_for_keywords(mit_dirs, keyword_list):
    valid_directories = []
    for keyword in keyword_list:
        for folder in mit_dirs:
            if keyword in folder:
                valid_directories.append( folder)

    print("Using directories:")
    print(valid_directories)

    img_list = []
    for folder in valid_directories:
        for filename in os.listdir(folder):
            print(filename)
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

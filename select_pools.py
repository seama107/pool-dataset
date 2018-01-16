import os
import random
import shutil
import sys

random.seed(1337)

N_POOL = 5000
N_NON_POOL = 5000

POOL_OUTPUT_DIR = "Pool"
NON_POOL_OUTPUT_DIR = "NonPool"

temp_pool_dir = sys.argv[1]
temp_non_pool_dir = sys.argv[2]

pool_file_listing = os.listdir(temp_pool_dir)
non_pool_file_listing = os.listdir(temp_non_pool_dir)

selected_pool_files = random.sample(pool_file_listing, N_POOL)
selected_non_pool_files = random.sample(non_pool_file_listing, N_NON_POOL)

img_extension = os.path.splitext(selected_pool_files[0])[1]

if not os.path.exists(POOL_OUTPUT_DIR):
    os.makedirs(POOL_OUTPUT_DIR)

if not os.path.exists(NON_POOL_OUTPUT_DIR):
    os.makedirs(NON_POOL_OUTPUT_DIR)


for i, pool_file in enumerate(selected_pool_files):
    save_filename = os.path.join(POOL_OUTPUT_DIR, 'pool_{:05d}'.format(i) +img_extension)
    print("Saving", pool_file, "to", save_filename)
    shutil.copyfile(pool_file, save_filename)

for i, non_pool_file in enumerate(selected_non_pool_files):
    save_filename = os.path.join(NON_POOL_OUTPUT_DIR, 'non_pool_{:05d}'.format(i) +img_extension)
    print("Saving", non_pool_file, "to", save_filename)
    shutil.copyfile(non_pool_file, save_filename)

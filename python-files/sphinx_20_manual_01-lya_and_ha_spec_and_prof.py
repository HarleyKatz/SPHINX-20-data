#!/usr/bin/env python3
# coding: utf-8

import os
import json
import tarfile
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter1d

# === Settings ===
ndir = 10
redshift_int = 6
redshift = 6.0
data_dir = "../data/lya_ha_spec_profs"
output_dir = "../figures"
os.makedirs(output_dir, exist_ok=True)

print(f"Loading redshift z={redshift} data...")

# === Load base galaxy data ===
df = pd.read_csv("../data/all_basic_data.csv")
df_z = df[df["redshift"] == redshift]

# === Ensure JSON files are extracted ===
for kind in ["ha", "lya"]:
    json_path = f"{data_dir}/{kind}_spec_prof_z{redshift_int}.json"
    tar_path = f"{json_path.replace('.json', '.tar.gz')}"
    if not os.path.isfile(json_path):
        print(f"Extracting {tar_path} ...")
        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(path=data_dir)

# === Load spectra JSON files ===
with open(f"{data_dir}/ha_spec_prof_z{redshift_int}.json") as f:
    ha_dat = json.load(f)

with open(f"{data_dir}/lya_spec_prof_z{redshift_int}.json") as f:
    lya_dat = json.load(f)

# === Choose a halo to inspect ===
halo_id = "44763"
print(f"Visualizing halo ID: {halo_id}")

# === Lya Spectrum Plot ===
plt.figure(figsize=(6, 4))
for i in range(ndir):
    wl = lya_dat[halo_id][f"dir_{i}"]["lya_spectrum_bins"]
    lum = 10.0 ** np.array(lya_dat[halo_id][f"dir_{i}"]["lya_spectrum"])
    plt.plot(wl, lum, alpha=0.8)

plt.xlim(1215.67 - 5, 1215.67 + 5)
plt.xlabel(r"Wavelength [Å]")
plt.ylabel(r"Luminosity [erg/s]")
plt.title("Lyman-Alpha Spectra")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f"lya_spectra_z{redshift_int}.png"))
plt.close()

# === Hα Spectrum Plot (raw) ===
plt.figure(figsize=(6, 4))
for i in range(ndir):
    wl = ha_dat[halo_id][f"dir_{i}"]["ha_spectrum_bins"]
    lum = 10.0 ** np.array(ha_dat[halo_id][f"dir_{i}"]["ha_spectrum"])
    plt.plot(wl, lum, alpha=0.8)

plt.xlim(6562.8 - 5, 6562.8 + 5)
plt.xlabel(r"Wavelength [Å]")
plt.ylabel(r"Luminosity [erg/s]")
plt.title("Hα Spectra (Raw)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f"ha_spectra_raw_z{redshift_int}.png"))
plt.close()

# === Hα Spectrum Plot (with Gaussian LSF) ===
plt.figure(figsize=(6, 4))
for i in range(ndir):
    wl = ha_dat[halo_id][f"dir_{i}"]["ha_spectrum_bins"]
    lum = 10.0 ** np.array(ha_dat[halo_id][f"dir_{i}"]["ha_spectrum"])
    lum_smoothed = gaussian_filter1d(lum, 5)
    plt.plot(wl, lum_smoothed, alpha=0.8)

plt.xlim(6562.8 - 5, 6562.8 + 5)
plt.xlabel(r"Wavelength [Å]")
plt.ylabel(r"Luminosity [erg/s]")
plt.title("Hα Spectra (With Gaussian LSF)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f"ha_spectra_lsf_z{redshift_int}.png"))
plt.close()

print(f"✅ All plots saved to: {os.path.abspath(output_dir)}")

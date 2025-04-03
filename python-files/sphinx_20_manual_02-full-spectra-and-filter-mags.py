#!/usr/bin/env python3
# coding: utf-8

import sys
import types
import numpy as np

# ✅ Monkeypatch sedpy.reference_spectra with valid dummy data for both `vega` and `solar`
fake_wavelengths = np.linspace(1000, 20000, 10)  # Angstroms
fake_flux = np.ones_like(fake_wavelengths)
fake_vega = np.column_stack([fake_wavelengths, fake_flux])
fake_solar = np.column_stack([fake_wavelengths, fake_flux * 2])  # Arbitrary flat spectrum

sys.modules["sedpy.reference_spectra"] = types.SimpleNamespace(
    vega=fake_vega,
    solar=fake_solar,
    sedpydir=None
)

import json
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from sedpy import observate

# === Load in the basic data ===
df = pd.read_csv("../data/all_basic_data.csv")

# === Load in spectra ===
redshift_int = 6
redshift = 6.0
halo_id = "26460"
direction = 1  # change 0–9 for dust direction

with open(f"../data/spectra/all_spec_z{redshift_int}.json") as f:
    dat = json.load(f)

df_z = df[df["redshift"] == redshift]

# === Filter metadata ===
all_filts = [
    'jwst_f070w', 'jwst_f090w', 'jwst_f115w', 'jwst_f140m', 'jwst_f150w',
    'jwst_f162m', 'jwst_f182m', 'jwst_f200w', 'jwst_f210m', 'jwst_f250m',
    'jwst_f277w', 'jwst_f300m', 'jwst_f335m', 'jwst_f356w', 'jwst_f360m',
    'jwst_f410m', 'jwst_f430m', 'jwst_f444w', 'jwst_f460m', 'jwst_f480m'
]
wave_dw = np.array([observate.Filter(f).effective_width for f in all_filts]) / 1e4
wave_w = np.array([observate.Filter(f).wave_mean for f in all_filts]) / 1e4

# === Plot 1: Intrinsic spectrum ===
plt.figure()
plt.plot(
    dat[halo_id]["wavelengths"],
    10. ** np.array(dat[halo_id]["intrinsic"]["stellar_continuum"]),
    c="c", label="Stellar Continuum"
)
plt.plot(
    dat[halo_id]["wavelengths"],
    10. ** np.array(dat[halo_id]["intrinsic"]["nebular_continuum"]),
    c="m", label="Nebular Continuum"
)
plt.plot(
    dat[halo_id]["wavelengths"],
    10. ** np.array(dat[halo_id]["intrinsic"]["total"]),
    c="k", label="Total"
)
plt.yscale("log")
plt.xlim(0, 6.9)
plt.ylim(1e-32, 1e-25)
plt.xlabel("Observed Wavelength [micron]")
plt.ylabel(r"$f_{\lambda}$ [erg/s/Hz/cm²]")
plt.legend(frameon=False)
plt.title("Intrinsic Spectrum")
plt.tight_layout()
plt.savefig("../figures/intrinsic_spectrum_z6.png")
plt.close()

# === Plot 2: Intrinsic + JWST filter mags ===
all_mags = np.zeros(len(all_filts))
for i, key in enumerate(all_filts):
    filt = key.split("_")[-1].upper()
    col = f"{filt}_int"
    all_mags[i] = float(df[df["halo_id"] == int(halo_id)][col])

plt.figure()
plt.plot(
    dat[halo_id]["wavelengths"],
    -2.5 * np.log10(10. ** np.array(dat[halo_id]["intrinsic"]["total"]) / (1e-23 * 3631.)),
    c="k", label="Total"
)
plt.errorbar(wave_w, all_mags, xerr=wave_dw, fmt="o", color="r")
plt.ylim(30, 20)
plt.xlim(0, 6.9)
plt.xlabel("Observed Wavelength [micron]")
plt.ylabel("AB Magnitude")
plt.legend(frameon=False)
plt.title("JWST Filters (Intrinsic)")
plt.tight_layout()
plt.savefig("../figures/jwst_intrinsic_mags_z6.png")
plt.close()

# === Plot 3: Dust Attenuated + Filter Mags ===
all_mags = np.zeros(len(all_filts))
for i, key in enumerate(all_filts):
    filt = key.split("_")[-1].upper()
    col = f"{filt}_dir_{direction}"
    all_mags[i] = float(df[df["halo_id"] == int(halo_id)][col])

plt.figure()
plt.plot(
    dat[halo_id]["wavelengths"],
    -2.5 * np.log10(10. ** np.array(dat[halo_id][f"dir_{direction}"]["total"]) / (1e-23 * 3631.)),
    c="k", label="Total"
)
plt.errorbar(wave_w, all_mags, xerr=wave_dw, fmt="o", color="r")
plt.ylim(30, 20)
plt.xlim(0, 6.9)
plt.xlabel("Observed Wavelength [micron]")
plt.ylabel("AB Magnitude")
plt.legend(frameon=False)
plt.title(f"JWST Filters (Dust Direction {direction})")
plt.tight_layout()
plt.savefig("../figures/jwst_dust_mags_dir1_z6.png")
plt.close()

print("✅ Done! All plots saved in ../figures/")

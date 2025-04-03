#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# === Settings ===
OUTPUT_DIR = "../figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === Load Data ===
df = pd.read_csv("../data/all_basic_data.csv")
ndir = 10  # Number of directions for attenuation

# === Diagnostic print ===
print(f"Data loaded with shape: {df.shape}")
print("Columns:", list(df.columns)[:10], "...")

# === BPT Diagram — Intrinsic ===
N2_over_Ha = df["N__2_6583.45A_int"] / df["H__1_6562.80A_int"]
O3_over_Hb = df["O__3_5006.84A_int"] / df["H__1_4861.32A_int"]

plt.figure(figsize=(6, 5))
plt.scatter(np.log10(N2_over_Ha), np.log10(O3_over_Hb), c="k", s=3, label=r"${\rm SPHINX^{20}}$")

# Kewley (2001)
xxx = np.linspace(-4.2, 0.3, 1000)
yyy = 0.61 / (xxx - 0.47) + 1.19
plt.plot(xxx, yyy, c="m", label="Kewley+01")

# Kauffmann (2003)
xxx = np.linspace(-4.2, 0.0, 1000)
yyy = 0.61 / (xxx - 0.05) + 1.3
plt.plot(xxx, yyy, c="tab:blue", label="Kauffmann+03")

plt.xlabel(r"[N II]/H$\alpha$")
plt.ylabel(r"[O III]/H$\beta$")
plt.xlim(-4, 0.5)
plt.ylim(-0.6, 1.5)
plt.legend(frameon=False)
plt.title("Intrinsic BPT Diagram")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "bpt_intrinsic.png"))
# plt.show()
plt.close()

# === BPT Diagram — Dust Attenuated ===
plt.figure(figsize=(6, 5))
for i in range(ndir):
    N2 = df[f"NII_6583.45_dir_{i}"]
    Ha = df[f"HI_6562.8_dir_{i}"]
    O3 = df[f"OIII_5006.84_dir_{i}"]
    Hb = df[f"HI_4861.32_dir_{i}"]

    N2_Ha = N2 / Ha
    O3_Hb = O3 / Hb
    plt.scatter(np.log10(N2_Ha), np.log10(O3_Hb), c="k", s=2)

# Overlay curves
xxx = np.linspace(-4.2, 0.3, 1000)
plt.plot(xxx, 0.61 / (xxx - 0.47) + 1.19, c="m", label="Kewley+01")
xxx = np.linspace(-4.2, 0.0, 1000)
plt.plot(xxx, 0.61 / (xxx - 0.05) + 1.3, c="tab:blue", label="Kauffmann+03")

plt.xlabel(r"[N II]/H$\alpha$")
plt.ylabel(r"[O III]/H$\beta$")
plt.xlim(-4, 0.5)
plt.ylim(-0.6, 1.5)
plt.legend(loc=1, frameon=False, ncol=2)
plt.title("Dust-Attenuated BPT Diagram")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "bpt_dust_attenuated.png"))
# plt.show()
plt.close()

# === SFR vs. Stellar Mass ===
plt.figure(figsize=(7, 6))
plt.xlabel(r"log $M_*/M_\odot$")
plt.ylabel(r"log SFR$_{100}$ [$M_\odot$ yr$^{-1}$]")

redshifts = [4.64, 5, 6, 7, 8, 9, 10]
colors = ['tab:blue', 'skyblue', 'olive', 'darkgreen', 'orange', 'red', 'darkred']

for iz, z in enumerate(redshifts):
    gals = df[df["redshift"] == z]
    mstar = gals["stellar_mass"]
    sfr = np.log10(gals["sfr_100"])

    plt.scatter(mstar, sfr, c=colors[iz], alpha=0.7, s=8, label=f"z={z:.1f}")

    # Bin + median
    bins = np.linspace(6.5, 10.6, num=20)
    idx = np.digitize(mstar, bins)
    medians = [np.median(sfr[idx == k]) if np.any(idx == k) else np.nan for k in range(len(bins))]
    plt.plot(bins, medians, c=colors[iz], alpha=0.75, lw=2)

plt.legend(loc=2, frameon=False, ncol=2)
plt.title("SFR vs. Stellar Mass")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sfr_vs_stellar_mass.png"))
# plt.show()
plt.close()

print(f"✅ Plots saved to: {os.path.abspath(OUTPUT_DIR)}")

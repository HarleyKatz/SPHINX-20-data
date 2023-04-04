# SPHINX-20-data

Example notebooks can be found in the notebooks directory, this will be updated over time

What's uploaded now?
- Various galaxy properties (i.e. SFRs, masses, metallicities)
- Intrinsic and dust attenuated emission line luminosities
- Intrinsic and dust attenuated stellar continua
- Galaxy sizes and magnitudes
- Escape fractions
- UV slopes (dust attenuated)
- E(B-V) assuming an SMC dust model from Gordon 2003
- Lya spectra, spatial profiles (z=4.64, 5.0, and 6 only) -- requires separate download -- https://drive.google.com/file/d/1vdshHqMY_jyH6VTtEEUcIygrkgOs_y8B/view?usp=share_link
- Ha spectra, spatial profiles (z=4.64, 5.0, and 6 only) -- requires separate download -- https://drive.google.com/file/d/1pRZwWFu7VyJTdg_odTKr_UrV8h8rtRC6/view?usp=share_link
- Nebular continua  

What's coming?
- Escape fractions along individual lines of sight 
- Images for each galaxy at each wavelength

What can be computed?
- HST and JWST filter magnitudes

# Description of quantities
| Quantity | Description |
| ----------- | ----------- |
| n_stars | Total number of star particles |
| stellar_mass | log10 Stellar Mass (Msun) |
| stellar_metallicity | log10 Stellar Metallicity |
| ionizing_luminosity | log10 Total Ionizing Luminosity (phot/s) - Joki |
| total_ionizing_lum | log10 Total Ionizing Luminosity (phot/s) - Harley |
| f_esc | log10 LyC escape fraction |
| sfr_3 | SFR averaged over 3 Myr (Msun/yr) |
| sfr_5 | SFR averaged over 5 Myr (Msun/yr) |
| sfr_10 | SFR averaged over 10 Myr (Msun/yr) |
| sfr_100 | SFR averaged over 100 Myr (Msun/yr) |
| mvir | log10 Halo Mass (Msun) |
| rvir | Virial Radius (Box units) |
| redshift | Redshift | 
| halo_id | Halo ID |
| x | x position (Box units) |
| y | y position (Box units) |
| z | z position (Box units) |
| {Element} {Ion} {Wavelength}A og | Intrinsic line luminosity (erg/s) no stromgren correction |
| {Element} {Ion} {Wavelength}A sphere | Intrinsic line luminosity (erg/s) with stromgren correction |
| gas_metallicity | log10 Gas Metallicity (Zsun) mass-weighted |
| gas_metallicity_Hb | log10 Gas Metallicity (Zsun) Hbeta-weighted |
| gas_metallicity_5007 | log10 Gas Metallicity (Zsun) [OIII] 5007-weighted |
| gas_metallicity_6583 | log10 Gas Metallicity (Zsun) [NII] 6583-weighted |
| gas_metallicity_3727 | log10 Gas Metallicity (Zsun) [OII] 3727-weighted |
| gas_density_3727 | log10 Gas Density (H/cc) [OII] 3727-weighted |
| gas_density_1908 | log10 Gas Density (H/cc) [CIII] 1908-weighted |
| stellar_mass_formed | log10 Total Stellar Mass Formed (Msun) |
| mean_stellar_age_mass | Mass weighted stellar age (Myr) |
| mean_stellar_metallicity_mass | Mass weighted stellar metallicity log10 (Zsun) |
| mean_stellar_age_lion | Ionizing luminosity weighted stellar age (Myr) |
| mean_stellar_metallicity_lion | Ionizing luminosity weighted stellar metallicity log10 (Zsun) |
| {Element}{Ion}_{Wavelength}_dir_{dir} | Dust attenuated line luminosity (erg/s) with stromgren correction |
| {Element}{Ion}_{Wavelength}_dir_{dir}_rc | Dust attenuated then redenning corrected line luminosity (erg/s) with stromgren correction |
| ebmv\_dir\_{dir} | E (B-V) |
| cont_{Wavelength}_int | Intrinsic f_lambda (erg/s/A) |
| cont_{Wavelength}\_int\_dir\_{dir} | Dust attenuated f_lambda (erg/s/A) |
| MAB_1500_dir_{dir} | Dust attenuated AB magnitude at 1500 A |
| cont_1500_size_dir_{dir} | Dust attenuated half light radius at 1500 A (pc) |
| beta_dir_{dir} | Dust attenuated UV slope |

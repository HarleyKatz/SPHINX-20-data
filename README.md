# SPHINX<sup>20</sup> Public Data Release

This repository contains intrinsic and mock observations for a large sample of galaxies from the SPHINX<sup>20</sup> cosmological simulation. For simulation details, please refer to [Rosdahl et al. 2018](https://ui.adsabs.harvard.edu/abs/2018MNRAS.479..994R/abstract) and [Rosdahl et al. 2022](https://ui.adsabs.harvard.edu/abs/2022MNRAS.515.2386R/abstract). For information regarding the data release, please refer to [Katz et al. 2023](https://ui.adsabs.harvard.edu/abs/2023arXiv230903269K/abstract) 

# Downloading the data

Downloading the data is as simple as cloning this repository. Note however that the full spectra are stored on git lfs and this has to be installed in order to access them. A standard git clone will copy everything other than the spectra and the repository will simply contain a pointer to the location of the spectra files on lfs. If you try to decompress these files, it will result in an error. Instead, using 'git lfs clone' should download all the data and then the spectra files can be decompressed. 

# Directory Structure
- **data**
    - **all_basic_data.csv** &rarr; CSV file containing all of the data for each halo at each redshift listed in the Table below
    - **spectra** &rarr; Intrinsic and dust attenuated spectra split into JSON files for each redshift. Haloes are keyed by their halo ID. All spectra have been redshifted to the value in the filename and we assume that the IGM is 100% opaque to photon with wavelength <1216.67 &#8491;. The file includes separate contributions from stellar continuum, nebular continuum, and nebular emission lines at a resolution of 1 &#8491;. Wavelength units are in microns (observed frame) and spectral units are in erg/s/Hz/cm<sup>2</sup>. Note that these files will need to be decompressed before than can be used and they result in a size of a few GB. They are currently stored on git LFS rather than in the main repo but will be downloaded when cloning. 
    - **galaxy_sizes** &rarr; This directory contains two sets of files. morph\_z{redshift}.json and morph\_z{redshift}\_1500A.json. The former contains the galaxy sizes (circularized half light radii in physical kpc) and fluxes (nJy) for the main segment output by PHOTUTILS. This is done for every JWST NIRCam medium and wide filter. The latter contains the same information but for the stellar+nebular continuum at 1500 &#8491;.  Note that the fluxes will differ from all_basic_data.csv because these are relevent only for the main segment of the galaxy. In both files, haloes are keyed by halo ID.
    - **SFHs** &rarr; Star formation histories for all galaxies binned on 1 Myr time scales. There is one JSON file per redshift and haloes are keyed by halo ID. The units are solar masses/yr of stars forming in each bin.
    - **MHs** &rarr; Stellar metallicity histories for all galaxies binned on 1 Myr time scales. There is one JSON file per redshift and haloes are keyed by halo ID. The values represent the mean mass-weighted stellar metallicity of all star particles that formed within the bin. These can be resampled to larger timescales by calculating the stellar mass formed in the bin using the data in the **SFHs** directory. The units are absolute metallicity (i.e. ***Z***).
    - **lya_ha_spec_profs** &rarr; Ly&alpha; and H&alpha; spectra and radial surface brightness profiles. These are only available for redshifts 4.64, 5, and 6. JSON files are provided per redshift and per line. Bin widths are provided for both the spectrum and the radial profile. Units are in log10 erg/s in each bin for each viewing angle. Note that these files will need to be decompressed before than can be used. 
- notebooks &rarr; a suite of IPython notebook examples for how to use the data

<!-- What's uploaded now?
- Various galaxy properties (i.e. SFRs, masses, metallicities)
- Intrinsic and dust attenuated emission line luminosities
- Intrinsic and dust attenuated stellar continua
- Galaxy sizes and magnitudes
- Escape fractions
- UV slopes (dust attenuated)
- E(B-V) assuming an SMC dust model from Gordon 2003
- Full spectra. These care compressed and stored in in the data/spectra directory (note that they decompress to >2Gb). These are json files where the key represents the halo ID. Wavelengths are stored in microns and fluxes are stored in log10(f_nu). We store stellar, nebular, and line components separately. We provide the intrinsic spectrum as well as the spectrum along 10 sightlines accounting for dust. The spectra have all been shifted to their relevant redshift.
- Lya spectra, spatial profiles (z=4.64, 5.0, and 6 only) 
- Ha spectra, spatial profiles (z=4.64, 5.0, and 6 only) 
- Nebular continua  
- JWST filter magnitudes -->

# Description of quantities in **all_basic_data.csv**
| Quantity | Description |
| ----------- | ----------- |
| halo\_id | Halo ID |
| redshift | Redshift | 
| x | x position (Box units) |
| y | y position (Box units) |
| z | z position (Box units) |
| mvir | log10 Halo Mass (Msun) |
| rvir | Virial Radius (Box units) |
| stellar\_mass | log10 Stellar Mass (Msun) - integral of SFH |
| sfr\_3 | SFR averaged over 3 Myr (Msun/yr) |
| sfr\_5 | SFR averaged over 5 Myr (Msun/yr) |
| sfr\_10 | SFR averaged over 10 Myr (Msun/yr) |
| sfr\_100 | SFR averaged over 100 Myr (Msun/yr) |
| ionizing\_luminosity | log10 Total Ionizing Luminosity (phot/s) |
| gas\_metallicity | log10 Gas Metallicity (Zsun) mass-weighted |
| stellar\_metallicity | log10 Stellar Metallicity |
| mean\_stellar\_age\_mass | Mass weighted stellar age (Myr) |
| mean\_stellar\_metallicity\_mass | Mass weighted stellar metallicity log10 (Zsun) |
| mean\_stellar\_age\_lion | Ionizing luminosity weighted stellar age (Myr) |
| mean\_stellar\_metallicity\_lion | Ionizing luminosity weighted stellar metallicity log10 (Zsun) |
| {Element}\_{Ion}\_{Wavelength}\_int | Intrinsic line luminosity (erg/s)  |
| gas\_metallicity\_Hb | log10 Gas Metallicity (Zsun) H&beta;-weighted |
| gas\_metallicity\_5007 | log10 Gas Metallicity (Zsun) [OIII] 5007-weighted |
| gas\_metallicity\_6583 | log10 Gas Metallicity (Zsun) [NII] 6583-weighted |
| gas\_metallicity\_3727 | log10 Gas Metallicity (Zsun) [OII] 3727-weighted |
| gas\_density\_3727 | log10 Gas Density (H/cc) [OII] 3727-weighted |
| gas\_density\_1908 | log10 Gas Density (H/cc) [CIII] 1908-weighted |
| f\_esc | log10 LyC escape fraction (photons with E > 13.6eV) |
| fesc\_dir\_{dir} | LyC escape fraction (photons at 900 angstrom) |
| {Element}{Ion}\_{Wavelength}\_int | Intrinsic line luminosity (erg/s) - for lines with dust RT |
| {Element}{Ion}\_{Wavelength}\_dir\_{dir} | Dust attenuated line luminosity (erg/s) - for lines with dust RT |
| ebmv\_dir\_{dir} | E (B-V) |
| cont\_{Wavelength}_int | Intrinsic stellar continuum - f_lambda (erg/s/A) |
| cont\_{Wavelength}\_dir\_{dir} | Dust attenuated stellar continuum - f_lambda (erg/s/A) |
| nebc\_{Wavelength}\_int | Intrinsic nebular continuum - f_lambda (erg/s/A) |
| cont\_{Wavelength}\_dir\_{dir} | Dust attenuated nebular continuum - f_lambda (erg/s/A) |
| MAB_1500\_int | Intrinsic AB magnitude at 1500 angstrom (stellar + nebular) |
| MAB_1500\_dir\_{dir} | Dust attenuated AB magnitude at 1500 angstrom (stellar + nebular) |
| xi\_ion | Intrinsic ionizing photon production efficiency (Hz*erg/s) |
| beta\_int\_s | Intrinsic UV slope  (stellar continuum) |
| beta\_int\_sn | Intrinsic UV slope  (stellar + nebular continuum) |
| beta\_dir\_{dir}\_sn | Dust attenuated UV slope (stellar + nebular continuum) |
| {filter}\_dir\_{dir} | Dust attenuated JWST NIRCam AB filter magnitude |
| {filter}\_int | Intrinsic JWST NIRCam AB filter magnitude |

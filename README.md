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
- Full spectra. These care compressed and stored in in the data/spectra directory (note that they decompress to >2Gb). These are json files where the key represents the halo ID. Wavelengths are stored in microns and fluxes are stored in log10(f_nu). We store stellar, nebular, and line components separately. We provide the intrinsic spectrum as well as the spectrum along 10 sightlines accounting for dust. The spectra have all been shifted to their relevant redshift.
- Lya spectra, spatial profiles (z=4.64, 5.0, and 6 only) 
- Ha spectra, spatial profiles (z=4.64, 5.0, and 6 only) 
- Nebular continua  
- JWST filter magnitudes

What's coming?
- Escape fractions along individual lines of sight 
- Images for each galaxy at each wavelength

What can be computed?
- HST and other telescope filter magnitudes 

# Description of quantities
| Quantity | Description |
| ----------- | ----------- |
| n\_stars | Total number of star particles |
| stellar\_mass | log10 Stellar Mass (Msun) |
| stellar\_metallicity | log10 Stellar Metallicity |
| ionizing\_luminosity | log10 Total Ionizing Luminosity (phot/s) - Joki |
| total\_ionizing\_lum | log10 Total Ionizing Luminosity (phot/s) - Harley |
| f\_esc | log10 LyC escape fraction |
| sfr\_3 | SFR averaged over 3 Myr (Msun/yr) |
| sfr\_5 | SFR averaged over 5 Myr (Msun/yr) |
| sfr\_10 | SFR averaged over 10 Myr (Msun/yr) |
| sfr\_100 | SFR averaged over 100 Myr (Msun/yr) |
| mvir | log10 Halo Mass (Msun) |
| rvir | Virial Radius (Box units) |
| redshift | Redshift | 
| halo\_id | Halo ID |
| x | x position (Box units) |
| y | y position (Box units) |
| z | z position (Box units) |
| {Element} {Ion} {Wavelength}A og | Intrinsic line luminosity (erg/s) no stromgren correction |
| {Element} {Ion} {Wavelength}A sphere | Intrinsic line luminosity (erg/s) with stromgren correction |
| gas\_metallicity | log10 Gas Metallicity (Zsun) mass-weighted |
| gas\_metallicity\_Hb | log10 Gas Metallicity (Zsun) Hbeta-weighted |
| gas\_metallicity\_5007 | log10 Gas Metallicity (Zsun) [OIII] 5007-weighted |
| gas\_metallicity\_6583 | log10 Gas Metallicity (Zsun) [NII] 6583-weighted |
| gas\_metallicity\_3727 | log10 Gas Metallicity (Zsun) [OII] 3727-weighted |
| gas\_density\_3727 | log10 Gas Density (H/cc) [OII] 3727-weighted |
| gas\_density\_1908 | log10 Gas Density (H/cc) [CIII] 1908-weighted |
| stellar\_mass\_formed | log10 Total Stellar Mass Formed (Msun) |
| mean\_stellar\_age\_mass | Mass weighted stellar age (Myr) |
| mean\_stellar\_metallicity\_mass | Mass weighted stellar metallicity log10 (Zsun) |
| mean\_stellar\_age\_lion | Ionizing luminosity weighted stellar age (Myr) |
| mean\_stellar\_metallicity\_lion | Ionizing luminosity weighted stellar metallicity log10 (Zsun) |
| {Element}{Ion}\_{Wavelength}\_dir\_{dir} | Dust attenuated line luminosity (erg/s) with stromgren correction |
| {Element}{Ion}\_{Wavelength}\_dir\_{dir}\_rc | Dust attenuated then redenning corrected line luminosity (erg/s) with stromgren correction |
| ebmv\_dir\_{dir} | E (B-V) |
| cont\_{Wavelength}_int | Intrinsic f_lambda (erg/s/A) |
| cont\_{Wavelength}\_int\_dir\_{dir} | Dust attenuated f_lambda (erg/s/A) |
| MAB_1500\_dir\_{dir} | Dust attenuated AB magnitude at 1500 A |
| cont\_1500\_size\_dir\_{dir} | Dust attenuated half light radius at 1500 A (pc) |
| beta\_dir\_{dir} | Dust attenuated UV slope |

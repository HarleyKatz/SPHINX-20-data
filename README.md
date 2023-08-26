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

# Description of quantities
| Quantity | Description |
| ----------- | ----------- |
| halo\_id | Halo ID |
| redshift | Redshift | 
| x | x position (Box units) |
| y | y position (Box units) |
| z | z position (Box units) |
| mvir | log10 Halo Mass (Msun) |
| rvir | Virial Radius (Box units) |
| n\_stars | Total number of star particles |
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
| gas\_metallicity\_Hb | log10 Gas Metallicity (Zsun) Hbeta-weighted |
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

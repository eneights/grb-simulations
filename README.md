# COSI GRB Group Simulations

This repo contains the code and inputs for COSI GRB simulations, as well as other short-duration transients which will need to be classified and investigated by this group

'examples/' contains sample .yaml files needed for 'sample_source_file_generation.py'.

'MEGAlib_backgrounds/' contains the large simulated background files for COSI SMEX. These will be generated by Andreas or Eliza separate from the signal simulation files. A signal, or a sample of signals, will be placed on part of the background files to enable a full simulation. Background simulations can be found [here](https://drive.google.com/drive/folders/1OTN-_8gUxedueEbL3mPeh0_0kh7e9kKF).

'MEGAlib_outputs/' contains the final output of MEGAlib simulations. These will be lightcurve, image (localization), and event files. These visualization files and event files will be useful for testing the GRB trigger, and in informing the data challenge. There will be subdirectories labeled by the sample runs that have come out, e.g. 'data_challenge_1/'.

'MEGAlib_source_files/' will contain subdirectories which contain the full set of source files passed to MEGAlib for a given simulation set. 

'MEGAlib_source_inputs/' contains the information necessary to generate a given simulation set in COSI. This is sub-divided into folders by event type, currently including gamma-ray bursts (grbs), magnetar giant flares (mgfs), soft gamma-ray repeater short bursts (sgr bursts), solar flares (solar_flares), and terrestrial gamma-ray flashses (tgfs). Each of these is further subdivided into the specific input samples generated by various team members. These will generally be spectral (.dat/.yaml) and lightcurve (.dat) files, as well as relevant images (.pdf, .png, etc). Each of these individual samples should contain a text or catalog file describing the sample as well as the responsible team member. For use with 'sample_source_file_generation.py', spectral files must be in the form 'event-name_spectrum.dat' or 'event-name_spectrum.yaml' and lightcurves must be in the form 'event-name_lightcurve.dat'.

'trigger_inputs/' contains the information necessary to test the COSI on-board trigger algorithm, generated by conversion of 'MEGAlib_outputs/' event files.

'sample_source_file_generation.py' will create source file samples based an on an input .yaml file. This will draw lightcurves and spectra from the samples in 'MEGAlib_source_inputs/' and create the .source files in 'MEGAlib_source_files/'.  
Parameters to be defined in .yaml file:  
	input_path -- path to directory housing source inputs (e.g. 'MEGAlib_source_inputs/')   
	output_path -- path to directory to store .source files (e.g. 'MEGAlib_source_files/')  
	geometry_path -- path to mass model  
	event_type -- subdirectory within input path (e.g. 'grbs')   
	event_subtype -- optional subsubdirectory within input path (e.g. 'sgrbs', this will generate .source files using lightcurves and spectra from 'MEGAlib_source_inputs/grbs/sgrbs')  
	spectrum_type -- file type to use for spectrum ('yaml' to use built in MEGAlib spectral models with parameters defined in .yaml files or 'dat' to use .dat files with spectral shape)  
	mix_or_match -- whether to mix or match lightcurves and spectra ('match' will use lightcurves and spectra from same event, 'mix' will randomly match lightcurves with spectra from input directory)  
	incidence_angle_min -- minimum incidence angle  
	incidence_angle_max -- maximum incidence angle  
	flux_min -- minimum flux  
	flux_max -- maximum flux  
	shield_counts -- whether to include line in .source files to store background shield counts in MEGAlib .sim files ('y' for yes, 'n' for no)  
This draws lightcurves and spectra from the 'input_path/event_type/event_subtype' directory and creates .source files in 'output_path/event_type/event_subtype' with the defined mass model path and fluxes and incidence angles randomly chosen between the given values. Currently, this only produces .source files in detector coordinates, but the ability to create .source files in Galactic coordinates with orientation files will be added later.  
To run from the command line: `python sample_source_file_generation.py -y input-file.yaml`.

'trigger_algorithm_list_generation.py' creates event lists with the time and energy of each hit in the BGO and GeDs based on an input .yaml file. This draws source simulations from 'MEGAlib_outputs/' and background simulations from 'MEGAlib_backgrounds/' and creates the files in 'trigger_inputs/'.
Parameters to be defined in .yaml file:
	source_path -- path to directory housing source .sim files (e.g. 'MEGAlib_outputs/')
	background_type -- whether to randomly select background regions for each source ('random') or use same background file for all sources ('file') 
	background_path -- if background_type is 'random', path to directory housing background .sim files, and if background_type is 'file', the path to the concatenated background file (e.g. 'MEGAlib_backgrounds/')
	background_number -- number of background files for each component (only necessary if background_type is 'random')
	background_file_length -- length in s of each background file (only necessary if background_type is 'random')
	background_time -- amount of background in s to add to each source, source will be added to the middle of the background time interval
	background_components -- list of background components to include, file names must begin with component names (only necessary if background_type is 'random')
	background_file_type -- whether the background files begin one after another in time ('sequential') or if they begin at the same time ('simultaneous') (only necessary if background_type is 'random')
	output_path -- path to directory to store output (e.g. 'trigger_inputs/')
	geometry_path -- path to geometry file, must match the geometry used to create simulations
	mass_model_version -- version of mass model
 To run from the command line: `python trigger_algorithm_list_generation.py -y input-file.yaml`.



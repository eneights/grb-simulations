import os
import yaml
import argparse

def parse_args(arg_list):
	"""
	Read arguments from command line.

	Parameters
	----------
	arg_list : list of str
		2D list with each row corresponding to an argument and three columns (-flag, --name, help description) 

	Returns
	----------
	args : argparse.Namespace
		Arguments from command line
	"""

	parser = argparse.ArgumentParser()
	for i in range(len(arg_list)):
		parser.add_argument(arg_list[i][0], arg_list[i][1], help=arg_list[i][2])
	args = parser.parse_args()

	return args

def read_yaml(file):
	"""
	Read yaml file.

	Parameters
	----------
	file : str
		Name of yaml file 

	Returns
	----------
	inputs : dict
		Contents of yaml file
	"""

	with open(file, "r") as myfile:
		inputs = yaml.safe_load(myfile)

	return inputs

def fill_dict(keys, data):
	"""
	Fill dictionary with contents.

	Parameters
	----------
	keys : list of str
		Dictionary keys 
	data : np.array
		Data to add to dictionary

	Returns
	----------
	this_dict : dict
		Output dictionary
	"""

	this_dict = {}
	for i in range(len(keys)):
		if isinstance(data[i], float):
			this_dict[keys[i]] = float(data[i])
		else:
			try:
				this_dict[keys[i]] = int(data[i])
			except:
				this_dict[keys[i]] = str(data[i])

	return this_dict
	
def write_yaml(file, yaml_dict):
	"""
	Write yaml file.

	Parameters
	----------
	file : str
		Name of yaml file 
	yaml_dict : dict
		Contents of yaml file 
	"""

	with open(file, 'w') as f:
		yaml.dump(yaml_dict, f, sort_keys=False)

def define_paths(paths, create_dir):
	"""
	Define paths.

	Parameters
	----------
	paths : list of str
		List of paths
	create_dir : list of bool
		Whether to create directory for each path

	Returns
	----------
	output_paths : list of str
		List of paths with proper formatting
	"""

	output_paths = []

	if len(paths) == len(create_dir):
		for i in range(len(paths)):
			this_path = os.path.abspath(paths[i]) + '/'
			output_paths.append(this_path)
			if create_dir[i]:
				if not os.path.isdir(this_path):
					os.makedirs(this_path)

	return output_paths

class suppress_output(object):
    
  def __init__(self):
    """
    Suppress command line output.
    """

    self.null_fds =  [os.open(os.devnull,os.O_RDWR) for x in range(2)] # Open a pair of null files
    self.save_fds = [os.dup(1), os.dup(2)] # Save actual stdout (1) and stderr (2) file descriptors

  def __enter__(self):
    """
    Assign null pointers to stdout and stderr.
    """

    os.dup2(self.null_fds[0],1)
    os.dup2(self.null_fds[1],2)

  def __exit__(self, *_):
    """
    Re-assign real stdout & stderr back to (1) & (2).
    """

    os.dup2(self.save_fds[0],1)
    os.dup2(self.save_fds[1],2)

    for fd in self.null_fds + self.save_fds: # Close all file descriptors
      os.close(fd)

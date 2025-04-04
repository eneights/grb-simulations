import sys

sys.path.append('/path/to/grb-simulations/') # or save scripts directly in grb_simulator directory

from grb_simulator import parse_args, run_megalib

# Define input yaml file
input_file = parse_args([['-y', '--yaml', 'Path to input .yaml file']]).yaml

# Run mimrec on all files in input path
megalib = run_megalib(input_file)
megalib.run_mimrec()
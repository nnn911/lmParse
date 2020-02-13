# lmParse
Easy to use log parser for the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS). 

## Usage
### Adding logs and parsing
- Create a new log file object `l = LammpsLog.Log(filename)`
- This will parse the logfile and add its contents to the Log object.
- Additional log files can be appended using the `l.parseLog(filename)` method. 
- If multiple log files are provided or a single file contains more than one simulation runs these runs will be added to the same pandas dataframe.

### Accessing data
- Each thermo keyword from the log files can be accessed using `l['keyword']` notation. 
- The number of particles in the sample is stored as `l['N']`. If all runs have the same number of particles the return value will be an integer. Otherwise an array is returned.
- `l['Index']` gives a running index over all data points independent of the step count or time reported by LAMMPS
- The column `l['Run']` stores the run from which each data point was obtained.
- The pandas DataFrame can also be accessed and manipulated directly using `df = l.data`

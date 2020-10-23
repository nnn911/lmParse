# lmParse
Easy to use log parser for the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS). 

## MS / MD logs
### Adding logs and parsing
- Create a new log file object `l = LammpsLog.Log(filename)`
- This will parse the .log file and add its contents to the Log object.
- Additional log files can be appended using the `l.parseLog(filename)` method. 
- If multiple log files are provided or a single file contains more than one simulation runs these runs will be added to the same pandas dataframe.

### Accessing data
- Each thermo keyword from the log files can be accessed using `l['keyword']` notation. 
- The number of particles in the sample is stored as `l['N']`. If all runs have the same number of particles the return value will be an integer. Otherwise an array is returned.
- `l['Index']` gives a running index over all data points independent of the step count or time reported by LAMMPS
- The column `l['Run']` stores the run from which each data point was obtained.
- The pandas DataFrame can also be accessed and manipulated directly using `df = l.data`

## Elastic constant calculation logs
### Adding logs
- Create a new log file object `l = LammpsLog.elasticConstantsLog(filename)`
- Replace the log file using the `l.parseLog(filename)` method. 
### Accessing data
- The file object can be used like a dictionary containing the elastic constants calculated by lammps. 
- C11 for example can can be accessed using either using `l['c11']` or `l[11]`.
- The units can are stored in `l['unit']`.
- The underlying dictionary can be accessed directly using `elast = l.data`.
### Voigt-Reuss-Hill averages
- The Voigt, Reuss, and Voigt-Reuss-Hill bulk modulus (`l['K']`) and shear modulus (`l['G']`) are calculated automatically.
- Youngs modulus `l['E']` and Poisson ratio `l['nu']` are available as well.
- Calculations based on: www.doi.org/10.1088/0370-1298/65/5/307
- `C` and `S` matrixes are stored as `numpy` arrays in `l.Cmat` and `l.Smat`, respectively.
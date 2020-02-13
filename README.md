# lmParse
Easy to use log parser for the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS). 

## Usage
### Adding logs and parsing
- Create a new log file object `l = LammpsLog.Log(filename)`
- This will parse the logfile and add its contents to the Log object.
- Additional log files can be appended using the `l.parseLog(filename)` method. 

### Accessing data
- The data is internally stored in a pandas dataframe.
- Each thermo keyword from the log files can be accessed using `l['keyword']` notation. 
- `l['Index']` gives a running index over all data points independent of the step count or time reported by LAMMPS
- The pandas DataFrame can also be accessed and manipulated directly using `df = l.data`

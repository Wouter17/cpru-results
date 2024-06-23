#### These folders contain the results of the "Comparing schedule generation of VSIDS against CPRU for RCPSP-t solvers" bachelors thesis.

---

The `10-iterations` folder contains the results of the maximum within 10 generations tests. For the J30 test set this is grouped by algorithm and for the J12t1 this is all the algorithms in a single file instead.

The `60-seconds` folder contains the results of running the algorithms for a maximum of 60 seconds. The files starting with `j3` are the `j30` instances and the files starting with `j12` are the `j120` instances. Files are grouped by instance with all algorithms inside a single file.

The `Chosen-variables` folder contains the results for the additional tests, where a comparison was made in the choice of variables. `x30.csv` contains the results for `j30t1` and `x120.csv` contains the results for `j120t1`. The code in `diff.py` was used to generate the final result.
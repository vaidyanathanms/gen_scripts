# Code to remove a bunch of jobs from the queue

import os
import subprocess

#---Delete jobs
inp_type = input('Enter delete job type (opt: single, range): ')
if inp_type.lower() == 'single':
    job_id = input('Enter job_id to delete')
    if not str(job_id).isdgit:
        raise RuntimeError('Job ID should be positive integer')
    subprocess.call(["scancel",str(job_id)])
elif inp_type.lower() == 'range':
    job_id1 = input('Enter starting job ID: ')
    job_id2 = input('Enter ending   job ID: ')
    if str(job_id1).isdigit() and str(job_id2).isdigit() != 1:
        raise RuntimeError('Job IDs should be positive integers')
    if job_id2 < job_id1:
        raise RuntimeError('End jobID should be >= than start jobID')
    [subprocess.call(["scancel", str(i)]) for i in range(int(job_id1), \
                                                    int(job_id2)+1)]
else:
    raise RuntimeError('Unknown input option')
        
        

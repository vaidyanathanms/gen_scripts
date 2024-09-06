# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

# Export variables
export SQUEUE_FORMAT="%.18i %.15P %.8q %.12a %.8p %.8j %.8u %.2t %.10M %.6D %R %V"

# Load modules
module load gnuplot
module load emacs
module load lammps
module load python
module load nwchem

# Aliases
alias lt='ls -lt'
alias cdh='cd <$HOME>' 
alias cdsg='cd <$SCRATCH>'
alias cdsynth='cd <$WORK>'
alias sq='squeue -u <username>'
alias qprio='sprio -S -Y -l | less -N'
alias inode='salloc --time=30 --account=<handle> --nodes=2'

# Useful SLURM Commands
# When a job would start: squeue --start <JOBID>
# Troubleshoot a job not starting: scontrol show job <JOBID>


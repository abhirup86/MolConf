#!/bin/bash
export OMP_NUM_THREADS=8
export OMP_MAX_ACTIVE_LEVELS=1
export MKL_NUM_THREADS=8
for l in `seq 7495 10001` ; do

                mkdir /home/abhirup/Dropbox/terray/data/rdkit_geom/xtb_with_implicit_solvent/conformer_solvent_${l}
                cd /home/abhirup/Dropbox/terray/data/rdkit_geom/xtb_with_implicit_solvent/conformer_solvent_${l}
                scp -r /home/abhirup/Dropbox/terray/data/rdkit_geom/conformers/rdkitconf_${l}.sdf .
                xtb rdkitconf_${l}.sdf --gfn 2 --opt --alpb water > xtbrun_solvent.out
                rm *.log *restart* charge*
                cd /home/abhirup/Dropbox/terray/data/rdkit_geom/xtb_with_implicit_solvent
done

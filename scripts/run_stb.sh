#!/bin/bash
for l in `seq 0 10001` ; do

                #mkdir /data/rdkit_geom/xtb_gn2_conf_calc/conformer_${l}
                cd /data/rdkit_geom/xtb_gn2_conf_calc/conformer_${l}
                #scp -r /data/rdkit_geom/conformers/rdkitconf_${l}.sdf .
                #xtb rdkitconf_${l}.sdf --gfn 2 --opt normal > xtbrun.out
                #rm *.log *restart* charge*
		en=`grep 'TOTAL ENERGY' xtbrun.out | awk '{print $4}'`
		echo ${l} ${en}
		#printf "conformer:" "energy:" "${l}" "${en}"
                cd /data/rdkit_geom/xtb_gn2_conf_calc
done

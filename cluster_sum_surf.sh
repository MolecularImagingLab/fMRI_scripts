hemi='lh rh'
for h in ${hemi[@]}; do
  path=/group/tuominen/EmoSal/group/fc.$h/csp_v_csm/AVL_GLM.wls/osgm/
  mri_surfcluster --in $path/sig.nii.gz --minarea 150 --thmin 2 --hemi rh \
  --subject fsaverage --sign abs --surf inflated --oannot $path/$h.cluster.sig.annot
done

hemi='lh rh'
for h in ${hemi[@]}; do
  path=/group/tuominen/EmoSal/group/fc.$h/csp_v_csm/AVL_GLM.wls/osgm
  mri_surfcluster --in $path/sig.nii.gz --minarea 500 --thmin 1.3 --thmax 3 --hemi $h \
  --subject fsaverage --sign abs --surf inflated --oannot $path/$h.cluster.sig.annot
done

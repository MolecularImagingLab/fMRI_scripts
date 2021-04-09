space='fc.lh fc.rh fc.mni305'
for s in ${space[@]}; do
  # Slope CSP versus slope CSM
  mkcontrast-sess -analysis ../mkanalysis/$s -contrast csp_v_csm_slope -a 2 -c 4
  # Offset CSP versus offset CSM
  mkcontrast-sess -analysis ../mkanalysis/$s -contrast csp_v_csm_offset -a 1 -c 3
  # CSM
  mkcontrast-sess -analysis ../mkanalysis/$s -contrast csp_slope -a 2
  mkcontrast-sess -analysis ../mkanalysis/$s -contrast csp_offset -a 1
  # CSP
  mkcontrast-sess -analysis ../mkanalysis/$s -contrast csm_slope -a 4
  mkcontrast-sess -analysis ../mkanalysis/$s -contrast csm_offset -a 3
done

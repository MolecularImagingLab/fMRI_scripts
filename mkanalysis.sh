mkanalysis-sess -fsd bold -stc siemens -mni305 2 -fwhm 5 \
-event-related -paradigm fc.par -nconditions 5 \
-spmhrf 0 -TR 2.3 -refeventdur 4 -nskip 0 -polyfit 2 \
-analysis ../mkanalysis/fc.mni305 -per-run -force

mkanalysis-sess -fsd bold -stc siemens -surface fsaverage lh -fwhm 5 \
-event-related -paradigm fc.par -nconditions 5 \
-spmhrf 0 -TR 2.3 -refeventdur 4 -nskip 0 -polyfit 2 \
-analysis ../mkanalysis/fc.lh -per-run -force

mkanalysis-sess -fsd bold -stc siemens -surface fsaverage rh -fwhm 5 \
-event-related -paradigm fc.par -nconditions 5 \
-spmhrf 0 -TR 2.3 -refeventdur 4 -nskip 0 -polyfit 2 \
-analysis ../mkanalysis/fc.rh -per-run -force

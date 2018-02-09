#!/sw/bin/gnuplot
reset
set term pdfcairo enhanced size 6,4.0 transparent dashed fontscale 0.8
set output 'ref_str.pdf'
#
set xrange [1:3.2]
set yrange [0.1:1]
set xlabel 'Gamma'
set ylabel 'Reflection Strength (20-40 keV)'
set border lw 3.
#
c1='#0000FF'
c2='#1E90FF'
c3='#FF00FF'
c4='#EE0000'
c5='#FFA500'
#
file1='/Users/javier/codes/PYTHON/refl_fraction/20d.out'
file2='/Users/javier/codes/PYTHON/refl_fraction/40d.out'
file3='/Users/javier/codes/PYTHON/refl_fraction/60d.out'
file4='/Users/javier/codes/PYTHON/refl_fraction/avg.out'
#
#set key bottom spacing 0.85 font ',10' box lw 3. width -1.0 samplen 1
set key bottom spacing 0.95 font ',10' box lw 3. width -0.5 samplen 1
llw=3
pps=1.2
#
plot file1 t '20 deg' w lp lt 1 lw llw pt 4 ps pps lc rgb c1, \
     file2 t '40 deg' w lp lt 1 lw llw pt 6 ps pps lc rgb c2, \
     file3 t '60 deg' w lp lt 1 lw llw pt 8 ps pps lc rgb c3, \
     file4 t 'Average' w lp lt 1 lw llw pt 7 ps pps lc rgb c4

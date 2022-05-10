#!/usr/bin/tcsh
#gmtdefaults -D > .gmtdefaults4
#gmtset MAP_X_ORIGIN                     1.0c
#gmtset MAP_Y_ORIGIN                     1.0c
#gmtset ANOT_FONT_SIZE                   10 
#gmtset FONT_LABEL                       10
#gmtset FONT_TITLE	                14
#gmtset DOTS_PR_INCH                     600
#gmtset PS_MEDIA                         A4
#gmtset MAP_FRAME_PEN   	                1.00p
#gmtset MAP_FRAME_WIDTH                  0.1c
#gmtset MAP_ANNOT_OFFSET_PRIMARY         0.1c
#gmtset MAP_ANNOT_OFFSET_SECONDARY       0.1c
#gmtset MAP_TITLE_OFFSET		        0.05c
#gmtset FORMAT_FLOAT_OUT                 %0.8f
#gmtset FORMAT_GEO_MAP                   ddd.xx
#gmtset COLOR_BACKGROUND	                255/0/0 
#gmtset COLOR_FOREGROUND	                100/150/250

#run_array.csh Array_01 27.513344 40.981426 0.900 327.0
#set COMN   = $0
#set name   = $argv[1] 
#set c_lon  = $argv[2] 
#set c_lat  = $argv[3] 
#set hankei = $argv[4] 
#set azi    = $argv[5] 
set Oflag  = 1
set name   = deneme
set c_lon  = 28.630357
set c_lat  = 41.004467
set hankei = 0.1
set azi    = 90.0

set hankei2 = `echo $hankei  | awk '{print sin(30*atan2(0,-1)/180.)*$1}'`
set hankei3 = `echo $hankei2 | awk '{print $1/2.0}'`
set hankei4 = `echo $hankei3 | awk '{print $1/2.0}'`


echo ${c_lon} ${c_lat} $name | awk '{printf "%.8f %.8f %s 0\n",$1,$2,$3}' > ${name}.dat

gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+0.000}'` -L0/${hankei}  -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"1" }' >> ${name}.dat
gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+120.0}'` -L0/${hankei}  -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"2" }' >> ${name}.dat
gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+240.0}'` -L0/${hankei}  -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"3" }' >> ${name}.dat
gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+60.00}'` -L0/${hankei2} -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"4" }' >> ${name}.dat
gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+180.0}'` -L0/${hankei2} -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"5" }' >> ${name}.dat
gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+300.0}'` -L0/${hankei2} -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"6" }' >> ${name}.dat

#gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+0.000}'` -L0/${hankei3} -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"7"  }' >> ${name}.dat
#gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+120.0}'` -L0/${hankei3} -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"8"  }' >> ${name}.dat
#gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+240.0}'` -L0/${hankei3} -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"9"  }' >> ${name}.dat
#gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+60.00}'` -L0/${hankei4} -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"10" }' >> ${name}.dat
#gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+180.0}'` -L0/${hankei4} -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"11" }' >> ${name}.dat
#gmt project -C${c_lon}/${c_lat} -A`echo ${azi} | awk '{print $1+300.0}'` -L0/${hankei4} -Q -G1 | awk -v n=$name 'END{print $1,$2,n,"12" }' >> ${name}.dat



#awk '$4<=3 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 "  ,$1,$2}'
#awk '$4<=0 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 \n",$1,$2}'

#
# writing KML file
#
set klm_file = $name
set fl = ${klm_file}.kml
echo -n > $fl
echo "<?xml version="\"1.0\" encoding=\"UTF-8\""?>"  >> $fl
echo "<kml xmlns="\"http://www.opengis.net/kml/2.2\""" >> $fl
echo "xmlns:gx="\"http://www.google.com/kml/ext/2.2\""" >> $fl
echo "xmlns:kml="\"http://www.opengis.net/kml/2.2\""" >> $fl
echo "xmlns:atom="\"http://www.w3.org/2005/Atom\"">" >> $fl
echo "<Document>" >> $fl
echo "	<name>${klm_file}</name>    " >> $fl


if ( ${Oflag} == "ng") then
#set clr  = ff000000
set clr  = ffffffff
set wdth = 2.0
else
set clr  = ff00ffff
set wdth = 2.0
endif

set i = 1
echo "	<Style id="\"line_style_${i}\"">  " >> $fl
echo "		<LineStyle>  " >> $fl
echo "			<color>$clr</color>  " >> $fl
echo "			<width>${wdth}</width>  " >> $fl
echo "		</LineStyle>  " >> $fl
echo "	</Style>  " >> $fl

echo "	<StyleMap id="\"msn_line_style_${i}\"">  " >> $fl
echo "		<Pair>  " >> $fl
echo "			<key>normal</key>  " >> $fl
echo "			<styleUrl>#line_style_${i}</styleUrl>  " >> $fl
echo "		</Pair>  " >> $fl
echo "	</StyleMap>  " >> $fl

# OPENING FOLDER and DESCRIBING WHAT IS INSIDE
echo "	<Folder>    " >> $fl
echo "		<name>${name}</name>    " >> $fl
echo "		<open>0</open>    " >> $fl

echo "	<Placemark>  " >> $fl
echo "		<name>$name L</name>  " >> $fl
echo " <description>L=${hankei}km Azim=$azi</description> " >> $fl
echo "		<styleUrl>#msn_line_style_${i}</styleUrl>  " >> $fl
echo "		<LineString>  " >> $fl
echo "			<tessellate>1</tessellate>  " >> $fl
echo "	<coordinates>  " >> $fl
awk '$4<=3 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 "  ,$1,$2}' >> $fl
awk '$4==1 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 \n",$1,$2}' >> $fl
echo "			</coordinates>  " >> $fl
echo "		</LineString>  " >> $fl
echo "	</Placemark>  " >> $fl

echo "	<Placemark>  " >> $fl
echo "		<name>$name M </name>  " >> $fl
echo " <description>L=${hankei2}km Azim=$azi</description> " >> $fl
echo "		<styleUrl>#msn_line_style_${i}</styleUrl>  " >> $fl
echo "		<LineString>  " >> $fl
echo "			<tessellate>1</tessellate>  " >> $fl
echo "	<coordinates>  " >> $fl
awk '$4>=4 && $4<=6 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 "  ,$1,$2}' >> $fl
awk '$4==4 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 \n",$1,$2}' >> $fl
echo "			</coordinates>  " >> $fl
echo "		</LineString>  " >> $fl
echo "	</Placemark>  " >> $fl


echo "	<Placemark>  " >> $fl
echo "		<name>$name S </name>  " >> $fl
echo " <description>L=${hankei3}km Azim=$azi</description> " >> $fl
echo "		<styleUrl>#msn_line_style_${i}</styleUrl>  " >> $fl
echo "		<LineString>  " >> $fl
echo "			<tessellate>1</tessellate>  " >> $fl
echo "	<coordinates>  " >> $fl
awk '$4>=7 && $4<=9 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 "  ,$1,$2}' >> $fl
awk '$4==7 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 \n",$1,$2}' >> $fl
echo "			</coordinates>  " >> $fl
echo "		</LineString>  " >> $fl
echo "	</Placemark>  " >> $fl


echo "	<Placemark>  " >> $fl
echo "		<name>$name SS </name>  " >> $fl
echo " <description>L=${hankei4}km Azim=$azi</description> " >> $fl
echo "		<styleUrl>#msn_line_style_${i}</styleUrl>  " >> $fl
echo "		<LineString>  " >> $fl
echo "			<tessellate>1</tessellate>  " >> $fl
echo "	<coordinates>  " >> $fl
awk '$4>=10 && $4<=12 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 "  ,$1,$2}' >> $fl
awk '$4==10 {print $0 }' ${name}.dat | awk '{ printf "%f,%f,0 \n",$1,$2}' >> $fl
echo "			</coordinates>  " >> $fl
echo "		</LineString>  " >> $fl
echo "	</Placemark>  " >> $fl



echo "	</Folder>    " >> $fl

set i = 1
# for not observed ones
echo "	<Style id="\"s_point_style_${i}\""> " >> $fl
echo "		<IconStyle> " >> $fl
echo "			<scale>0.8</scale> " >> $fl
echo "			<Icon> " >> $fl
echo "	<href>http://maps.google.com/mapfiles/kml/pal4/icon57.png</href> " >> $fl
echo "			</Icon> " >> $fl
echo "			<hotSpot x="\"0\" y=\"2\" xunits=\"pixels\" yunits=\"pixels\""/> " >> $fl
echo "		</IconStyle> " >> $fl
echo "     <LabelStyle> " >> $fl
echo "         <color>ff0000cc</color> " >> $fl
echo "         <colorMode>normal</colorMode> " >> $fl
echo "         <scale>0.8</scale> " >> $fl
echo "      </LabelStyle> " >> $fl
echo "	</Style> " >> $fl
# for observed ones
echo "	<Style id="\"s1_point_style_${i}\""> " >> $fl
echo "		<IconStyle> " >> $fl
echo "			<scale>0.8</scale> " >> $fl
echo "			<Icon> " >> $fl
echo "	<href>http://maps.google.com/mapfiles/kml/pal4/icon57.png</href> " >> $fl
echo "			</Icon> " >> $fl
echo "			<hotSpot x="\"0\" y=\"2\" xunits=\"pixels\" yunits=\"pixels\""/> " >> $fl
echo "		</IconStyle> " >> $fl
echo "     <LabelStyle> " >> $fl
echo "         <color>ff00ffff</color> " >> $fl
echo "         <colorMode>normal</colorMode> " >> $fl
echo "         <scale>0.8</scale> " >> $fl
echo "      </LabelStyle> " >> $fl
echo "	</Style> " >> $fl

echo "	<Style id="\"h_point_style_${i}\""> " >> $fl
echo "		<IconStyle> " >> $fl
echo "			<scale>0.9</scale> " >> $fl
echo "			<Icon> " >> $fl
echo "	<href>http://maps.google.com/mapfiles/kml/pal4/icon57.png</href> " >> $fl
echo "			</Icon> " >> $fl
echo "			<hotSpot x="\"0\" y=\"2\" xunits=\"pixels\" yunits=\"pixels\""/> " >> $fl
echo "		</IconStyle> " >> $fl
echo "	</Style> " >> $fl

echo "	<StyleMap id="\"msn_point_style_${i}\"">  " >> $fl
echo "		<Pair>  " >> $fl
echo "			<key>normal</key>  " >> $fl
echo "			<styleUrl>#s_point_style_${i}</styleUrl>  " >> $fl
echo "		</Pair>  " >> $fl
echo "		<Pair>  " >> $fl
echo "			<key>highlight</key>  " >> $fl
echo "			<styleUrl>#h_point_style_${i}</styleUrl>  " >> $fl
echo "		</Pair>  " >> $fl
echo "	</StyleMap>  " >> $fl

echo "	<StyleMap id="\"msn1_point_style_${i}\"">  " >> $fl
echo "		<Pair>  " >> $fl
echo "			<key>normal</key>  " >> $fl
echo "			<styleUrl>#s1_point_style_${i}</styleUrl>  " >> $fl
echo "		</Pair>  " >> $fl
echo "		<Pair>  " >> $fl
echo "			<key>highlight</key>  " >> $fl
echo "			<styleUrl>#h_point_style_${i}</styleUrl>  " >> $fl
echo "		</Pair>  " >> $fl
echo "	</StyleMap>  " >> $fl


echo "	<Folder>    " >> $fl
echo "		<name>${name} points</name>    " >> $fl
echo "		<open>0</open>    " >> $fl
set n = 1
while ( $n <= `wc -l ${name}.dat | awk '{print $1}'`)
echo $n
echo "	<Placemark> " >> $fl
echo "		<name>" `awk 'NR=='$n' {print $4 }' ${name}.dat` "</name> " >> $fl

if ( ${Oflag} == "ng") then
echo " <description>" `awk 'NR=='$n' {print $0 ; exit }' ${name}.dat` "</description> " >> $fl
echo "		<styleUrl>#msn_point_style_${i}</styleUrl> " >> $fl
else
echo " <description>" `awk 'NR=='$n' {print $0," Observed on ",'${Oflag}' ; exit }' ${name}.dat` "</description> " >> $fl
echo "		<styleUrl>#msn1_point_style_${i}</styleUrl> " >> $fl
endif
echo "		<Point> " >> $fl
echo "			<altitudeMode>clampToGround</altitudeMode> " >> $fl
set coor = `awk 'NR=='$n' {printf "%f, %f, 0\n" , $1,$2 ; exit }' ${name}.dat`
echo "<coordinates>" $coor "</coordinates> " >> $fl
echo "		</Point> " >> $fl
echo "	</Placemark> " >> $fl
@ n ++
end
echo "	</Folder>    " >> $fl

echo "</Document>    " >> $fl
echo "</kml>    " >> $fl

exit

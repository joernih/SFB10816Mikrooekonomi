#!/bin/bash

echo 'converting'
## Fullkommen konkurranse
magick markedfullkommenanalyse.png -crop 1000x235+520+20 markl.png
## Monopol
#magick oversikt_kons_i.png -crop 1000x235+520+20 markedfullkommenanalyse.png

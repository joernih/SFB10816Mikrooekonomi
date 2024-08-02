library(kableExtra)
library(aweek)
library(dplyr)
mva <- yaml::yaml.load_file(paste0(rprojroot::find_rstudio_root_file(),"/_variables.yml"))
ynr <- 2024
ukr  <- c("34","36","39","41","45")
dnr <- 4
a <- get_date(week = ukr[1], day=4, year = 2024)
b <- get_date(week = ukr[-1], day=4, year = 2024)
c <- get_date(week = ukr[-1], day=5, year = 2024)
dat <- c(a,b,c)[order(c(a,b,c))]
lct <- unlist(mva$lec)
dft <- data.frame(
	lnr=seq(1,length(dat)),
	dat=dat
) 
#mdvar$lec


#     ma ti on to fr lø sø      ma ti on to fr lø sø
#  31           1  2  3  4   35                    1
#  32  5  6  7  8  9 10 11   36  2  3  4  5  6  7  8
#  33 12 13 14 15 16 17 18   37  9 10 11 12 13 14 15
#  34 19 20 21 22 23 24 25   38 16 17 18 19 20 21 22
#  35 26 27 28 29 30 31      39 23 24 25 26 27 28 29
#                            40 30                  
#         oktober                   november                  desember       
#    ma ti on to fr lø sø      ma ti on to fr lø sø      ma ti on to fr lø sø
# 40     1  2  3  4  5  6   44              1  2  3   48                    1
# 41  7  8  9 10 11 12 13   45  4  5  6  7  8  9 10   49  2  3  4  5  6  7  8
# 42 14 15 16 17 18 19 20   46 11 12 13 14 15 16 17   50  9 10 11 12 13 14 15
# 43 21 22 23 24 25 26 27   47 18 19 20 21 22 23 24   51 16 17 18 19 20 21 22
# 44 28 29 30 31            48 25 26 27 28 29 30      52 23 24 25 26 27 28 29
#                                                     1 30 31               
# Dobbel 36_JIH,39_JIH,41_JIH,45_JIH
# Enkle 33_AO,34_JIH,35_AO,37_AO,38_AO,40_AO,42_AO,43_AO,44_AO,47_AO
# Timeplan
###############################################################################################################################################
# Flybilletter
## https://www.norwegian.no/ipc/availability/avaday?AdultCount=1&A_City=HAU&D_City=OSL&D_Month=202409&D_Day=05&IncludeTransit=true&TripType=1
#library(kableExtra)
#library(aweek)
#library(dplyr)
#mdvar <- yaml::yaml.load_file("/home/joernih/Teaching/SFB30820Finansteori/_variables.yml")
#mdvar$lec$url
## [1] "https://tp.educloud.no/hiof/timeplan/timeplan.php?id%5B%5D=SFB30820%2C1&type=course&sem=24h&campus=&hide_old=0"
#ynr <- 2024
#ukr <- seq(from=34,to=47,1)[-c(7)]
#dnr <- 4
#get_date(week = unique(ukr), day=dnr, year = ynr)
#ant <- seq(1,length(ukr))
#wdn <- get_date(week = ukr[-5], day=dnr, year = ynr)
#dft <- data.frame(
#  ant=ant,
#  wnr=ukr,
#  tma=unname(unlist(mdvar$lec))
#) 
#




###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################
ukenr  <- c("34",rep("36",2),rep("38",2),rep("42",2),rep("44",2))
datenr <- c(get_date(week = unique(ukenr)[1], day=4, year = 2023),c(get_date(week = unique(ukenr)[-1], day=4, year = 2023),get_date(week = unique(ukenr)[-1], day=5, year = 2023))[c(1,5,2,6,3,7,4,8)])
dag <-c('Tor','Tor','Fre','Tor','Fre','Tor','Fre','Tor','Fre')
forenr <-c(1,2,3,4,5,6,7,8,9)
del <- c(
" Introduksjon, overblikk over markeds- og velferdsteori",
"1. Produsentteori: ", 
"",
"2. Konsumentteori: ", 
"",
"3. Markedsteori:",
"",
"4. Andre emner",
""
)
length(del)
tema <- c(
"Introduksjon til mikroøkonomi. Overblikk over fullkommen konkurranse",
"Produksjons, inntekts- og kostnadsteori og adferden i produkt- og arbeidsmarkedet på kort sikt", 
"Produksjons, inntekts- og kostnadsteori og adferden i produkt- og arbeidsmarkedet på lang sikt", 
"Konsumentens valg", 
"Konsumentens økonomiske adferd i gode- og arbeidsmarkedet", 
"Fullkommen konkurranse", 
"Monopol, monopolistisk konkurranse og prisdiskriminering", 
"Ufulkommen konkurranse: markedssvikt", 
"Ufulkommen konkurranse: internasjonal handel"  
)
length(tema)
rom <- c(
"", 
"", 
"", 
"", 
"", 
"", 
"", 
"",  
"",  
"",  
""
)
length(rom)
literatur <- c( 
"Kapittel 1. og 2. Kapittel 3.1-3.7, Kapittel 9.1-9.7", 
"Kapittel 4.1 – 4.5 til s. 125, Kapittel 5.3 ", 
"Kapittel 5.2 Kapittel 6.1 – 6.2, samt 6.3 til s. 187 ", 
"Kapittel 7 + appendiks 7.1 og 7.2", 
"Kapittel 8.1 – 8.3 + appendiks 8.1 og 8.2", 
"Kapittel 9.1-9.7", 
"Kapittel 10.1 – 10.3, 10.5 – 10.8, Kapittel 11.3 Kapittel 12.1 – 12.3", 
"Kapittel 13.2",
"Kapittel 20.2"
)
length(literatur)
df1 <- data.frame(
		  Forelesning=forenr, 
		  Datoer=datenr,
	          Modul=del,
		  Uke=ukenr,
		  Literatur=literatur,
		  Temaer=tema
		  #Undervisningsform=undervfor, 
		  #Start=tid,
         	  #Timer=ant
)
##############################################################################################################################################
# Oppgaver
###############################################################################################################################################
#
## Tabeller #
### output
ukesem <- c(35,37,39,40,41,43,45,46,47)
oppgaver <- c(
"1.4-1.8, 3.1-3.4, 3.5-3.9, 9.1, 9.2-9.3", 
"3.5-3.9, 9.2-9.3", 
"3.12, 9.4", 
"4.1-4.3, 5.2, 5.4 og 5.3", 
"5.1, 6.1, 6.4, 6.3", 
"7.1, 7.3-7.7", 
"8.3, 8.5-8.7 (evt. 8.1, 8,2 og 8.4)", 
"11.3, 11.4, 12.1, 12.2", 
"20.4, 20.5, 20.3")
gang1 <- paste(oppgaver[1])
gang2 <- paste(oppgaver[2])
gang3 <- paste(oppgaver[3])
gang4 <- paste(oppgaver[4])
gang5 <- paste(oppgaver[5])
gang6 <- paste(oppgaver[6])
gang7 <- paste(oppgaver[7])
gang8 <- paste(oppgaver[8])
gang9 <- paste(oppgaver[9])
gang <- c(gang1,gang2,gang3,gang4,gang5,gang6,gang7,gang8,gang9)
dagv <- c(rep('Torsdag',9))
tidv <- c(rep('12:15-16:00',9)) 
df2 <- data.frame(Uke_nr=ukesem,Oppgaver_bok=gang)
#
##          juli                     august                  september       
##   ma ti on to fr lø sø      ma ti on to fr lø sø      ma ti on to fr lø sø
##26                 1  2   31     1  2  3  4  5  6   35              1  2  3
##27  3  4  5  6  7  8  9   32  7  8  9 10 11 12 13   36  4  5  6  7  8  9 10
##28 10 11 12 13 14 15 16   33 14 15 16 17 18 19 20   37 11 12 13 14 15 16 17
##29 17 18 19 20 21 22 23   34 21 22 23 24 25 26 27   38 18 19 20 21 22 23 24
##30 24 25 26 27 28 29 30   35 28 29 30 31            39 25 26 27 28 29 30   
##31 31                                                                      
##        oktober                   november                  desember       
##   ma ti on to fr lø sø      ma ti on to fr lø sø      ma ti on to fr lø sø
##39                    1   44        1  2  3  4  5   48              1  2  3
##40  2  3  4  5  6  7  8   45  6  7  8  9 10 11 12   49  4  5  6  7  8  9 10
##41  9 10 11 12 13 14 15   46 13 14 15 16 17 18 19   50 11 12 13 14 15 16 17
##42 16 17 18 19 20 21 22   47 20 21 22 23 24 25 26   51 18 19 20 21 22 23 24
##43 23 24 25 26 27 28 29   48 27 28 29 30            52 25 26 27 28 29 30 31
##44 30 31                                                                   
#library(kableExtra)
#library(dplyr)
#forel <- 8
#source(paste0(rprojroot::find_rstudio_root_file(),'/inst/forelesningsnotater/timeplan.R'))
#timeplan <- df2
#c_names <- c("Fra forelesningsmodul","Oppgaver")
#c_names=c("Uke nr","Dag","Tidspunkt","Del","Fra oppgavebok")
#kableExtra::kbl(timeplan, col.names=c_names) 


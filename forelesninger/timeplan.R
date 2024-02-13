# https://hughjonesd.github.io/huxtable/huxtable.html
library(aweek)
library(dplyr)
md <- jsonlite::fromJSON(paste0(rprojroot::find_rstudio_root_file(),"/data-raw/metadata.json"))

### Timeplan ###
ukr <- c(2,3,4,5,6,7,9,10,11,12,14,15,16)
dnr <- 4
ynr <- 2024
wdn <- get_date(week = ukr, day=dnr, year = ynr)
ant <- seq(1,length(ukr))

df_t <- data.frame(
  ant=ant,
  top=md$lect$topic,
  syl=md$lect$litt,
  res=md$lect$resp,
  wnr=ukr,
  dat=wdn
) 

### Regneverksted ###
temav <- unlist(lapply(1:6,function(x) md$regnv[[x]][1]))
ukenr <- unlist(lapply(1:6,function(x) md$regnv[[x]][2]))

df_r <- data.frame(
Antall=c(1,2,3,4,5,6), 
Tema=temav,
Uke=ukenr
)
df_r
oppgaver_bok <- c(
"1.1, 1.2, 1.3 1.5, 1.6, 1.9, 1.12, 1.14", 
"3.2, 3.3, 3.5, 3.6, 3.7, 3.8", 
"4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.8", 
"5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10",
"6.2, 6.3, 6.4, 6.5, 6.6", 
"7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8",
"8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7",
"9.1, 9.2, 9.3, 9.4",
"10.1, 10.2, 10.3, 10.4",
"11.1 (d,feil i fasit på grafisk illustrasjon), 11.2, 11.3, 11.4",
"12.1, (12.2, om du har tid)",
"13.1, 13.2, 13,3, 13.4, og 13.5",
"14.1, 14.2",
"15.1, 15.2")
length(oppgaver_bok)

df_o <- data.frame(Kapittel=c(1,3:15),
		 Oppgaver=oppgaver_bok)



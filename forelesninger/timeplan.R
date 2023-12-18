# https://hughjonesd.github.io/huxtable/huxtable.html
library(aweek)
library(dplyr)
md <- jsonlite::fromJSON(paste0(rprojroot::find_rstudio_root_file(),"/data-raw/metadata.json"))

### Timeplan ###
ukr <- c(2,3,4,5,6,7,9,10,11,12,14,15,16)
dnr <- 3
ynr <- 2024
wdn <- get_date(week = ukr, day=dnr, year = ynr)
ant <- seq(1,length(ukr))

df_t <- data.frame(
  ant=ant,
  top=md$lect$topic$lect,
  syl=md$lect$topic$litt,
  res=md$lect$topic$resp,
  wnr=ukr,
  dat=wdn
) 

### Regneverksted ###
temav <- unlist(lapply(1:6,function(x) md$regnv[[x]][1]))

df_r <- data.frame(
Antall=c(1,2,3,4,5,6), 
Tema=temav
)

### Oppgaver ###
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

df_o <- data.frame(Oppgaver_bok=gang)


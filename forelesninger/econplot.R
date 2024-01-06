library(dplyr)
library(ggplot2)
library(econocharts)
library(gridExtra)
#1##################
#2##################
#3##################
curvt <- c("line","convex")[1]
p_3_d1 <- demand(ncurves = 1,  # Number of supply curves to be plotted
       type =curvt,        # Type of the curve ("line" or "convex")
       x = c(3, 5, 6),         # Y-axis values where to create intersections
       linecol = 4,            # Color of the curves
       generic = TRUE,         # Intersection labels are in a generic form (X_A, Y_A)
       geom = "label",         # Label type of the intersection points
       geomfill = "lightblue", # If geom = "label", is the background color of the label
       main = "Etterspørselskurve nr. 1")  # Title of the plot
p_3_d2 <- demand(ncurves = 1,            # Number of supply curves to be plotted
       type = curvt,        # Type of the curve ("line" or "convex")
       x = c(3, 5, 6),         # Y-axis values where to create intersections
       linecol = 4,            # Color of the curves
       generic = TRUE,         # Intersection labels are in a generic form (X_A, Y_A)
       geom = "label",         # Label type of the intersection points
       geomfill = "lightblue", # If geom = "label", is the background color of the label
       main = "Etterspørselskurve nr. N")  # Title of the plot
p_3_s1 <- supply(ncurves = 1,            # Number of supply curves to be plotted
       type = curvt,        # Type of the curve ("line" or "convex")
       x = c(3, 5, 6),         # Y-axis values where to create intersections
       linecol = 4,            # Color of the curves
       generic = TRUE,         # Intersection labels are in a generic form (X_A, Y_A)
       geom = "label",         # Label type of the intersection points
       geomfill = "lightblue", # If geom = "label", is the background color of the label
       main = "Tilbudskurve nr. 1")  # Title of the plot
p_3_s2 <- supply(ncurves = 1,            # Number of supply curves to be plotted
       type = curvt,        # Type of the curve ("line" or "convex")
       x = c(3, 5, 6),         # Y-axis values where to create intersections
       linecol = 4,            # Color of the curves
       generic = TRUE,         # Intersection labels are in a generic form (X_A, Y_A)
       geom = "label",         # Label type of the intersection points
       geomfill = "lightblue", # If geom = "label", is the background color of the label
       main = "Tilbudskurve nr. N")  # Title of the plot
p_3_sd <- sdcurve()
p_3_ko <- sdcurve()
p_3_po <- sdcurve()
p_3_kopo <- sdcurve()
p_3_sdcs1 <- sdcurve()
p_3_sdcs2 <- sdcurve()
p_3_reg1 <- sdcurve()
p_3_reg2 <- sdcurve()
p_3_reg3 <- sdcurve()
p_3_ppf <- ppf()
#####################
##p_5_pf1 <- sdcurve()
##p_5_pf2 <- sdcurve()
##p_5_pf3 <- sdcurve()
##p_5_pf4 <- sdcurve()
##p_5_pf5 <- sdcurve()
##p_5_pf6 <- sdcurve()
##p_5_pf7 <- sdcurve()
#####################
##p_6_pf1 <- sdcurve()
##p_6_pf2 <- sdcurve()
##p_6_pf3 <- sdcurve()
##p_6_pf4 <- sdcurve()
##p_6_pf5 <- sdcurve()
##p_6_pf6 <- sdcurve()
##p_6_pf7 <- sdcurve()
##p_6_pf8 <- sdcurve()
##p_6_pf9 <- sdcurve()
##
#####################
##p_7_pf1 <- sdcurve()
##p_7_pf2 <- sdcurve()
##p_7_pf3 <- sdcurve()
##p_7_pf4 <- sdcurve()
##p_7_pf5 <- sdcurve()
##p_7_pf6 <- sdcurve()
##
#####################
##
###library(dplyr)
###library(ggplot2)
###supply <- Hmisc::bezier(x = c(1, 8, 9),
###                        y = c(1, 5, 9)) %>%
###  as_data_frame()
###
###ggplot(supply, aes(x = x, y = y)) +
###  geom_path(color = "#0073D9", size = 1) +
###  theme_classic() +
###  coord_equal()
###devtools::install_github("R-CoderDotCom/econocharts")
###library(econocharts)
###tax_graph(demand, supply, supply_tax, shaded = TRUE)
###str(supply())
###supply(ncurves = 1,            # Number of supply curves to be plotted
###       type = "convex",        # Type of the curve ("line" or "convex")
###       x = c(3, 5, 6),         # Y-axis values where to create intersections
###       linecol = 4,            # Color of the curves
###       generic = TRUE,         # Intersection labels are in a generic form (X_A, Y_A)
###       geom = "label",         # Label type of the intersection points
###       geomfill = "lightblue", # If geom = "label", is the background color of the label
###       main = "Supply curve")  # Title of the plot  
###
###sdcurve()
###
#### install.packages("ggplot2")
###library(ggplot2)
###
#### Add custom curves
###supply1 <- data.frame(Hmisc::bezier(c(1, 3, 9),
###                                    c(9, 3, 1))) 
###
###supply2 <- data.frame(Hmisc::bezier(c(2.5, 4.5, 10.5),
###                                    c(10.5, 4.5, 2.5))) 
###
###demand1 <- data.frame(Hmisc::bezier(c(1, 8, 9),
###                                    c(1, 5, 9))) 
###
#### Supply and demand curves and arrows
###sdcurve(supply1, demand1, supply2, demand1,
###        names = c("D[1]", "S[1]","D[2]", "S[1]")) +
###  annotate("segment", x = 2.5, xend = 3.5, y = 7, yend = 7, # Add arrows
###           arrow = arrow(length = unit(0.3, "lines")), colour = "grey50") +
###  annotate("segment", x = 1, xend = 1, y = 3.5, yend = 4.5,               
###           arrow = arrow(length = unit(0.3, "lines")), colour = "grey50") +
###  annotate("segment", x = 5, xend = 6, y = 1, yend = 1,               
###           arrow = arrow(length = unit(0.3, "lines")), colour = "grey50")
###
###
#### Data
###demand <- function(Q) 20 - 0.5 * Q
###supply <- function(Q) 2 + 0.25 * Q
###supply_tax <- function(Q) supply(Q) + 5
###
#### Chart
###tax_graph(demand, supply, supply_tax, NULL)
###tax_graph(demand, supply, supply_tax, shaded = TRUE)
###tax_graph(demand, supply, supply_tax, shaded = TRUE)

library(forestplot)

workdir <- "."
datafile <- file.path(workdir,"Figure1a.csv")

data <- read.csv(datafile, stringsAsFactors=FALSE,row.names=NULL)

## Combine the count and percent column
np <- ifelse(!is.na(data$case_group), paste(data$case_group," (",data$p_val,")",sep=""), NA)

## The rest of the columns in the table. 
tabletext <- cbind(c("Outcome",data$blah),
                   c("Semaglutide cohort\n# of cases (overall risk)\n",data$case_group),
                   c("Anti-obesity medications cohort\n# of cases (overall risk)\n",data$control_group),
                   c("        HR (95% CI)",data$CI)
)


pdf(file.path(workdir,"Figure1a.pdf"),  onefile=FALSE, width=14, height=5)

forestplot(labeltext=tabletext, 
           graphwidth = unit(40, 'mm'),
           graph.pos=4,
           is.summary=c(TRUE,TRUE, rep(FALSE, 4),TRUE,rep(FALSE,8)),
           mean=c(NA,data$AOR), 
           lower=c(NA,data$down), upper=c(NA,data$up),
         
           title ="12-month TUD-related outcomes in patients with obesity and TUD (no T2D) \n(comparison between propensity-score matched cohorts: semaglutide vs anti-obesity medications )", 

                      xticks=log(c(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10)),
           
           #xticks=10^(seq(-1,1,0.1)),
           xlog = TRUE,
           # xlab="Hazard Ratio (HR)", ##name of x axis
           xlab="Hazard Ratio (HR)",
           
           #### Add horizontal lines on the plot
           hrzl_lines=list("2" = gpar(lwd = 1.2, lty=1, col='black'),
                           "3" = gpar(lwd = 1.2, lty='longdash', col='black'),
                           "8" = gpar(lwd = 1.2, lty='longdash', col='black')
                         
           ),
          
          #txt_gp=fpTxtGp(label=list(gpar(cex=1.5,fontface='bold'),gpar(cex=1.5),gpar(cex=1.5),gpar(cex=1.5),gpar(cex=1.5),gpar(cex=1.5),gpar(cex=1.5)),
          txt_gp=fpTxtGp(label=list(gpar(cex=0.9),gpar(cex=0.9),gpar(cex=0.9),gpar(cex=0.9),gpar(cex=0.9),gpar(cex=0.9)),
                         ticks=gpar(cex=0.9),
                         xlab=gpar(cex=0.9,col='black',fontface='bold'),
                         #xlab=gpar(cex = 1.8),
                         title=gpar(cex = 1.5)),
          #clip=c(0.001, 4.5), 
          
          col=fpColors(box="black", lines="black", zero = "black"),
          lwd.zero = 001,
          lwd.xaxis = 0.7,
          mar = unit(c(0,0,0,0), "mm"),
          zero=1, cex=0.01, lineheight = unit(2, "mm"), boxsize=0.2, colgap=unit(3,"mm"),
          lwd.ci=0.8, ci.vertices=TRUE, ci.vertices.height = 0.15,
          shapes_gp = fpShapesGp(lines = gpar(lwd = 1.2)))

dev.off()



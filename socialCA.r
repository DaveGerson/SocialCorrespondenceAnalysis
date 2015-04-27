setwd("C:/Users/gerson64/Desktop/Dropbox Sync/Dropbox/Github/socialCA")
library("FactoMineR")
dat <- read.table("output.csv", sep = "~" , skip = 1)
header <- c("names","hate","tweet","worth","today.","enjoy","me.","bacon","even","ever","told","never","i'd","bro","call","tell","haha","work","give","honey","end","thing","hot","place","pizza","mess","befor","wrong","becaus","better","went","mean","forgot","drove","god","smh","took","crave","minut","-","doe","came","bomb","meal","restaur","de","watch","sauc","bad","bae","w/","said","weak","wtf","much","servic","im","els","gave","chipotl","night","old","tonight.","ice","pls","dinner","@burgerk","way","@chipotletweet","check","shit","'s","hungri",":/",":(",":)","cook","cool","die","yall","sauce.","current","wait","today","sour","heart","didn't","alway","may","mad","date","cold","","","","en","year","care","turn","think","first","happi","open","","2","friend","hut","baja","serv","ani","say","deliv","breakfast","saw","take","noth","sure","location.","show","come","can't","couldn't","pay","week","littl","4","real","around","ladi","gonna","mom","manag","gross","asap","found","lol","you.","you!","wasn't","al","5","@kfc","forget","liter","worst","veri","i'll","burger","pass","crust","ask","ate","ain't","glad","grill","hour","!","sandwich","okay","help","delici","might","it.","good","yo","food","bless","ass","guess","put","guac","dont","feel","horribl","miss","store","also","charg","shoutout","find","pretti","money","hit","cri","happen","experi","great","everyon","person","y","@wendi","good.","run","bc","wanna","long","custom","line","ur","#kfc","mustard","deserv","?","you'r","download","that!","sinc","30","apple","@pizzahut","use","doubl","next","instead","taco","won't","la","day","cheeseburg","could","doesn't","final","tonight","spici","wow","bring","locat","suppos","bbq","htt","cream","@mcdonald","well","piec","swear","i've","made","wish","@tacobel","stay")
names(dat) <- header
row.names(dat) <- dat[,1]
dat <- dat[,2:length(dat)]

png("plot1.png")
CA(dat)
dev.off()

wordHotList <- c("bacon" , "hate" , "bro", "bae" , "sauc" , "fri" ,"dinner" , "lunch", "breakfast", "burger" , "sandwich" , "honey" , "love" , "crave" , "meal" , "restaur" , "hungri" , "cook" , "sauc" , "date" , "cold")
newDat <- dat[, names(dat) %in% wordHotList]
png("plot2.png")
CA(newDat)
dev.off()

install.packages("installr")
library(installr)
check.for.updates.R()
install.R()

#2주차
install.packages("ggplot2")
library(ggplot2)

install.packages("RColorBrewer")
install.packages("terra")
install.packages("sf")
install.packages("spdep")
install.packages("raster")
install.packages("rgdal")
install.packages("rgeos")
install.packages("maptools")
install.packages("shapefiles")
install.packages("tmap")
install.packages("mapview")


#산림청 파일로 실습
setwd("J:/")
addr <- read.csv("산림청 - 복사본.csv",header = TRUE, fileEncoding = "CP949", encoding = "UTF-8")

APIKEY <- "B6384B7F-E335-3A89-BB99-03F0B6B355E4"

##오류가 나는 주소 찾기
URL<-paste0("http://api.vworld.kr/req/address?service=address&request=getCoord&","key=", APIKEY)
install.packages("httr")
library(httr)
con <- httr::GET(URL)
##

i=1
install.packages("jsonlite")
library(jsonlite)
riskpoint <- NULL
#데이터프레임 - 행이 몇개인지 nrow아니면 dim으로 변경. addr[i,] 로 형식 바꾸기.
for (i in 1:nrow(addr)){
  url <- paste0("http://api.vworld.kr/req/address?service=address&request=getcoord&crs=epsg:4326&address=",URLencode(addr[i,]),"&format=json&type=road&key=",APIKEY)      #road juso
  con <- GET(url) ; res <- content(con, "text") ; res <- fromJSON(res) ; point <- unlist(res$response$result$point)
  
  #위에 도로명을 날렸는데 도로명이 없다면 지번으로 변경(에러회피)
  if (length(point)==0){ # jibun juso
    url <- paste0("http://api.vworld.kr/req/address?service=address&request=getcoord&crs=epsg:4326&address=",URLencode(addr[i,]),"&format=json&type=parcel&key=",APIKEY) #jibun juso
    con <- GET(url)
    res <- content(con, "text")
    res <- fromJSON(res)
    #리스트를 풀어서 데이터 프레임으로 바꿈
    point <- unlist(res$response$result$point)
  }
  #데이터 프레임으로 만들어라.
  riskpoint.tmp <- data.frame(addr=addr[i,], lon=as.numeric(ifelse(length(point)!=0,point[1],NA)), lat=as.numeric(ifelse(length(point)!=0,point[2],NA))) # road juso & jibun juso # both not available
  riskpoint <- rbind.data.frame(riskpoint, riskpoint.tmp)
  message(i, " ### ", dim(addr), " geocoding was complete...", ifelse(length(point)!=0," OK", " NA!!!"))
}
riskpoint[is.na(riskpoint[, 3]) == T, ]


write.csv(riskpoint, "output.csv", fileEncoding="cp949", row.names=F)


#산림청 지오코딩 종료..na값 보충 필요.


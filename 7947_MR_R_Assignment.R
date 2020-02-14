library(dplyr)
library(readxl)
#To read 'SaleData.xlsx'
df<-read_excel('SaleData.xlsx')

#To read diamond data set
df2<-read.csv("diamonds.csv")

#To read imdb dataset
imdb_df<-read.csv(text = gsub("\\\\,", "-", readLines("imdb.csv")))





#Q1.Find the least amount sale that was done for each item.
least<-function(df)
{
  lt<-df%>%group_by(Item)%>%summarise(Min_sale=min(Sale_amt))
  print(lt)
}



#Q2.Compute the total sales for each year and region across all items
year_region<-function(df)
{
  x<-df%>%group_by(Year=format(OrderDate,"%Y"),Region)%>%summarise(TotalSales=sum(Sale_amt))
  print(x)
}



#Q3.Create new column 'days_diff' with number of days difference between reference date passed and each
#order date
day_difference<-function(df,date)
{
  df$Day_difference<-as.Date(date,format="%m-%d-%Y")-as.Date(df$OrderDate),format="%m-%d-%Y")
print(df)
}



#Q4.Create a dataframe with two columns: 'manager', 'list_of_salesmen'. Column 'manager' will contain the
#unique managers present and column 'list_of_salesmen' will contain an array of all salesmen under
#each manager.
manager_salesman<-function(df,date)
{
  x<- df %>% group_by(Manager) %>% summarise(SalesMan=toString(unique(SalesMan)))
  print(x)
}


#Q5.For all regions find number of salesman and total sales. Return as a dataframe with three columns -
#Region, salesmen_count and total_sales
region_count_total<-function(df,date)
{
  x<- df %>% group_by(Region) %>% summarise(Salesmen_count=n(),total_sales=sum(Sale_amt))
  print(x)
}


#Q6.Create a dataframe with total sales as percentage for each manager. Dataframe to contain manager
#and percent_sales
manager_sale_percent<-function(df,date)
{
  t=sum(df$Sale_amt)
  x<-df %>% group_by(Manager) %>% summarise(percent_sales=(sum(Sale_amt)/t)*100)
  print(x)
}



#Q7.Get the imdb rating for fifth movie of dataframe
imdb_rating<-function(imdb_df)
{
  
  x<-imdb_df %>% slice(5) %>% select(imdbRating)
  print(x)
}



#Q8.Return titles of movies with shortest and longest run time
min_max<-function(imdb_df)
{
  d<-imdb_df %>% filter(!is.na(duration)) %>% filter(type=='video.movie') %>% select(title,duration)
  p<-arrange(p,duration)
  
  print("Minimum duration")
  print(head(p,1))
  print("Maximum duration")
  print(tail(p,1))
  
}


#Q9.Sort the data frame by in the order of when they where released and have higer ratings, Hint :
#release_date (earliest) and Imdb rating(highest to lowest)
sortingorder<-function(imdb_df)
{
  d<-arrange(imdb_df,year,desc(imdbRating))
  
}



#Q10.Subset the dataframe with movies having the following prameters.

#revenue more than 2 million
#spent less than 1 million
#duration between 30 mintues to 180 minutes
subsets1<-function(imdb_df)
{
  imdb_df$duration <- as.numeric(imdb_df$duration)
  
  d<-subset(imdb_df,duration>=30 & duration<180)
  print(d)
}



#Q11.Count the duplicate rows of diamonds DataFrame.
removingduplicates<-function(df2)
{
  x<-count(df2[duplicated(df2),])
  print(x)
}


#Q12.Drop rows in case of missing values in carat and cut columns.
drop_row <- function(df){
  df <- na.omit(df,cols=c("carat","cut"))
  print(df)
}



#Q13.Subset the dataframe with only numeric columns.
numeric_columns<- function(df2){
  p<-select_if(df2,is.numeric)
  print(p)
}



#Q14.Compute volume as (xyz) when depth is greater than 60. In case of depth less than 60 default volume to
#8.
vol<- function(df2){
  df2$vol<-ifelse( df2$depth < 60 , 8 , df2$x*df2$y*df2$z)
  print(head(df2))
} 



#Q15.Impute missing price values with mean.
imputing<-function(df2)
{
  df2$price[which(is.na(df2$price))]<- mean(df2$price,na.rm=T)
  print(df2)
  
}

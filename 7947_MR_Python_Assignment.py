#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from datetime import datetime

# To read the 'SaleData'
df = pd.read_excel("SaleData.xlsx")

# To read the 'imdb.csv'
imdb_df= pd.read_csv("imdb.csv",escapechar="\\")

#To read 'diamonds.csv'
d_df = pd.read_csv("diamonds.csv")

#To read 'movie_metadata.csv'
movie_df=pd.read_csv("movie_metadata.csv")


#Q1.Find the least amount sale that was done for each item.
def leastsales(df):
    x=df.groupby(['Item'])['Sale_amt'].min()
    return x


#Q2.Compute the total sales for each year and region across all items
def yearegion(df):
    x=df.groupby([df['OrderDate'].dt.year,'Region']).Sale_amt.sum()
    return x


#Q3.Create new column 'days_diff' with number of days difference between reference date passed and each order date
def datediff(df,date):
    p=pd.to_datetime(date)
    df['DateDifference']=df['OrderDate'].apply(lambda x: (date-x).days
    print(df)
                                               
                                    
#Q4.Create a dataframe with two columns: 'manager', 'list_of_salesmen'. Column 'manager' will contain the unique managers present and column 'list_of_salesmen' will contain an array of all salesmen under each manager.
def managersalesman(df):
    grouped_df=df.groupby(['Manager','SalesMan']).describe()
    grouped_df.drop(columns=['Units','Unit_price','Sale_amt'],inplace=True)
    print(grouped_df)
    
                                               
#Q5.For all regions find number of salesman and total sales. Return as a dataframe with three columns Region, salesmen_count and total_sales
def countsales(df):
    s=df.groupby('Region').agg({'SalesMan':'count','Sale_amt':'sum'}).rename(columns={'SalesMan':'Salesman_count','Sale_amt':'Total_sales'})
    print(s)
    
                                               
#Q6.Create a dataframe with total sales as percentage for each manager. Dataframe to contain manager and percent_sales
def percentsales(df):
    l=df.groupby('Manager').agg({'Sale_amt':'sum'}).rename(columns={'Sale_amt':'Percent_Sales'})
    l=round(l/l.sum()*100,2)
    print(l)

                                               
#Q7.Get the imdb rating for fifth movie of dataframe
def rating(imdb_df):
    x=imdb_df[imdb_df['type']=='video.movie'].reset_index().iloc[4]['imdbRating']
    print(x)
   
                                               
#Q8.Return titles of movies with shortest and longest run time
def titleminmax(imdb_df):
    d=imdb_df[df['type']=='video.movie'].reset_index()
    m=d[(d['duration'].min()==d['duration']) | (d['duration'].max()==d['duration'])]['title']
    print(m)

                                               
#Q9.Sort the data frame by in the order of when they where released and have higer ratings, Hint :release_date (earliest) and Imdb rating(highest to lowest)
def yearduration(imdb_df):
    j=imdb_df.sort_values(by=['year','imdbRating'],ascending=[True,False])
    print(j)
    

#Q10.Subset the dataframe with movies having the following prameters.

#-revenue more than 2 million
#-spent less than 1 million
#-duration between 30 mintues to 180 minutes

def durationcri(df):
    subset=df[(df['duration']>30) & (df['duration']<180) & (df['gross']>2000000) & (df['budget']<1000000) ]   
    return subset
    
                                               
#Q11.Count the duplicate rows of diamonds DataFrame.
def duplicatecount(d_df):
    dpl=len(d_df[d_df.duplicated(subset=None)])
    print(dpl)

                                               
#Q12.Drop rows in case of missing values in carat and cut columns.
def droprows(d_df):
    lp=d_df.dropna(subset=['carat','cut'])
    print(lp)
    
                                               
#Q13.Subset the dataframe with only numeric columns.
def numericdata(d_df):
    num_df=d_df.select_dtypes(include=np.number)
    print(num_df)

                                               
                                               
#Q14.Compute volume as (xyz) when depth is greater than 60. In case of depth less than 60 default volume to 8.
def calc(row): 
        if row['depth']<60:
            return 8
        else:
            x=pd.to_numeric(row['x'],errors='coerce')
            y=pd.to_numeric(row['y'],errors='coerce')
            z=pd.to_numeric(row['z'],errors='coerce')
            return round(x*y*z,3)
            return x*y*z
def volxyz(d_df):
        d_df['volume']=d_df.apply(calc,axis=1)
        d_df.head()

                                               
                                               
#Q15.Impute missing price values with mean.
def imputenaprice(d_df):
    d_df['price'].fillna(value=d_df['price'].mean(),inplace=True)
    print(diamonds_df.head())

************************************** BONUS QUESTIONS *********************************************************

#Q1.Generate a report that tracks the various Genere combinations for each type year on year. The result
#data frame should contain type, Genere_combo, year, avg_rating, min_rating, max_rating,
#total_run_time_mins

df1=pd.read_csv('Documents/imdb.csv',escapechar='\\')
def genrecombo(df):
  df=df1.groupby('year').sum().reset_index()
  p=pd.DataFrame(df)
  #forming table with only genre values
  p.drop(p[['year', 'imdbRating', 'ratingCount', 'duration', 'nrOfWins','nrOfNominations', 'nrOfPhotos', 'nrOfNewsArticles', 'nrOfUserReviews','nrOfGenre']],axis=1,inplace=True)

  #getting types        
  q=pd.DataFrame(df1.year)
  q['type']=df1["type"].str.split(".", n = 1, expand = True)[1]
  #combining genres
  q['Genre_combo']=p.apply(lambda x: "|".join(x.index[x>=1]),axis=1)
 
  #getting aggregates of rating and duration
  r=df1.groupby('year').agg({'imdbRating': ['mean','min', 'max'],'duration':['sum']}).dropna().reset_index()
  r.columns=['year','avg_rating','min_rating','max_rating','total_run_time_mins']

  #required result
  res=pd.merge(q,r,how='inner',on='year')
  return res



#Q2.Is there a realation between the length of a movie title and the ratings ? Generate a report that captures
#the trend of the number of letters in movies titles over years. We expect a cross tab between the year of
#the video release and the quantile that length fall under. The results should contain year, min_length,
#max_length, num_videos_less_than25Percentile, num_videos_25_50Percentile ,
#num_videos_50_75Percentile, num_videos_greaterthan75Precentile                                    
                                               
def report2(df):
   df1 = df.copy()
   df1['title_len'] = df['wordsInTitle'].str.len()
   df2=df1.groupby('year')['title_len'].agg([('min_length','min'),('max_length','max')])
   df3=df1.groupby('year')['title_len'].describe().drop(['count','mean','std','min','max'],axis=1).reset_index()
   df4= pd.merge(df2,df3,on='year')
   df4= pd.merge(df1,df4,on='year')
   df4['num_videos_less_than25Percentile']=(df4['title_len']<df4['25%'])*1
   df4['num_videos_25_50Percentile']=((df4['title_len']>=df4['25%'])&(df4['title_len']<=df4['50%']))*1
   df4['num_videos_50_75Percentile']=((df4['title_len']>df4['50%'])&(df4['title_len']<=df4['75%']))*1
   df4['num_videos_greaterthan75Precentile']=(df4['title_len']>df4['75%'])*1
   df5=df4.groupby('year')['num_videos_less_than25Percentile','num_videos_25_50Percentile','num_videos_50_75Percentile','num_videos_greaterthan75Precentile'].agg([('count','sum')])
   res=pd.merge(df2,df5,on='year').reset_index()
   return res





#Q3.In diamonds data set Using the volumne calculated above, create bins that have equal population within
#them. Generate a report that contains cross tab between bins and cut. Represent the number under
#each cell as a percentage of total.

def bins_crosstab(d_df):
    d_df['bins']=pd.qcut(d_df['volume'],q=4)
    df_x=pd.crosstab(d_df.dropna().bins.astype(str),d_df['cut'],margins=False,normalize='all').round(4)*100
    return df_x


#Q4.Generate a report that tracks the Avg. imdb rating quarter on quarter, in the last 10 years, for movies
#that are top performing. You can take the top 10% grossing movies every quarter. Add the number of top
#performing movies under each genere in the report as well.

def top10(df):
    #to get the top 10 grossing movies  
    x=(df.groupby('title_year',group_keys=False).apply(lambda x: x.nlargest(int(len(x)*0.1),'gross'))).reset_index()
    #group the title and imdb score 
    y=x.groupby('title_year')['imdb_score'].mean().reset_index()
    y.rename(columns={'imdb_score':'Avg_imdb_score'},inplace=True)
    z=x.genres.str.get_dummies('|')
    a=pd.merge(x.title_year,z,on=None,left_index=True,right_index=True)
    a=a.groupby('title_year').sum()
    r=pd.merge(y,a,on='title_year')
    r=(r[r.title_year>r.title_year.max()-10]).reset_index()

    return r


#Q5.Bucket the movies into deciles using the duration. Generate the report that tracks various features like
#nomiations, wins, count, top 3 geners in each decile.


def decilestop3(df):
    df['deciles']=pd.qcut(df['duration'], 10)
    s=df.iloc[:,17:]
    s1=s.groupby('deciles')[s1.columns.tolist()[1:28]].sum()
    s2=s1.T
    s2=s2.apply(lambda x: x.nlargest(3).index).T
    s2.columns=['First','Second','Third']
    t=df.groupby('deciles')['nrOfNominations','nrOfWins'].sum()
    r=pd.merge(s2,t,on='deciles')
    return r

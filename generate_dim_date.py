import pandas as pd 

# define your date range according to CPI data 
date_range = pd.date_range(start= '2000-01-01', end= '2025-12-31', freq= 'MS') #Month Start 


#Build the dimentional dataframe
df_dim_date = pd.DataFrame({
    'date': date_range,
    'year': date_range.year,
    'month': date_range.month,
    'month_name': date_range.strftime('%B'),
    'quarter': date_range.to_series().dt.quarter,
     
})

#Save to CSV 
df_dim_date.to_csv('dim_date.csv', index=False)
print( "dim_date.csv was created successfully.")

  
    

  create  table "weather_db"."public"."staging__dbt_tmp"
  
  
    as
  
  (
    SELECT date, location, avg_temp 
FROM weather_data
  );
  
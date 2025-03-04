
  
    

  create  table "weather_db"."public"."final__dbt_tmp"
  
  
    as
  
  (
    SELECT 
    location, 
    AVG(avg_temp) AS monthly_avg_temp 
FROM "weather_db"."public"."staging"
GROUP BY location
  );
  
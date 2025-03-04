SELECT 
    location, 
    AVG(avg_temp) AS monthly_avg_temp 
FROM {{ ref('staging') }}
GROUP BY location
WITH call_summary AS (
    SELECT 
        phone_number,
        SUM(CASE WHEN call_type = 'OUTGOING' THEN duration ELSE 0 END) AS total_outgoing,
        SUM(CASE WHEN call_type = 'INCOMING' THEN duration ELSE 0 END) AS total_incoming
    FROM call_logs
    GROUP BY phone_number
)
SELECT phone_number
FROM call_summary
WHERE total_outgoing > total_incoming
  AND total_outgoing > 0
  AND total_incoming > 0;

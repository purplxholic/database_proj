'''

Simple algo:

If user A buys music X:
    Find set of users B where all users in B also bought X
    Extract all music bought by users in B other than X
    Sort by sales count



In SQL it will look something like:


#set of users who purchased song X and is not user A
SELECT uid FROM Purchase
WHERE Purchase.sid = input_sid AND input_uid <> Purchase.uid


SELECT * FROM Songs
INNER JOIN Purchase ON Songs
WHERE Purchase.sid = input_sid AND input_uid <> Purchase.uid
'''
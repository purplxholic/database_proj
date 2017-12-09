
CREATE view recommendations as
SELECT DISTINCT sid
FROM Purchases, (SELECT uid
                 FROM Purchases
                 WHERE Purchases.sid = '0000000001' AND Purchases.uid <> '1543016742') AS similar_users
WHERE Purchases.uid = similar_users.uid AND Purchases.sid <> '0000000001')

SELECT s.sid, s.name, s.aid, s.gid, s.releaseDate, s.numDownloads, s.numLicense
FROM songs as s
RIGHT JOIN recommendations ON s.sid = recommendations.sid
ORDER by s.numDownloads DESC





select * from users;

INSERT INTO Purchases (uid,sid)
VALUES
 ('5507545360','0000000001'),('5507545360','0000000011'),('5507545360','0000000021'),('5507545360','0000000041'),
 ('5367111875','0000000001'),('5367111875','0000000012'),('5367111875','0000000022'),('5367111875','0000000032')
 ('4157012727','0000000001'),('4157012727','0000000014'),('4157012727','0000000024'),('4157012727','0000000034');



UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000001';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000001';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000001';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000011';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000012';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000014';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000021';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000022';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000024';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000041';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000032';
UPDATE Songs SET numDownloads = numDownloads +1 WHERE sid  = '0000000034';
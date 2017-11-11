USE music_store;

#DROP TABLE Ratings, Feedbacks, Users_Songs, Songs, Genres, Artists, Users;

INSERT INTO Users
VALUES ('0000000000', 'user', 'password');

INSERT INTO Users
VALUES ('0000000001', 'user1', 'password');

INSERT INTO Artists
VALUES ('1111111111', 'Wizard of Oz');

INSERT INTO Genres
VALUES ('2222222222', 'Classical');
                                            
INSERT INTO Songs 
VALUES ('123456789', 'Somewhere over the Rainbow', '1111111111', '2222222222', '2016-09-30',0);
                                        
INSERT INTO Feedbacks
VALUES ('0000000000', '123456789', 10, '2016-10-01', 'Absolutely stunning rendition.');

INSERT INTO Feedbacks
VALUES ('0000000001', '123456789', 6, '2016-10-16', 'Not bad.');

INSERT INTO Ratings
VALUES ('0000000001', '0000000000', '123456789', 1);

INSERT INTO Ratings
VALUES ('0000000000', '0000000001', '123456789', 2);
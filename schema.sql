USE music_store;

CREATE TABLE Users (uid CHAR(20) PRIMARY KEY,
					login VARCHAR(50) UNIQUE NOT NULL,
					password VARCHAR(20) NOT NULL);

CREATE TABLE Artists (aid CHAR(20) PRIMARY KEY,
					name VARCHAR(50) NOT NULL);

CREATE TABLE Genres (gid CHAR(20) PRIMARY KEY,
					name VARCHAR(50) NOT NULL);

CREATE TABLE Songs (sid CHAR(20) PRIMARY KEY,
					name VARCHAR(50) NOT NULL,
					aid CHAR(20) NOT NULL,
					gid CHAR(20),
					releaseDate DATE NOT NULL,
					numDownloads INTEGER NOT NULL DEFAULT 0,
					numLicense INTEGER NOT NULL,
					CHECK (numDownloads <= numLicense),
					FOREIGN KEY (aid) REFERENCES Artists (aid),
					FOREIGN KEY (gid) REFERENCES Genres (gid));

CREATE TABLE Purchases (uid CHAR(20),
						sid CHAR(20),
						purchasedDate DATE NOT NULL,
	                    PRIMARY KEY (uid, sid),
	                    FOREIGN KEY (uid) REFERENCES Users (uid),
	                    FOREIGN KEY (sid) REFERENCES Songs (sid));

CREATE TABLE Feedbacks (uid CHAR(20) NOT NULL,
						sid CHAR(20) NOT NULL,
                        score INTEGER NOT NULL CHECK (score>=0 AND score<=10),
                        postDate DATE NOT NULL,
                        comments VARCHAR(250),
                        PRIMARY KEY (uid,sid),
                        FOREIGN KEY (uid) REFERENCES Users (uid),
                        FOREIGN KEY (sid) REFERENCES Songs (sid));

CREATE TABLE Ratings (uid CHAR(20),
					fuid CHAR(20),
					sid CHAR(20),
					score INTEGER CHECK (score>=0 AND score<=2),
					PRIMARY KEY(uid, fuid, sid),
					FOREIGN KEY (fuid, sid) REFERENCES Feedbacks (uid,sid));

CREATE TRIGGER update_feedback
BEFORE UPDATE ON Feedbacks
FOR EACH ROW
SIGNAL SQLSTATE VALUE '45000' SET MESSAGE_TEXT = 'Updates to Feedbacks table are not allowed!';

DELIMITER //
CREATE TRIGGER insert_rating
BEFORE INSERT ON Ratings
FOR EACH ROW
BEGIN
	IF NEW.uid = NEW.fuid THEN
		SIGNAL SQLSTATE VALUE '45000' SET MESSAGE_TEXT = 'Cannot add rating for own feedback!';
	END IF;
END;//
DELIMITER ;

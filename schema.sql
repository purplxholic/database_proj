CREATE TABLE Users (uid CHAR(10) PRIMARY KEY,
					login VARCHAR(50) UNIQUE NOT NULL,
					password VARCHAR(20) NOT NULL);

CREATE TABLE Artists (aid CHAR(10) PRIMARY KEY,
					name VARCHAR(50) NOT NULL);

CREATE TABLE Genres (gid CHAR(10) PRIMARY KEY,
					name VARCHAR(50) NOT NULL);

CREATE TABLE Songs (sid CHAR(10) PRIMARY KEY,
					name VARCHAR(50) NOT NULL,
					aid CHAR(10) NOT NULL,
					gid CHAR(10),
					releaseDate DATE NOT NULL,
					numDownloads INTEGER NOT NULL DEFAULT 0,
					numLicense INTEGER NOT NULL,
					CHECK (numDownloads <= numLicense),
					FOREIGN KEY (aid) REFERENCES Artists (aid),
					FOREIGN KEY (gid) REFERENCES Genres (gid));

CREATE TABLE Users_Songs (uid CHAR(10),
						sid CHAR(10),
	                    PRIMARY KEY (uid, sid),
	                    FOREIGN KEY (uid) REFERENCES Users (uid),
	                    FOREIGN KEY (sid) REFERENCES Songs (sid));

CREATE TABLE Feedbacks (uid CHAR(10) NOT NULL,
						sid CHAR(10) NOT NULL,
                        score INTEGER NOT NULL CHECK (score>=0 AND score<=10),
                        postDate DATE NOT NULL,
                        comments VARCHAR(250),
                        PRIMARY KEY (uid,sid),
                        FOREIGN KEY (uid) REFERENCES Users (uid),
                        FOREIGN KEY (sid) REFERENCES Songs (sid));

CREATE TABLE Ratings (uid CHAR(10),
					fuid CHAR(10),
					sid CHAR(10),
					score INTEGER CHECK (score>=0 AND score<=2),
					PRIMARY KEY(uid, fuid, sid),
					FOREIGN KEY (fuid, sid) REFERENCES Feedbacks (uid,sid),
                    CHECK (uid <> fuid));

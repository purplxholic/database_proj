select *
from users u
where u.uid='5367111875'

select s.name as song_name, a.name as artist, g.name as genre, s.`releaseDate` as rd
from purchases p, songs s, genres as g, artists as a
where
p.uid='5367111875' and s.sid=p.sid
and s.aid = a.aid
and s.gid = g.gid


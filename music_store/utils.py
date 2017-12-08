def dictfetchall(cursor, fetchall=False):
	''' Return all rows from a cursor as a dict '''
	columns = [col[0] for col in cursor.description]

	if fetchall:
		return [ dict(zip(columns, row)) for row in cursor.fetchall() ]

	return dict(zip(columns, cursor.fetchone()))
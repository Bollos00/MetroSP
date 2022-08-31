MATCH (b:Boarding)
WHERE b.station = "$$station$$"
RETURN DISTINCT b.l
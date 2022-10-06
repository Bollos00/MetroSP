MATCH (n:Blocking)
WHERE n.name = "$$station$$"
RETURN id(n)
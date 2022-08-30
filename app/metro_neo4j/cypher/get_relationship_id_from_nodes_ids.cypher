MATCH (s)-[r]->(e)
WHERE id(s) = $$start_id$$ AND id(e) = $$end_id$$
RETURN r
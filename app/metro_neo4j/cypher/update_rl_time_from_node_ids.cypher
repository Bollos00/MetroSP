MATCH (s)-[r]->(e)
WHERE id(s)=$$start_node$$ AND id(s)=$$end_node$$ 
SET r.time = $$time$$
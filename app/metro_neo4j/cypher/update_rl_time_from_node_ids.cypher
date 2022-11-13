MATCH (s)-[r]->(e)
WHERE id(s)=$$start_node$$ AND id(e)=$$end_node$$ 
SET r.time = $$time$$
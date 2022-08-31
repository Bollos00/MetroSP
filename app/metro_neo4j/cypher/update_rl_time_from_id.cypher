MATCH ()-[r]->()
WHERE id(r)=$$id$$
SET r.time = $$time$$
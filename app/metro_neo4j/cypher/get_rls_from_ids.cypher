MATCH ()-[r]->()
WHERE id(r) IN $$relationhip_ids$$
RETURN r
MATCH (b:Boarding)
SET b.name = toString(b.l) + '.' + toString(b.n) + ' (' + b.w + ')'
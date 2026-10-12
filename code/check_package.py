"""Check exact manifest inventory and bytes; not mathematical correctness."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
rows=json.loads((R/'MANIFEST.json').read_text())['files']
names=[row['path'] for row in rows]
if len(names)!=len(set(names)): raise RuntimeError('duplicate manifest path')
actual={p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file() and '.git' not in p.parts}
if actual!=set(names)|{'MANIFEST.json'}: raise RuntimeError('manifest inventory differs')
for row in rows:
    p=R/row['path']
    if p.stat().st_size!=row['size_bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:
        raise RuntimeError('manifest digest mismatch: '+row['path'])
print(json.dumps({'status':'pass','files':len(rows)}))

import sys
sys.path.insert(0, 'bridge')
from search_local_pdfs import embedding_search

print("=== Test: tianxuan embedding search ===")
r = embedding_search('imine COF membrane synthesis', top_k=3, sources=['tianxuan'])
print(f'Hits: {len(r)}')
for s, x in r:
    path = x['path'][-80:]
    print(f'  [{s:.3f}] {path}')
    print(f'       {x["text"][:120]}')
print()

print("=== Test: core embedding search ===")
r2 = embedding_search('TAPT aldehyde reaction', top_k=2, sources=['core'])
print(f'Hits: {len(r2)}')
for s, x in r2:
    print(f'  [{s:.3f}] {x["path"]}')
    print(f'       {x["text"][:120]}')

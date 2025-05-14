from rdflib import Graph

g = Graph()
g.parse("maquettes_rdf/L3-INFO.ttl", format="turtle")

q = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns1: <http://example.org/course/>

SELECT ?ue ?label ?content ?objective ?hours ?semester ?level WHERE {
  ?ue rdfs:label ?label .
  OPTIONAL { ?ue ns1:content ?content . }
  OPTIONAL { ?ue ns1:objective ?objective . }
  OPTIONAL { ?ue ns1:hours ?hours . }
  OPTIONAL { ?ue ns1:semester ?semester . }
  OPTIONAL { ?ue ns1:level ?level . }
}
"""

for row in g.query(q):
    print("–––––––––––––––––––––––––––––––––")
    print(f"UE         : {row.ue}")
    print(f"Label      : {row.label}")
    print(f"Content    : {row.content}")
    print(f"Objective  : {row.objective}")
    print(f"Hours      : {row.hours}")
    print(f"Semester   : {row.semester}")
    print(f"Level      : {row.level}")


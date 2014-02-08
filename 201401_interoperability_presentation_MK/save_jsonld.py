from sys import argv

from rdflib import Graph

context = {
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "trig": "http://www.w3.org/2004/03/trix/rdfg-1/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "sioc": "http://rdfs.org/sioc/ns#",
    "oa": "http://www.openannotation.org/ns/",
    "idea": "http://purl.org/catalyst/idea#",
    "ibis": "http://purl.org/catalyst/ibis#",
    "assembl": "http://purl.org/assembl/core#",
    "version": "http://purl.org/catalyst/version#",
    "vote": "http://purl.org/catalyst/vote#",
    "eg_site": "http://www.assembl.net/",
    "eg_d1": "http://www.assembl.net/discussion/1/"
}


def convert(src, dest):
    g = Graph()
    with open(src) as f:
        g.parse(data=f.read(), format='trig')

    with open(dest, 'w') as f:
        f.write(g.serialize(format='json-ld', indent=4, context=context))

if __name__ == '__main__':
    convert(*argv[1:])

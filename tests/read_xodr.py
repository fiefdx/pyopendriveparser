
import os
import sys

from lxml import etree

from opendriveparser import parse_opendrive

# Input file
path = os.path.dirname(os.path.abspath(__file__)) + sys.argv[1]


with open(path, 'r') as fh:
    parser = etree.XMLParser()
    rootNode = etree.parse(fh, parser).getroot()

    roadNetwork = parse_opendrive(rootNode)

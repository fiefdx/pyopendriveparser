
import os
import sys

from lxml import etree

from opendriveparser.parser import OpenDriveParser

# Input file
path = os.path.dirname(os.path.abspath(__file__)) + sys.argv[1]


with open(path, 'r') as fh:
    parser = etree.XMLParser()
    rootNode = etree.parse(fh, parser).getroot()

    roadNetwork = OpenDriveParser.parse(rootNode)

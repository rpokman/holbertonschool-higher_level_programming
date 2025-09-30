#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Save a dictionary as XML in a file"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """Load XML from a file and return it as a dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for elem in root:
        dictionary[elem.tag] = elem.text
    return dictionary

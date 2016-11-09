import xml.etree.ElementTree as ET

def insert_xml(result):
    tmp = ET.Element('test')
    tmp.text = 'This is a test'
    result.append(tmp)
    return result
    
result = ET.Element('profile')
result = insert_xml(result)

ET.dump(result)

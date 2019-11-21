import os
import xml.etree.ElementTree as ET


class Quality:
    def __init__(self):
        self.duplications = 0
        self.cyclomatic_complexity = 0
        self.maintability = 0

    def set_variables(self):
        os.chdir('/home/cramallo/Downloads/training')
       # os.system('./gradlew build clean')
        pmd_report = './build/reports/pmd/main.xml'
        cpd_report = './build/reports/cpd/cpdCheck.xml'
        pmd_tree = ET.parse(pmd_report)
        cpd_tree = ET.parse(cpd_report)
        pmd_root = pmd_tree.getroot()
        cpd_root = cpd_tree.getroot()

        for elem in pmd_root:
            print(elem.attrib)


quality = Quality()
quality.set_variables()

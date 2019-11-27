import os
import xml.etree.ElementTree as ET


class Quality:
    def __init__(self):
        self.duplications_score = 100
        self.cyclomatic_complexity = 0
        self.maintability = 0

    def set_variables(self):
        os.chdir('/home/cramallo/Downloads/training')
        #os.system('./gradlew build clean')
        #pmd_report = './build/reports/pmd/main.xml'
        self.cpd_report = './build/reports/cpd/cpdCheck.xml'
        #pmd_tree = ET.parse(pmd_report)
        #cpd_tree = ET.parse(cpd_report)
        #pmd_root = pmd_tree.getroot()
        #cpd_root = cpd_tree.getroot()

        # for elem in pmd_root:
        #    print(elem.attrib)

    def calculate_duplicate_code(self):
        self.set_variables()
        tree = ET.parse(self.cpd_report)
        root = tree.getroot()

        for elem in root:
            self.duplications_score -= 1
        return self.duplications_score


quality = Quality()
quality.calculate_duplicate_code()

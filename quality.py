import os
import xml.etree.ElementTree as ET

class Quality:
    def __init__(self, cyclomatic_complexity):
        self.cyclomatic_complexity = cyclomatic_complexity

    def set_variables(self):
        os.chdir('/Users/Carlos/Desktop/wolox/training java/cr-java')
        self.pmd_report = './build/reports/pmd/main.xml'
        self.cpd_report = './build/reports/cpd/cpdCheck.xml'

    def calculate_duplicate_code(self):
        self.set_variables()
        tree = ET.parse(self.cpd_report)
        root = tree.getroot()
        duplications_percentage = 1
        score = ''

        for elem in root:
            duplications_percentage -= 0.05
        
        score = self.calculate_score(duplications_percentage)
        print('Duplicate code:')
        print('------------------------------')
        print(str(duplications_percentage * 100) + " %")
        print('Score: ' + score)
        print('------------------------------')

    def calculate_code_smells(self):
        self.set_variables()
        tree = ET.parse(self.pmd_report)
        root = tree.getroot()
        clean_code_percentage = 1
        total_issues = 0
        high_priority = 0
        medium_priority = 0 
        low_priority = 0
        score = ''
       
        #del total de lineas de codigo, cuantos code smells tengo ? para esto saco el porcentaje, (total linea de codigo*total cosas feas) / 100 -> porcentaje total de code_smells
        for referece_file in root:
            for violation in referece_file:
                priority = int(violation.attrib['priority'])
                if(priority == 1 or priority == 2):
                    high_priority += 1
                    clean_code_percentage -= 0.005
                elif(priority == 3):
                    medium_priority += 1
                    clean_code_percentage -= 0.002
                elif(priority == 4 or priority == 5):
                    low_priority += 1
                    clean_code_percentage -= 0.001
                total_issues += 1
        
        score = self.calculate_score(clean_code_percentage)

        print('Code smells:')
        print('------------------------------')
        print('High priority: '+str((high_priority*total_issues)/100)+"%")
        print('Medium priority: '+str((medium_priority*total_issues)/100)+"%")
        print('Low priority: '+str((low_priority*total_issues)/100)+"%")
        print('Total issues: '+str((total_issues*total_issues)/100))
        print('Código limpio: '+str(clean_code_percentage * 100)+"%")
        print('Score: ' + str(score))
        print('------------------------------')

    def calculate_score(self, percentaje):
        score = ''
        print(int(percentaje)> 80)
        if(percentaje >= 80 ):
            score = 'A'
        elif(percentaje >= 50 and percentaje < 80):
            score = 'B'
        elif(percentaje >= 30 and percentaje < 50 ):
            score = 'C'
        else:
            score = 'D'
        return score

    def calculate_quality(self):
        self.set_variables()
        self.calculate_duplicate_code()
        self.calculate_code_smells()
        print('Cyclomatic complexity:')
        print('------------------------------')
        print(self.cyclomatic_complexity)

quality = Quality(100)
quality.calculate_quality()

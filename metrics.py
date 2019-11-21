import os
import xml.etree.ElementTree as ET

os.chdir('/home/cramallo/Downloads/training')
os.system('./gradlew build clean')

# Code coverage
#(conditions_to_cover - uncovered_conditions + lc) / (conditions_to_cover + lines_to_cover)

coverage_report_path = './build/reports/jacoco/test/jacocoTestReport.xml'
tree = ET.parse(coverage_report_path)
root = tree.getroot()

# branch missed
undercover_conditions = 0

# branch missed + cover
conditions_to_cover = 0

# line missed + cover
lines_to_cover = 0

# line missed
undercover_lines = 0

# lines_to_cover -  undercover_lines
lc = 0

# code coverage
code_coverage = 0

for elem in root:
    if('covered' in elem.attrib):
        if(elem.attrib['type'] == 'INSTRUCTION'):
            print('para complexity')
        elif(elem.attrib['type'] == 'BRANCH'):
            undercover_conditions = int(elem.attrib['missed'])
            conditions_to_cover = int(
                elem.attrib['covered']) + undercover_conditions
        elif(elem.attrib['type'] == 'LINE'):
            undercover_lines = int(elem.attrib['missed'])
            lines_to_cover = int(elem.attrib['covered']) + undercover_lines
            lc = lines_to_cover - undercover_lines


def calculate_code_coverage():
    code_coverage = (conditions_to_cover - undercover_conditions + lc) \
        / (conditions_to_cover + lines_to_cover)
    print(code_coverage)


calculate_code_coverage()

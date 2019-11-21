import os
import xml.etree.ElementTree as ET


class DependencyMetric():
    def __init__(self):
        self.direct_dependencies = 0
        self.indirect_dependencies = 0

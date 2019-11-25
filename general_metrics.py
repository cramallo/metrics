from coverage import Coverage
from dependencies import DependencyMetric

coverage_metric = Coverage()
dependency_metric = DependencyMetric()

print("Code coverage metric:")
print(coverage_metric.calculate_code_coverage())
print("-----------------------")
print("Dependency metric:")
print(dependency_metric.calculate_dependencies_metrics())
print("-----------------------")
print("Quality metric:")

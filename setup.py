from setuptools import setup, find_packages
from pathlib import Path

readme_path = Path(__file__).with_name("README.md")
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")
else:
    long_description = ""

# Runtime dependencies should be modern and flexible so they do not force
# incompatible NumPy versions into downstream environments.
install_requires = [
    "numpy>=1.26",
    "pandas>=2.0",
    "scikit-image>=0.25",
    "scikit-learn>=1.4",
    "graphviz>=0.20.3",
]

setup(
    name='scikitty',
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3.10',
    version='1.0.1',
    description='A package to create Decision Trees like Scikitlearn.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='John Rojas',
    author_email='john.rojas.chinchilla@gmail.com',
    url='https://github.com/JohnRojas222/SciKittyPackage/',
    download_url='https://github.com/JohnRojas222/SciKittyPackage/tarball/0.1',
    keywords=['scikitlearn', 'decision trees', 'metrics'],
    classifiers=[],
    license='MIT',
    include_package_data=True
)
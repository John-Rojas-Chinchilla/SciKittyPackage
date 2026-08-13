from setuptools import setup, find_packages
from pathlib import Path

readme_path = Path(__file__).with_name("README.md")
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")
else:
    long_description = ""

# Inline runtime dependencies to avoid reading files during PEP517 isolated builds.
install_requires = [
    "pandas>=1.5,<3",
    "numpy>=1.24.1,<2",
    "scikit-image>=0.20,<1",
    "scikit-learn>=1.0,<2",
    "scikit-learn-intelex>=2024.4.0,<2025",
    "graphviz>=0.20.3",
]

setup(
    name='scikitty',
    packages=find_packages(),
    install_requires=install_requires,
    version='1.0',
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
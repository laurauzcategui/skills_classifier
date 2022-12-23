import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='skills classifier',
    version='0.1.0',
    author='Laura U',
    author_email='laura@uzcategui.dev',
    description="German Skills Classifier",
    packages=setuptools.find_packages(),
    python_requires='>=3.10',
)
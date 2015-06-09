from distutils.core import setup

setup(
    name='chimera_template',
    version='0.0.1',
    packages=['chimera_template', 'chimera_template.instruments', 'chimera_template.controllers'],
    scripts=[],
    url='http://github.com/astroufsc/chimera-template',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    description='Template for chimera plugins'
)

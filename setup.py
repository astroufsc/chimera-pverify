from distutils.core import setup

setup(
    name='chimera_pverify',
    version='0.0.1',
    packages=['chimera_pverify', 'chimera_pverify.controllers'],
    scripts=['scripts/chimera-pverify'],
    url='http://github.com/astroufsc/chimera-pverify',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    description='Pointing accuracy verification and correction with Astrometry.net'
)

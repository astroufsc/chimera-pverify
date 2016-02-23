chimera-pverify plugin
======================

Plugin for automatically verify (and correct) the pointing of telescopes using chimera and Astrometry.net
https://github.com/astroufsc/chimera.

Usage
-----

Install this plugin and add it as a controller to your `chimera.config` file. Then, follow the instructions given by
`chimera-pverify --help`.


Installation
------------

This plugins depends of SExtractor http://www.astromatic.net/software/sextractor and Astrometry.net `solve-field`
command line tool working with the necessary astrometry databases.

For more info on installing astrometry.net: http://astrometry.net/use.html

::

    pip install -U git+https://github.com/astroufsc/chimera-pverify.git


Configuration Example
---------------------

::

    controllers:
      - type: PointVerify
        name: pv
        telescope: /FakeTelescope/fake      # Telescope to verify pointing.
        camera: /FakeCamera/fake            # Camera attached to the telescope.
        filterwheel: /FakeCamera/fake       # Filterwheel, if exists.
        exptime:  10.0                      # Exposure time.
        filter: R                           # Filter to expose.
        max_fields: 100                     # Maximum number of Landlodt fields to use.
        max_tries: 5                        # Maximum number of tries to point the telescope correctly.
        dec_tolerance: 0.0167               # Maximum declination error tolerance (degrees).
        ra_tolerance: 0.0167                # Maximum right ascension error tolerance (degrees).


Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera-pverify/

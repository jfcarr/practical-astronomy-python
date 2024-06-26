# practical-astronomy-python

Algorithms from [Practical Astronomy with your Calculator or Spreadsheet](https://www.amazon.com/Practical-Astronomy-your-Calculator-Spreadsheet/dp/1108436072) by Peter Duffett-Smith, implemented in Python 3.  API documentation is published [here](https://jfcarr.github.io/practical-astronomy-python/).

If you're interested in this topic, please buy the book!  It provides far more detail and context.

## Quick Start

Install:

```bash
pip install practical-astronomy
```

Create `easter.py`:

```python
import practical_astronomy.pa_datetime as pd

print(pd.get_date_of_easter(2024))
```

Run it:

```bash
python easter.py
```

Result:

```
(3, 31, 2024)
```

## Unit Tests

If you clone the [repo](https://github.com/jfcarr/practical-astronomy-python) locally, you can run unit tests with the Make utility:

```
make all-tests
```

## Library Functions

Documentation [here](https://jfcarr.github.io/practical-astronomy-python/).

### Date/Time

Type | Description
-----|------------
Calculate | Date of Easter
Convert | Civil Date to Day Number
Convert | Greenwich Date <-> Julian Date
Convert | Julian Date to Day-of-Week
Extract | Day, Month, and Year parts of Julian Date
Convert | Civil Time <-> Decimal Hours
Extract | Hour, Minutes, and Seconds parts of Decimal Hours
Convert | Local Civil Time <-> Universal Time
Convert | Universal Time <-> Greenwich Sidereal Time
Convert | Greenwich Sidereal Time <-> Local Sidereal Time

### Coordinates

Type | Description
-----|------------
Convert | Angle <-> Decimal Degrees
Convert | Right Ascension <-> Hour Angle
Convert | Equatorial Coordinates <-> Horizon Coordinates
Calculate | Obliquity of the Ecliptic
Convert | Ecliptic Coordinates <-> Equatorial Coordinates
Convert | Equatorial Coordinates <-> Galactic Coordinates
Calculate | Angle between two objects
Calculate | Rising and Setting times for an object
Calculate | Precession (corrected coordinates between two epochs)
Calculate | Nutation (in ecliptic longitude and obliquity) for a Greenwich date
Calculate | Effects of aberration for ecliptic coordinates
Calculate | RA and Declination values, corrected for atmospheric refraction and geocentric parallax
Calculate | Heliographic coordinates
Calculate | Carrington rotation number
Calculate | Selenographic (lunar) coordinates (sub-Earth and sub-Solar)

### The Sun

Type | Description
-----|------------
Calculate | Approximate and precise positions of the Sun
Calculate | Sun's distance and angular size
Calculate | Local sunrise and sunset
Calculate | Morning and evening twilight
Calculate | Equation of time
Calculate | Solar elongation

### Planets

Type | Description
-----|------------
Calculate | Approximate and precise position of planet
Calculate | Visual aspects of planet (distance, angular diameter, phase, light time, position angle of bright limb, and apparent magnitude)
Calculate | Position of comet (elliptical and parabolic)
Calculate | Binary star orbit data

### The Moon

Type | Description
-----|------------
Calculate | Approximate and precise position of Moon
Calculate | Moon phase and position angle of bright limb
Calculate | Times of new Moon and full Moon
Calculate | Moon's distance, angular diameter, and horizontal parallax
Calculate | Local moonrise and moonset

### Eclipses

Type | Description
-----|------------
Calculate | Lunar eclipse occurrence and circumstances
Calculate | Solar eclipse occurrence and circumstances

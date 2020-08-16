#!/usr/bin/python3

import lib.pa_planet as PP
import unittest as UT

lct_hour = 22 
lct_min = 0 
lct_sec = 0 
is_daylight_saving = True 
zone_correction_hours = -5 
local_date_day = 7 
local_date_month = 10 
local_date_year = 2019 
planet_name = "Uranus"

planet_ra_hour, planet_ra_min, planet_ra_sec, planet_dec_deg, planet_dec_min, planet_dec_sec = PP.precise_position_of_planet(lct_hour,lct_min,lct_sec,is_daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year,planet_name)

print(f"Precise position of planet: [Local Time] {lct_hour}:{lct_min}:{lct_sec} [DST?] {is_daylight_saving} [Zone Correction] {zone_correction_hours} [Local Date] {local_date_month}/{local_date_day}/{local_date_year} [Planet] {planet_name} = [Right Ascension] {planet_ra_hour}h {planet_ra_min}m {planet_ra_sec}s [Declination] {planet_dec_deg}d {planet_dec_min}m {planet_dec_sec}s")



#!/bin/bash

./pa-cli.py --doe --year 2019
./pa-cli.py --cd_to_dn --cd "2/1/2019"
./pa-cli.py --gd_to_jd --gd "6/19.75/2009"
./pa-cli.py --jd_to_gd --jd 2455002.25
./pa-cli.py --ct_to_dh --ct "18:31:27"
./pa-cli.py --dh_to_ct --dh 18.52416667
./pa-cli.py --lct_to_ut --cd "7/1/2013" --ct "3:37:00" --zc 4 --dst
./pa-cli.py --ut_to_lct --cd "6/30/2013" --ut "22:37:00" --zc 4 --dst
./pa-cli.py --ut_to_gst --ut "14:36:51.67" --gd "4/22/1980"
./pa-cli.py --gst_to_ut --gst "4:40:5.23" --gd "4/22/1980"
./pa-cli.py --gst_to_lst --gst "4:40:5.23" --gl -64
./pa-cli.py --lst_to_gst --lst "0:24:5.23" --gl -64
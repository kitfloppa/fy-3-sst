# ================================ Main info ================================
# File name: iquam_nc_to_csv.py
# Authot: Timofeev A.N, Vladivostok, FEFU
# Description: This script transform iqua file in netCDF4 format from FTP,
# FTP: ftp://ftp.star.nesdis.noaa.gov/pub/socd/sst/iquam/v2.10/ to CSV file.
# ===========================================================================

import os
import ftplib
import urllib

def download_file(url: str, out_path: str) -> None:
    """
    Download file from <url>

    :param url: URL to file
    :type url: str
    :param out_path: path to save the file to
    :type out_path: str
    """

    filename = os.path.basename(url)  # get the name of the file from the url
    path_with_filename = os.path.join(out_path, filename)  # build the path where the file is saved
    
    if not os.path.isfile(path_with_filename):  # check whether the specified path is an existing regular file or not.
        wget.download(url, out_path)
        print('\n Download Finished')
    else:
        print('{} file already exist.'.format(filename))


def get_filenames(url: str) -> list[str]:
    """

    :param url: URL to files folder
    :type url: str
    """


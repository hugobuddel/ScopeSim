"""
Put functions which connect the IPDB to SimCADO here
Possibly also add the skycalc_cli interface here

Write function to:
0. Connect to the server
1a. Read which packages are available
1b. Look at which packages are available locally
2. Display a list of which packages are available
3. Download a package
4. Unpack into it's own folder

"""
import os
from .. import default_keywords as dkeys
from astropy.io import ascii as ioascii

def data_database():
    return "Sorry Dave"

def get_local_packages(path=None):

    if path is None:
        path = os.path.join(dkeys.PKG_DIR,
                            dkeys.INST_PKG_LOCAL_PATH,
                            dkeys.INST_PKG_LOCAL_DB_NAME)

    if not os.path.exists(path):
        raise FileNotFoundError

    list_of_packages = ioascii.read(path)

    return list_of_packages





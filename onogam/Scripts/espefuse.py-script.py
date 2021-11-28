#!c:\users\onoga\desktop\mydocker\git\sqlite\onogam\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'esptool==3.2','console_scripts','espefuse.py'
__requires__ = 'esptool==3.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('esptool==3.2', 'console_scripts', 'espefuse.py')()
    )

from utils import get_credentials
from constants import *
from emis import EMIS

# Getting login creds
creds = get_credentials()

emis_adapter = EMIS(
    user_id=creds[JSON_K_ID],
    nat_id=creds[JSON_K_NAT],
    user_pass=creds[JSON_K_PASS],
)

try:
    print('[+] Logging In...')
    emis_adapter.login()
    print('[+] Loading Teacher\'s Profile...')
    emis_adapter.get_techer_profile()
    print('[+] Getting PDF statement...')
    emis_adapter.load_statement_pdf()
    emis_adapter.save_pdf()
    print('[+] Openning PDF...')
    emis_adapter.open_pdf()

    input('>> Done')
except BaseException as e:
    input(f'[X] Error caught: {e}')
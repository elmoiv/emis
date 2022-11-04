__import__('warnings').filterwarnings("ignore")
import requests
from constants import *
from utils import *
from exceptions import *
import webbrowser

class EMIS(requests.Session):
    def __init__(self, user_id: str, nat_id: str, user_pass: str):
        super().__init__()
        self.verify = False

        self.user_id = user_id
        self.nat_id = nat_id
        self.user_pass = user_pass
        
        self.cur_url = URL_EMP
        self.raw_pdf = None
        self.pdf_path = None
    
    def login(self):
        resp = self.get(self.cur_url, headers=HEADERS_HOME)
        payload = update_payload(
            LOGIN_PAYLOAD,
            {
                KEY_VIEW_STATE: get_payload_value(resp.text, KEY_VIEW_STATE),
                KEY_VIEW_STATE_GEN: get_payload_value(resp.text, KEY_VIEW_STATE_GEN),
                KEY_EVENT_VALID: get_payload_value(resp.text, KEY_EVENT_VALID),
                KEY_USER_ID: self.user_id,
                KEY_USER_NAT_ID: self.nat_id,
                KEY_USER_PASS: self.user_pass,

            }
        )
        login_resp = self.post(self.cur_url, data=payload, headers=HEADERS_LOGIN)
        if login_resp.url.strip('/') == self.cur_url.strip('/'):
            raise LoginFailedException('Incorrect login data!')
        self.cur_url = login_resp.url

    def get_techer_profile(self):
        resp = self.get(self.cur_url)
        payload = update_payload(
            STATUS_PAYLOAD,
            {
                KEY_VIEW_STATE: get_payload_value(resp.text, KEY_VIEW_STATE),
                KEY_VIEW_STATE_GEN: get_payload_value(resp.text, KEY_VIEW_STATE_GEN),
                KEY_EVENT_VALID: get_payload_value(resp.text, KEY_EVENT_VALID),
            }
        )
        status_resp = self.post(self.cur_url, data=payload, headers=HEADERS_STATUS)
        if status_resp.url.strip('/') == self.cur_url.strip('/'):
            raise ProfileIssueException('Profile net issue!')
        self.cur_url = status_resp.url
    
    def load_statement_pdf(self):
        resp = self.get(self.cur_url)
        payload = update_payload(
            PRINT_PAYLOAD,
            {
                KEY_VIEW_STATE: get_payload_value(resp.text, KEY_VIEW_STATE),
                KEY_VIEW_STATE_GEN: get_payload_value(resp.text, KEY_VIEW_STATE_GEN),
                KEY_EVENT_VALID: get_payload_value(resp.text, KEY_EVENT_VALID),
                KEY_PDF_DATA: get_payload_value(resp.text, KEY_PDF_DATA_RGX).replace('&#39;', '"')
            }
        )
        self.cur_url = resp.url
        self.raw_pdf = self.post(self.cur_url, data=payload, headers=HEADERS_PRINT).content
    
    def save_pdf(self, save_dir=None):
        date = pretty_date()
        self.pdf_path =  os.path.join(
                save_dir or '',
                f'EMIS_STATUS_{date}.pdf'
            )
        pdf_writer = open(
            os.path.join(
                save_dir or '',
                f'EMIS_STATUS_{date}.pdf'
            ),
            'wb'
        )
        pdf_writer.write(self.raw_pdf)
    
    def open_pdf(self):
        webbrowser.open(self.pdf_path)
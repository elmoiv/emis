URL_EMP = 'https://teacher.emis.gov.eg/emp_teacher/'
JSON_FILE = 'emis.json'

JSON_K_ID = 'teacher_id'
JSON_K_NAT = 'national_id'
JSON_K_PASS = 'password'
KEY_VIEW_STATE = '__VIEWSTATE'
KEY_VIEW_STATE_GEN = '__VIEWSTATEGENERATOR'
KEY_EVENT_VALID = '__EVENTVALIDATION'
KEY_USER_ID = 'ctl00$ContentPlaceHolder1$TextBox1'
KEY_USER_NAT_ID = 'ctl00$ContentPlaceHolder1$TextBox2'
KEY_USER_PASS = 'ctl00$ContentPlaceHolder1$TextBox3'
KEY_PDF_DATA = '__CRYSTALSTATEctl00$ContentPlaceHolder1$CrystalReportViewer1'
KEY_PDF_DATA_RGX = KEY_PDF_DATA.replace('$', r'\$')
LOGIN_PAYLOAD = {
    KEY_VIEW_STATE: '',
    KEY_VIEW_STATE_GEN: '',
    KEY_EVENT_VALID: '',
    KEY_USER_ID: '',
    KEY_USER_NAT_ID: '',
    KEY_USER_PASS: '',
    'ctl00$ContentPlaceHolder1$Button2':'تسجيل دخول'
}
STATUS_PAYLOAD = {
    KEY_VIEW_STATE: '',
    KEY_VIEW_STATE_GEN: '',
    KEY_EVENT_VALID: '',
    '__EVENTARGUMENT': '',
    '__EVENTTARGET':'ctl00$LinkButton1',
}
PRINT_PAYLOAD = {
    KEY_VIEW_STATE: '',
    KEY_VIEW_STATE_GEN: '',
    KEY_EVENT_VALID: '',
    KEY_PDF_DATA: '',
    '__EVENTARGUMENT': '{"text":"PDF", "range":"false", "tb":"crexport"}',
    '__EVENTTARGET':'ctl00$ContentPlaceHolder1$CrystalReportViewer1',
    'CrystalReportViewer1_toptoolbar_search_textField': 'Find...',
    'text_CrystalReportViewer1_toptoolbar_selectPg': '1 of 1',
    'text_CrystalReportViewer1_toptoolbar_zoom': '100%',
}
HEADERS_HOME = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
HEADERS_LOGIN = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "Referer": "https://teacher.emis.gov.eg/emp_teacher/",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
HEADERS_STATUS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "Referer": "https://teacher.emis.gov.eg/emp_teacher/Alert_Rec.aspx",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
HEADERS_PRINT = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "pragma": "no-cache",
    "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "iframe",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "Referer": "https://teacher.emis.gov.eg/emp_teacher/crevision.aspx",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
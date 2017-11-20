#HOST_IP = 10.0.0.214
SECRET_KEY = 'RIvJZJNplu0qr2iLmFAOMg31hRpGo/3fhfcXqmNYDE0'
DEBUG = True
ELASTALERT_PATH = '/Users/hades/Documents/GitHub/elastalert'
DATABASE_PATH = '/Users/hades/Documents/GitHub/ElastAlertGUI/database.db'
RULES_PATH = '/Users/hades/Documents/GitHub/elastalert/rules/'
BACKUP_PATH = '/Users/hades/Documents/GitHub/elastalert/backup/'
MAIN_CONFIG = '/Users/hades/Documents/GitHub/elastalert/config.yaml'
INDEX_TYPES = [('logstash-supplier-log-*','logstash-supplier-log-*')]
RULE_TYPES = [('frequency','frequency')]
ALERT_TYPES = [('email','email'),('slack','slack'),('wechat','wechat')]
SEARCH_TYPE = [('time_out','time_out'),('third_part_error','third_part_error')]
CONDITION_TYPE = [('curlErrMsg','curlErrMsg'),('reqtime','reqtime'),('error_code','error_code')]
#will be change to sql query
SUPPLIER_ID = [('woyao2','woyao2'),('woyao','woyao')]
API_ID = [('208','208'),('207','207')]
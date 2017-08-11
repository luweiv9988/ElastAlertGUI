SECRET_KEY = 'RIvJZJNplu0qr2iLmFAOMg31hRpGo/3fhfcXqmNYDE0'
DEBUG = True
ELASTALERT_PATH = '/opt/elastalert/'
DATABASE_PATH = '/var/www/html/ElasAlertGUI/database.db'
RULES_PATH = '/opt/elastalert/rules/'
BACKUP_PATH = '/opt/elastalert/backup/'
MAIN_CONFIG = '/opt/elastalert/config.yaml'
DOC_TYPES = [('apache_web_server','apache_web_server'),
            ('asterisk_ivr','asterisk_ivr'),
            ('asterisk_vcc','asterisk_vcc'),
            ('jboss_broker_server','jboss_broker_server'),
            ('jboss_call_server','jboss_call_server'),
            ('apache_call_server','apache_call_server'),
            ('cassandra','cassandra'),
            ('jboss_sb_server','jboss_sb_server'),
            ('jboss_csr_server','jboss_csr_server'),
            ('eservices','eservices'),
            ('gir','gir'),
            ('gvp_csmf','gvp_csmf'),
            ('gvp_mcp','gvp_mcp'),
            ('gvp_rm','gvp_rm'),
            ('gvp_rs','gvp_rs'),
            ('gvp_sips','gvp_sips'),
            ('gws','gws'),
            ('jboss_hornetq_live_server','jboss_hornetq_live_server'),
            ('jboss_hornetq_backup_server','jboss_hornetq_backup_server'),
            ('htcc','htcc'),
            ('jboss_lgt_server','jboss_lgt_server'),
            ('mail','mail'),
            ('nuance','nuance'),
            ('jboss_ocmeng_server','jboss_ocmeng_server'),
            ('jboss_ocmweb_server','jboss_ocmweb_server'),
            ('opensips','opensips'),
            ('jboss_out_server','jboss_out_server'),
            ('psphp','psphp'),
            ('jboss_rpt_server','jboss_rpt_server'),
            ('rws','rws'),
            ('jboss_sbapi_server','jboss_sbapi_server'),
            ('jboss_sms_server','jboss_sms_server'),
            ('audiocodes','audiocodes'),
            ('vom','vom'),
            ('jboss_sb_server','jboss_sb_server'),
            ('webrtc','webrtc')]
RULE_TYPES = [('frequency','frequency')]
ALERT_TYPES = [('email','email')]

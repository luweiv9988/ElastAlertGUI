from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
#from config import DOC_TYPES, RULE_TYPES, ALERT_TYPES
from config import RULE_TYPES, ALERT_TYPES

class LoginForm(FlaskForm):
    user_login = StringField('user_login', validators=[DataRequired("Please enter your login")])
    user_password = PasswordField('user_password', validators=[DataRequired("Please enter your password")])

class PassChangeForm(FlaskForm):
    old_pass = PasswordField('user_password_old_pass', validators=[DataRequired("Please enter your old password")])
    new_pass1 = PasswordField('user_password_new_pass', validators=[DataRequired("Please enter your new password")])
    new_pass2 = PasswordField('user_password_new_pass1', validators=[DataRequired("Please repeat your new password")])

class RuleForm(FlaskForm):
    name = StringField('name', validators=[DataRequired("Please enter rule name")])
    type = SelectField('type', choices=RULE_TYPES, validators=[DataRequired("Please enter rule type")])
    index = StringField('index', default='logstash-supplier-log-*', validators=[DataRequired("Please enter index name")])
    num_events = StringField('num_events', default='1', validators=[DataRequired("Please enter num events")])
    timeframe = StringField('timeframe', default='1', validators=[DataRequired("Please enter time frame")])
    timeframe2 = SelectField('timeframe2', choices=[('seconds:', 'seconds'), ('minutes:', 'minutes'), ('hours:', 'hours'), ('days:', 'days'), ('weeks:', 'weeks')], validators=[DataRequired()])
    filter = StringField('filter', default='http:404', validators=[DataRequired("Please enter Elasticsearch Condition")])
    ## just remove one filed ,it will be add in next version
    #filter = SelectField('filter', choices=DOC_TYPES, validators=[DataRequired("Please enter filter type")]) 
    #filter2 = StringField('filter2', default='Your Search...', validators=[DataRequired("Please enter filter query")])
    alert = SelectField('alert', choices=ALERT_TYPES, validators=[DataRequired("Please enter alert type")])
    email = StringField('email', default='luwei@think-land.com', validators=[DataRequired("Please enter emails addresses")])
    smtp_auth_file = StringField('smtp_auth_file',default='smtp_auth_file.yaml', validators=[DataRequired("Please enter smtp auth path")])
    smtp_host = StringField('smtp_host',default='smtp.exmail.qq.com', validators=[DataRequired("Please enter smtp_server ip")])
    smtp_port = StringField('smtp_port',default='25', validators=[DataRequired("Please enter smtp_server port")])


    saving_button = SubmitField(label='Save rule')
    goback_button = SubmitField(label='Go Back')

class RulesList(FlaskForm):
    rules_list = SelectField('rules_list', choices=[], coerce=int, validators=[DataRequired()])
    edit_button = SubmitField(label='Edit rule')
    del_button = SubmitField(label='Delete rule')

class TextEditForm(FlaskForm):
    text = TextAreaField('text', render_kw={"rows": 20, "cols": 50}, validators=[DataRequired()])
    saving_button = SubmitField(label='Save')
    goback_button = SubmitField(label='Go Back')

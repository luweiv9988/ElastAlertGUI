#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from config import RULE_TYPES, ALERT_TYPES, INDEX_TYPES
from config import RULE_TYPES, ALERT_TYPES, API_ID, SUPPLIER_ID

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
    index = SelectField('index', choices=INDEX_TYPES, validators=[DataRequired("Please choose index name")])
    num_events = StringField('num_events', default='10', validators=[DataRequired("Please enter num events")])
    timeframe = StringField('timeframe', default='1', validators=[DataRequired("Please enter time frame")])
    timeframe2 = SelectField('timeframe2', choices=[('seconds:', 'seconds'), ('minutes:', 'minutes'), ('hours:', 'hours'), ('days:', 'days'), ('weeks:', 'weeks')], validators=[DataRequired()])
    supplierId = SelectField('supplierId', choices=SUPPLIER_ID, validators=[DataRequired("Please enter apiId query")])
    apiId = SelectField('apiId', choices=API_ID, validators=[DataRequired("Please enter apiId query")])
    filter = StringField('filter', default='curlErrMsg:CURLE_OPERATION_TIMEDOUT', validators=[DataRequired("Please enter Kibana query")])  
    alert = SelectField('alert', choices=ALERT_TYPES, validators=[DataRequired("Please choose alert type")])
    alert_subject = StringField('alert_subject', default='供应商日志报警:{0} ---> apiId:{1} 发生请求超时', validators=[DataRequired("Please enter alert_subject")])
    alert_text = StringField('alert_text',default='---> 供应商名称:{0} 供应商ID:{1} apiId:{2} 在2分钟内reqtime大于8秒发生至少10次', validators=[DataRequired("Please enter alert_text")])
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

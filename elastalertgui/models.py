class User():

    def __init__(self,user_id,name,password,active = True):
        self.id = user_id
        self.name = name
        self.password = password
        self.active = active

    def is_authenticated():
        return True
        #return true if user is authenticated, provided credentials

    def is_active():
        return True
        #return true if user is activte and authenticated

    def is_annonymous():
        return False
        #return true if annon, actual user return false

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.name)

class RuleObj():

    def __init__(self,name = '',type = '',index = '',num_events = '',
                timeframe2 = '', timeframe = '', supplierId = '', apiId = '', 
                filter = '', alert_subject = '', alert_subject_args = '', alert = ''):
        self.name = name
        self.type = type
        self.index = index
        self.num_events = num_events
        self.timeframe2 = timeframe2
        self.timeframe = timeframe
        self.supplierId = supplierId
        self.apiId = apiId
        self.filter = filter
        self.alert = alert
        self.alert_subject = alert_subject
        self.alert_subject_args = alert_subject_args

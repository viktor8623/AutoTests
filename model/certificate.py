


class Certificate:

    def __init__(self, type, activity=None, first_tickets_type=None, second_tickets_type=None, third_tickets_type=None,
                 initial_amount=None, remain_amount=None, name_first_tickets_type=None,
                 name_second_tickets_type=None, name_third_tickets_type=None, id_testdata=None,
                 first_name="Automated test", last_name="By Viktor", email="test123@email.com"):
        self.type = type
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.activity = activity
        self.first_tickets_type = first_tickets_type
        self.second_tickets_type = second_tickets_type
        self.third_tickets_type = third_tickets_type
        self.name_first_tickets_type = name_first_tickets_type
        self.name_second_tickets_type = name_second_tickets_type
        self.name_third_tickets_type = name_third_tickets_type
        self.initial_amount = initial_amount
        self.remain_amount = remain_amount
        self.id = id_testdata


    def __repr__(self):
        return "%s" % (self.id)
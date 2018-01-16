from model.certificate import Certificate


testdata = [
    Certificate(type="Activity Tickets", activity="Dead of Night Tour", first_tickets_type="3", second_tickets_type="3",
                third_tickets_type=None, initial_amount="120.00", remain_amount=None,
                name_first_tickets_type="Adult", name_second_tickets_type="Child", name_third_tickets_type=None,
                first_name="John", last_name="Graham-Cumming", email="test123@email.com", id_testdata="GoDo-32"),
    # GoDo-32 Purchasing certificate with number of tickets (120$, Check)

    Certificate(type="Specific Dollar Amount", activity=None, first_tickets_type=None, second_tickets_type=None,
                third_tickets_type=None, initial_amount="1000.00", remain_amount=None, name_first_tickets_type=None,
                name_second_tickets_type=None, name_third_tickets_type=None, first_name="Patrick",
                last_name="McKenzie", email="John.Mathew@xyz.com", id_testdata="GoDo-21"),
    # GoDo-21 Purchasing certificate with Specific Dollar Amount (1000$,cash)

    Certificate(type="Activity Tickets", activity="Beyond Good and Evil Tours", first_tickets_type="5",
                second_tickets_type="5", third_tickets_type=None, initial_amount="250.00", remain_amount=None,
                name_first_tickets_type="Adult", name_second_tickets_type="Child", name_third_tickets_type=None,
                first_name="Jose Eduardo", last_name="Santos Tavares Melo Silva", email="test123@email.com",
                id_testdata="GoDo-31"),
    # GoDo-31 Purchasing certificate with number of tickets (250$, credit card)

    Certificate(type="Specific Dollar Amount", activity=None, first_tickets_type=None, second_tickets_type=None,
                third_tickets_type=None, initial_amount="500.00", remain_amount=None, name_first_tickets_type=None,
                name_second_tickets_type=None, name_third_tickets_type=None, first_name="Lauren-May",
                last_name="e Silva", email="test123@email.com", id_testdata="GoDo-22"),
    # GoDo-22 Purchasing certificate with Specific Dollar Amount (500$, credit card)

    Certificate(type="Specific Dollar Amount", activity=None, first_tickets_type=None, second_tickets_type=None,
                third_tickets_type=None, initial_amount="100.00", remain_amount=None, name_first_tickets_type=None,
                name_second_tickets_type=None, name_third_tickets_type=None, first_name="John Q.",
                last_name="Public", email="test123@email.com", id_testdata="GoDo-23"),
    # GoDo-23 Purcahsing certificate with Specific Dollar Amount (100$, Check)

    Certificate(type="Activity Tickets", activity="AlertTest", first_tickets_type="5", second_tickets_type="10",
                third_tickets_type=None, initial_amount="1000.00", remain_amount=None,
                name_first_tickets_type="Adult", name_second_tickets_type="Child", name_third_tickets_type=None,
                first_name="J", last_name="O'brian", email="test123@email.com", id_testdata="GoDo-30"),
    # GoDo-30 Purchasing certificate with number of tickets (1000$, cash)

    Certificate(type="Activity Tickets", activity="Beyond Good and Evil Tours", first_tickets_type="10",
                second_tickets_type="10", third_tickets_type=None, initial_amount="500.00", remain_amount=None,
                name_first_tickets_type="Adult", name_second_tickets_type="Child", name_third_tickets_type=None,
                first_name="de' Medici", last_name="J", email="test123@email.com", id_testdata="GoDo-47"),
    # GoDo-47 Customer-Facing - Purchasing certificate with number of tickets
]
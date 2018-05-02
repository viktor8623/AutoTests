from model.tickets import Tickets


testdata = [

    Tickets(id_testdata="GoDo-473",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", first_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT", first_name="Benjamin",
            last_name="McLane Spock", phone="15044466025", email="godo-473@mailinator.com", zip_code="35801",
            payment_type="Credit Card", card_number="4000056655665556", card_date="1020", card_cvc="303",
            card_zip="35801", ticket_total="$30.00", discount="- $0.00", gift_certificate="- $0.00", taxes="$1.50",
            booking_fee="$0.00", grand_total="$31.50"),

    # GoDo-473 Credit card payment - Visa (debit).

    Tickets(id_testdata="GoDo-474",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", first_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT", first_name="Donna",
            last_name="Macris", phone="15044466025", email="godo-474@mailinator.com", zip_code="35801",
            payment_type="Credit Card", card_number="5555555555554444", card_date="1020", card_cvc="303",
            card_zip="35801", ticket_total="$30.00", discount="- $0.00", gift_certificate="- $0.00", taxes="$1.50",
            booking_fee="$0.00", grand_total="$31.50"),

    # GoDo-474 Credit card payment - Mastercard.

    Tickets(id_testdata="GoDo-475",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", first_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT",
            first_name="Antonie Frederik Jan Floris Jacob",
            last_name="van Omphal", phone="15044466025", email="godo-475@mailinator.com", zip_code="83254",
            payment_type="Credit Card", card_number="5200828282828210", card_date="1020", card_cvc="303",
            card_zip="83254", ticket_total="$30.00", discount="- $0.00", gift_certificate="- $0.00", taxes="$1.50",
            booking_fee="$0.00", grand_total="$31.50"),

    # GoDo-475 Credit card payment - Mastercard (debit).

    Tickets(id_testdata="GoDo-476",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", first_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT",
            first_name="James", last_name="Boswell", phone="15044466025",
            email="godo-476@mailinator.com", zip_code="60641", payment_type="Credit Card",
            card_number="2223003122003222", card_date="1020", card_cvc="303", card_zip="83254", ticket_total="$30.00",
            discount="- $0.00", gift_certificate="- $0.00", taxes="$1.50", booking_fee="$0.00", grand_total="$31.50"),

    # GoDo-476 Credit card payment - Mastercard (2-series).

    Tickets(id_testdata="GoDo-477",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", first_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT", first_name="Ralph",
            last_name="Ueltzhoeffer", phone="15044466025", email="godo-477@mailinator.com", zip_code="62701",
            payment_type="Credit Card", card_number="5105105105105100", card_date="1020", card_cvc="303",
            card_zip="62701", ticket_total="$30.00", discount="- $0.00", gift_certificate="- $0.00", taxes="$1.50",
            booking_fee="$0.00", grand_total="$31.50"),

    # GoDo-477 Credit card payment - Mastercard (prepaid).

    Tickets(id_testdata="GoDo-478",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", first_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT", first_name="Jacques-Pierre",
            last_name="Amette", phone="15044466025", email="godo-478@mailinator.com", zip_code="67221",
            payment_type="Credit Card", card_number="378282246310005", card_date="1020", card_cvc="3031",
            card_zip="67221", ticket_total="$30.00", discount="- $0.00", gift_certificate="- $0.00", taxes="$1.50",
            booking_fee="$0.00", grand_total="$31.50"),

    # GoDo-478 Credit card payment - American Express.

    Tickets(id_testdata="GoDo-479",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", first_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT",
            first_name="Simone Lucie Ernestine Marie Bertrand", last_name="de Beauvoir", phone="15044466025",
            email="godo-479@mailinator.com",
            zip_code="70119", payment_type="Credit Card", card_number="6011111111111117", card_date="1020",
            card_cvc="303", card_zip="70119", ticket_total="$30.00", discount="- $0.00", gift_certificate="- $0.00",
            taxes="$1.50", booking_fee="$0.00", grand_total="$31.50"),

    # GoDo-479 Credit card payment - Discover.

    Tickets(id_testdata="GoDo-480",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", second_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT",
            first_name="Henri", last_name="Fauconnier", phone="15044466025",
            email="godo-480@mailinator.com", zip_code="02137", payment_type="Credit Card",
            card_number="30569309025904", card_date="1020", card_cvc="303", card_zip="02137", ticket_total="$20.00",
            discount="- $0.00", gift_certificate="- $0.00", taxes="$1.00", booking_fee="$0.00", grand_total="$21.00"),

    # GoDo-480 Credit card payment - Diners Club.

    Tickets(id_testdata="GoDo-481",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", second_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT", first_name="Johnny",
            last_name="Dawkins", phone="15044466025", email="godo-481@mailinator.com", zip_code="87506",
            payment_type="Credit Card", card_number="3566002020360505", card_date="1020", card_cvc="303",
            card_zip="87506", ticket_total="$20.00", discount="- $0.00", gift_certificate="- $0.00", taxes="$1.00",
            booking_fee="$0.00", grand_total="$21.00"),

    # GoDo-481 Credit card payment - JCB.

    Tickets(id_testdata="GoDo-482",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", second_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT", first_name="Matt",
            last_name="Harpring", phone="15044466025", email="godo-482@mailinator.com", zip_code="10048",
            payment_type="Credit Card", card_number="4000001240000000", card_date="1020", card_cvc="303",
            card_zip="P0P 0B4", ticket_total="$20.00", discount="- $0.00", gift_certificate="- $0.00", taxes="$1.00",
            booking_fee="$0.00", grand_total="$21.00"),

    # GoDo-482 Credit card payment - Visa, Canada.

    Tickets(id_testdata="GoDo-483",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", second_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT", first_name="Billy",
            last_name="Cunningham", phone="15044466025", email="godo-483@mailinator.com", zip_code="22223",
            payment_type="Credit Card", card_number="4000004840000008", card_date="1020", card_cvc="303",
            card_zip="22223", ticket_total="$20.00", discount="- $0.00", gift_certificate="- $0.00", taxes="$1.00",
            booking_fee="$0.00", grand_total="$21.00"),

    # GoDo-483 Credit card payment - Visa, Mexico.

    Tickets(id_testdata="GoDo-484",
            customer_URL="https://dev.godo.io.com/customer_facing.aspx?Activity=f571b951-4cc6-4101-9628-01432bc7988b",
            activity="Beyond Good and Evil Tours", second_tickets_type="1", name_first_tickets_type="Adult",
            name_second_tickets_type="Child", year="2018", month="5", day="3", time="4:15 PM CT", first_name="Tom",
            last_name="McMillen", phone="15044466025", email="godo-484@mailinator.com", zip_code="22223",
            payment_type="Credit Card", card_number="4000008260000000", card_date="1020", card_cvc="303",
            card_zip="SE23 1PJ", ticket_total="$20.00", discount="- $0.00", gift_certificate="- $0.00", taxes="$1.00",
            booking_fee="$0.00", grand_total="$21.00"),

    # GoDo-484 Credit card payment - Visa, United Kingdom.

]

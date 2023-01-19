#!/usr/bin/env python
# coding: utf-8

# ### TKinter Project No. 1: VMGA Loan System
# Developer: Galinato, Valfrid G.
# 
# Start Date: Oct. 5, 2022
# 
# End Date: Oct. 27, 2022 (v1.0)
# 
# ### Goals:
# Develop an application that can do the following:
# - connect to a database that can store information
# - has a simple yet efficient graphics user interface (GUI) that is useful for user interaction
# - is portable and can be used on any Windows devices
# 
# Features of the application are:
# - a subpanel containing labels and entries (of each detail below), and button (add personal record to database) widgets that is useful to add personal record that will store the following in the tables of the database:
#     - debtor's details table:
#         - name
#         - age
#         - sex
#         - address
#         - contact no.
# - another subpanel containing labels and entries (of each detail below), and button (add transaction to database) widgets that is useful to add transaction that will store the following in the tables of the database:
#     - debt's details table:
#         - debt date
#         - loaned amount
#         - interest amount
#         - total amount (automated calculation; formula = loaned amount + interest amount)
#     - payment's details table:
#         - payment date
#         - amount paid
#         - balance amount (automated calculation; formula = total amount - amount paid)
# - a subpanel containing labels and entries (of debtor's name detail), and button (edit selected existing debtor's personal record OR remove selected debtor's personal record and their debts) widgets that is useful to either:
#     - edit an existing personal record in the selected debtor's details table by looking up the debtor's name; OR
#         - note: there must be no option to edit debt's details for security reasons
#     - remove the selected debtor's details, including their debt history
# - another subpanel containing labels and entries (of debtor's name detail), and button (view all debtors' details OR view all debt history OR view all payment history) widgets that is useful to either:
#     - show a list of debtors and their details in a tabular screen in the interface; OR
#     - show all debt history of all debtors
#         - note: this option must have sort options (sort by alphabetical name OR gender OR debt date OR balance amount
#     - show all payment history of all debtors
#         - note: this option must have sort options (sort by alphabetical name OR gender OR payment date OR balance amount
# - a subpanel that will serve as the display screen of any sort of data that the user wants to see (list of debtors and their details OR view all debt history OR view all payment history)

# In[ ]:


# START OF THE PROGRAM CODE: INITIALIZATION AND DATABASE CONNECTION UPON STARTUP
# import tkinter (for GUI), ttk (for tree/table), and sqlite3 (for SQL) modules
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import sqlite3

# create root widget or main window
root = Tk()

# set title to show in title bar
root.title('VMGA Loan System v1.0')

# set main window size and disable resizing
root.geometry('1050x690')
root.resizable(False, False)

# create a main frame that is separate from the root window then place it by filling all sides equally
main = Frame(root)
main.pack(fill = BOTH, expand = 1)

# create a canvas then place it in the main frame by filling from left side outwards equally
canvas = Canvas(main)
canvas.pack(side = LEFT, fill = BOTH, expand = 1)

# add a scrollbar by putting it in the main frame but is attached and can move canvas contents vertically
scrollbar = ttk.Scrollbar(main, orient = VERTICAL, command = canvas.yview)
scrollbar.pack(side = RIGHT, fill = Y)

# configure the canvas then use yscrollcommand argument to allow it to move vertically
canvas.configure(yscrollcommand = scrollbar.set)

# bind the configuration by passing mouse even (lambda e) into the area to scroll using canvas.configure
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox('all')))

# create another frame inside the canvas that will now contain widgets you want the user to scroll into
sub = Frame(canvas)

# add the sub frame to a window in the canvas
canvas.create_window((0, 0), window = sub, anchor = 'nw')

# use tkFont to change default font of the entire program
default_font = tkFont.nametofont('TkDefaultFont')
default_font.configure(family = 'Candara', size = 13)
root.option_add("*Font", default_font)

# create a database OR connect to an existing one
conn = sqlite3.connect('vmga-loan-system-database.db')

# create a cursor to be used in executing SQL commands
c = conn.cursor()


# In[ ]:


# FIRST PART OF THE PROGRAM CODE: FUNCTION FOR BUTTON TO ADDING NEW DEBTOR'S RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# a function containing instructions that addDebtorB_1 button will execute once clicked
def addRecord():
    # get inputs from entry widgets and store them in their respective variables
    name = nameE_1.get()
    age = ageE_1.get()
    sex = sexE_1.get()
    address = addressE_1.get()
    contact = contactE_1.get()
    
    # delete contents of the entry widgets after retrieving inputted values
    nameE_1.delete(0, END)
    ageE_1.delete(0, END)
    sexE_1.delete(0, END)
    addressE_1.delete(0, END)
    contactE_1.delete(0, END)
    
    # create a database OR connect to an existing one within this function
    conn = sqlite3.connect('vmga-loan-system-database.db')

    # create a cursor to be used in executing SQL commands
    c = conn.cursor()
    
    # use the created cursor to execute an SQL command of inserting user-inputted data to the table
    c.execute("INSERT INTO debtor_details ('name', 'age', 'sex', 'address', 'contact_no') VALUES (?, ?, ?, ?, ?)", (name, age, sex, address, contact))
    
    # commit the changes made within this function to the database
    conn.commit()
    
    # close the database connection within this function
    conn.close()


# In[ ]:


# SECOND PART OF THE PROGRAM CODE: PANEL FOR ADDING NEW DEBTOR'S RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# create a panel for adding new debtor's records
addDebtorPanel = LabelFrame(sub, text = "ADD NEW DEBTOR'S RECORDS", padx = 10, pady = 5, width = 405, height = 230)

# add label and entry widgets for 'name' detail
nameL_1 = Label(addDebtorPanel, text = 'Name: ')
nameE_1 = Entry(addDebtorPanel, width = 30)

# add label and entry widgets for 'age' detail
ageL_1 = Label(addDebtorPanel, text = 'Age: ')
ageE_1 = Entry(addDebtorPanel, width = 30)

# add label and entry widgets for 'sex' detail
sexL_1 = Label(addDebtorPanel, text = 'Sex: ')
sexE_1 = Entry(addDebtorPanel, width = 30)

# add label and entry widgets for 'address' detail
addressL_1 = Label(addDebtorPanel, text = 'Address: ')
addressE_1 = Entry(addDebtorPanel, width = 30)

# add label and entry widgets for 'contact no.' detail
contactL_1 = Label(addDebtorPanel, text = 'Contact No.: ')
contactE_1 = Entry(addDebtorPanel, width = 30)

# add button widget for 'add new record'
addDebtorB_1 = Button(addDebtorPanel, text = 'ADD NEW RECORD', command = addRecord)


# In[ ]:


# THIRD PART OF THE PROGRAM CODE: FUNCTION FOR BUTTON TO ADDING NEW DEBT RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# a function containing instructions that addDebtB_2 button will execute once clicked
def addDebt():
    # get inputs from entry widgets and store them in their respective variables
    name = nameE_2.get()
    date = dateE_2.get()
    loan = loanE_2.get()
    interest = interestE_2.get()
    total = str(int(loan) + int(interest))
    
    # delete contents of the entry widgets after retrieving inputted values
    nameE_2.delete(0, END)
    dateE_2.delete(0, END)
    loanE_2.delete(0, END)
    interestE_2.delete(0, END)
    
    # create a database OR connect to an existing one within this function
    conn = sqlite3.connect('vmga-loan-system-database.db')
    
    # create a cursor to be used in executing SQL commands
    c = conn.cursor()
    
    # use the created cursor to execute an SQL command of selecting all records from debtor_details table
    c.execute("SELECT * FROM debtor_details")
    
    # use the created cursor to execute an SQL command of fetching selected records
    fetchDebtors = c.fetchall()
    
    # use a for-loop to search through the returned tuple contained in the fetchDebtors variable
    for i in fetchDebtors:
        # if name is in a list within the said tuple...
        if(name in i):
            # ...get the debtor_id stored in index 0 and store it in id variable
            id = i[0]
    
    # use the created cursor to execute an SQL command of inserting user-inputted data to the table
    c.execute("INSERT INTO debt_details ('debtor_id', 'debt_date', 'loaned_amount', 'interest_amount', 'total_amount') VALUES (?, ?, ?, ?, ?)", (id, date, loan, interest, total))
    
    # commit the changes made within this function to the database
    conn.commit()
    
    # close the database connection within this function
    conn.close()


# In[ ]:


# FOURTH PART OF THE PROGRAM CODE: FUNCTION FOR BUTTON TO ADDING NEW PAYMENT RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# a function containing instructions that addPaymentB_3 button will execute once clicked
def addPayment():
    # get inputs from entry widgets and store them in their respective variables
    name = nameE_3.get()
    debtdate = debtdateE_3.get()
    paymentdate = paymentdateE_3.get()
    payment = paymentE_3.get()
    value = firstpayment.get()
    
    # delete contents of the entry widgets after retrieving inputted values
    nameE_3.delete(0, END)
    debtdateE_3.delete(0, END)
    paymentdateE_3.delete(0, END)
    paymentE_3.delete(0, END)
    
    # create a database OR connect to an existing one within this function
    conn = sqlite3.connect('vmga-loan-system-database.db')
    
    # create a cursor to be used in executing SQL commands
    c = conn.cursor()
    
    # use the created cursor to execute an SQL command of selecting all records from debtor_details table
    c.execute("SELECT * FROM debtor_details")
    
    # use the created cursor to execute an SQL command of fetching selected records
    fetchDebtors = c.fetchall()
    
    # use a for-loop to search through the returned tuple contained in the fetchDebtors variable
    for i in fetchDebtors:
        # if name is in a list within the said tuple...
        if(name in i):
            # ...get the debtor_id stored in index 0 and store it in debtorid variable
            debtorid = i[0]
    
    # use the created cursor to execute an SQL command of selecting all records from debt_details table
    c.execute("SELECT * FROM debt_details")
    
    # use the created cursor to execute an SQL command of fetching selected debts
    fetchDebts = c.fetchall()
    
    # use a for-loop to search through the returned tuple contained in the fetchDebts variable
    for i in fetchDebts:
        # if debtdate is in a list within the said tuple...
        if(debtdate in i):
            # ...get the debt_id stored in index 0 and store it in debtid variable...
            debtid = i[0]
            
            # ...and the interest_amount stored in index 4 and store it in interest variable...
            interest = i[4]
            
            # ...and also the total_amount stored in index 5 and store it in total variable
            total = i[5]
    
    # ------------------------PAYMENT PART (ONE DEBT MAY HAVE ONE OR MORE PAYMENTS)------------------------ #
    # INSTANCE ONE (THE CURRENT INSTANCE IS THE FIRST PAYMENT OF THAT SPECIFIC DEBTOR FOR A SPECIFIC DEBT) #
    # if value is 'Yes'...
    if(value == 'Yes'):
        # calculate balance amount by subtracting payment from total
        balance = str(int(total) - int(payment))

        # use the created cursor to execute an SQL command of inserting user-inputted data to the table
        c.execute("INSERT INTO payment_details ('debtor_id', 'debt_id', 'payment_date', 'amount_paid', 'balance_amount') VALUES (?, ?, ?, ?, ?)", (debtorid, debtid, paymentdate, payment, balance))
    
    # INSTANCE TWO (THE CURRENT INSTANCE IS NOT THE FIRST PAYMENT OF THAT SPECIFIC DEBTOR FOR A SPECIFIC DEBT) #
    # if value is not 'Yes'...
    else:
        # use the created cursor to execute an SQL command of selecting all records from payment_details table
        c.execute("SELECT * FROM payment_details")

        # use the created cursor to execute an SQL command of fetching selected payments
        fetchPayments = c.fetchall()

        # a newfetchPayments tuple that will store specific list within the said tuple
        newfetchPayments = []

        # use a for-loop to search through the returned tuple contained in the fetchPayments variable
        for i in fetchPayments:
            # if the specific debtorid and debtid is in a list within the said tuple...
            if(i[1] == debtorid and i[2] == debtid):
                # ...append the list in the newfetchPayments tuple
                newfetchPayments.append(i)

        # a paymentid variable that will store the greatest current paymentid for comparison in for loop below
        paymentid = 0

        # an oldbalance variable that will store the balance of the list with the current greatest paymentid
        oldbalance = 0

        # use a for-loop to search through the stored tuple contained in the newfetchPayments variable
        for i in newfetchPayments:
            if(paymentid == 0 or i[0] > paymentid):
                # ...store the current tuple's payment_id in the paymentid variable...
                paymentid = i[0]

                # ...and also store the current tuple's balance_amount in the oldbalance variable
                oldbalance = i[5]

        # calculate new interest with regards to the current oldbaalance by multiplying oldbalance to 10%
        interest = int(oldbalance) * 0.1
        
        # calculate balance amount by adding oldbalance and interest, then subtracting payment
        balance = str(int(oldbalance) + int(interest) - int(payment))

        # use the created cursor to execute an SQL command of inserting user-inputted data to the table
        c.execute("INSERT INTO payment_details ('debtor_id', 'debt_id', 'payment_date', 'amount_paid', 'balance_amount') VALUES (?, ?, ?, ?, ?)", (debtorid, debtid, paymentdate, payment, balance))
    
    # commit the changes made within this function to the database
    conn.commit()
    
    # close the database connection within this function
    conn.close()


# In[ ]:


# FIFTH PART OF THE PROGRAM CODE: PANEL FOR ADDING NEW DEBT OR PAYMENT TRANSACTION RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# create a panel for adding new transaction records
addTransactionPanel = LabelFrame(sub, text = "ADD NEW DEBTOR'S TRANSACTION", padx = 10, pady = 5, width = 405, height = 510)

# FIRST PART OF THE MAIN PANEL: SUBPANEL FOR ADDING DEBTOR'S DEBT
# create a subframe specifically for adding debtor's debt
addDebtSubpanel = LabelFrame(addTransactionPanel, text = "ADD NEW DEBTOR'S DEBT", padx = 10, pady = 5, width = 380, height = 200)

# add label and entry widgets for 'name' detail
nameL_2 = Label(addDebtSubpanel, text = 'Add Debt to Debtor: ')
nameE_2 = Entry(addDebtSubpanel, width = 21)

# add label and entry widgets for 'debt date' detail
dateL_2 = Label(addDebtSubpanel, text = 'Debt Date: ')
dateE_2 = Entry(addDebtSubpanel, width = 21)

# add label and entry widgets for 'loan amount' detail
loanL_2 = Label(addDebtSubpanel, text = 'Loan Amount: ')
loanE_2 = Entry(addDebtSubpanel, width = 21)

# add label and entry widgets for 'interest amount' detail
interestL_2 = Label(addDebtSubpanel, text = 'Interest Amount: ')
interestE_2 = Entry(addDebtSubpanel, width = 21)

# add button widget for 'add new debt'
addDebtB_2 = Button(addDebtSubpanel, text = 'ADD NEW DEBT', command = addDebt)

# SECOND PART OF THE MAIN PANEL: SUBPANEL FOR ADDING DEBTOR'S PAYMENT
# create a subframe specifically for adding debtor's payment
addPaymentSubpanel = LabelFrame(addTransactionPanel, text = "ADD NEW DEBTOR'S PAYMENT", padx = 10, pady = 5, width = 380, height = 235)

# add label and entry widgets for 'name' detail
nameL_3 = Label(addPaymentSubpanel, text = 'Add Payment to Debtor: ')
nameE_3 = Entry(addPaymentSubpanel, width = 18)

# add label and entry widgets for 'date of debt to pay' detail
debtdateL_3 = Label(addPaymentSubpanel, text = 'Date of Debt to Pay: ')
debtdateE_3 = Entry(addPaymentSubpanel, width = 18)

# add label and entry widgets for 'payment date' detail
paymentdateL_3 = Label(addPaymentSubpanel, text = 'Payment Date: ')
paymentdateE_3 = Entry(addPaymentSubpanel, width = 18)

# add label and entry widgets for 'amount paid' detail
paymentL_3 = Label(addPaymentSubpanel, text = 'Amount Paid: ')
paymentE_3 = Entry(addPaymentSubpanel, width = 18)

# create a tkinter string variable to keep track of firstpayment radio button
firstpayment = StringVar()

# set 'Yes' as the initial, default selection of the two radio buttons
firstpayment.set('Yes')

# add a label and two radio button widgets for 'first payment?' detail
firstpaymentL_3 = Label(addPaymentSubpanel, text = 'First Payment?: ')
Checkbutton(addPaymentSubpanel, text = 'Yes', variable = firstpayment, onvalue = 'Yes', offvalue = 'No').grid(row = 4, column = 1)

# add button widget for 'add new payment'
addPaymentB_3 = Button(addPaymentSubpanel, text = 'ADD NEW PAYMENT', command = addPayment)


# In[ ]:


# SIXTH PART OF THE PROGRAM CODE: FUNCTION FOR BUTTON TO SHOW SUBPANEL TO EDIT EXISTING DEBTOR'S RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# a function containing instructions that editDebtorB_4 button will execute once clicked
def editSubpanel():
    # create a database OR connect to an existing one within this function
    conn = sqlite3.connect('vmga-loan-system-database.db')

    # create a cursor to be used in executing SQL commands
    c = conn.cursor()
    
    # get inputs from entry widget and store them in their respective variable
    global name
    oldname = nameE_4.get()
    
    # delete contents of the entry widget after retrieving inputted values
    nameE_4.delete(0, END)
    
    # FIRST FUNCTION OF THE MAIN FUNCTION: SUBFUNCTION FOR BUTTON TO EDIT EXISTING DEBTOR'S RECORDS
    # NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
    # a function containing instructions that editedDebtorB_4 button will execute once clicked
    def editDebtor():
        # get inputs from entry widgets and store them in their respective variables
        name = nameE_5.get()
        age = ageE_5.get()
        sex = sexE_5.get()
        address = addressE_5.get()
        contact = contactE_5.get()

        # delete contents of the entry widgets after retrieving inputted values
        nameE_5.delete(0, END)
        ageE_5.delete(0, END)
        sexE_5.delete(0, END)
        addressE_5.delete(0, END)
        contactE_5.delete(0, END)

        # create a database OR connect to an existing one within this function
        conn = sqlite3.connect('vmga-loan-system-database.db')

        # create a cursor to be used in executing SQL commands
        c = conn.cursor()

        # use the created cursor to execute an SQL command of inserting user-inputted data to the table
        c.execute("UPDATE debtor_details SET name = ?, age = ?, sex = ?, address = ?, contact_no = ? WHERE name = ?", (name, age, sex, address, contact, oldname))

        # commit the changes made within this function to the database
        conn.commit()

        # close the database connection within this function
        conn.close()

    # add label and entry widgets for 'name' detail
    nameL_5 = Label(editDebtorSubpanel, text = 'Name: ')
    nameE_5 = Entry(editDebtorSubpanel, width = 19)

    # add label and entry widgets for 'age' detail
    ageL_5 = Label(editDebtorSubpanel, text = '     Age: ')
    ageE_5 = Entry(editDebtorSubpanel, width = 19)

    # add label and entry widgets for 'sex' detail
    sexL_5 = Label(editDebtorSubpanel, text = 'Sex: ')
    sexE_5 = Entry(editDebtorSubpanel, width = 19)

    # add label and entry widgets for 'address' detail
    addressL_5 = Label(editDebtorSubpanel, text = '     Address: ')
    addressE_5 = Entry(editDebtorSubpanel, width = 19)

    # add label and entry widgets for 'contact no.' detail
    contactL_5 = Label(editDebtorSubpanel, text = 'Contact No.: ')
    contactE_5 = Entry(editDebtorSubpanel, width = 19)

    # add button widget for 'add new record'
    editedDebtorB_5 = Button(editDebtorSubpanel, text = 'SAVE EDITED RECORDS', command = editDebtor)
    
    

    # place widgets of editDebtorSubpanel in order within its frame
    nameL_5.grid(row = 0, column = 0, sticky = W, pady = 1)
    nameE_5.grid(row = 0, column = 1, pady = 1)
    ageL_5.grid(row = 0, column = 2, sticky = W, pady = 1)
    ageE_5.grid(row = 0, column = 3, pady = 1)
    sexL_5.grid(row = 1, column = 0, sticky = W, pady = 1)
    sexE_5.grid(row = 1, column = 1, pady = 1)
    addressL_5.grid(row = 1, column = 2, sticky = W, pady = 1)
    addressE_5.grid(row = 1, column = 3, pady = 1)
    contactL_5.grid(row = 2, column = 0, sticky = W, pady = 1)
    contactE_5.grid(row = 2, column = 1, pady = 1)
    editedDebtorB_5.grid(row = 2, column = 2, columnspan = 2, pady = 1)
    
    # use the created cursor to execute an SQL command of retrieving current information of oldname
    c.execute("SELECT * from debtor_details WHERE name = '%s'" % oldname)
    
    # use the created cursor to execute an SQL command of fetching selected records
    fetchRecords = c.fetchall()
    
    # use a for-loop to store current information of oldname into their respective entry widgets
    for record in fetchRecords:
        # note: each index number in record[0] corresponds to each data column
        # therefore, 0 = first name; 1 = last name; 2 = address; etc.
        # you did this in order to display the current values of each field to the user
        nameE_5.insert(0, record[1])
        ageE_5.insert(0, record[2])
        sexE_5.insert(0, record[3])
        addressE_5.insert(0, record[4])
        contactE_5.insert(0, record[5])
        
    # commit the changes made within this function to the database
    conn.commit()
    
    # close the database connection within this function
    conn.close()


# In[ ]:


# SEVENTH PART OF THE PROGRAM CODE: FUNCTION FOR BUTTON TO REMOVE AN EXISTING DEBTOR'S RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# a function containing instructions that removeDebtorB_4 button will execute once clicked
def removeDebtor():
    # get inputs from entry widget and store them in their respective variable
    name = nameE_4.get()
    
    # delete contents of the entry widget after retrieving inputted values
    nameE_4.delete(0, END)
    
    # create a database OR connect to an existing one within this function
    conn = sqlite3.connect('vmga-loan-system-database.db')
    
    # create a cursor to be used in executing SQL commands
    c = conn.cursor()
    
    # use the created cursor to execute an SQL command of selecting all records from debtor_details table
    c.execute("SELECT * FROM debtor_details")
    
    # use the created cursor to execute an SQL command of fetching selected records
    fetchDebtors = c.fetchall()
    
    # use a for-loop to search through the returned tuple contained in the fetchDebtors variable
    for i in fetchDebtors:
        # if name is in a list within the said tuple...
        if(name in i):
            # ...get the debtor_id stored in index 0 and store it in debtorid variable
            debtorid = i[0]
            
            # test: print debtorid and its type
            print(debtorid, type(debtorid))
    
    # use the created cursor to execute an SQL command of deleting all records from payment_details, debt_details, and debtor_details table
    # note: we can't use (?, ?) as placeholder because the argument contains no open and close parentheses
    # note2: instead, use '%s' as placeholder then follow it with % variablename
    c.execute("DELETE FROM payment_details WHERE debtor_id = '%s'" % debtorid)
    c.execute("DELETE FROM debt_details WHERE debtor_id = '%s'" % debtorid)
    c.execute("DELETE FROM debtor_details WHERE name = '%s'" % name)
    
    # commit the changes made within this function to the database
    conn.commit()
    
    # close the database connection within this function
    conn.close()


# In[ ]:


# EIGHTH PART OF THE PROGRAM CODE: PANEL FOR EDITING OR REMOVING SELECTED EXISTING DEBTOR'S RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# create a panel for either editing or removing selected existing debtor's records
existingDebtorPanel = LabelFrame(sub, text = "EDIT OR REMOVE EXISTING DEBTOR'S RECORDS", padx = 10, width = 600, height = 230)

# add label and entry widgets for 'name' detail
nameL_4 = Label(existingDebtorPanel, text = "Debtor's Name to Edit/Remove Records: ")
nameE_4 = Entry(existingDebtorPanel, width = 29)

# add button widget for "edit debtor's records"
editDebtorB_4 = Button(existingDebtorPanel, text = "EDIT DEBTOR'S RECORDS", command = editSubpanel)

# add button widget for "remove debtor's records"
removeDebtorB_4 = Button(existingDebtorPanel, text = "REMOVE DEBTOR'S RECORDS", command = removeDebtor)

# FIRST PART OF THE MAIN PANEL: SUBPANEL FOR EDITING DEBTOR'S RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# create a subframe specifically for editing debtor's records
editDebtorSubpanel = LabelFrame(existingDebtorPanel, text = "EDIT SELECTED DEBTOR'S RECORDS", padx = 10, width = 575, height = 120)


# In[ ]:


# NINTH PART OF THE PROGRAM CODE: FUNCTION FOR BUTTON TO VIEW DEBTOR'S RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
def viewDebtors():
    # use a for-loop to destroy existing widgets within this panel before putting new widgets
    for widgets in viewRecordsPanel.winfo_children():
        widgets.destroy()
    
    # get inputs from entry widget and store them in their respective variable
    name = nameE_6.get()
    
    # delete contents of the entry widget after retrieving inputted values
    nameE_6.delete(0, END)
    
    # create a database OR connect to an existing one within this function
    conn = sqlite3.connect('vmga-loan-system-database.db')
    
    # create a cursor to be used in executing SQL commands
    c = conn.cursor()
    
    # if name is 'all', show all existing debtors' records
    if(name == 'all'):
        # create a hierarchical representation of data and columns to make it look like a table using treeview
        tree = ttk.Treeview(viewRecordsPanel, column = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6'), show = 'headings')

        #set columns and set center as anchor of values that might be inputted...
        tree.column('#1', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#2', anchor = CENTER, stretch = NO, width = 200)
        tree.column('#3', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#4', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#5', anchor = CENTER, stretch = NO, width = 120)
        tree.column('#6', anchor = CENTER, stretch = NO, width = 120)

        # ...and set headings of each column to give them labels
        tree.heading('#1', text = 'ID')
        tree.heading('#2', text = 'NAME')
        tree.heading('#3', text = 'AGE')
        tree.heading('#4', text = 'SEX')
        tree.heading('#5', text = 'ADDRESS')
        tree.heading('#6', text = 'CONTACT NO.')

        # pack the initialized hierarchical representation with columns or tables to display it
        tree.pack()

        #  use the created cursor to execute an SQL command of selecting all records from debtor_details table
        c.execute("SELECT * FROM debtor_details")

        # use the created cursor to execute an SQL command of fetching selected records
        datarows = c.fetchall()

        # use a for-loop to go through all fetched data then place them in their respective places in the table
        for data in datarows:
            # print the row then insert them in the table called tree variable
            print(data) 
            tree.insert("", END, values=data)
            
    # else, show a specific debtor's details only
    else:
        # create a hierarchical representation of data and columns to make it look like a table using treeview
        tree = ttk.Treeview(viewRecordsPanel, column = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6'), show = 'headings')

        #set columns and set center as anchor of values that might be inputted...
        tree.column('#1', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#2', anchor = CENTER, stretch = NO, width = 200)
        tree.column('#3', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#4', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#5', anchor = CENTER, stretch = NO, width = 120)
        tree.column('#6', anchor = CENTER, stretch = NO, width = 120)

        # ...and set headings of each column to give them labels
        tree.heading('#1', text = 'ID')
        tree.heading('#2', text = 'NAME')
        tree.heading('#3', text = 'AGE')
        tree.heading('#4', text = 'SEX')
        tree.heading('#5', text = 'ADDRESS')
        tree.heading('#6', text = 'CONTACT NO.')

        # pack the initialized hierarchical representation with columns or tables to display it
        tree.pack()

        #  use the created cursor to execute an SQL command of selecting all records from debtor_details table
        c.execute("SELECT * FROM debtor_details WHERE name = '%s'" % name)

        # use the created cursor to execute an SQL command of fetching selected records
        datarows = c.fetchall()

        # use a for-loop to go through all fetched data then place them in their respective places in the table
        for data in datarows:
            # print the row then insert them in the table called tree variable
            print(data) 
            tree.insert("", END, values=data)

    # close the database connection
    conn.close()


# In[ ]:


# TENTH PART OF THE PROGRAM CODE: FUNCTION FOR BUTTON TO VIEW DEBTOR'S DEBTS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
def viewDebts():
    # use a for-loop to destroy existing widgets within this panel before putting new widgets
    for widgets in viewRecordsPanel.winfo_children():
        widgets.destroy()
    
    # get inputs from entry widget and store them in their respective variable
    name = nameE_6.get()
    date = dateE_6.get()
    
    # delete contents of the entry widget after retrieving inputted values
    nameE_6.delete(0, END)
    dateE_6.delete(0, END)
    
    # create a database OR connect to an existing one within this function
    conn = sqlite3.connect('vmga-loan-system-database.db')
    
    # create a cursor to be used in executing SQL commands
    c = conn.cursor()
    
    # if name is not '' and date is 'all', show all debts of specific debtor
    if(name != '' and date == 'all'):
        # create a hierarchical representation of data and columns to make it look like a table using treeview
        tree = ttk.Treeview(viewRecordsPanel, column = ('c1', 'c2', 'c3', 'c4', 'c5'), show = 'headings')

        #set columns and set center as anchor of values that might be inputted...
        tree.column('#1', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#2', anchor = CENTER, stretch = NO, width = 100)
        tree.column('#3', anchor = CENTER, stretch = NO, width = 150)
        tree.column('#4', anchor = CENTER, stretch = NO, width = 145)
        tree.column('#5', anchor = CENTER, stretch = NO, width = 145)

        # ...and set headings of each column to give them labels
        tree.heading('#1', text = 'ID')
        tree.heading('#2', text = 'DEBT DATE')
        tree.heading('#3', text = 'LOANED AMOUNT')
        tree.heading('#4', text = 'INTEREST AMOUNT')
        tree.heading('#5', text = 'BALANCE AMOUNT')

        # pack the initialized hierarchical representation with columns or tables to display it
        tree.pack()

        # use the created cursor to execute an SQL command of selecting all records from debtor_details table
        c.execute("SELECT * FROM debtor_details")

        # use the created cursor to execute an SQL command of fetching selected records
        fetchDebtors = c.fetchall()
        
        # use a for-loop to search through the returned tuple contained in the fetchDebtors variable
        for i in fetchDebtors:
            # if name is in a list within the said tuple...
            if(name in i):
                # ...get the debtor_id stored in index 0 and store it in id variable
                id = i[0]
        
        #  use the created cursor to execute an SQL command of selecting all debts of specific debtor from debt_details table
        c.execute("SELECT * FROM debt_details WHERE debtor_id = '%s'" % id)

        # use the created cursor to execute an SQL command of fetching selected records
        datarows = c.fetchall()

        # use a for-loop to go through all fetched data then place them in their respective places in the table
        for data in datarows:
            # print the row then insert them in the table called tree variable
            print(data)
            newdata = data[:1] + data[2:]
            tree.insert("", END, values=newdata)
            
    # else, show all debts of specific debtor in a specific date
    else:
        # create a hierarchical representation of data and columns to make it look like a table using treeview
        tree = ttk.Treeview(viewRecordsPanel, column = ('c1', 'c2', 'c3', 'c4', 'c5'), show = 'headings')

        #set columns and set center as anchor of values that might be inputted...
        tree.column('#1', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#2', anchor = CENTER, stretch = NO, width = 100)
        tree.column('#3', anchor = CENTER, stretch = NO, width = 150)
        tree.column('#4', anchor = CENTER, stretch = NO, width = 145)
        tree.column('#5', anchor = CENTER, stretch = NO, width = 145)

        # ...and set headings of each column to give them labels
        tree.heading('#1', text = 'ID')
        tree.heading('#2', text = 'DEBT DATE')
        tree.heading('#3', text = 'LOANED AMOUNT')
        tree.heading('#4', text = 'INTEREST AMOUNT')
        tree.heading('#5', text = 'BALANCE AMOUNT')

        # pack the initialized hierarchical representation with columns or tables to display it
        tree.pack()

        # use the created cursor to execute an SQL command of selecting all records from debtor_details table
        c.execute("SELECT * FROM debtor_details")

        # use the created cursor to execute an SQL command of fetching selected records
        fetchDebtors = c.fetchall()
        
        # use a for-loop to search through the returned tuple contained in the fetchDebtors variable
        for i in fetchDebtors:
            # if name is in a list within the said tuple...
            if(name in i):
                # ...get the debtor_id stored in index 0 and store it in id variable
                id = i[0]
        
        #  use the created cursor to execute an SQL command of selecting debts of specific debtor from a specific date from debt_details table
        c.execute("SELECT * FROM debt_details WHERE debtor_id = ? AND debt_date = ?", (id, date))

        # use the created cursor to execute an SQL command of fetching selected records
        datarows = c.fetchall()

        # use a for-loop to go through all fetched data then place them in their respective places in the table
        for data in datarows:
            # print the row then insert them in the table called tree variable
            print(data)
            newdata = data[:1] + data[2:]
            tree.insert("", END, values=newdata)

    # close the database connection
    conn.close()


# In[ ]:


# ELEVENTH PART OF THE PROGRAM CODE: FUNCTION FOR BUTTON TO VIEW DEBTOR'S PAYMENTS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
def viewPayments():
    # use a for-loop to destroy existing widgets within this panel before putting new widgets
    for widgets in viewRecordsPanel.winfo_children():
        widgets.destroy()
    
    # get inputs from entry widget and store them in their respective variable
    name = nameE_6.get()
    date = dateE_6.get()
    
    # delete contents of the entry widget after retrieving inputted values
    nameE_6.delete(0, END)
    dateE_6.delete(0, END)
    
    # create a database OR connect to an existing one within this function
    conn = sqlite3.connect('vmga-loan-system-database.db')
    
    # create a cursor to be used in executing SQL commands
    c = conn.cursor()
    
    # if name is not '' and date is 'all', show all payments with respective dates of specific debtor
    if(name != '' and date == 'all'):
        # create a hierarchical representation of data and columns to make it look like a table using treeview
        tree = ttk.Treeview(viewRecordsPanel, column = ('c1', 'c2', 'c3', 'c4', 'c5'), show = 'headings')

        #set columns and set center as anchor of values that might be inputted...
        tree.column('#1', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#2', anchor = CENTER, stretch = NO, width = 125)
        tree.column('#3', anchor = CENTER, stretch = NO, width = 125)
        tree.column('#4', anchor = CENTER, stretch = NO, width = 145)
        tree.column('#5', anchor = CENTER, stretch = NO, width = 145)

        # ...and set headings of each column to give them labels
        tree.heading('#1', text = 'ID')
        tree.heading('#2', text = 'DEBT DATE')
        tree.heading('#3', text = 'PAYMENT DATE')
        tree.heading('#4', text = 'AMOUNT PAID')
        tree.heading('#5', text = 'BALANCE AMOUNT')

        # pack the initialized hierarchical representation with columns or tables to display it
        tree.pack()

        # use the created cursor to execute an SQL command of selecting all records from debtor_details table
        c.execute("SELECT * FROM debtor_details")

        # use the created cursor to execute an SQL command of fetching selected records
        fetchDebtors = c.fetchall()
        
        # use a for-loop to search through the returned tuple contained in the fetchDebtors variable
        for i in fetchDebtors:
            # if name is in a list within the said tuple...
            if(name in i):
                # ...get the debtor_id stored in index 0 and store it in id variable
                id = i[0]
        
        #  use the created cursor to execute an SQL command of selecting all payments of specific debtor from payment_details table
        c.execute("SELECT payment_details.payment_id, debt_details.debt_date, payment_details.payment_date, payment_details.amount_paid, payment_details.balance_amount FROM payment_details JOIN debt_details ON payment_details.debt_id = debt_details.debt_id WHERE payment_details.debtor_id = '%s'" % id)

        # use the created cursor to execute an SQL command of fetching selected records
        datarows = c.fetchall()

        # use a for-loop to go through all fetched data then place them in their respective places in the table
        for data in datarows:
            # print the row then insert them in the table called tree variable
            print(data)
            tree.insert("", END, values=data)
            
    # else, show all payments of specific debtor in a specific date
    else:
        # create a hierarchical representation of data and columns to make it look like a table using treeview
        tree = ttk.Treeview(viewRecordsPanel, column = ('c1', 'c2', 'c3', 'c4', 'c5'), show = 'headings')

        #set columns and set center as anchor of values that might be inputted...
        tree.column('#1', anchor = CENTER, stretch = NO, width = 50)
        tree.column('#2', anchor = CENTER, stretch = NO, width = 125)
        tree.column('#3', anchor = CENTER, stretch = NO, width = 125)
        tree.column('#4', anchor = CENTER, stretch = NO, width = 145)
        tree.column('#5', anchor = CENTER, stretch = NO, width = 145)

        # ...and set headings of each column to give them labels
        tree.heading('#1', text = 'ID')
        tree.heading('#2', text = 'DEBT DATE')
        tree.heading('#3', text = 'PAYMENT DATE')
        tree.heading('#4', text = 'AMOUNT PAID')
        tree.heading('#5', text = 'BALANCE AMOUNT')

        # pack the initialized hierarchical representation with columns or tables to display it
        tree.pack()

        # use the created cursor to execute an SQL command of selecting all records from debtor_details table
        c.execute("SELECT * FROM debtor_details")

        # use the created cursor to execute an SQL command of fetching selected records
        fetchDebtors = c.fetchall()
        
        # use a for-loop to search through the returned tuple contained in the fetchDebtors variable
        for i in fetchDebtors:
            # if name is in a list within the said tuple...
            if(name in i):
                # ...get the debtor_id stored in index 0 and store it in id variable
                id = i[0]
        
        #  use the created cursor to execute an SQL command of selecting payments of specific debtor from a specific debt date from payment_details table
        c.execute("SELECT payment_details.payment_id, debt_details.debt_date, payment_details.payment_date, payment_details.amount_paid, payment_details.balance_amount FROM payment_details JOIN debt_details ON payment_details.debt_id = debt_details.debt_id WHERE payment_details.debtor_id = ? AND debt_details.debt_date = ?", (id, date))

        # use the created cursor to execute an SQL command of fetching selected records
        datarows = c.fetchall()

        # use a for-loop to go through all fetched data then place them in their respective places in the table
        for data in datarows:
            # print the row then insert them in the table called tree variable
            print(data)
            tree.insert("", END, values=data)

    # close the database connection
    conn.close()


# In[ ]:


# TWELFTH PART OF THE PROGRAM CODE: PANEL FOR VIEWING RECORDS
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# create a panel for viewing records
viewRecordsPanel = LabelFrame(sub, text = 'VIEW RECORDS', padx = 10, pady = 5, width = 600, height = 790)

#note = Label(viewRecordsPanel, text = 'A LIST OF RECORDS WILL BE VIEWED HERE').pack(padx = 175, pady = 250)


# In[ ]:


# THIRTEENTH PART OF THE PROGRAM CODE: PANEL FOR SELECTING RECORDS TO VIEW
# NOTE: CHANGE PLACEHOLDER '5' PAD VALUE TO A BETTER PADDING ONCE ALL WIDGETS PLACED
# create a panel for selecting records to view
viewSelectorPanel = LabelFrame(sub, text = 'VIEW RECORDS SELECTOR', padx = 10, pady = 5, width = 405, height = 270)

# add label and entry widgets for 'view debtor records' detail
nameL_6 = Label(viewSelectorPanel, text = "Debtor's Name*: ")
nameE_6 = Entry(viewSelectorPanel, width = 20)

# add label and entry widgets for 'view debtor's debt date for payment' detail
dateL_6 = Label(viewSelectorPanel, text = "Debtor's Debt Date*^: ")
dateE_6 = Entry(viewSelectorPanel, width = 20)

# add label widgets for additional notes
note1L_6 = Label(viewSelectorPanel, text = "* Type 'all' to view all records")
note2L_6 = Label(viewSelectorPanel, text = "^ Required to view debtor's specific debts/payments")

# add button widget for "view debtor's records"
viewDebtorsB_6 = Button(viewSelectorPanel, text = "VIEW DEBTOR'S RECORDS", command = viewDebtors)

# add button widget for "view debtor's debts"
viewDebtsB_6 = Button(viewSelectorPanel, text = "VIEW DEBTOR'S DEBTS", command = viewDebts)

# add button widget for "view debtor's payments"
viewPaymentsB_6 = Button(viewSelectorPanel, text = "VIEW DEBTOR'S PAYMENTS", command = viewPayments)


# In[ ]:


# FOURTEENTH PART OF THE PROGRAM CODE: PLACING WIDGETS USING GRID
# place addDebtorPanel in root window and turn off propagation to disable automatic growth/shrink depending on frame contents
addDebtorPanel.grid(row = 0, column = 0, padx = 5, pady = 5)
addDebtorPanel.grid_propagate(0)

# place widgets of addDebtorPanel in order within its frame
nameL_1.grid(row = 0, column = 0, sticky = W, pady = 1)
nameE_1.grid(row = 0, column = 1, pady = 1)
ageL_1.grid(row = 1, column = 0, sticky = W, pady = 1)
ageE_1.grid(row = 1, column = 1, pady = 1)
sexL_1.grid(row = 2, column = 0, sticky = W, pady = 1)
sexE_1.grid(row = 2, column = 1, pady = 1)
addressL_1.grid(row = 3, column = 0, sticky = W, pady = 1)
addressE_1.grid(row = 3, column = 1, pady = 1)
contactL_1.grid(row = 4, column = 0, sticky = W, pady = 1)
contactE_1.grid(row = 4, column = 1, pady = 1)
addDebtorB_1.grid(columnspan = 2, pady = 1)

# place addTransactionPanel in root window and turn off propagation to disable automatic growth/shrink depending on frame contents
addTransactionPanel.grid(row = 1, column = 0, padx = 5, pady = 5)
addTransactionPanel.grid_propagate(0)

# place addDebtSubpanel in addTransactionPanel and turn off propagation to disable automatic growth/shrink depending on frame contents
addDebtSubpanel.grid(pady = 5)
addDebtSubpanel.grid_propagate(0)

# place widgets of addDebtSubpanel in order within its frame
nameL_2.grid(row = 0, column = 0, sticky = W, pady = 1)
nameE_2.grid(row = 0, column = 1, pady = 1)
dateL_2.grid(row = 1, column = 0, sticky = W, pady = 1)
dateE_2.grid(row = 1, column = 1, pady = 1)
loanL_2.grid(row = 2, column = 0, sticky = W, pady = 1)
loanE_2.grid(row = 2, column = 1, pady = 1)
interestL_2.grid(row = 3, column = 0, sticky = W, pady = 1)
interestE_2.grid(row = 3, column = 1, pady = 1)
addDebtB_2.grid(columnspan = 2, pady = 1)

# place addPaymentSubpanel in addTransactionPanel and turn off propagation to disable automatic growth/shrink depending on frame contents
addPaymentSubpanel.grid(pady = 5)
addPaymentSubpanel.grid_propagate(0)

# place widgets of addPaymentSubpanel in order within its frame
nameL_3.grid(row = 0, column = 0, sticky = W, pady = 1)
nameE_3.grid(row = 0, column = 1, pady = 1)
debtdateL_3.grid(row = 1, column = 0, sticky = W, pady = 1)
debtdateE_3.grid(row = 1, column = 1, pady = 1)
paymentdateL_3.grid(row = 2, column = 0, sticky = W, pady = 1)
paymentdateE_3.grid(row = 2, column = 1, pady = 1)
paymentL_3.grid(row = 3, column = 0, sticky = W, pady = 1)
paymentE_3.grid(row = 3, column = 1, pady = 1)
firstpaymentL_3.grid(row = 4, column = 0, sticky = W, pady = 1)
addPaymentB_3.grid(columnspan = 3, pady = 1)

# place existingDebtorPanel in root and turn off propagation to disable automatic growth/shrink depending on frame contents
existingDebtorPanel.grid(row = 0, column = 1, padx = 5, pady = 5)
existingDebtorPanel.grid_propagate(0)

# place editDebtorSubpanel in existingDebtorPanel and turn off propagation to disable automatic growth/shrink depending on frame contents
editDebtorSubpanel.grid(row = 2, columnspan = 2, pady = 5)
editDebtorSubpanel.grid_propagate(0)

# place widgets of existingDebtorPanel in order within its frame
nameL_4.grid(row = 0, column = 0, sticky = W, pady = 1)
nameE_4.grid(row = 0, column = 1, pady = 1)
editDebtorB_4.grid(row = 1, column = 0, pady = 1)
removeDebtorB_4.grid(row = 1, column = 1, pady = 1)

# place viewRecordsPanel in root window and turn off propagation to disable automatic growth/shrink depending on frame contents
viewRecordsPanel.grid(row = 1, column = 1, rowspan = 2, padx = 5, pady = 5)
viewRecordsPanel.grid_propagate(0)

# place viewSelectorPanel in root window and turn off propagation to disable automatic growth/shrink depending on frame contents
viewSelectorPanel.grid(row = 2, column = 0, padx = 5, pady = 5)
viewSelectorPanel.grid_propagate(0)

# place widgets of viewSelectorPanel in order within its frame
nameL_6.grid(row = 0, column = 0, sticky = W, pady = 1)
nameE_6.grid(row = 0, column = 1, pady = 1)
dateL_6.grid(row = 1, column = 0, sticky = W, pady = 1)
dateE_6.grid(row = 1, column = 1, pady = 1)
viewDebtorsB_6.grid(columnspan = 2, pady = 1)
viewDebtsB_6.grid(columnspan = 2, pady = 1)
viewPaymentsB_6.grid(columnspan = 2, pady = 1)
note1L_6.grid(columnspan = 2, sticky = W, pady = 1)
note2L_6.grid(columnspan = 2, sticky = W, pady = 1)


# In[ ]:


# END OF THE PROGRAM CODE: RUN THE PROGRAM AND DATABASE DISCONNECTION UPON EXIT 
# close the database connection
conn.close()

# create an event loop to keep the program running until user ends it
root.mainloop()


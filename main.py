# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""SELECT firstname,lastname FROM employees join offices using(officecode) where city ="Boston";""", conn)


# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""SELECT officecode, count(employeenumber) no_emp FROM offices left join employees using(officecode) group by officecode having no_emp =0;""", conn)


# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""SELECT firstname, lastname,city,state FROM employees join offices using(officecode) order by firstname,lastname;""",conn)


# STEP 4
# Replace None with your code
df_contacts =  pd.read_sql("""SELECT contactfirstname,contactlastname,phone,salesrepemployeenumber FROM customers left join orders using(customernumber) group by customernumber having count(ordernumber) = 0 order by contactlastname;""",conn)


# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""select contactfirstname,contactlastname,amount,paymentdate from customers join payments using(customernumber) order by cast(amount as float) desc;""",conn)


# STEP 6
# Replace None with your code
df_credit = pd.read_sql("""select employeenumber, firstname,lastname, count(customernumber) no_cust from employees join customers on employeenumber = salesrepemployeenumber group by employeenumber having avg(creditlimit) > 90000 order by no_cust desc limit 4;""",conn)


# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""select productname ,count(ordernumber) numorders, sum(quantityordered) totalunits from products join orderdetails using(productcode) join orders using(ordernumber) group by productcode order by totalunits desc;""",conn)


# STEP 8
# Replace None with your code
df_total_customers = None

# STEP 9
# Replace None with your code
df_customers = None

# STEP 10
# Replace None with your code
df_under_20 = None

conn.close()
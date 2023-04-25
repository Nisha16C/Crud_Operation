import streamlit as st
import mysql.connector

# Connectivity of Database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='chaurasiya',
    port='3306',
    database='crud',
)

mycursor = mydb.cursor()


def main():
    st.title("CRUD Operations With MySQL")

    # Display options for CRUD Operations
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))

# ................................Insert Data...........................................................................

    # Perform Selected CRUD Operations
    if option == "Create":
        st.subheader("Create a Record")
        name = st.text_input("Enter a Name")
        email = st.text_input("Enter Email")
        if st.button("Create"):
            sql = "insert into crud_table(name,email) values(%s,%s)"
            val = (name, email)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!")



# ..................................Read Data.....................................................................

    elif option == "Read":
        st.subheader("Read Record")
        mycursor.execute("select * from crud_table")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)


# ..................................Update Data....................................................................

    elif option == "Update":
        st.subheader("Update a Record")
        ID = st.number_input("Enter id")
        name = st.text_input("Enter a Name")
        email = st.text_input("Enter New Email")
        if st.button("Update"):
            sql = "update crud_table set name=%s, email=%s where id=%s"
            val = (name, email, ID)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!")



# ..................................Delete Data....................................................................

    elif option == "Delete":
        st.subheader("Delete a Record")
        ID = st.number_input("Enter id")
        if st.button("Delete"):
            sql = "delete from crud_table where id =%s"
            val = (ID,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!")


# The if__name__ == "__main__" statement is a conditional statement that checks if the special variable "__name__" is
# equal to the string "__main__". if this is true ,it means that the script is being run as the main program.

if __name__ == "__main__":
    main()

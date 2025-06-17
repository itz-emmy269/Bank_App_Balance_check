# --- Check Balance ---
elif menu == "Check Balance":
    st.subheader("Check Account Balance")
    name = st.text_input("Enter Account Name", key='name_input', value=get_input_value('name_input'))
    acc_type = st.selectbox(
        "Account Type",
        ["Savings", "Current"],
        key='type_input',
        index=0 if get_input_value('type_input') == "Savings" else 1
    )
    if st.button("Check"):
        key = name.strip().lower()
        if key in accounts:
            account = accounts[key]
            if account.acc_type == acc_type:
                st.info(account.get_balance())
            else:
                st.error(f"Account type mismatch! Your account is {account.acc_type}.")
        else:
            st.error("Account not found.")
        reset_inputs()
import streamlit as st

class Admission:
    def __init__(self, name, dob, age, phone_number, standard):
        self.name = name
        self.dob = dob
        self.age = age
        self.phone_number = phone_number
        self.standard = standard

    def check_eligibility(self):
        if self.standard <= 10:
            st.write("For checking the eligibility criteria to get admission in {}th standard enter the following details:".format(self.standard))
            maths = st.number_input("Enter your marks obtained in Maths:")
            science = st.number_input("Enter your marks obtained in Science:")
            social_science = st.number_input("Enter your marks obtained in Social Science:")
            english = st.number_input("Enter your marks obtained in English:")

            maths_eligibility = maths >= 75
            science_eligibility = science >= 75
            social_science_eligibility = social_science >= 75
            english_eligibility = english >= 75

            if maths_eligibility and science_eligibility and social_science_eligibility and english_eligibility:
                st.write("Your Admission is confirmed. You will receive a message regarding the fee structure soon through your WhatsApp.")
            else:
                st.write("Your marks are not as expected to meet the eligibility criteria. You are not eligible.")

        elif self.standard == 11:
            group = st.text_input("Enter the group that you want to enroll for:")
            math_10 = st.number_input("Enter your marks obtained in Maths:")
            science_10 = st.number_input("Enter your marks obtained in Science:")

            if math_10 >= 75 and science_10 >= 75:
                st.write("You are eligible to choose BIO MATHS and COMPUTER SCIENCE and COMMERCE WITH MATHS and COMMERCE WITHOUT MATHS")
                group_select = st.text_input("Choose the Group")
                st.write("You have successfully registered for {}. Your Admission is confirmed. You will receive a message soon through your WhatsApp.".format(group_select))
                com_elig = 55 <= math_10 < 75
                com_elig_1 = 55 <= science_10 < 75

                if com_elig and com_elig_1:
                    group_select_1 = st.text_input("Choose the Group")
                    st.write("You have successfully registered for {}. Your Admission is confirmed. You will receive a message soon through your WhatsApp.".format(group_select_1))
            else:
                st.write("Your marks are not as expected to meet the eligibility criteria. You are not eligible.")

        elif self.standard == 12:
            group_1 = st.text_input("Enter the group that you want to enroll for:")
            math_11 = st.number_input("Enter your marks obtained in Maths:")
            science_11 = st.number_input("Enter your marks obtained in Science:")

            if math_11 >= 75 and science_11 >= 75:
                st.write("You are eligible to choose BIO MATHS and COMPUTER SCIENCE and COMMERCE WITH MATHS and COMMERCE WITHOUT MATHS")
                group_select_a = st.text_input("Choose the Group")
                st.write("You have successfully registered for {}. Your Admission is confirmed. You will receive a message soon through your WhatsApp.".format(group_select_a))
                com_elig_a = 55 <= math_11 < 75
                com_elig_2 = 55 <= science_11 < 75

                if com_elig_a and com_elig_2:
                    group_select_2 = st.text_input("Choose the Group")
                    st.write("You have successfully registered for {}. Your Admission is confirmed. You will receive a message soon through your WhatsApp.".format(group_select_2))
            else:
                st.write("Your marks are not as expected to meet the eligibility criteria. You are not eligible.")
        else:
            st.write("Enter some valid input.")

def main():
    st.title("Admission Application")
    st.write("Fill out the following details for admission:")

    name = st.text_input("Enter the name of the student:")
    dob = st.date_input("Enter student's Date of Birth:")
    age = st.number_input("Enter student's age:")
    phone_number = st.number_input("Enter the parent's phone number:")
    standard = st.selectbox(
    'Select your standard?',
    tuple([i for i in range(1,13)]))
    if standard>1:
        admission_instance = Admission(name, dob, age, phone_number, standard)
        admission_instance.check_eligibility()

if __name__ == "__main__":
    main()

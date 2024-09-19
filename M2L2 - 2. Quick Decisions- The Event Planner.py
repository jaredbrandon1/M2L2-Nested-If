#Task 1: Code Correction
#Task 2: Venue Selection
#Task 3: Catering Choices

attendees = int(input("Enter number of attendees: "))
if attendees > 100:
    venue = "large hall" 
else:
    venue = "conference room"

#Default Response
print('''
The''',venue, '''will best accomodate your needs.''')

#Attendee number based response with Premium Package description and upgrade options
if venue == "large hall":
    print("To accomodate your attendees best, we would like to reccomend the Large Hall Premium Package.")
    about_premium_package = input('''
Would you like to hear more about the Premium Package? (yes/no)''')
    if about_premium_package == str("yes"):
        premium_package = input('''
For a limited time we are offering a discount on the Large Hall Premium Package. 
This package comes equip with an Upgraded Audio System, Higher Quality Projectors, and Luxury catering for the event. 

Would you like to upgrade to the Premium Package? (yes/no)''')
        if premium_package == str("yes"):
            print('''
Great choice! You won't regret it!''')
        elif premium_package == str("no"):
            print('''
No worries. You can still have a great event without the Premium Package.''')
        else:
            print('''
Invalid entry. Check your spelling,''')
    elif about_premium_package == str("no"):
        premium_package = str("no")
        print('''
Feel free to ask about the Large Hall Premium Package at any time.''')  

elif venue == "conference room":
    print("To accomodate your attendees best, we would like to reccomend the Conference Room Premium Package.")
    about_premium_package = input('''
Would you like to hear more about the Premium Package? (yes/no)''')
    if about_premium_package == str("yes"):
        premium_package = input('''
For a limited time we are offering a discount on the Conference Room Premium Package.
This package comes equip with an Upgraded Audio System, Higher Quality Projectors, and Luxury catering for the event.

Would you like to upgrade to the Premium Package? (yes/no)''')
        if premium_package == str("yes"):
            print('''
Great choice! You won't regret it!''')
        elif premium_package == str("no"):
            print('''
No worries. You can still have a great event without the Premium Package.''')
        else:
            print('''
Invalid entry. Check your spelling,''')
    elif about_premium_package == str("no"):
        premium_package = str("no")
        print('''
Feel free to ask about the Conference Room Premium Package at any point in time.''')


#Vegetarian Option ?
veg_option = input("Would you like to have a vegetarian option for the event? (yes/no)")

if premium_package == str("yes") and veg_option == str("yes"):
    print('''
We recommend Veggie Delight Caterers, and lucky for you... this vegtarian catering comes FREE with the Premium Package''')
elif premium_package == str("no") and veg_option == str("yes"):
    print('''
We recommend Veggie Delight Caterers, this vegetarian catering comes FREE with the Premium Package. It might be worth upgrading if you need Vegetarian options.''')
elif premium_package == str("no") and veg_option == str("no"):
    print('''
We recommend Gourmet Meals Caterers, they are top of the line catering for Gourmet meals.''')
elif premium_package == str("yes") and veg_option == str("no"):
    print('''
We recommend Gourmet Meals Caterers, they are top of the line catering for Gourmet meals.''')
else:
    print('''
Invalid Entry. Check your spelling.''')
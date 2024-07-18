#creating loops and input prompts for poll
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")

    response = input("What is your ideal place to visit for vacation? ")
    
    responses[name] = response

    repeat = input("Would you like someone else to take the poll? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to visit {response} for vacation.")


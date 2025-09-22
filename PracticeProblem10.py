projects = {}

while True:
    print("""\n1. Project Initiation\n2. Project Closure\n3. Project Progress Report\n4. Print Project Data\n5. Print all Projects\n6. Exit Application""")
    inp = int(input("\nWhat would you like to do? "))


    if inp == 1:
        p_id = int(input("\nWhat is the project id? "))
        title = input("What is the title of the project? ")
        tot_man = int(input("How many managers are there? "))
        man = []
        while tot_man > 0:
            man.append(input("What is the name of the manager? "))
            tot_man -= 1
        strt = input("What is the start date in the format: MMM DD YYYY? ")
        end_date = input("What is the end date in the format: MMM DD YYYY? ")
        sponsor = input("Who is the sponsor? ")
        budget = int(input("What is the budget for this project? "))
        tot_tech = int(input("How many types of tech will be used in this project? "))
        tech = []
        while tot_tech > 0:
            tech.append(input("What is the type of tech that will be used? "))
            tot_tech -= 1
        tot_team = int(input("How many team members will there be? "))
        team = []
        while tot_team > 0:
            team.append(input("What is the name of the team member? "))
            tot_team -= 1

        projects.update({p_id: {{"Project Title": title}, {"managers": man}, {"start date": strt}, {"end date": end_date}, {"sponsor": sponsor}, {"budget": budget}, {"technologies": tech}, {"team members": team}}})
        print("\nProject Created Successfully")


    elif inp == 2:
        clo = int(input("\nWhat is the id of the project you want to close? "))
        found = False
        for e in projects:
            if clo == e:
                del projects[e]
                found = True
                print("Project Closed")
        if not found:
            print("\nThere is no project with that id - check for typos and try again")


    elif inp == 3:
        check_id3 = int(input("What is the id of the project to check? "))
        yep = False
        for e in projects:
            if e == check_id3:
                print("The project start date is " + projects[check_id3]["start date"] + " and the end date is " + projects[check_id3]["end date"])
                yep = True
            if not yep:
                print("There is no project with that id - check for typos and try again")


    elif inp == 4:
        check_id4 = int(input("What is the id of the project to check? "))
        fou = False
        for e in projects:
            if e == check_id4:
                print(projects[check_id4].items())
                fou = True
            if not fou:
                print("There is no project with that id - check for typos and try again")


    elif inp == 5:
        for e in projects.items():
            print(e)
            print("------------------------------------------------------------------")

    elif inp == 6:
        print("Exiting Program")
        break
    else:
        print("That is not a valid input - check for typos and try again")
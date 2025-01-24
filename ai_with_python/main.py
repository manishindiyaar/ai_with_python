from file import read_file
from helper_function import print_llm_response


task_list = [

    {
        "description": "Compose a brief email to my boss explaining that I will be late for next week's meeting.",
        "time_to_complete": 3
    },
    {
        "description": "Create an outline for a presentation on the benefits of remote work.",
        "time_to_complete": 60
    },
    {
        "description": "Write a 300-word review of the movie 'The Arrival'.",
        "time_to_complete": 30
    },
    {
        "description": "Create a shopping list for tofu and olive stir fry.",
        "time_to_complete": 5
    }
]


# task = task_list[0]
# print(task)

# print(task['time_to_complete'] <= 5)

 
# print_llm_response("Hello, world!")   

# task = task_list[0]
# if task["time_to_complete"] <= 5:
#     task_to_do = task["description"]
#     print_llm_response(task_to_do)

# task = task_list[2]
# if task["time_to_complete"]<=5:
#     task_to_do = task['description']
#     print_llm_response(task_to_do)

# task = task_list[3]
# if task["time_to_complete"] <= 5:
#     task_to_do = task["description"]
#     print_llm_response(task_to_do)



# for task in task_list:
#     if task["time_to_complete"]<=100:
#         task_to_do = task["description"]
#         print_llm_response(task_to_do)        



# for task in task_list:
#     if task["time_to_complete"]<=5:
#         task_to_do = task["description"]
#         print_llm_response(task_to_do)
#     else:
#         print(f"To complete later: {task['time_to_complete']} time to complete.")    



# Saving tasks for later using lists
# tasks_for_later = []

# for task in task_list:
#     if task["time_to_complete"] <= 5:
#         task_to_do = task["description"]
#         print_llm_response(task_to_do)
#     else:
#         tasks_for_later.append(task)


# print(tasks_for_later)



# Reading file

journal = read_file()
# print(journal)


prompt = f"""

Given is all about my journey and about why statrted and how i want to become a great poetry person and 
you will be reading about my journey and then you will comeup with great hinglish type poetry for me.
here is my journey :

{journal}

"""

response = print_llm_response(journal)
print(response)




if __name__ == "__main__":
    response = print_llm_response(journal)
    print(response)

import random

# helper
def build_summary(result_dict):
    wildcards = ['relentlessly', 'tenaciously', 'persistently', 'insatiably']

    first_part = "I am a {0}".format(random.choice(wildcards))

    summary = first_part + " {d[adj1]}, {d[adj2]}, and {d[adj3]} {d[noun1]} who lives to {d[verb1]} {d[plnoun1]}, {d[verb2]} {d[plnoun2]}, {d[verb3]} {d[plnoun3]} and {d[verb4]}.".format(d = result_dict)

    return summary
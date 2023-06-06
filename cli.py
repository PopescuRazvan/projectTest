import click
from retrive_data import Read_CV_Data

@click.command("print_cv")
def print_cv():

    cv_data = Read_CV_Data.get_instance().retrive_data()
    
    cv_info = '''
CV Data:
General Information:
''' + ("\n".join([f"{key.capitalize()}: {value}" for key, value in cv_data["general_information"].items()]) if "general_information" in cv_data else "No information available.") + '''

Experience:
''' + ("\n".join([", ".join([f"{key.capitalize()}: {value}" for key, value in exp.items()]) for exp in cv_data.get("experience", [])]) if "experience" in cv_data else "No information available.")+ '''

Education:
'''+ ("\n".join([", ".join([f"{key.capitalize()}: {value}" for key, value in exp.items()]) for exp in cv_data.get("education", [])]) if "education" in cv_data else "No information available.")
   
    click.echo(cv_info)


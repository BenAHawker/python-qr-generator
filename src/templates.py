from os import listdir;
from os.path import isfile, join;
from pathlib import Path;

def getTemplates():
    templatePath = Path(__file__).parent.parent / 'assets/templates'
    onlyfiles = [f for f in listdir(templatePath) if isfile(join(templatePath, f))]
    return onlyfiles


# White_House_Press_Briefing_Summarization

to use this model, wordwise package is needed.
But in my cases, wordwise package doesn't function properly. Need to find the source file and
in the file __init__.py, change the code 'from core import Extractor' into 'from .core import Extractor'
and in the file core.py, change the code 'from utils import get_all_candidates, squash' into 'from .utils import get_all_candidates, squash'
NOt changing it may not cause problem in all users. But at least, in my case, there's this issue

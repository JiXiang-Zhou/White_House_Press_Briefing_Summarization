# White_House_Press_Briefing_Summarization

to use this model, wordwise package is needed.
But in my cases, wordwise package doesn't function properly. Need to find the source file and make some change

in the file __init__.py, change the code 'from core import Extractor' into 'from .core import Extractor'

in the file core.py, change the code 'from utils import get_all_candidates, squash' into 'from .utils import get_all_candidates, squash'

Not changing it may not cause problem in all users. But at least, in my case, there's this issue

# About my model
The model first separate questions from reporters and answers by press secratry. Then my model use Bertkey and wordwise to extract keyword 
from questions by reporters. Users input a search word. Using word vector similarity, the model will match the earch word with keywords.
If it matches, the corresponding answers will be included into a 'related answers'. In the end, the bert summary model is used to summarize
the 'related answers'.

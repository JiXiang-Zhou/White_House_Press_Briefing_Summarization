# White_House_Press_Briefing_Summarization

to use this model, 'wordwise' package is needed.
But in my cases, wordwise package doesn't function properly. It is needed to find the source file and make some changes

In the file __init__.py, change the code 'from core import Extractor' into 'from .core import Extractor'

In the file core.py, change the code 'from utils import get_all_candidates, squash' into 'from .utils import get_all_candidates, squash'

Not changing it may not cause problem for all users. But at least, in my case, there's an issue

# About my model
The model first separates questions from reporters and answers by press secratry. Then my model uses Bertkey and wordwise model to extract keywords 
from questions by reporters. Users input a search word. Using word vector similarity, the model can find the keywords that is similar to search word.
If it matches, the corresponding answers will be included into a 'related answers'. In the end, the bert summary model is used to summarize
the 'related answers'.

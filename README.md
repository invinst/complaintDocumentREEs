# complaintDocumentREEs

Complaint Document REEs is a python-based statistical language model that takes in a corpus of semi-divided plain text (i.e. contained in different CSV tuples/rows), organizes them according to specified criteria, and outputs several important pieces of information: <br>
__Lite Version__ 
1. (In Development) Most common words appearing in a specified category of plain text (i.e. cases categorized with an official category code, containing the names of specific officers/specific police unit, or other identifying information)
2. (In Development) Running most common words from a specified context to see if they appear in any other officers' cases, grouping those officers, and running the program again with the most common words excluded - to identify more identifying words. 
<br>

__Complicated Version__ 
1. (In Development) Running a TensorFlow feedforward neural network on the raw text to identify any hidden features that might not have been available by hard-coding. 

### Required Packages
  For those new to Python, these can be downloaded using the following Linux command: ```bash pip install your_program_here``` after you install [Pip](https://pip.pypa.io/en/stable/). 

- __NOTE__: In creating this program, I used an Anaconda environment that I set up with all the required packages in PyCharm. For some reason, installing a variety of non-default packages on your computer with pip and then trying to use them in PyCharm gets a bit wonky. Creating an environment in Anaconda and installing everything to that same environment through Terminal, then setting that environment as the interpreter of your project gets around this issue. 
  
__Lite Version__ <br>
- [csv](https://docs.python.org/3/library/csv.html)
- [nltk](https://www.nltk.org/)
- os
- sys
- [matplotlib](https://matplotlib.org/)
- [numpy](https://docs.scipy.org/doc/)
<br>

__Complicated Version__ <br>
- tensorflow
- pandas

## Goals
- The goal of this program is to identify contexts that might not readily be apparent in certain groupings. One example is sexual violence/assault narratives that might be contained within a report. Each of these reports is categorized based on the nature of the complaint, but might contain additional problems - such as racial bias or paperwork issues, that might cause the report to be labeled under those problems rather than sexual violence/assault. This one-dimensional classification is problematic for researchers looking to evaluate metrics on these issues. Ideally, the first iteration of this program will be used to identify a broad swath of keywords and phrases that we can run on our reports collection and add additional dimensionality to the classification system. 

## What this Repo Contains: 
(Anything in italics can be substituted for your own files for your own use)<br>
- *masterFile*.csv = a Master CSV that contains the raw text and its associated codes that the program takes as an input
- preprocessing.py = a python file that organizes the raw text and associated codes into a dictionary that can be analyzed by the Relation Extraction model. 
- mostCommonWords.py = a python file that iterates over the raw text groupings and finds the most common words

## Running the Program:
1. Clone the program onto your computer using GitHub's terminal commands. 
2. Open the folder in PyCharm, or your IDE of choice. 
3. Put your csv file of choice in the directory (__IMPORTANT__!!!!! Delete the other .csv file already in the folder. The command in preprocessing.py only searches for one .csv file in the directory). You can also just keep the original .csv that comes with the Clone to see how the program runs and see its outputs. 
4. Right-click on the code in preprocessing.py to prepare the .csv information 
5. Right-click on the code in mostCommonWords.py to display the most common words from the provided raw text. 

## Notes:
- At the moment, several aspects of this program are hard-coded - limiting its flexibility for use across a variety of projects. Things like #3 in Running the Program aren't applicable at the moment. 

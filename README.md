# Word Problem Solver 

### Prerequisites:
- NLTK 3.1
- ScikitLearn 0.16.1
- NumPy
- Install MaxEnt 'megam'

### Data

Data is provided in the data/ folder.
Follow the format given in data/questions.json
- Index
- Wordproblem
- Equation
- Solution

### Run

Initially, we convert all equations into generic equations (equation templates)
We then divide the dataset into two halves - one is for training, the other is for testing.

Execute the following command:
python Parser.py

You can see the accuracy for each of the classifier in both NLTK and Sklearn libraries.
The templates for each wordproblem will be available in data/templates.txt

### References

- http://textminingonline.com/dive-into-nltk-part-viii-using-external-maximum-entropy-modeling-libraries-for-text-classification
- http://www.nltk.org/
- http://scikit-learn.org/stable/

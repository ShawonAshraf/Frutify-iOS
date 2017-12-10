import turicreate as tc

model = tc.load_model('Fruitify_V1.model')

# Load the data
data =  tc.SFrame('frutifyV1.sframe')

# Make a train-test split
train_data, test_data = data.random_split(0.8)
# Evaluate the model and save the results into a dictionary
metrics = model.evaluate(test_data)
print metrics['accuracy'] 

print "Accuracy         : %s" % metrics['accuracy']
print "Confusion Matrix : \n%s" % metrics['confusion_matrix']
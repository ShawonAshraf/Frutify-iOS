import turicreate as tc

# Load the data
data = tc.SFrame('frutify_multi_class_V1.sframe')

# Make a train-test split
train_data, test_data = data.random_split(0.8)

# Create a model
model = tc.image_classifier.create(train_data, target='label', max_iterations=1000)

# Save predictions to an SFrame (class and corresponding class-probabilities)
predictions = model.classify(test_data)

# Evaluate the model and save the results into a dictionary
results = model.evaluate(test_data)
print "Accuracy         : %s" % results['accuracy']
print "Confusion Matrix : \n%s" % results['confusion_matrix']

# Save the model for later use in Turi Create
model.save('Fruitify_MC_V1.model')

# Export for use in Core ML
# model.export_coreml('Frutify_MC_V1_beta.mlmodel')
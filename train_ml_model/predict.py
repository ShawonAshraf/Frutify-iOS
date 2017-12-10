"""
    taken from:
    https://github.com/apple/turicreate/blob/master/userguide/image_classifier/introduction.md
"""

import turicreate as tc

# Load the data
data =  tc.SFrame('frutifyV1.sframe')

# Make a train-test split
train_data, test_data = data.random_split(0.8)

# Automatically picks the right model based on your data.
model = tc.image_classifier.create(train_data, target='label', max_iterations = 1000)

# Save predictions to an SArray
predictions = model.predict(test_data)

# Evaluate the model and save the results into a dictionary
metrics = model.evaluate(test_data)
print(metrics['accuracy'])

# Save the model for later use in Turi Create
model.save('Fruitify_V1.model')

# Export for use in Core ML
model.export_coreml('FrutifyV1_beta.mlmodel')
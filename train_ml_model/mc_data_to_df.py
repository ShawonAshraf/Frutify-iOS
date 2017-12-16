# for multiclass classification

import turicreate as tc

# load data
image_data = tc.image_analysis.load_images('image_data', with_path=True)

labels = ['fresh_apple',
            'fresh_mango',
            'fresh_banana',
            'fresh_orange',
            'rotten_apple',
            'rotten_banana',
            'rotten_mango',
            'rotten_orange'
        ]

def get_label(path, labels=labels):
    for label in labels:
        if label in path:
            return label

image_data['label'] = image_data['path'].apply(get_label)

# save data
image_data.save('frutify_multi_class_V1.sframe')

# explore
image_data.explore()


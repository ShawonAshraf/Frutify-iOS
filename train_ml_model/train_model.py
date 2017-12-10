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



image_data['label'] = image_data['path'].apply(lambda path: 'fresh' if 'fresh' in path else 'rotten')

# save data
image_data.save('frutifyV1.sframe')

# explore
image_data.explore()
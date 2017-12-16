import turicreate as tc

model = tc.load_model('Fruitify_MC_V1.model')

model.export_coreml('Frutify_MC_V1_beta.mlmodel')
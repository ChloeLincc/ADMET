from admet_ai import ADMETModel
import pandas as pd

df = pd.read_csv('random_100_molecules.csv')
model = ADMETModel()
res = model.predict(smiles=df['SMILES'].tolist())
res.to_csv('predicted_results.csv', index=False)
print('预测完成！')

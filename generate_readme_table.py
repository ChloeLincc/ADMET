import pandas as pd

# 读取两个数据文件
df_smiles = pd.read_csv('random_100_molecules.csv')
df_results = pd.read_csv('random_100_admet_results.csv')

# 拼接（确保 SMILES 在前，预测结果在后）
df = pd.concat([df_smiles[['SMILES']], df_results], axis=1)

# 选取核心指标列（避免104列太长，挑重点的看）
cols = ['molecular_weight', 'logP', 'QED', 'hERG', 'AMES', 'DILI', 'Caco2_Wang']
df_subset = df[['SMILES'] + cols].copy()

# 给分子加个编号
df_subset.insert(0, 'ID', range(1, len(df_subset) + 1))

# 转成 Markdown 表格
markdown_table = df_subset.round(2).to_markdown(index=False)

# 保存
with open('README_TABLE.md', 'w') as f:
    f.write(markdown_table)

print('Markdown 表格已生成：/root/autodl-tmp/Admet_Project/README_TABLE.md')
print('--- 预览前5行 ---')
print('\n'.join(markdown_table.split('\n')[:8]))

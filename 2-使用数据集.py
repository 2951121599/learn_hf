from datasets import load_dataset

# 加载一个文本分类数据集
imdb_dataset = load_dataset("imdb")
print(imdb_dataset)

# 查看数据集的一个样本
print(imdb_dataset["train"][0])

# 查看数据集的特征
print(imdb_dataset["train"].features)


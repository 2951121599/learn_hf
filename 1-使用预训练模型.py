from transformers import pipeline

# # 使用情感分析 pipeline
# sentiment_analyzer = pipeline("sentiment-analysis")
# result = sentiment_analyzer("I love using Hugging Face!")
# print(result)

# 使用文本生成 pipeline
text_generator = pipeline("text-generation", model="gpt2")
generated_text = text_generator("The quick brown fox", max_length=50, num_return_sequences=1)
print(generated_text)
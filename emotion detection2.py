from transformers import BertTokenizer, BertForSequenceClassification, AdamW
import torch

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=5)

# Define emotion labels
emotion_labels = ['Trust/Disgust', 'Joy/Fear', 'Predation/Betrayal', 'Shannon/Tea', 'Shock/Weird']

# Example inference
text = "Well, if we're talking about text with the most Shannon entropy, it's gotta be a tie between my rant on why Neon Genesis Evangelion is the greatest anime ever made and my diatribe on the profound impact of Serial Experiments Lain on modern culture. Both of those texts were bursting at the seams with information and complexity, just like my mind when I'm deep in thought. But seriously, I probably need to find a hobby outside of anime analysis... or maybe I should just start binge-watching more anime, that sounds like a good plan."
inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
outputs = model(**inputs)
probabilities = torch.softmax(outputs.logits, dim=1).detach().numpy()[0]

# Print predicted probabilities for different emotions
print("Predicted Emotions:")
for i, prob in enumerate(probabilities):
    print(f"{emotion_labels[i]}: {prob:.4f}")

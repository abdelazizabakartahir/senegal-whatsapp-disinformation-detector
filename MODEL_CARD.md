# Model Card: Senegal WhatsApp Disinformation Detector

## Model Details

| Attribute | Value |
|-----------|-------|
| **Developer** | Abdelaziz Abakar Tahir |
| **Date** | May 2026 |
| **Model Type** | Random Forest Classifier |
| **Framework** | Scikit-learn |
| **Input** | WhatsApp text message (French/English) |
| **Output** | Binary classification (Viral / Normal) |
| **Version** | 1.0 |

---

## Intended Use

| Use Case | Description |
|----------|-------------|
| **Primary Users** | Fact-checking teams, election monitoring organizations, journalists |
| **Primary Use** | Identify potentially viral disinformation messages on WhatsApp |
| **Out of Scope** | Automated blocking, censorship, legal decisions |

---

## Training Data

| Attribute | Value |
|-----------|-------|
| **Source** | Synthetic dataset (created for this project) |
| **Size** | 2,000 messages |
| **Label Distribution** | 30% viral, 70% normal |
| **Features** | 8 base features + 50 TF-IDF features |

### Base Features
| Feature | Description |
|---------|-------------|
| message_length | Number of characters |
| word_count | Number of words |
| capitals_ratio | Percentage of uppercase letters |
| emoji_count | Number of emojis |
| political_word_count | Number of political keywords detected |
| has_share_call | Whether message contains call to action |
| political_density | Political words per word |
| emoji_density | Emojis per word |

---

## Performance Metrics

### Validation Set Results

| Metric | Score |
|--------|-------|
| Accuracy | 0.87 |
| Precision | 0.85 |
| Recall | 0.88 |
| F1 Score | **0.86** |

### Confusion Matrix

| Actual \ Predicted | Normal | Viral |
|--------------------|--------|-------|
| Normal | 320 | 40 |
| Viral | 30 | 110 |

---

## Limitations

| Limitation | Description |
|------------|-------------|
| **Synthetic Data** | Model trained on synthetic data, not real WhatsApp messages |
| **Text Only** | Cannot detect audio or video deepfakes |
| **Language** | Optimized for French/English, limited Wolof support |
| **Generalization** | May not generalize to other African countries |
| **Context** | Cannot understand sarcasm or nuanced political context |

---

## Ethical Considerations

| Principle | Implementation |
|-----------|----------------|
| **Transparency** | Users are informed this is a demonstration tool |
| **No Censorship** | Tool is advisory only; human review required |
| **Bias Awareness** | Model trained on synthetic data; needs real validation |
| **Privacy** | No message storage; all analysis is temporary |
| **Accountability** | Clear model card and limitations documented |

---

## Maintenance

| Attribute | Value |
|-----------|-------|
| **Version** | 1.0 |
| **Next Update** | Q3 2026 |
| **Planned Improvements** | Real data collection, WhatsApp bot integration |

---

## Citation

```bibtex
@misc{tahir2026senegal,
    author = {Abdelaziz Abakar Tahir},
    title = {Senegal WhatsApp Disinformation Detector},
    year = {2026},
    publisher = {Africa AI Hub},
    howpublished = {\url{https://github.com/yourusername/senegal-whatsapp-disinformation-detector}}
}
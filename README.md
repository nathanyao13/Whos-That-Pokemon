# Pokémon ML: Who's That Pokémon?

Pokémon has been a significant part of my life—from trading cards with classmates in elementary school to competing in TCG tournaments, playing the video games on emulators, and watching the anime on television. As a longtime fan, I’ve followed this iconic Japanese franchise since childhood. 

However, as I’ve grown older, my interactions with Pokémon have become less frequent. Now, as a college student studying **Statistics and Machine Learning** at **Carnegie Mellon University**, I’ve been learning various machine learning concepts through my coursework. This project is an opportunity to merge my passion for Pokémon with my knowledge of machine learning.

---

The inspiration behind this project comes from a classic segment in the Pokémon anime:  
### **"Who’s That Pokémon?"**

In these moments, right before a commercial break, the screen would silhouette a Pokémon and challenge the viewer to identify it.

![image](https://github.com/user-attachments/assets/c8ddf82f-97ee-4646-acfa-7d7286d0b918)

As a kid, I would always yell the answer at the screen—though the show usually made it obvious by introducing the Pokémon just moments before.

But what if it wasn’t obvious?  
What if the only thing you had was the image of the Pokémon itself?  
Could you still tell which one it is?

---

## Problem Description

I have split this project into two different sections. The first showcases
my understanding of ML. The second shows how I am able to apply models 
in the real world. 

Both revolve around classifying a Pokémon's primary type out of the 18 Pokémon types:
    Grass, Fire, Water, Bug, Normal, Poison, Electric, Ground, 
    Fairy, Fighting, Psychic, Rock, Ghost, Ice, Dragon, Dark, 
    Steel, Flying. 

1. Convolutional Neural Network (CNN) From Scratch: cnn.ipynb

    Description: In this project, I implemented a CNN from scratch using the PyTorch Library, building up layers such as convolutional layers, ReLU activations, max pooling, batch normalization, and fully connected layers to form a complete deep learning pipeline.
    

    Results: <br>
    **3 Type Classification**: <br>
    - Best Validation Accuracy: 85.19% <br>

    **18 Type Classification**:<br>
    - Best Validation Accuracy: 34.44% <br>

2. Transfer Learning Model Using ResNet: transfer_learning.ipynb

    Description: In this project, I applied transfer learning using both ResNet18 and ResNet50 architectures to classify Pokémon images. The appeal of ResNet models lies in  their use of Residual Blocks, which are designed to address the challenges that come with training very deep neural networks. Furthermore, these Pre-Trained models have been trained on ImageNet, whereas training a model from scratch would typically require vast amounts of data and computational resources.

    Results: <br>
    **3 Type Classification**:
    - ResNet18: 
        - Best Validation Accuracy: 88.89%
    - ResNet50:  
        - Best Validation Accuracy: 83.33%

    **18 Type Classification**:
    - ResNet18:
        - Best Validation Accuracy: 35.00%
    - ResNet50: 
        - Best Validation Accuracy: 28.88% 

(Note: These results all have standard deviations due to randomness) <br>


---
## Analysis and Conclusion

### Overall Trend

- Models consistently showed **higher validation accuracy** and **shorter training times** when classifying into **3 types** (Fire, Water, Grass) compared to **18 types**.
- Classifying Pokémon into 18 distinct types is inherently more difficult due to:
  - **Class imbalance** — some types appear far more frequently than others.
  - **Finer visual distinctions** between certain classes.
  - **Higher output dimensionality**, requiring more nuanced predictions.

This added complexity leads to:
- **Longer training times** due to a more difficult optimization landscape.
- **Lower validation accuracy**, as the model struggles to distinguish between visually similar types.

In contrast, the **3-type classification task** is:
- More **balanced**,
- More **visually distinct**, and
- Achieves **over 80% accuracy** with shorter training times.


### Custom CNN vs. ResNet (Transfer Learning)

- **Pretrained models** like ResNet consistently **outperform custom CNNs** on both tasks.
- ResNet models are pretrained on large-scale datasets like **ImageNet**, allowing them to extract more powerful visual features.
- **Transfer learning** enables these models to **generalize well** even on smaller, task-specific datasets (e.g., Pokémon images).


### ResNet18 vs. ResNet50

- **ResNet18** achieved **higher validation accuracy** than **ResNet50**.
- Despite ResNet50’s deeper architecture and theoretical advantage, it **underperformed** due to:
  - The **small dataset size**, which increases the risk of overfitting.
  - The **task complexity** not justifying the use of a deeper model.

---


## Further Exploration

### Primary and Secondary Typing

- Many Pokémon have **dual types** — a **primary type** and, if present, a **secondary type**.
- This project focused solely on classifying the **primary type**, which simplifies the problem but may overlook important features.
- Some model errors appear to be caused by **confusion with secondary types**, especially in dual-typed Pokémon.
- In future work, a **multi-label classification** approach could be adopted to account for both primary and secondary types, potentially improving accuracy.

### Accuracy and Dataset Limitations

- The dataset contains images of approximately **800 Pokémon**, which limits model performance due to its relatively small size.
- As **new Pokémon generations** are released, the dataset will grow in both **diversity** and **size**.
- A larger and more balanced dataset would enable:
  - Better **generalization**,
  - Reduced **overfitting**, and
  - More accurate classification across all types.
- Future iterations of this project using expanded datasets could yield **significantly better results**.

---

Sources:

    Datasets:
    - https://www.kaggle.com/datasets/cristobalmitchell/pokedex/data
    - https://www.kaggle.com/datasets/hlrhegemony/pokemon-image-dataset/data

    Research and Coding:
    - https://www.cs.cmu.edu/~mgormley/courses/10601/
    - https://www.youtube.com/watch?v=FaW9JCSJn2s&ab_channel=SebastianRaschka
    - https://github.com/rasbt/stat453-deep-learning-ss21
    - https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
    - https://docs.pytorch.org/vision/0.9/models.html
    - https://www.youtube.com/watch?v=ZoZHd0Zm3RY&ab_channel=AladdinPersson
    - https://www.youtube.com/watch?v=jztwpsIzEGc&ab_channel=NicholasRenotte
    - https://www.youtube.com/watch?v=H69j69FFMV0&ab_channel=GregHogg
    - https://www.youtube.com/watch?v=CtzfbUwrYGI&ab_channel=NeuralNine
    - https://www.youtube.com/watch?v=uZKm8RgljCI&ab_channel=NeuralNine


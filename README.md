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

I have split this project into two different sections. The first problem showcases
my understanding of ML. The second problem shows how I am able to apply models 
in the real world. 

Both revolve around classifying a Pokémon's primary type out of the 18 Pokémon types:
    Grass, Fire, Water, Bug, Normal, Poison, Electric, Ground, 
    Fairy, Fighting, Psychic, Rock, Ghost, Ice, Dragon, Dark, 
    Steel, Flying. 

1. Convolutional Neural Network (CNN) From Scratch

    Description: In this project, I implemented a CNN from scratch using the PyTorch Library, building up layers such as convolutional layers, ReLU activations, max pooling, and fully connected layers to form a complete deep learning pipeline.
    

    Results: <br>
    **3 Type Classification**: <br>
    - Best Validation Accuracy: 68.51% <br>

    **18 Type Classification**:<br>
    - Best Validation Accuracy: 24.44% <br>

3. Transfer Learning Model Using ResNet

    Description:
       - In this project, I applied transfer learning using both ResNet18 and ResNet50 architectures to classify Pokémon images. The appeal of ResNet models lies in  their use of Residual Blocks, which are designed to address the challenges that come with training very deep neural networks.

    Results:
    **3 Type Classification**:
    - ResNet18: 
        - Best Validation Accuracy: 79.62%
    - ResNet50:  
        - Best Validation Accuracy: 66.66%

    **18 Type Classification**:
    - ResNet18:
        - Best Validation Accuracy: 35.00%
    - ResNet50: 
        - Best Validation Accuracy: 28.88% 

(Note: These results all have standard deviations due to randomness) <br>

---

Sources:

    Datasets:
    - https://www.kaggle.com/datasets/cristobalmitchell/pokedex/data
    - https://www.kaggle.com/datasets/hlrhegemony/pokemon-image-dataset/data

    Research and Coding:
    - https://www.youtube.com/watch?v=FaW9JCSJn2s&ab_channel=SebastianRaschka
    - https://github.com/rasbt/stat453-deep-learning-ss21
    - https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
    - https://docs.pytorch.org/vision/0.9/models.html
    - https://www.youtube.com/watch?v=ZoZHd0Zm3RY&ab_channel=AladdinPersson
    - https://www.youtube.com/watch?v=jztwpsIzEGc&ab_channel=NicholasRenotte


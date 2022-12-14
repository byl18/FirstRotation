# Reinforcement Learning + Transfer Learning

This is the main outcome of the first rotation. If there is any other questions, please contact me by baiyl22@mails.tsinghua.edu.cn

## Content

[1 Aim](#Aim)

[2 Pipeline](#Pipeline)

[3 Results](#Results)

[4 Discussion](#Discussion)

[5 Data availability](#MrWhite)

[6 References](#References)



## Aim

To combine Reinforcement Learning (RL) and Transfer Learning (TL) to search for some common pattern in strategies to play Atari 2600 games. 

Deep Q-network (DQN) is a convolutional neural network (CNN) and a classical model of the reinforcement learning. We apply DQN to four Atari 2600 games from gym environment to learn control policies with inputs as raw pixels and outputs as a value function estimating future rewards. However, RL has poor generalization ability and a strong environmental dependence, which means its parameters will change with the environment.

Transfer learning is the reuse of a pre-trained model on a new problem. It’s currently very popular in deep learning because it can train deep neural networks with comparatively little data.  In transfer learning, a machine exploits the knowledge gained from a previous task to improve generalization about another.

Therefore, we aim to combine their advantages to create a model that is able to perform well on various game environments with a certain generalization ability. 

## Pipeline

Our idea is to preserve the neural network except for the final output layer. Several game environments share this network with the only difference of respective the output layer. In this way, some common pattern could probably be hidden from the shared network. 

**1 forward network**

Establish the Resnet network(left) and the traditional CNN network(right) respectively as the shared network. 

<img src="RotationSource\Resnet.png" width = "300" />

<img src="RotationSource\BothFlow.png" width = "500" />

**2 Back propagation**

 Apply the DQN (shown below) as the back propagation algorithm to update the neural network.

<img src="RotationSource\DQN.png"  width = "500" /> 

**3 Model training**

Use this reinforcement model to train 3 Atari games: Flappy Bird, Space Invaders, and Breakout (left to right).

After the performance effect gradually converged, terminate the training process and preserve the trained model. 

<img src="RotationSource\flappybird.gif"/> <img src="RotationSource\space_invaders.gif"/> <img src="RotationSource\breakout.gif"/>

**4 Transfer learning**

As my hand-drawn flowchart showed below, the networks with the dense layer of two games for example are trained independently in the step of reinforcement learning. Then the parameters of the Game 1 network except the dense layer are transferred to the Game 2. In this way, if better outputs and less training time to converge are obtained, that suggested that some common pattern may be included in the shared network.

<img src="RotationSource\mydraw.jpg"  width = "500" />

## Results

### 1 Traditional DQN shows good performance on several games

Flappy Bird converged at about 800,000 step

<img src="RotationSource\Video\FlappyBirdResult.gif" width = "450" /> <img src="RotationSource\train_curve_fb.png"  width = "400"/>

Space Invaders converged at about 50,000 steps (local optimum)

<img src="RotationSource\Video\SpaceInvadersResult.gif" width = "450" /> <img src="RotationSource\train_curve_si.png"  width = "400" />

Breakout converged at about 100,000 steps

<img src="RotationSource\Video\BreakoutResult.gif" width = "450" /> <img src="RotationSource\train_curve_bo.png"  width = "400" />

### 2 TF can improve the performance of some games

Figures below show RL only training curves(left) and RL + TL training curves respectively.

<img src="RotationSource\train_curve_fb.png"  width = "400" /><img src="RotationSource\tl_fb.png"  width = "400" />

<img src="RotationSource\train_curve_si.png"  width = "400" /><img src="RotationSource\tl_si.png"  width = "400" />

<img src="RotationSource\train_curve_bo.png"  width = "400" /><img src="RotationSource\tl_bo.png"  width = "400" />

## Discussion

**1 Tranfer learning can make up for reinforcement learning in some degree**

Although RL can generate experience continuously and decompose problems to a simple form, it still has a list of drawbacks such as the low generalization ability, sparse rewards, and high sensitivity to hyperparameters. On the other hand, TL can combine networks of several games together into a shared network, which can improve the generalization ability to deal with different environments. This shared network can accelerate the convergence of Q value and increase Q value in some cases as shown in part 2 of the Results section. Therefore, it seems like these drawbacks of RL can be compensated in some degree by introducing TL. 

**2 There exists some common information in the shared network**

As demomstrated above, one game can use network parameters from another game to improve its training speed and performance. This suggests that some common pattern may be included in the shared network and it represents some underlying logic information hidden in these games. In future research, maybe further common patterns can be dug up from the shared network.

**3 Limitations**

In fact, we have tried lots of other Atari games but most failed to achieve the performance as expected. There are some obvious factors responsible for this. The action spaces of these games are too large (>12) and the rewards of some games are too sparse so that it's hard to train enough in a limited time and memory consumption. Besides we cannot arbitrarily adjust or remove the convolution layer in the pre-trained network because of the shared parameters. Therefore, when importing a pre-trained model, the network structure needs to be the same as the pre-trained network structure for training.



<h2 id="MrWhite">Data availability</h2>

Any methods, additional references, source data, extended data, supplementary information and statements of data and codes are available at [my github](https://github.com/byl18/FirstRotation)

## References

[1] [Schrittwieser, J., Antonoglou, I., Hubert, T. et al. Mastering Atari, Go, chess and shogi by planning with a learned model. Nature 588, 604–609 (2020).](https://www.nature.com/articles/s41586-020-03051-4)

[2] [Mnih, V., Kavukcuoglu, K., Silver, D. et al. Human-level control through deep reinforcement learning. *Nature* **518**, 529–533 (2015). ](https://www.nature.com/articles/nature14236)

[3] [Whittington, James C R et al. “The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation.” *Cell* vol. 183,5 (2020)](https://www.cell.com/cell/fulltext/S0092-8674(20)31388-X)

[4] [K. He, X. Zhang, S. Ren and J. Sun, "Deep Residual Learning for Image Recognition,"IEEE Conference on Computer Vision and Pattern Recognition (CVPR)(2016)](https://ieeexplore.ieee.org/document/7780459/citations#citations)

[5] [Mnih, Volodymyr, et al.Playing Atari with Deep Reinforcement Learning. (2013)](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)

[6] [Gym Documentation](https://www.gymlibrary.dev)

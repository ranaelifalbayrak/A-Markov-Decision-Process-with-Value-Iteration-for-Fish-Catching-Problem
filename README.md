# Fish Catching Problem - Markov Decision Process

## Overview

In this project, we address the Fish Catching Problem in a village using a Markov Decision Process (MDP) and value iteration.
The fishers aim to maximize their harvest while considering the growth rate of the fish population and avoiding overfishing.

## Problem Statement

- The fishers need to decide the optimal number of fish to catch each year.
- Overfishing decreases the yield the following year.
- The growth rate (R) is a random variable, influencing the fish population for the next year.
- Due to limited resources, the fish population cannot exceed M.
- Initial utilities are 0.

## Parameters 

- Discount Factor (γ): 0.9
- Maximum Fish Population (M): 100  <!-- Note: This is different from the report, please adjust as needed -->

## Probability Distribution over R

The probability distribution over R is as follows:

- P(R = 1) = 0.2
- P(R = 1.25) = 0.3
- P(R = 1.5) = 0.3
- P(R = 1.75) = 0.2



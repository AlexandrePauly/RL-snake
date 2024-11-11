import numpy as np
import os
import matplotlib.pyplot as plt
from IPython import display

def plot(scores, mean_scores, mean_slider, rewards, memories, MAX_MEMORY, baseline_scores=None, comparison_scores=None):
    record = np.max(scores)

    # Creating subplots similar to those in the image you uploaded
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # First subplot: Score vs episode graph (similar to Fig 5a)
    axs[0].plot(scores, label='Scores', color='blue')
    axs[0].plot(mean_slider, color='orange', label='Moyenne glissante')
    axs[0].plot(mean_scores, color='red', label='Moyenne')
    axs[0].fill_between(range(len(scores)), np.array(scores) - np.std(scores), np.array(scores) + np.std(scores), color='blue', alpha=0.2)
    axs[0].set_title('(a) Score vs. episode graph')
    axs[0].set_xlabel('Episode')
    axs[0].set_ylabel('Score')
    axs[0].text(0.05, 0.95, f'Num. épisodes : {len(scores)}', transform=axs[0].transAxes, fontsize=12, verticalalignment='top')
    axs[0].legend(['Scores', 'Moyenne glissante', 'Moyenne', f'Record : {record}'])
    
    # Second subplot: Memory vs episode graph (similar to Fig 5b)
    axs[1].plot(memories, label='Memory', color='blue')
    
    # Find the first episode where memory reaches MAX_MEMORY
    if max(memories) >= MAX_MEMORY:
        idx_max_memory = next(i for i, mem in enumerate(memories) if mem >= MAX_MEMORY)
        axs[1].axvline(x=idx_max_memory, color='red', linestyle='--', label=f'MAX_MEMORY ({MAX_MEMORY}) atteint à l\'épisode {idx_max_memory}')
    
    axs[1].set_title('(b) Memory vs. episode graph')
    axs[1].set_xlabel('Episode')
    axs[1].set_ylabel('Memory')
    axs[1].legend()

    save_plot(plt)

def save_plot(plt, save_dir='save', base_filename='plot'):
    # Creating the directory if necessary
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
 
    # Find the good filename
    i = 1
    while os.path.exists(f'{save_dir}/{base_filename}_{i}.png'):
        i += 1
 
    # Saving plot
    file_path = f'{save_dir}/{base_filename}_{i}.png'
    plt.savefig(file_path)

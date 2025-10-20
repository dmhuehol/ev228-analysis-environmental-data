'''utensils_demo
Demonstrate plotting counts in discrete bins with utensil choices.
'''
from icecream import ic
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

font_path = '/Users/danielhueholt/Library/Fonts/'
for font in fm.findSystemFonts(font_path):
    fm.fontManager.addfont(font)

#  Enter names of people who chose each utensil here
knife = ['owen', 'james']
spoon = ['theo', 'eli']
fork = ['avery', 'jordan', 'noah', 'julien', 'morgan']
chopsticks = ['david',]
tongs = ['daniel',]
ic(knife, spoon, fork, chopsticks, tongs)

chosen_utensils = [
    len(knife), len(spoon), len(fork), len(chopsticks), len(tongs)]
utensil_names = ['Knife', 'Spoon', 'Fork', 'Chopsticks', 'Tongs']

plt.rcParams.update({'font.family': 'Figtree'})
fig, ax = plt.subplots()
ax.bar(utensil_names, chosen_utensils, color='#6e7aaa')
plt.xlabel('Utensils', fontsize=14)
plt.xticks(fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.yticks(fontsize=14)
plt.title('Number of people choosing each utensil')
plt.savefig('/Users/danielhueholt/Documents/Figures/ev228_fig/utensils.pdf')
from gettext import find
from itertools import count
from mimetypes import init
import string
import random
import itertools, re
from collections import Counter
import itertools, re
from turtle import color
from tools import *

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = string.ascii_letters + " "
Index_of_coincidence = 0
cipher_text = "Xmjpnhtfy niiyiipyoh uno ey ftydyz ni n pyno hm yovnouy hvy qynjotow ljmuyii. Eniyz mo hvy jyigqhi mx iguv niiyiipyohi, ihgzyohi dtqq ey neqy hm niiyii hvytj romdqyzwy noz tzyohtxb ihjyowhvi noz dynroyiiyi. Hvy hynuvyj dtqq nqim vnfy toztunhtmo mo vmd dyqq hvy ihgzyohi njy wjniltow hvy xgoznpyohnq xnuhi noz dvyhvyj vy oyyzi hm nqhyj hvytj hynuvtow hm yplvniti impy tplmjhnoh umouylhi."
print(len(cipher_text))
removed_spacing = ''.join(e for e in cipher_text if e.isalnum())
cipher_text = removed_spacing.lower()
freq_analysis = dict(Counter(cipher_text))
print(freq_analysis)

for key in freq_analysis:
    print(freq_analysis.get(key))
    Index_of_coincidence += (int(freq_analysis.get(key))*(int(freq_analysis.get(key))-1)) / (len(cipher_text)*(len(cipher_text)-1))

print(Index_of_coincidence)

cipher_text = conditioning(cipher_text)
print(cipher_text)
frequencies, alphabet = frequency_counter(cipher_text)
sorted_alphabet = [x for y, x in sorted(zip(frequencies, alphabet),reverse=True)]
most_common_char = sorted_alphabet[0]

y_pos = np.arange(len(alphabet))
plt.bar(y_pos, frequencies, align='center', alpha=0.5)
plt.xticks(y_pos, alphabet)
plt.ylabel('Frequency')
plt.xlabel('Letter')
plt.title('Frequency Analysis')
plt.show()

y_pos = np.arange(len(alphabet))
plt.bar(y_pos, sorted(frequencies,reverse=True), align='center', color = 'red')
plt.xticks(y_pos, sorted_alphabet)
plt.ylabel('Frequency')
plt.xlabel('Ciphered Letter')
plt.title('Frequency Analysis')
plt.show()

# plain_text = 'FORMATIVE ASSESSMENT CAN BE VIEWED AS A MEAN TO ENHANCE THE LEARNING PROCESS BASED ON THE RESULTS OF SUCH ASSESSMENTS STUDENTS WILL BE ABLE TO ASSESS THEIR KNOWLEDGE AND IDENTIFY STRENGTHS AND WEAKNESSES THE TEACHER WILL ALSO HAVE INDICATION ON HOW WELL THE STUDENTS ARE GRASPING THE FUNDAMENTAL FACTS AND WHETHER HE NEEDS TO ALTER THEIR TEACHING TO EMPHASIS SOME IMPORTANT CONCEPTS'
# print(plain_text.lower())

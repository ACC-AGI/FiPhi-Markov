import random
import math
import time


PHI = (1 + math.sqrt(5)) / 2


text = "Hello world this is a test."
words = text.split()
chain = {}


for i in range(len(words) - 1):
   current_word = words[i]
   next_word = words[i + 1]
   if current_word not in chain:
       chain[current_word] = []
   chain[current_word].append(next_word)


def generate_text(length):
   if not chain:
       return ""


   current_word = random.choice(list(chain.keys()))
   result = [current_word]


   for _ in range(length - 1):
       if current_word in chain:
           current_word = random.choice(chain[current_word])
           result.append(current_word)
       else:
           break


   return " ".join(result)


base_length = 5


while True:
   generated_text = generate_text(round(base_length))
   print("\nGenerated Text:", generated_text)


   base_length *= PHI 


   time.sleep(2)




import random
import math
import time


PHI = (1 + math.sqrt(5)) / 2


text = "Hello world this is a test."
words = text.split()
chain = {}


for i in range(len(words) - 1):
   current_word = words[i]
   next_word = words[i + 1]
   if current_word not in chain:
       chain[current_word] = []
   chain[current_word].append(next_word)


def generate_text(length):
   if not chain:
       return ""


   current_word = random.choice(list(chain.keys()))
   result = [current_word]


   for _ in range(length - 1):
       if current_word in chain:
           current_word = random.choice(chain[current_word])
           result.append(current_word)
       else:
           break


   return " ".join(result)


base_length = 5


while True:
   generated_text = generate_text(round(base_length))
   print("\nGenerated Text:", generated_text)


   base_length *= PHI 


   time.sleep(2)





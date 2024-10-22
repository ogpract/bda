### create New File For Each

<h3>Mapper.py</h3>

```bash
import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))
```

<h3>Reducer.py</h3>

```bash
import sys
current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
if current_word:
    print('%s\t%s' % (current_word, current_count))

#CMD1: cat word_count.txt | python Mapper.py
#CMD2: cat word_count.txt | python Mapper.py | python Reducer.py
```

<h3>word_count.txt</h3>

```bash
HI A A A A A BA b B AB
```

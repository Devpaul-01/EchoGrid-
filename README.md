EchoGrid 🔁📐

EchoGrid is a fun, experimental tool that extracts all strings from a nested data structure, detects palindromes, and generates randomized sublists (a "character matrix") from them. Great for word puzzles, encryption experiments, and character-level data manipulation.


---

🚀 Features

✅ Recursively extracts strings from deeply nested dictionaries/lists

🔁 Checks which strings are palindromes (like racecar, deed, noon)

🎲 Randomly slices characters to build a matrix of sublists

🔧 Designed to be modular and reusable for other projects



---

📂 Example

data = {
    "a": ["racecar", {"x": ["noon", "apple"]}],
    "b": [["deed", "hello"], "world"],
    "c": {"inner": ["civic", ["radar", "python"]]}
}

Output:

['racecar', 'noon', 'apple', 'deed', 'hello', 'world', 'civic', 'radar', 'python']
['racecar', 'noon', 'deed', 'civic', 'radar']
[
  [['a', 'c', 'r'], ['e', 'c', 'r'], ...],
  [['n', 'o', 'o'], ['n', 'o', 'n'], ...],
  ...
]


---

🛠 How It Works

collate_strings(data) → Recursively gathers all strings

palindrome_check(string) → Returns True if it's a palindrome

get_matrix(palindromes) → Shuffles and randomly slices characters into mini lists



---

🧪 Use Cases

Word games or palindrome-based puzzles

Preprocessing text for character-level machine learning

Experimenting with encryption or randomization tools



---

📱 How to Run on Mobile (No Laptop Needed!)

You can use this project on a phone with apps like:

PyDroid3 (Android)

Juno or Carnets (iOS)


Just paste in the code and run directly!

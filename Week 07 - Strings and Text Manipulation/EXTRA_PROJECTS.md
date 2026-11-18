# Week 7 — Extra Practice Projects

Optional. Beyond the lab — classic beginner projects, adapted from Angela
Yu's *100 Days of Code*. Both of these are string-manipulation-heavy —
looping over characters, building strings up piece by piece — which is
exactly this week's territory, even though the loops and lists they lean
on were taught back in Weeks 2 and 4.

---

## Hangman

**Uses:** string indexing/looping, `in`, lists, `random.choice()`

1. Pick a random word from a list of words: `chosen_word =
   random.choice(word_list)`.
2. Build a `placeholder` string of underscores, one per letter of
   `chosen_word` (e.g. `"apple"` → `"_ _ _ _ _"`).
3. Loop: ask the user to guess a letter. If it's `in chosen_word`,
   reveal it in the display at the correct position(s) — a letter can
   appear more than once. If not, lose a life.
4. Track `lives` (start at 6). Stop the game when either the display has
   no more blanks (win) or `lives` reaches 0 (lose).
5. Don't deduct a life for guessing a letter already guessed — just
   remind them.

*Adapted from: 100 Days of Code, Day 7.*

---

## Caesar Cipher

**Uses:** string indexing, `.index()`, `%` (modulo), functions

1. Write `encrypt(original_text, shift_amount)`: for each letter in
   `original_text`, find its position in the alphabet, add
   `shift_amount`, and use `% 26` to wrap back around from `z` to `a`
   instead of running off the end of the alphabet.
2. Write `decrypt(original_text, shift_amount)` the same way, but
   shifting backwards (multiply the shift by `-1`).
3. Combine both into one `caesar(direction, text, shift)` function that
   calls the right one based on `direction`.
4. Handle characters that aren't letters (spaces, punctuation, digits) —
   they should pass through unchanged, not crash the program or vanish.
5. Ask the user if they want to go again in a loop, instead of the
   program just ending after one message.

*Adapted from: 100 Days of Code, Day 8.*

---

Stuck on `%` giving an index that's still out of range? That's this
week's `04 - Parsing Real Text`, and Week 1's `03 - Numbers and
Arithmetic` on the modulo operator itself.

# Lab 4 – VibeCoding
​
**Course:** Software Engineering (SE) Lab  
**SRN:** PES1UG24CS122  
**Project:** Arm Wrestle Showdown (Pygame)  
**LLM Used:** ChatGPT  
**Date of Completion:** 7 October 2026
​
---
​
## Objective
​
Use a Vibe Coding tool (LLM) to fix a deliberately broken Python game and add the features listed in its README, getting each task done in a few well-written prompts. The assigned repo was forked to a personal account, and each task was committed separately.
​
## Links
​
| Item | Link |
|------|------|
| Forked Repo (updated code) | https://github.com/Chaitanya-171005/53_arm_wrestle |
| Chat History | https://chatgpt.com/share/6ac6558b-8190-83ec-9717-63bc77d5d385 |
​
## Tasks
​
| Task | Description | Commit |
|:---:|-------------|:---:|
| 1 | **Fix the inverted arm push bug.** Alternating Left/Right arrow keys pushed the arm toward the computer. Every alternating keypress now moves the arm toward the player's winning threshold (−100). | [`17e98c5`](https://github.com/Chaitanya-171005/53_arm_wrestle/commit/17e98c5f54b8b70605ff41318cd404190407680d) |
| 2 | **Dynamic AI surge.** The AI cycles through Normal → Surge (higher push force) → Cooldown (reduced resistance) with randomized timings, instead of pushing at a constant rate. | [`6230f47`](https://github.com/Chaitanya-171005/53_arm_wrestle/commit/6230f47555563fac50eebe31d934d4fc38dd5d8d) |
| 3 | **Exhaustion warning indicator.** A flashing "AI Surge!" warning appears during the AI's surge, and an "Exhausted" state is shown when the player's stamina is too low to push. | [`e6da584`](https://github.com/Chaitanya-171005/53_arm_wrestle/commit/e6da584afa4e03b09c78819a9eeacfd43c6d4f59) |
| 4 | **Counter-surge bonus.** Pushing right as the AI's surge ends grants a temporary stamina recovery boost and double push strength, shown with a "Counter!" indicator. | [`b6d9533`](https://github.com/Chaitanya-171005/53_arm_wrestle/commit/b6d9533be3fc62afc61db6d3e3e2a9c65f236d63) |
​
## Files in this folder
​
| File | Description |
|------|-------------|
| `Lab4_PES1UG24CS122.pdf` | Lab summary with repo link, chat link, and task explanations |
| `53_arm_wrestle (Before).mov` | 10-second gameplay before changes (bug: computer wins) |
| `53_arm_wrestle (After).mov` | 10-second gameplay after changes (AI Surge, Counter bonus, player wins) |
| `README.md` | This file |
​
## How to Run
​
```bash
git clone https://github.com/Chaitanya-171005/53_arm_wrestle.git
cd 53_arm_wrestle
pip install pygame
python main.py
```
​
**Controls:** Rapidly alternate **←** and **→** to push. Press **R** to rematch after a match ends.
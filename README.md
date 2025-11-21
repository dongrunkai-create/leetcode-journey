# leetcode-journey
Challenges when I do leetcode and how I solved them

#Roman to Integer Solution
## Core Logic 
I used a "Reverse Pass" strategy to solve this. By iterating the string backwards, the logic simplifies significantly. 

## Challenge & Solution
The trickiest part was determining when to add when to substract (e.g., distinguishing IV from VI).

To solve this, I introduced a `prev_value` variable acting like a **"realy baton" (memory buffer)**
- Inside this loop, I compare the `current_value` with the `prev_value`.
- If `current < prev`, its a subtract case, so result - curr_value.
- Otherwise, I add.

  This "relay baton" concept helped me understand how to **carry context to the next iteration**.

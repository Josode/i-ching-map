import tkinter as tk
import random



# Hexagrams with short descriptions
hexagrams = [
    ("1 ䷀ Qian – The Creative", "Pure creative power and initiative."),
    ("2 ䷁ Kun – The Receptive", "Receptivity, support, patience."),
    ("3 ䷂ Zhun – Difficulty at the Beginning", "Initial struggles and growth."),
    ("4 ䷃ Meng – Youthful Folly", "Learning through inexperience."),
    ("5 ䷄ Xu – Waiting", "Patience and timing in preparation."),
    ("6 ䷅ Song – Conflict", "Tension and the need for resolution."),
    ("7 ䷆ Shi – The Army", "Discipline, strength in unity."),
    ("8 ䷇ Bi – Holding Together", "Unity and cooperation."),
    ("9 ䷈ Xiao Xu – The Taming Power of the Small", "Influence through gentle restraint."),
    ("10 ䷉ Lü – Treading", "Careful movement and caution."),
    ("11 ䷊ Tai – Peace", "Harmony and fruitful cooperation."),
    ("12 ䷋ Pi – Standstill", "Stagnation and inactivity."),
    ("13 ䷌ Tong Ren – Fellowship", "Community and shared purpose."),
    ("14 ䷍ Da You – Great Possession", "Abundance and achievement."),
    ("15 ䷎ Qian – Modesty", "Humility and restraint."),
    ("16 ䷏ Yu – Enthusiasm", "Inspiration and rallying support."),
    ("17 ䷐ Sui – Following", "Adaptability and trust."),
    ("18 ䷑ Gu – Work on What Has Been Spoiled", "Correcting errors with care."),
    ("19 ䷒ Lin – Approach", "Progress with attentive effort."),
    ("20 ䷓ Guan – Contemplation", "Reflection and insight."),
    ("21 ䷔ Shi He – Biting Through", "Resolving obstacles decisively."),
    ("22 ䷕ Bi – Grace", "Beauty, refinement, decorum."),
    ("23 ䷖ Bo – Splitting Apart", "Dissolution and letting go."),
    ("24 ䷗ Fu – Return", "Rebirth and renewed direction."),
    ("25 ䷘ Wu Wang – Innocence", "Natural sincerity and integrity."),
    ("26 ䷙ Da Xu – Great Taming Power", "Cultivated strength and restraint."),
    ("27 ䷚ Yi – Nourishment", "Care and support for growth."),
    ("28 ䷛ Da Guo – Great Exceeding", "Emphasis and dynamic pressure."),
    ("29 ䷜ Kan – Danger", "Facing peril with caution."),
    ("30 ䷝ Li – Clinging", "Clarity, awareness, vision."),
    ("31 ䷞ Xian – Influence", "Attraction and harmonious impact."),
    ("32 ䷟ Heng – Duration", "Steadfast continuity."),
    ("33 ䷠ Dun – Retreat", "Wisdom in stepping back."),
    ("34 ䷡ Da Zhuang – Great Power", "Force and assertiveness."),
    ("35 ䷢ Jin – Progress", "Advancement through clarity."),
    ("36 ䷣ Ming Yi – Darkening of the Light", "Hidden truth under challenge."),
    ("37 ䷤ Jia Ren – Family", "Harmony in relationships."),
    ("38 ䷥ Kui – Opposition", "Differences that refine."),
    ("39 ䷦ Jian – Obstruction", "Overcoming resistance."),
    ("40 ䷧ Xie – Deliverance", "Resolving difficulty."),
    ("41 ䷨ Sun – Decrease", "Letting go to grow."),
    ("42 ䷩ Yi – Increase", "Expansion with purpose."),
    ("43 ䷪ Guai – Breakthrough", "Decisive change."),
    ("44 ䷫ Gou – Coming to Meet", "Opportunity in encounter."),
    ("45 ䷬ Cui – Gathering Together", "Community alignment."),
    ("46 ䷭ Sheng – Pushing Upward", "Steady progress upward."),
    ("47 ䷮ Kun – Oppression", "Testing pressure builds resolve."),
    ("48 ䷯ Jing – The Well", "Basic resources refreshed."),
    ("49 ䷰ Ge – Revolution", "Transformation and renewal."),
    ("50 ䷱ Ding – The Cauldron", "Nourishment and culture."),
    ("51 ䷲ Zhen – The Arousing", "Sudden movement or shock."),
    ("52 ䷳ Gen – Keeping Still", "Stillness and meditation."),
    ("53 ䷴ Jian – Development", "Gradual growth."),
    ("54 ䷵ Gui Mei – The Marrying Maiden", "Adaptation within limits."),
    ("55 ䷶ Feng – Abundance", "Abundant energy and clarity."),
    ("56 ䷷ Lu – The Wanderer", "Experience through travel."),
    ("57 ䷸ Xun – The Gentle", "Subtle influence."),
    ("58 ䷹ Dui – The Joyous", "Joy and clear expression."),
    ("59 ䷺ Huan – Dispersion", "Dissolution of obstacles."),
    ("60 ䷻ Jie – Limitation", "Healthy boundaries."),
    ("61 ䷼ Zhong Fu – Inner Truth", "Integrity and trust."),
    ("62 ䷽ Xiao Guo – Small Exceeding", "Precise effort matters."),
    ("63 ䷾ Ji Ji – After Completion", "Order after completion."),
    ("64 ䷿ Wei Ji – Before Completion", "Emerging fulfillment.")
]

# Function to show description in a custom popup
def show_desc(name, desc):
    popup = tk.Toplevel(root)
    popup.title(name)
    popup.configure(bg="#0b1e5f")
    popup.resizable(False, False)

    # Set desired size
    popup_width = 600
    popup_height = 400

    # Get screen width and height
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    # Calculate x and y coordinates for center
    x = (screen_width // 2) - (popup_width // 2)
    y = (screen_height // 2) - (popup_height // 2)

    # Set geometry
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    # Name label
    tk.Label(popup, text=name, font=("Helvetica", 20, "bold"),
             fg="#ffffff", bg="#0b1e5f", wraplength=550).pack(pady=20)
    # Description label
    tk.Label(popup, text=desc, font=("Helvetica", 16),
             fg="#ffffff", bg="#0b1e5f", wraplength=550, justify="center").pack(pady=10)
    # Close button
    tk.Button(popup, text="Close", font=("Helvetica", 14),
              bg="#d3d3d3", fg="#000000", width=15,
              command=popup.destroy).pack(pady=20)

# Function for random hexagram
def random_hexagram():
    name, desc = random.choice(hexagrams)
    show_desc(name, desc)

# Tkinter setup
root = tk.Tk()
root.title("I Ching Hexagrams (Dark Mode)")
root.geometry("1400x1200")
root.configure(bg="#0b1e5f")
root.resizable(True, True)

# Frame for hexagram buttons
frame = tk.Frame(root, bg="#0b1e5f")
frame.pack(pady=20)

# 8x8 grid of hexagram buttons
for i, (name, desc) in enumerate(hexagrams):
    row = i // 8
    col = i % 8
    tk.Button(frame, text=name, width=20, height=5,
              wraplength=180,
              bg="#d3d3d3",
              fg="#000000",
              relief="raised",
              command=lambda n=name, d=desc: show_desc(n, d)).grid(row=row, column=col, padx=5, pady=5)

# Random hexagram button
rand_frame = tk.Frame(root, bg="#0b1e5f")
rand_frame.pack(pady=30)
tk.Button(rand_frame, text="🎲 Random Hexagram", font=("Helvetica", 20, "bold"),
          bg="#d3d3d3", fg="#000000", width=40, height=3,
          command=random_hexagram).pack()

# 8x8 grid of hexagram buttons
for i, (name, desc) in enumerate(hexagrams):
    row = i // 8
    col = i % 8
    tk.Button(frame,
              text=name,
              width=14, height=3,          # smaller button size
              wraplength=160,               # wrap text inside button
              bg="#d3d3d3",
              fg="#000000",
              relief="flat",                # flat to allow border to show nicely
              highlightbackground="#000000",  # black border
              highlightthickness=1,        # thin border
              font=("Helvetica", 12, "bold"),
              command=lambda n=name, d=desc: show_desc(n, d)
              ).grid(row=row, column=col, padx=5, pady=5)


root.mainloop()
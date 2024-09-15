# 🏥 **Hospital Placement Optimization** 🌟

Welcome to the **Hospital Placement Optimization** project! This Python script is like your very own hospital planner, helping you find the perfect spots to place hospitals on a grid to minimize the travel time for houses. With a sprinkle of Hill Climbing magic, this script will make sure everyone gets the best care possible with minimal fuss!

## 📦 **What’s Inside?**

- **Grid Layout**: A spacious grid where you can place houses and hospitals. Perfect for urban planning enthusiasts!
- **Hill Climbing Algorithm**: Our smart algorithm that iteratively finds the optimal hospital placements by minimizing the total distance for house-to-hospital travel.
- **Visuals Galore**: Check out the cool images that show you the current state of your grid. Visualize your hospital placements and see how your algorithm performs in real-time!

## 🚀 **Getting Started**

To get started with this awesome project, you'll need a couple of things:

1. **Python**: Make sure you have Python installed on your system.
2. **Pillow (PIL)**: We use this to create those stunning visuals. Install it using:
   ```bash
   pip install pillow
---

## 💻 **How to Use**

- Set Up Your Space: Define your grid dimensions and number of hospitals.
- Add Some Houses: Sprinkle some houses onto your grid.
- Run the Algorithm: Let the Hill Climbing algorithm find the best hospital placements.
- Check Out the Results: Look at the images to see the optimized placements and costs.

---

## 🛠️ **Code Walkthrough**

Here’s a quick peek at how things work:

- Space Class: Manages the grid, houses, and hospitals.
- add_house(): Add houses to your grid.
- get_cost(): Calculate the total distance cost.
- hill_climb(): Optimize hospital placements using Hill Climbing.
- output_image(): Generate visual representations of the grid.

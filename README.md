[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22204871)
# Programming in Science - Midterm Exam - V1

This template repository is the starter project for the Programming in Science Midterm Exam V1. Written in Python, and tested with Pytest.

### Question(s)

1. **Write a function `area_of_circle(radius)` that calculates the area of a circle.**
   - The function should return the area rounded to 2 decimal places.
   - Use the mathematical constant `π` from the `math` module.

   #### Example:
   ```python
   area_of_circle(5)  # Output: 78.54
   ```

2. **Write a function `hollow_right_triangle(n)` that returns a string representing a hollow right triangle pattern of stars (`*`) with height `n`.**
   - The height should be at least 4; otherwise, return: `"The triangle height should be at least 4."`
   - The first and last rows should be completely filled with `*`.
   - The middle rows should only have `*` at the edges.

   #### Example (n = 3):
   ```
   The triangle height should be at least 4.
   ```

   #### Example (n = 4):
   ```
   *
   **
   * *
   ****
   ```

   #### Example (n = 5):
   ```
   *
   **
   * *
   *  *
   *****
   ```

3. **Write a function `inverted_pyramid(n)` that returns a string representing an inverted pyramid pattern of stars (`*`) with height `n`.**
   - The height should be at least 3; otherwise, return: `"The pyramid height should be at least 3."`
   - Each row should be centered with decreasing numbers of `*`.
   
   #### Example (n = 3):
   ```
   *****
    ***
     *
   ```
   #### Example (n = 4):
   ```
   *******
    *****
     ***
      *
   ```
   #### Example (n = 5):
   ```
   *********
    *******
     *****
      ***
       *
   ```

### Run Command

```
pytest
```
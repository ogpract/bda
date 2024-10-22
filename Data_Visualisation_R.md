<h1>1. Scatter Plot:</h1>

```bash
# Load necessary libraries
library(ggplot2)

# Manual data
data <- data.frame(
  x1 = c(3, 4, 5, 6, 1, 3, 7, 8, 9, 2),
  y = c(20, 25, 30, 35, 15, 22, 38, 40, 45, 18)
)

# Scatter Plot: x1 vs. y
ggplot(data, aes(x = x1, y = y)) +
  geom_point(color = "blue") +
  labs(title = "Scatter Plot: x1 vs y", x = "x1", y = "y") +
  theme_minimal()
```

<h1>2. Histogram:</h1>

```bash
# Load necessary libraries
library(ggplot2)

# Manual data
data <- data.frame(
  y = c(20, 25, 30, 35, 15, 22, 38, 40, 45, 18)
)

# Histogram: Distribution of y
ggplot(data, aes(x = y)) +
  geom_histogram(fill = "skyblue", color = "black", bins = 5) +
  labs(title = "Histogram of y", x = "y", y = "Frequency") +
  theme_minimal()
```

<h1>3. Box Plot:</h1>

```bash
# Load necessary libraries
library(ggplot2)

# Manual data
data <- data.frame(
  category = c("A", "B", "A", "C", "B", "A", "C", "B", "C", "A"),
  y = c(20, 25, 30, 35, 15, 22, 38, 40, 45, 18)
)

# Box Plot: y by category
ggplot(data, aes(x = category, y = y, fill = category)) +
  geom_boxplot() +
  labs(title = "Box Plot: y by Category", x = "Category", y = "y") +
  theme_minimal()
```

<h1>4. Bar Plot:</h1>

```bash
# Load necessary libraries
library(ggplot2)

# Manual data
data <- data.frame(
  category = c("A", "B", "A", "C", "B", "A", "C", "B", "C", "A")
)

# Bar Plot: Frequency of Categories
ggplot(data, aes(x = category, fill = category)) +
  geom_bar() +
  labs(title = "Bar Plot: Frequency of Categories", x = "Category", y = "Count") +
  theme_minimal()
```

<h1>5. Density Plot:</h1>

```bash
# Load necessary libraries
library(ggplot2)

# Manual data
data <- data.frame(
  x1 = c(3, 4, 5, 6, 1, 3, 7, 8, 9, 2)
)

# Density Plot: Distribution of x1
ggplot(data, aes(x = x1)) +
  geom_density(fill = "lightgreen") +
  labs(title = "Density Plot: Distribution of x1", x = "x1", y = "Density") +
  theme_minimal()
```

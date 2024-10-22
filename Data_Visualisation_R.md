<h3>1. Scatter Plot:</h3>

```bash
x1 <- c(3, 4, 5, 6, 1, 3, 7, 8, 9, 2)
y <- c(20, 25, 30, 35, 15, 22, 38, 40, 45, 18)

# Scatter Plot: x1 vs. y
plot(x1, y, main = "Scatter Plot: x1 vs y", xlab = "x1", ylab = "y", col = "blue", pch = 19)
```

<h3>2. Histogram:</h3>

```bash
y <- c(20, 25, 30, 35, 15, 22, 38, 40, 45, 18)

# Histogram: Distribution of y
hist(y, main = "Histogram of y", xlab = "y", ylab = "Frequency", col = "skyblue", border = "black", breaks = 5)
```

<h3>3. Box Plot:</h3>

```bash
category <- c("A", "B", "A", "C", "B", "A", "C", "B", "C", "A")
y <- c(20, 25, 30, 35, 15, 22, 38, 40, 45, 18)
data <- data.frame(category, y)

# Box Plot: y by category
boxplot(y ~ category, data = data, main = "Box Plot: y by Category", xlab = "Category", ylab = "y", col = c("red", "green", "blue"))
```

<h3>4. Bar Plot:</h3>

```bash
category <- c("A", "B", "A", "C", "B", "A", "C", "B", "C", "A")
category_counts <- table(category)

# Bar Plot: Frequency of Categories
barplot(category_counts, main = "Bar Plot: Frequency of Categories", xlab = "Category", ylab = "Count", col = c("lightblue", "lightgreen", "salmon"))
```

<h3>5. Density Plot:</h3>

```bash
x1 <- c(3, 4, 5, 6, 1, 3, 7, 8, 9, 2)

# Density Plot: Distribution of x1
plot(density(x1), main = "Density Plot: Distribution of x1", xlab = "x1", ylab = "Density", col = "lightgreen")
```

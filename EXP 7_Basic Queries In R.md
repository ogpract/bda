One Time Query
```bash
install.packages("dplyr")
library(dplyr)
data(mtcars)
query_condition <- mtcars %>%
  filter(mpg > 20)
print(query_condition)
```

adhoc query
```bash
library(dplyr)
data(mtcars)
ad_hoc_query_result <- mtcars %>%
  filter(hp > 150) %>%
  arrange(desc(hp))
print(ad_hoc_query_result)
```


continuous query
```bash
library(dplyr)
data(mtcars)
perform_continuous_query <- function(data, cylinder_count = 6, interval = 5) {
  for (i in 1:5) {
    result <- data %>%
      filter(cyl == cylinder_count) %>%
      arrange(desc(wt))
        print(paste("Period:", i))
    print(result)
    Sys.sleep(interval)
  }
}
perform_continuous_query(mtcars, cylinder_count = 6)
```

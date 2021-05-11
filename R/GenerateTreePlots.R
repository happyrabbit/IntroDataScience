path <- 'https://raw.githubusercontent.com/guru99-edu/R-Programming/master/titanic_data.csv'
titanic <-read.csv(path)
titanic$age <- as.numeric(titanic$age)
titanic$fare <- as.numeric(titanic$fare)

idx <- titanic$survived == 1
titanic$survived[idx] <- "survived"
titanic$survived[!idx] <- "died"
titanic$survived <- as.factor(titanic$survived)

tree_fit <- rpart(survived ~ sex + age,  data=titanic)
plot(as.party(tree_fit))

prp(tree_fit, extra = 6, prefix = "fraction\n")

decisionplot(tree_fit, x, class = "survived", main = "")


ti_tree <- decision_tree() %>%
  set_engine("rpart") %>%
  set_mode("classification") %>%
  fit(survived ~ sex + age, data = titanic)

titanic %>%
  ggplot(aes(x=sex, y=age)) +
  geom_jitter(aes(col=survived), alpha=0.7) +
  geom_parttree(data = ti_tree, aes(fill=survived), alpha = 0.1) +
  theme_minimal()

x <- iris[, c("Petal.Length", "Petal.Width", "Species")]
model <- rpart(Species ~ ., data=x)
decisionplot(model, x, class = "Species", main = "",
             xlab = 'Petal Length', ylab = "Petal Width")

library(ggplot2)


data <- read.csv("./data.csv")

ggplot(data, aes(factor(label), duration)) + geom_boxplot() + 
  labs(title="Duration of API calls") +
  xlab("API Call") +
  ylab("Duration (Seconds)") +
  scale_y_log10()

listServicesData <- data[data$label == "ListServices", ]
ggplot(listServicesData, aes(factor(route), duration)) + geom_boxplot() + 
  labs(title="Duration of ListServices calls by route") +
  xlab("Route called") +
  ylab("Duration (Seconds)")

servicesStatusData <- data[data$label == "ServiceStatus", ]
ggplot(servicesStatusData, aes(factor(route), duration)) + geom_boxplot() + 
  labs(title="Duration of ServiceStatus calls by route") +
  xlab("Route called") +
  ylab("Duration (Seconds)")


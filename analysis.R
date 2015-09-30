library(ggplot2)


data <- read.csv("./data.csv")

# Duration of API calls - Linear Y scale
ggplot(data, aes(factor(label), duration)) + geom_boxplot() + 
  labs(title="Duration of API calls") +
  xlab("API Call") +
  ylab("Duration (Seconds)")

## Log scale - useful for very large Y differences
#ggplot(data, aes(factor(label), duration)) + geom_boxplot() + 
#  labs(title="Duration of API calls") +
#  xlab("API Call") +
#  ylab("Duration (Seconds)") +
#  scale_y_log10()

# ListServices - duration by route
listServicesData <- data[data$label == "ListServices", ]
ggplot(listServicesData, aes(factor(route), duration)) + geom_boxplot() + 
  labs(title="Duration of ListServices calls by route") +
  xlab("Route called") +
  ylab("Duration (Seconds)")

# ServiceStatus - duration by route
servicesStatusData <- data[data$label == "ServiceStatus", ]
ggplot(servicesStatusData, aes(factor(route), duration)) + geom_boxplot() + 
  labs(title="Duration of ServiceStatus calls by route") +
  xlab("Route called") +
  ylab("Duration (Seconds)")


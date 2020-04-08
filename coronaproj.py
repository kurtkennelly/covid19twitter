import corona
import ggplot

corona %>%
  ggplot( aes(x=date, fill=Tweets)) +
    geom_density(alpha=0.6) +
    scale_fill_manual(values=c("#26d5b8", "#ff5733")) +
    labs(fill="Race",
         y = "Number of Tweets",
         x = "Corona Tweets",
         title = "Number of Corona tweets by date") +
    theme(text = bold.14.text)

p <- ggplot(corona, aes(x=x) ) +
  geom_density( aes(x = datetweeted, y = density), fill="#26d5b8" ) +
  geom_label( aes(x=28, y=0.05, label="Corona Twwets by Date"), color="#26d5b8", size = 6, fill = "black") +
  
  geom_density( aes(x = datetweeted, y = density), fill= "#ff5733") +
  geom_label( aes(x=27, y=-0.05, label="Tweets by Day"), color="#ff5733", size = 6, fill = "black") +
  xlab("Day")+
  labs(title = "Distribution of COVID-19 Tweets",
       subtitle = "By date from twitter.com") +
  scale_x_continuous(labels = Tweets) +
  theme(text = bold.14.text)
p
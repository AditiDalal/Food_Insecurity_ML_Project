#choropleth map across texas
#food insecurity indicator is LILATracks_1And20
install.packages(c("ggplot2", "sf", "tigris", "dplyr", "tidyverse"))
library(tidyverse)
library(ggplot2)
library(sf)
library(tigris)
library(dplyr)
library(stringr)


#GET COUNTIES ------------------------------
options(tigris_use_cache = TRUE)
txCounties <- counties(state="TX", cb = TRUE, class = "sf")


#CREATE MAP -----------------------------------
#make sure txCounties is "sf"
txCounties <- st_as_sf(txCounties)

#make county names all lowercase
txCounties$NAME = txCounties$NAME %>%
  str_to_lower()%>%
  str_trim

FoodAccessData$Name = FoodAccessData$Name %>%
  str_to_lower() %>%
  str_trim()

#join the data into txMapData
txMapData = txCounties %>%
  left_join(FoodAccessData, by = c("NAME" = "Name"))

#map based on foodInsecure (1/0)
ggplot(txMapData) + 
  geom_sf(aes(fill = factor(foodInsecure)), color = "white", size = 0.1) + 
  scale_fill_manual(values = c("0" = "#d4e6f1", "1" = "#e74c3c"),
                    name = "Food Insecure",
                    labels = c("No", "Yes")) + 
  theme_minimal() + 
  labs(title = "Food Insecurity By County Across Texas",
       subtitle = "Counties are classified as food insecure if more than half tracts are food insecure")

#map based on avgInsecurity (gradient)
ggplot(txMapData) + 
  geom_sf(aes(fill = avgInsecurity), color = "white", size = 0.1) + 
  scale_fill_gradient(
    low = "#FFE5E5", 
    high = "#8B0000",
    name = "Avg Food Insecurity",
    na.value = "grey90"
  ) + 
  theme_minimal() + 
  labs(title = "Degree of Food Insecurity By County Across Texas")

#median family income choropleth

  
  
  
  
  
  
  



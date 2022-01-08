# GPLAN-Custom-RFP
## **Floorplan Generation using RPLAN dataset**
This project is aimed at using data instead of traditional graph theoretic methods to determine architecturally desirable floor plans. In the project I have added a feature of automatically generating graph adjacencies. It just requires the type of rooms the user wants and immediately produces architecturally desirable floor plans using RPLAN dataset.

### **Dataset**
It is a manually collected large-scale densely annotated dataset of more than 80k floor plans from real residential buildings. 
We have used this dataset to filter out the best adjacency graphs on input number of rooms.

For the dataset, you can request the data.mat file from the authors of "Data-driven Interior Plan Generation for Residential Buildings"
Link- https://docs.google.com/forms/d/e/1FAIpQLSfwteilXzURRKDI5QopWCyOGkeb_CFFbRwtQ0SOPhEg0KGSfw/viewform

**Main Idea** is coded in RFPSearch.py

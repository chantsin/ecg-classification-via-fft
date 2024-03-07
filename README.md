# ECG Capstone

**Author**: Calvin Chan 

**Data**: The data set used for this project is called **PTB-XL** from **PhysioNet** and can be found [here](https://physionet.org/content/ptb-xl/1.0.3/).

The Capstone Repo contains a README file with pre-existing headers and bullet points to help guide your thoughts. You are required to fill this file in with a Project Overview. The overview should reflect the structure of your Areas of Interest Submission, explaining the Problem Area, including those affected, your proposed Data Science solution, the impact of your solution, and a description of your dataset. Any changes or refinements to your Area of Interest should be reflected in the README, and it is expected that your description of the data will be more granular (including a Data Dictionary if feasible) compared to the Area of Interest submission.

## Project Overview

A non-technical overview of the subject area and the problem statement / opportunity you identified
An overview of your proposed vision for tackling the problem using Data Science
An estimate of the potential impact of such a solution
An introduction to the dataset, including data quality concerns and findings from preliminary EDA.
Next steps in terms of data processing, feature engineering and baseline modeling.

Biomedical signals have always been an important aspect of the medical field. From medical diagnosis and treatment of patients to researching and developing drugs, it has helped many of those who were in need. An important aspect of why it works is because of its ability to capture many valuable information about the physiological state of the body that medical professions would not have known otherwise. However, whether this information is transferred to good use or not solely depends on the physicians ability to read the signal. In this project, we will be focusing on electrocardiograms (ECGs or EKGs) which is responsible for recording electrical activity in the heart. A systematic review and meta-analysis published in 2020 looked at 78 studies that assessed the accuracy of ECG interpretations by physicians with different levels of training and specialization, including medical students, residents, physicians in non-cardiology practice, and cardiologists. It was found that the accuracy scores varied significantly between the different physician levels, ranging from 4% to 95%. This poses a significant problem for patients and specialists as different ECG results can lead to vastly different decision and outcomes. 

In this project, we will attempt to utilize data science techniques to read ECG data and provide a diagnostic outcome, giving physicians and specialist an additional support for interpretation. More specifically, we will look into utilizing classification techniques used in data science to classify ECG signals into different diagnostic categories. This project can have a great impact on medical professionals as well as patients since it can act as an additional diagnostic confirmation, potentially decreasing diagostic errors made physicians allowing for more accurate and better treatment to patients. 

The dataset used for this project is called PTB-XL taken from PhysioNet. It contains 21799 12-lead ECG entries of 18869 unique patients collected using devices from Schiller AG. The signals were taken over the course of nearly seven years between October 1989 and June 1996. The dataset also contains a metadata file which includes patient information such as their sex, age, weight, as well as an annotation file which encodes the type of diagnosis for each ECG. 

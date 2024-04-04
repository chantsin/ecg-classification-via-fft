# ECG Signal Classification via Fourier Transforms

**Author**: Calvin Chan 

**Data**: The data set used for this project is called **PTB-XL** from **PhysioNet** and can be found [here](https://physionet.org/content/ptb-xl/1.0.3/).

## Table of Contents
- [Project Overview](#overview)
- [Workflow Timeline](#workflow)
- [Project Status](#status)
- [Setup Requirements](#setup)

<a id='overview'></a>
## 1 - Project Overview

### Problem Area

Biomedical signals has always been an important aspect of the medical field. From medical diagnosis and treatment of patients to researching and developing drugs, it has helped many of those who were in need. An important aspect of why it works is because of its ability to capture many valuable information about the physiological state of the body that medical professions would not have known otherwise. However, whether this information is transferred to good use or not solely depends on the physicians ability to read the signal. In this project, we will be focusing on electrocardiograms (ECGs or EKGs) which is responsible for recording electrical activity in the heart. A systematic review and meta-analysis published in 2020 looked at 78 studies that assessed the accuracy of ECG interpretations by physicians with different levels of training and specialization, including medical students, residents, physicians in non-cardiology practice, and cardiologists. It was found that the accuracy scores varied significantly between the different physician levels, ranging from 4% to 95%. This poses a significant problem for patients and specialists as different ECG results can lead to vastly different decision and outcomes. 

### Those Affected

This project can be significant if it is scaled to a larger setting. Being able to have access to this tool in a hospital setting should definitely help physicians of different levels to have better and more accurate diagnosis. It is possible to help medical students and residents in training when they are still learning about how to interpret ECG signals. In terms of business value, I believe this could also be implemented in current technologies. Imagine having a smart watch that would take your ECG on a regular basis and have feedback about your heart condition. This would be significant for people who may have unknown underlying heart conditions that have not seen a doctor yet. To have a device tell you that you may have an underlying condition advising you to see a physician can be lifesaving.

### Data Science Solution

In this project, we will attempt to utilize data science techniques to read ECG data and provide a diagnostic outcome, giving physicians and specialist an additional support for interpretation. More specifically, we will look into utilizing classification techniques used in data science to classify ECG signals into different diagnostic categories. This project can have a great impact on medical professionals as well as patients since it can act as an additional diagnostic confirmation, potentially decreasing diagostic errors made physicians allowing for more accurate and better treatment to patients. 

### Data Description

The dataset used for this project is called PTB-XL taken from PhysioNet. It contains 21799 12-lead ECG entries of 18869 unique patients collected using devices from Schiller AG. The signals were taken over the course of nearly seven years between October 1989 and June 1996. The dataset also contains a metadata file which includes patient information such as their sex, age, weight, as well as an annotation file which encodes the type of diagnosis for each ECG. 

### Data Dictionary
The dataset we are using includes two main metadata files, `ptbxl_database.csv` which we will call **Metadata** and it contains the patients information, and `scp_statements.csv` which we will call **Annotation** containing the official SCP-ECG statements for diagnosis. Below we present the data dictionary for each file.

- **Metadata** (`ptbxl_database.csv`):
<div align='center'>

| Column                       | Data Types | Description                                                     |
|------------------------------|------------|-----------------------------------------------------------------|
| patient_id                   | float      | Unique patient ID                                               |
| age                          | float      | Age in years                                                    |
| sex                          | integer    | Sex (M/F)                                                       |
| height                       | float      | Height in centimeters                                           |
| weight                       | float      | Weight in kilograms                                             |
| nurse                        | float      | Nurse that took the ECG (placeholder value)                     |
| site                         | float      | Site in which ECG was recorded                                  |
| device                       | string     | Device used to record ECG                                       |
| recording_date               | datetime   | Date time when ECG was recorded                                 |
| report                       | string     | Report by cardiologist or automatic intepretation by ECG device |
| scp_codes                    | dictionary | Standardized SCP-ECG statements                                 |
| heart_axis                   | string     | Hearts overall electrical activity direction                    |
| infarction_stadium1          | string     | First infarction stadium                                        |
| infarction_stadium2          | string     | Second infarction stadium                                       |
| validated_by                 | float      | Cardiologist that validated signal (placeholder value)          |
| second_opinion               | boolean    | Second opinion required                                         |
| initial_autogenerated_report | boolean    | Autogenerated report by ECG device                              |
| validated_by_human           | boolean    | Results validated by human                                      |
| baseline_drift               | string     | Leads with baseline drift                                       |
| static_noise                 | string     | Leads with static noise                                         |
| burst_noise                  | string     | Leads with burst noise                                          |
| electrodes_problems          | string     | Leads with electrode problem                                    |
| extra_beats                  | string     | Extra beats present                                             |
| pacemaker                    | string     | Pacemaker present in patient                                    |
| strat_fold                   | integer    | Suggested stratified folds for train test split                 |
| filename_lr                  | string     | Low sampling rate file path                                     |
| filename_hr                  | string     | High sampling rate file path                                    |
</div>

- **Annotation** (`scp_statements.csv`):
<div align='center'>

| Column                        | Data Types | Description                     |
|-------------------------------|------------|---------------------------------|
| description                   | string     | Annotation description          |
| diagnostic                    | float      | Related to diagnosis            |
| form                          | float      | Related to signal form          |
| rhythm                        | float      | Related to rhythm               |
| diagnostic_class              | string     | Superclass for diagnosis        |
| diagnostic_subclass           | string     | Subclass for diagnosis          |
| statement category            | string     | Medical description             |
| SCP-ECG statement description | string     | Official SCP-ECG description    |
| AHA code                      | float      | Unique AHA ID                   |
| aECG REFID                    | string     | Annotated ECG standard notation |
| CDISC code                    | string     | Controlled terminology          |
| DICOM code                    | string     | DICOM tags                      |
</div>

<a id='workflow'></a>
## 2 - Project Workflow
1. **Data cleaning after combining Metadata and Annotation**
    - Pulling SCP-ECG codes for diagnostic superclass
2. **ECG denoising using Fourier Analysis**
    - Removal of baseline wandering and powerline interference
3. **Baseline modeling**
    - Logistic Regression
    - Simple ANN
    - Autoencoder
4. **Advanced modeling**
    - CNN
    - RNN
5. **Model Evalutation**
    - Choosing best model

<a id='status'></a>
## 3 - Project Status

### Current Progress
Currently finishing off Sprint 2 for the project, which includes a cleaned version of our metadata. Thus far we have started to test our method of Fourier Transforms on a sample signal by removing low frequency noise associated with Baseline Wandering. We performed statistical analysis on our signals through ANOVA to justify our use of fourier transforms. Preliminary modelling has also commenced using a simple neural network architecture for classifying our five diagnostic superclasses, however accuracy scores do not show promising results. Autoencoders were also used in an attempt to reconstruct sample ECG signals, although the results indicate little learning is achieved even after measures were made to prevent oversampling. 

### Next steps 
Next steps include expanding Fourier Transforms for high frequency signals and applying the results to our full dataset before testing them on autoencoder and simple neural network model again. We will also try out new models such as CNNs and RNNs as previous attempts using these architectures by other individuals have led to positive results. 

<a id='setup'></a>
## 4 - Setup

### Environment Download
To run the notebooks, the appropriate packages needs to be installed. We have included all the packages used for this project in the environment file `ecgcap.yml`. 


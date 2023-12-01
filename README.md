Hello Everyone! Welcome to PDMS World... In this project, you are going to explore the functionalities of pharmacists to monitor, control, and analyze the pharmaceutical store transactions.

A pharmacy database management system is an essential database for the healthcare and pharmacy industry. 
It maintains all the transaction records, medicine details, etc. to make pharmacist easy to work and provide service to customers/patients in an efficient and friendly manner.


My Pharmacy DMBS can handle various aspects of pharmacy operations, maintaining patient records, data management, and patient care.

1)	Patient Management
2)	Medication Management 
3)	Prescription Processing
4)	Backup Recovery
5)	Billing 
6)	Reports and Analytics
7)	Research

System Features and Function Requirements:

•	**Deleting expired medicines from DB** – For this feature, I am using triggers because, before the delete operation, I would like to show expired medicines in a table, for the easy checklist. 

•	**To retrieve prescription history of a patient** – For this feature, I am using a procedural query to retrieve the prescription history for a specific patient using stored procedures.

•	**To calculate monthly medication expense for a patient (To claim insurance)** – For this feature, I am using a functional query to calculate monthly medication expense for a patient, which is useful for billing as well as insurance.

•	**To retrieve medicines with low stock**- For this feature, I am using a nested query based on the available quantity of medication with low stock.

•	**To find common medication prescribed by many doctors** - For this feature, I am using a nested query to retrieve the drug_name and corresponding count that were prescribed by many doctors.

•	**To analyze medication usage trend** - For this feature, I am using a correlated query to analyze medication usage trends by correlating data between ‘prescription’ and ‘patient’ entities.

•	**Visualization of medication usage by different age groups**- For this feature, I am using correlated query to analyze medication usage trends of different age groups by correlating data between ‘prescription’ and ‘patient’ entities and describing the data in pie charts and grouped bar graphs.


**To run the code:**

Execute the command -> python Login.py

**Admin Password:**
Username - user1
password - abc123





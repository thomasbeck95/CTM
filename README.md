# **Smart GP Task Manager**

## **Overview**

The **Smart GP Task Manager** is a digital tool designed to streamline and optimise the daily workflow of General Practitioners (GPs). By automating task triage, prioritising workload, and integrating seamlessly with clinical systems, this tool helps GPs focus on urgent patient needs while efficiently managing routine administrative tasks around regular scheduled appointments.

## **Key Features**

### 1. Intelligent Task Prioritisation 🔴 🟡 🟢

 Uses a **Red-Amber-Green (RAG) system** to prioritise tasks based on urgency.

- Automated triage of **prescription requests, investigation results, and administrative tasks**.
- Integration with patient records to assess factors like medication history, test results, and consultation urgency.

### 2. Prescription Management 💊

- **Auto-prioritisation of requests** based on medication type, supply levels, and patient risk factors, pre-test probability level
- **Traffic light categorisation:**
  - 🔴 **Red:** Critical/Urgent
    - Medication type: Critical medications (e.g. insulin, anticoagulants, anti-epileptic medications)
    - Medication supply levels: 0-2 day supply remaining, or already run out.
    - Patient factors: (e.g. Age, history of complex medical history, polypharmacy, immunocompromised, cognitive impairment, severe mental illness, requiring regular medications prior to travel)
    - Pre-test probability of serious illness: High
  - 🟡 **Amber:** Important but non-urgent
    - Medication type: Medications for managing chronic health conditions that may have consequences (e.g. antihypertensives, contraception, SSRIs), controlled drugs, antibiotics
    - Medication supply levels: 2-5 day supply remaining
    - Patient factors: (e.g. history of diabetes, obesity, heart disease, COPD, history of non-compliance, recent hospital discharge)
    - Pre-test probability of serious illness: Moderate
  - 🟢 **Green:** Routine requests&#x20;
    - Medication type: (e.g. topical steroids, antihistamines, vitamins, iron supplements)
    - Medication supply levels: 5+ day supply remaining
    - Patient factors: (e.g. stable chronic health conditions)
    - Pre-test probability of serious illness: Low

### **3. Investigation Results Triage** 🧪

- **Automated classification of lab results and imaging reports:**
  - 🔴 **Red:** Urgent - requiring notification within 24 hours
    - New lab result significantly outside normal range (e.g. hyper/hypoglycaemia, TSH, potassium, haemoglobin, INR, cancer markers, drug monitoring levels)
    - Abnormal result based on type: Troponin, D-dimer, positive Q-fit
    - New suspicious radiology finding (report containing certain positive findings/keywords e.g. mass, lesion, nodule, tumour, malignancy)
    - Pre-test probability of serious illness: High
  - 🟡 **Amber:** Requiring review/notification within 2-3 days&#x20;
    - &#x20;New result moderately outside normal range (e.g. HbA1c, haemoglobin, CRP)
    - Pre-test probability of serious illness: Moderate
  - **🟢  Green:** Requiring review/notification within 4-5-days&#x20;
    - New result slightly outside normal range
    - Abnormal result based on type: (e.g. Vitamin levels, LFTs, cholesterol panel)
    - Pre-test probability of serious illness: Low
- **Integration with patient record** to flag trends or anomalies.



### **4. Administrative Tasks**

- **🔴 Red:**&#x20;
  - Requiring completion within 1 day
  - Ad hoc patient review (e.g. unwell patient reviewed by nurse)
  - Respond to pharmacist/specialist/allied health request or communication
- **🟡 Amber:**
  - Requiring completion within 2-3 days
  - Respond to patient request via phone/email/eConsult/NHS app/AccuRx
  - Fit notes
  - Referral requests
  - Review recent discharge correspondence
- **🟢  Green:**&#x20;
  - Requiring completion within 4-5-days
  - Medical/DVLA/employment reports
  - Review outpatient  correspondence



### **5. On-the-Day Admin & Workflow Management**

- **Task inbox with real-time updates**&#x20;
- **Integration with EMIS/SystmOne/other EHR** for seamless workflow adaptation.
- **GP-focused dashboard** showing outstanding tasks, priority flags, and pending admin work.

## **How It Works**

1. **Syncs with existing clinical systems** to import prescription requests, test results, and admin tasks.
2. **Uses AI-driven prioritisation** to categorise and rank tasks in real time based on urgency.
3. **Displays an intuitive dashboard** for GPs to efficiently manage their workload and manually re-order/triage as required.
4. Trial use with clinicians to train learning 
5. **Provides smart automation options** to handle low-priority tasks in bulk.



## **User Interface Concept**

- **Clear, uncluttered UI** with traffic-light indicators.
- **Task filtering & search bar** to find urgent requests quickly.
- **One-click  system** for adding/editing/reordering tasks
- **Assign or edit task type with corresponding icon** (prescription/investigation/admin/phone call etc)



## **Benefits**

✅ **Reduces cognitive overload** by automatically triaging tasks.\
✅ **Saves time** on admin work, improving patient care efficiency.\
✅ **Ensures urgent cases are prioritised** while routine work is managed effectively.\
✅ **Integrates seamlessly with existing GP software** for a smooth workflow.



## **Future Enhancements**

- 📌 **Adapt for use in hospitals** for junior doctor/on call ward tasks
- 📌 **Voice command integration** for hands-free task management.
- 📌 **Patient communication module** to auto-notify patients of non-urgent or normal results.
- **📌 Adapt for use in hospitals** for junior doctor/on call ward tasks

## **Installation & Integration**

- Works as a **web-based tool** or **EMIS/SystmOne add-on**.
- Requires **EHR secure login** for access.
- **Minimal setup required** – plug & play with existing workflows.

## **Get Involved!**

We’re looking for **GPs, software developers, and NHS IT specialists** to collaborate on refining this tool. Join us to **help shape the future of GP workflow automation**! 🚀

For feedback, collaboration, or testing inquiries, contact: **[Your Contact Information]**.


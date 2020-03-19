# User Stories  
  
### Personas  
**and disambiguation of key words**  
  
In the following text the **user** is both the **mentor** and the **student**. "User" just is used to collect descriptions for the functionalities available for that both roles. In addition to the "user" and "mentor" roles listed above, there is also the **admin** role.  
- **Mentor**: a person who controls the whole process and collects data about Demos (presentations) for later use.  
- **Student**: a person who signs up to present during the Demo.  
- **Admin**: a person who develops the app and has all possible access.
- **DemoDay**: a day of the week in which presentations take place.   
- **Demo**: a set of the presentations (usually 2-4) at the DemoDay.  
  
### User Stories

| **Business value** | **Title** | **Acceptance criteria** |  
| :--- | :--- | :--- |  
|      | List of future Demos | As an **user** I see page with list of all scheduled **DemoDays**, which includes (groups in rows (web) or blocks (mobile)):<br/>**1.** Triple-letters weekday shortcut (e.g. FRI for Friday, THU for Thursday)<br/>**2.** Full date (format: 01-03-1973, dd-mm-yyyy)<br/>**3.** Visiting company name (or "not declared yet")<br/>**4.** Student projects titles which is declared to presentation<br/>**5.** Available empty slots (or none) |  
|      |   |   |  
|      | DemoDay page | As an **user** I see particular **DemoDay** page which includes:<br/>**1.** Triple-letters weekday shortcut (e.g. FRI for Friday, THU for Thursday)<br/>**2.** Full date (format: 01-03-1973, dd-mm-yyyy)<br/>**3.** Visiting company name (or "not declared yet")<br/>**4.** Technologies sought by a visiting company (visible only with company name or "not declared yet")<br/>**5.** The number of open junior positions for each technology of the visiting company (visible only with company name or "not declared yet")<br/>**6.** Short description/ notes about the visiting company (optional)<br/>**7.** **a**. Student project titles (with small logo of main technology: Java, C#, Python), **b**. names of teams members, short descriptions of projects (optional) -> only point **a**. is visible in the default view, rest is visible by the click<br/>**8.** As a **mentor** I see list of students proposed to declare their presentation on this Demo (simple scoring: if "0" then students has highest priority to be declared and then they are at the top of the proposed list)<br/>**9.** As a **student** I see link to the declaration form just below company info block (I can add only own project team to DemoDay) |  
|      |   |   |  
|      | List of active students | As a **mentor** I see list of all active students from the 3rd, 4th and 5th module (the 5th is a kind of pseudo module, that calls: "JobHunt"). Students of the 3rd module have the opportunity to declare their presentations, but they are not obliged to do so. Whereas students of the 4th and 5th module must present at least once. As a mentor, when I see a list of students, I see information about each of them in a row:<br/>**1.** A small colored circle that adopts one of four colors: green, yellow, red, blue.<br/>-- **Green** for each student of 4th and 5th modules, which presented twice or more for the visiting company.<br/>-- **Yellow** for those who have one such presentation on their account.<br/>-- **Red** are students from 4th and 5th modules without any presentations in a front of the visiting company.<br/>-- Whereas **blue** is the color assigned to students from the 3rd module (for whom presentation is not required).<br/>**2.** Number of presentations<br/>**3.** Name<br/>**4.** Second name (optional)<br/>**5.** Surname<br/>**6.** His or her actual module (important for 4th ["Advance"] and 5th ["JobHunt"])<br/>**6.** The name of the current team<br/>**7.** Main technology /ies |  
|      |   |   |  
|      | Declaration form for student presentation | As an **user** I want to add particular presentation to **DemoDay** with that fields (if I'm a **student**, I can only add my current team):</br>**1.** Title of presentation</br>**2.** Name of the project team</br>**3.** Names-surnames of project team members</br>**4.** Used technologies</br>**5.** Main technology (e.g. Java, C#, Python, Scala, etc.)</br>**6.** File with presentation (optional) |  
|      |   |   |  
|      | Declaration form for the visiting company | As a **mentor** I want to create **DemoDay** only with company name and DemoDay date. I see form with that fields:</br>**1.** Date (after clicking on the field I see a small calendar of the month with the option of selecting a specific date)</br>**2.** Company name</br>**3.** Sought technologies (optional)</br>**4.** Links to the company's website and company representatives (LinkedIn profiles) (optional)</br>**5.** The number of open junior positions for each technology of the visiting company (optional)</br>**6.** Short description/ notes (optional)|  
|      |   |   |  
|      | Users authentication by OAuth Google | As an **user** I want to be logged instantly if I am logged with my browser session with the same google-account (e-mail address) as my codecool-account. |  
|      |   |   |  
|      | List of past DemoDays | As a **mentor** I want to see list of all past **DemoDays**. Only:</br>- full dates,</br>- company names,</br>- students grouped by teams. |  
|      |   |   |  
|      | History of changes | As a **mentor** I want to be able to see history of changes on particular **DemoDay** page. |  
|      |   |   |  
|      | Option for declare teammate by one click | As an **user** [when filling out the declaration form] I want to add another presenter from the same project team with one click |  
|      |   |   |  
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
|      | List of future Demos | As an **user** I see list of all scheduled **DemoDays** with its:<br/>**1.** triple-letters weekday shortcut (e.g. FRI for Friday, THU for Thursday),<br/>**2.** full date (format: 01-03-1973, dd-mm-yyyy),<br/>**3.** guest company name (or "not declared yet"),<br/>**4.** student projects titles which is declared to presentation,<br/>**5.** available empty slots (or none) |  
|      |   |   |  
|      | DemoDay page | As an **user** I see:<br/>**1.** triple-letters weekday shortcut (e.g. FRI for Friday, THU for Thursday),<br/>**2.** full date (format: 01-03-1973, dd-mm-yyyy),<br/>**3.** guest company name (or "not declared yet"),<br/>**4.** technologies sought by a visiting company,<br/>**5.** the number of open junior positions for each technology of the visiting company (or "not declared yet")<br/>**6.** short description/ notes about the visiting company (optional)<br/>**7.** student project titles, names of teams members, short descriptions<br/>**8.**as a **mentor**: students proposed to declare their presentation on this Demo (simple scoring: if "0" then student has highest priority to be declared).<br/>**9.**as a student: link to the declaration form (adding own project team to this DemoDay) |  
|      |   |   |  
|      | List of active students | As a **mentor** I see list of all active students from the 3rd, 4th and 5th module (the 5th is a kind of pseudo module, that calls: "JobHunt"). Students of the 3rd module have the opportunity to declare their presentations, but they are not obliged to do so. Whereas students of the 4th and 5th module must present at least once. As a **mentor**, when I see a list of students, I see information about each of them in a row:<br/>**1.** A small colored circle that adopts one of four colors: green, yellow, red, blue.<br/>-- Green for each student of 4th and 5th modules, which presented twice or more for the visiting company.<br/>-- Yellow for those who have one such presentation on their account.<br/>-- Red are students from 4th and 5th modules without any presentations in a front of the visiting company.<br/>-- Whereas blue is the color assigned to students from the 3rd module (for whom presentation is not required).<br/>**2.** Number of presentations<br/>**3.** Name<br/>**4.** Second name (optional)<br/>**5.** Surname<br/>**6.** His or her actual module (important for 4th ["Advance"] and 5th ["JobHunt"])<br/>**6.** The name of the current team<br/>**7.** Main technology /ies |  
|      |   |   |  
|      | Declaration form for student presentation | As an **user** I want to add particular presentation to DemoDay with that fields (if I'm a **student**, I can only add my current team):</br>**1.** Title of presentation</br>**2.** Name of the project team</br>**3.** Names-surnames of project team members</br>**4.** Used technologies</br>**5.** File with presentation (optional) |  
|      |   |   |  
|      | Declaration form for the visiting company | As a mentor I want to add company to DemoDay with that fields:</br>**1.** Name</br>**2.** sought technologies</br>**3.** Links to the company's website and company representatives (LinkedIn profiles)</br>**4.** Short description/ notes (optional)|  
|      |   |   |  
|      | Users authentication by OAuth Google | As an user I want to be logged instantly if I am logged with my browser session with the same google-account (e-mail address) as my codecool-account. |  
|      |   |   |  
|      | List of past DemoDays | As a mentor I want to see list of all past DemoDays. Only: dates, company names, students grouped by teams. |  
|      |   |   |  
|      | History of changes  | As a mentor I want to be able to see history of changes on particular DemoDay page. |  
|      |   |   |  
|      | Option for declare teammate by one click | As a user [when filling out the declaration form] I want to add another presenter from the same project team with one click. |  
|      |   |   |  
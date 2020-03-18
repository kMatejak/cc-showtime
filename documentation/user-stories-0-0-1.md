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
|      | List of future Demos | As an user I see list of all scheduled DemoDays with its:<br/>**1.** triple-letters weekday shortcut (e.g. FRI for Friday, THU for Thursday),<br/>**2.** full date,<br/>**3.** guest company name (or none if not declared yet),<br/>**4.** student projects titles which is declared to presentation,<br/>**5.** available empty slots (or none) |  
|      |   |   |  
|      | One Demo page | As an user I see:<br/>**1.** triple-letters weekday shortcut (e.g. FRI for Friday, THU for Thursday),<br/>**2.** full date,<br/>**3.** guest company name (or none if not declared yet),<br/>**4.** guest company technologies,<br/>**5.** guest company volume of open junior positions for each one (or none if company not declared yet)<br/>**6.** guest company short description<br/>**7.** student project titles and short description for each one<br/>**8.** students proposed to declare their presentation on this Demo (simple scoring: if "0" then student has highest priority to be declared). |  
|      |   |   |  
|      | List of active students | As a mentor I see list of all active students from the 3rd, 4th and 5th module (the 5th is a kind of pseudo module, that calls: "JobHunt"). Students of the 3rd module have the opportunity to declare their presentations, but they are not obliged to do so. Whereas students of the 4th and 5th module must present at least once. As a mentor, when I see a list of students, I see information about each of them in a row:<br/>**1.** A small colored circle that adopts one of four colors: green, yellow, red, blue. Green for each student of modules 4th and 5th who presented twice or more times to a guest company. Yellow for those who have one such presentation on their account. Red are students from modules 4th and 5th without any presentations in front of a guest company. Whereas blue is the color assigned to students from the 3rd module.<br/>**2.** Number of presentations<br/>**3.** First name<br/>**4.** Second name<br/>**5.** His or her actual module (important for 4th - "Advance" and 5th - "JobHunt")<br/>**6.** Title of actual team<br/>**7.** Main technology /ies |  
|      |   |   |  
|      | Declaration form for student presentation | As an user I want to add particular presentation to DemoDay with that fields:</br>**1.** Title of presentation</br>**2.** Name of the project team</br>**3.**Names and surnames of project team members</br>**4.** Used technologies</br>**5.** File with presentation (optional) |  
|      |   |   |  
|      | Declaration form for guest company | As a mentor I want to add company to DemoDay with that fields:</br>**1.** Name</br>**2.** Seeking technologies</br>**3.** Links to company's webpage and guest personas</br>**4.** Short description/ notes (optional)|  
|      |   |   |  
|      | Users authentication by OAuth Google | As an user I want to be logged instantly if I am logged with my browser session with the same google-account (e-mail address) as my codecool-account. |  
|      |   |   |  
|      | List of past DemoDays | As a mentor I want to see list of all past DemoDays. Listed only dates, companies, students grouped by teams. |  
|      |   |   |  
|      | History of changes  | As a mentor I want to be able to see history of changes on particular Demo page. |  
|      |   |   |  
|      | Option for declare teammate by one click | As an user I want to add another presenter from the same project team by one click. |  
|      |   |   |  
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
|      | List of future Demos | As an user I see list of all scheduled DemoDays with its:<br/>1. triple-letters weekday shortcut (e.g. FRI for Friday, THU for Thursday),<br/>2. full date,<br/>3. guest company name (or none if not declared yet),<br/>4. student projects titles which is declared to presentation,<br/>5. available empty slots (or none) |
|      |   |   |  
|      | One Demo page | As an user I see:<br/>- triple-letters weekday shortcut (e.g. FRI for Friday, THU for Thursday),<br/>- full date,<br/>- guest company name (or none if not declared yet),<br/>- guest company technologies,<br/>- guest company volume of open junior positions for each one (or none if company not declared yet)<br/>- guest company short description<br/>- student project titles and short description for each one<br/>- students proposed to declare their presentation on this Demo (simple scoring: if "0" then student has highest priority to be declared). |
|      |   |   |  
|      | List of activ students | As a mentor I see list of all activ students from the 3rd, 4th and 5th module (the 5th is a kind of pseudomodule, that calls: "JobHunt"). Students of the 3rd module have the opportunity to declare their presentations, but they are not obliged to do so. Whereas students of the 4th and 5th module must present at least once. As a mentor, when I see a list of students, I see information about each of them in a row:<br/>- A small colored circle that adopts one of four colors: green, yellow, red, blue. Green for each student of modules 4th and 5th who presented twice or more times to a guest company. Yellow for those who have one such presentation on their account. Red are students from modules 4th and 5th without any presentations in front of a guest company. Whereas blue is the color assigned to students from the 3rd module.<br/>- Number of presentations<br/>- First name<br/>- Second name<br/>- His or her actual module (important for 4th - "Advance" and 5th - "JobHunt")<br/>- Title of actual team<br/>- Main technology /ies |
|      |   |   |
|      | Declaration form for student presentation | TODO:Option for declare teammate by one click |
|      |   |   |
|      | Declaration form for guest company |   |
|      |   |   |
|      | Students authentication by OAuth Google |   |
|      |   |   | 
|      | List of past Demos |   |
|      |   |   |
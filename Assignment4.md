# Model Proposal for _RecruitWalk_

Matthew Nelson
* Course ID: CMPLXSYS 530,
* Course Title: Computer Modeling of Complex Systems
* Term: Winter, 2018



&nbsp; 

### Goal 
*****
 
The goal of this model is to observe the interactions between individual jobseekers and companies looking for talent. The scope of the model will focus on college seniors majoring in computer science/computer engineering and companies looking to fill entry level engineering roles.

&nbsp;  
### Justification
****
During the recruiting process, both job-seekers and companies are individual actors acting on their own self-interest. Not every student and every company ends up interacting with each other. Using ABM makes it easier to add in additiona complexity in the future.

&nbsp; 
### Main Micro-level Processes and Macro-level Dynamics of Interest
****
The key micro-level processes of interest are as follows:
1. Students rank their companies in order of preference
2. Companies rank students whom they interact with in order of preference
3. Students have predetermined strategies of job-seeking
4. Companies have predetermined strategies of recruiting talent
5. There is a likelihood that companies and students interact
6. Companies offer students who meet their recruiting strategy and have interacted with them jobs
7. Students decide whether to accept specific offers
8. This process occurs until the recruiting cycle is complete

The key macro-level dynamics of interest are as follows
1. How does recruiting strategy affect yield?
2. Do certain companies end up without positions being filled?
3. Do any students end up without jobs?
4. As the number of companies increases, does the average value gained through recruiting change?

&nbsp; 


## Model Outline
****
&nbsp; 
### 1) Environment
The environment in this model is the recruiting landscape. The environment will keep track of interactions and the resultant outcomes. Here are the environmental variables being tracked


_Description of the environment in your model. Things to specify *if they apply*:_

* _Boundary conditions (e.g. wrapping, infinite, etc.)_
* _Dimensionality (e.g. 1D, 2D, etc.)_
* _List of environment-owned variables (e.g. resources, states, roughness)_
* _List of environment-owned methods/procedures (e.g. resource production, state change, etc.)_


```python
# Include first pass of the code you are thinking of using to construct your environment
# This may be a set of "patches-own" variables and a command in the "setup" procedure, a list, an array, or Class constructor
# Feel free to include any patch methods/procedures you have. Filling in with pseudocode is ok! 
# NOTE: If using Netlogo, remove "python" from the markdown at the top of this section to get a generic code block
```

&nbsp; 

### 2) Agents
 
The first type of agents are the students. Students will have the following attributes:
1. Student ID Number
2. University Rank
4. GPA
5. Level of previous experience

Students will have a set of weighted static preferences stored in a list, generated randomly upon creation of agent. These preferences include:
1. Preferred region
2. Preferred salary
3. Preferred bonus
4. Preferred industry

In addition, students will have a ranked order of desired companies based on who they interact with. This order will be based on how well the company meets their preferences

 The second type of agents are the companies. Each company has the following attributes
 1. Company ID Number
 2. Industry
 3. Region
 
 Companies will have a set of the following weighted static preferences used to rank candidates:
 1. Desired major
 2. Desired GPA
 3. Desired level of experience
 
 In addition, companies will have a recruiting strategy based on the following criteria:
 1. Minimum university rank
 2. Salary offered
 3. Bonus offered
 4. Minimum previous experience accepted
 
 
 
 
 
 
* _List of agent-owned variables (e.g. age, heading, ID, etc.)_
* _List of agent-owned methods/procedures (e.g. move, consume, reproduce, die, etc.)_


```python
# Include first pass of the code you are thinking of using to construct your agents
# This may be a set of "turtle-own" variables and a command in the "setup" procedure, a list, an array, or Class constructor
# Feel free to include any agent methods/procedures you have so far. Filling in with pseudocode is ok! 
# NOTE: If using Netlogo, remove "python" from the markdown at the top of this section to get a generic code block
```

&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

_Description of the topology of who interacts with whom in the system. Perfectly mixed? Spatial proximity? Along a network? CA neighborhood?_
 
**_Action Sequence_**

_What does an agent, cell, etc. do on a given turn? Provide a step-by-step description of what happens on a given turn for each part of your model_

1. Step 1
2. Step 2
3. Etc...

&nbsp; 
### 4) Model Parameters and Initialization
The global parameters being tracked are as follows:
1. Number of student job-seekers
2. Number of companies
3. Number of total job openings
4. Number of student-company interactions

The model will be initialized by creating 24,500 students (the number of comp sci/computer engineering graduates in 2016) and a defined number of companies.
Each student will be assigned an attribute matrix and a preference matrix, as well as an empty list for ranking companies.
Their GPA will be randomly generated from a distribution which matches the distribution of undergraduate engineering students at the Texas Agricultural and Mechanical University.
They will also be randomly assigned to a university.
They will be assigned a random level of previous experience, ranging from 0-4, representing years or reasearch/internship/co-op experience




_Describe and list any global parameters you will be applying in your model._

_Describe how your model will be initialized_

_Provide a high level, step-by-step description of your schedule during each "tick" of the model_

&nbsp; 

### 5) Assessment and Outcome Measures
The quantitative measures being tracked are as follows:
1. Number of job offers
2. Number of accepted job offers
3. Number of declined job offers
4. Number of unfilled job openings
5. Number of students without jobs

_What quantitative metrics and/or qualitative features will you use to assess your model outcomes?_

&nbsp; 

### 6) Parameter Sweep
Some of the paratemers I am interested in sweeping is:
* Number of companies - between 10,000 and 100,000
_What parameters are you most interested in sweeping through? What value ranges do you expect to look at for your analysis?_

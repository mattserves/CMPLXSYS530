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
During the recruiting process, both job-seekers and companies are individual actors acting on their own self-interest. Not every student and every company ends up interacting with each other. Using ABM makes it easier to add in additional complexity in the future.

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
* Student ID Number
* University Rank
* GPA
* Level of previous experience

Students will have a set of equally weighted static preferences stored in a list, generated randomly upon creation of agent. Future complexity will add weights to the preferences. These preferences include:
* Preferred region
* Preferred salary
* Preferred bonus
* Preferred industry

In addition, students will have a ranked order of desired companies based on who they interact with. This order will be based on how well the company meets their preferences.

The student agent procedures are as follows (in pseudocode):

```python
def create_students(number_students):
    """This procedure creates the number of specified agents, and creates the matrixes for attributes, preferences and ranking"""
    for agent in number_agents:
        s_id = agent
        students_ids.append(s_id)
        
        s_gpa = rand_gpa()                 # calls random GPA function
        students_gpas.append(s_gpa)        # adds agent's GPA to list of all GPAs
        
        s_urank = university_rank()        # calls university ranking assignment function
        students_uranks.append(s_urank)    # adds agent's university rank to the list of rankings
        
        s_exp = level_experience()         # calls level of experience function
        students_exp.append(s_gpa)         # adds agent's level of experience to list
        
        salary_pref = salary_preference()        # calls salary preference function
        students_salary.append(salary_pref)      # adds agent's salary preference to list
        
        bonus_pref = bonus_preference()          # calls bonus preference function
        students_bonus.append(bonus_pref)        # adds agent's bonus preference to list
        
        region_pref = region_preference()        # calls region preference function
        students_region.append(region_pref)      # adds agent's region preference to list
        
     s_dict = {"Student ID": students_ids, "GPA": students_gpa, "Level Experience": students_gpas, "Salary Preference": students_salary, "Bonus Preferred Amount": students_bonus, "Regional Preference": students_region}
     s_matrix = pd.DataFrame(s_dict)


def rand_gpa():
    """This procedure is called by student agents, and returns a random gpa based on an underlying distribution"""
    gpa = numpy.random.choice(numpy.arange(1,17), p = [0.003, 0.001, 0.002, 0.002, 0.004, 0.005, 0.009, 0.016, 0.046, 0.066, 0.108,     0.137, 0.179, 0.152, 0.125, 0.090, 0.057])
    return gpa
    
def university_rank()
    """This procedure assigns the student to a university, which has a ranking value based on fictional US News and World Report rankings"""
    """The procedure will assume the students are normally distributed for now; future complexity will reflect real-life enrollment levels"""
    urank = random.randint(0, 351)
    return urank
    
def level_experience()
    """This procedure assigns the student a level of experience from 0-4, based on the number of relevant years of research/internship experience"""
    exp = random.randint(0, 4)
    return exp
    
def salary_preference()
    """This procedure assigns the student a salary preference from $70,000 to $120,000"""
    spref = random.randint(70000, 120000)
    return spref
    
def bonus_preference()
    """This procedure assigns the student a bonus preference from $0 to $50,000"""
    bpref = random.randint(0, 50000)
    return bpref

def region_preference()
    """This procedure assigns the student a regional preference from 1-6"""
    """1 - Southwest, 2 - Northwest, 3 - Midwest, 4, Southeast, 5 - Northeast"""
    rpref = random.randint(1, 5)
    return rpref

def industry_preference()
    """This procedure assigns the student an industry preference from 1 to 7"""
    """1 - Software, 2 - Hardware, 3 - Automotive, 4 - Consumer Goods, 5 - Consulting, 6 - Manufacturing, 7 - Telecomm"""
    """Future complexity will create distribution based on student surveys"""
    ipref = random.randint(1, 7)
    return ipref

```
The second type of agents are the companies. Each company has the following attributes
* Company ID Number
* Industry
* Region
 
Companies will have a set of the following weighted static preferences used to rank candidates:
* Desired major
* Desired GPA
* Desired level of experience
 
In addition, companies will have a recruiting strategy based on the following criteria:
* Minimum university rank
* Salary offered
* Bonus offered
* Minimum previous experience accepted
 
The company agent procedures are as follows (in pseudocode):

```python 
def create_companies(number_companies):
    """This procedure creates the number of specified agents, and creates the matrixes for attributes, preferences and ranking"""
    for company in number_companies:
        co_id = company
        co_ids.append(co_id)
        
        co_region = region_location()            # calls region location function
        co_regions.append(region_pref)           # adds company's region to list
        
        co_industry = industry()                 # calls industry function
        co_industries.append(co_industry)        # adds company's industry to list
        
        
        co_gpa = min_gpa()                       # calls minimum GPA function
        co_min_gpa.append(co_gpa)                # adds company's minimum GPA to list of all GPAs
        
        co_urank = min_rank()                    # calls minimum university ranking assignment function
        co_min_rank.append(co_urank)             # adds company's university rank to the list of rankings
        
        co_exp = min_experience()                # calls minimum level of experience function
        co_min_exp.append(co_exp)                # adds company's level of experience to list
        
        salary_pref = salary_preference()        # calls salary preference function
        students_salary.append(salary_pref)      # adds agent's salary preference to list
        
        bonus_pref = bonus_preference()          # calls bonus preference function
        students_bonus.append(bonus_pref)        # adds agent's bonus preference to list
        
        
     co_dict = {"Company ID": co_ids, "Region": co_regions, "Industry": co_industries}
     s_matrix = pd.DataFrame(s_dict)

def region_location()
    """This procedure assigns each company to a randomly selected region"""
    """1 - Southwest, 2 - Northwest, 3 - Midwest, 4, Southeast, 5 - Northeast""
    rloc = numpy.random.choice(numpy.arange(1,5), p = [0.40, 0.25, 0.10, 0.10, 0.15])
    return rloc
    
def industry()
    """This procedure assigns the company to an industry"""
    """1 - Software, 2 - Hardware, 3 - Automotive, 4 - Consumer Goods, 5 - Consulting, 6 - Manufacturing, 7 - Telecomm"""
    """Future complexity will create distribution based on job openings"""
    ind = random.randint(1, 7)
    return ind

def min_gpa():
    """This procedure is called by student agents, and returns a random gpa based on an underlying distribution"""
    wgpa = numpy.random.choice(numpy.arange(1,5), p = [0.20, 0.20, 0.20, 0.20, 0.20)
    """1 - No requirement, 2 - 2.0 GPA, 3 - 2.5 GPA, 4 - 3.0 GPA, 5 - 3.5
    return wgpa
    
def university_rank()
    """This procedure assigns the student to a university, which has a ranking value based on fictional US News and World Report rankings"""
    """The procedure will assume the students are normally distributed for now; future complexity will reflect real-life enrollment levels"""
    urank = random.randint(0, 351)
    return urank
    
def level_experience()
    """This procedure assigns the student a level of experience from 0-4, based on the number of relevant years of research/internship experience"""
    exp = random.randint(0, 4)
    return exp
    
def salary_preference()
    """This procedure assigns the student a salary preference from $70,000 to $120,000"""
    spref = random.randint(70000, 120000)
    return spref
    
def bonus_preference()
    """This procedure assigns the student a bonus preference from $0 to $50,000"""
    bpref = random.randint(0, 50000)
    return bpref





```


 
 
 
 
* _List of agent-owned variables (e.g. age, heading, ID, etc.)_
* _List of agent-owned methods/procedures (e.g. move, consume, reproduce, die, etc.)_

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

The initialization code is as follows

def init():
    global time, number_students, number_companies, envir, number_openings_start, number_openings_end, number_offers, number_interact


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

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
* Accepted offer

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
    for agent in number_students:
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
    
def level_experience():
    """This procedure assigns the student a level of experience from 0-4, based on the number of relevant years of research/internship experience"""
    exp = random.randint(0, 4)
    return exp
    
def salary_preference():
    """This procedure assigns the student a salary preference from $70,000 to $120,000"""
    spref = random.randint(70000, 120000)
    return spref
    
def bonus_preference():
    """This procedure assigns the student a bonus preference from $0 to $50,000"""
    bpref = random.randint(0, 50000)
    return bpref

def region_preference():
    """This procedure assigns the student a regional preference from 1-6"""
    """1 - Southwest, 2 - Northwest, 3 - Midwest, 4, Southeast, 5 - Northeast"""
    rpref = random.randint(1, 5)
    return rpref

def industry_preference():
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
 
In addition, companies will have a recruiting strategy based on the following criteria:
* Minimum GPA
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
        
        co_industry = industry()                 # calls industry function
        co_industries.append(co_industry)        # adds company's industry to list
        
        co_region = region_location()            # calls region location function
        co_regions.append(region_pref)           # adds company's region to list
        
        co_open = initial_openings()             # calls number of initial job openings function
        co__init_openings.append(co_offers)      # adds company's number to list
       
        co_gpa = minimum_gpa()                   # calls minimum gpa function
        min_gpa.append(co_gpa)                   # adds company's minimum gpa to list
       
        co_urank = min_rank()                    # calls minimum university ranking assignment function
        min_rank.append(co_urank)                # adds company's university rank to the list of rankings
        
        co_exp = min_experience()                # calls minimum level of experience function
        co_min_exp.append(co_exp)                # adds company's level of experience to list
        
        co_salary = maximum_salary()             # calls maximum salary function
        max_salary.append(co_salary)             # adds company's max salary preference to list
        
        co_bonus = maximum_bonus()               # calls maximum bonus function
        max_bonus.append(co_bonus)               # adds company's max bonus to list
        
        
     co_dict = {"Company ID": co_ids, "Region": co_regions, "Industry": co_industries, "Desired GPA": co_dgpa, "Minimum GPA": min_gpa, "Maximum Salary": max_salary, "Maximum Bonus": max_bonus}
     c_matrix = pd.DataFrame(co_dict)

def industry():
    """This procedure assigns the company to an industry"""
    """1 - Software, 2 - Hardware, 3 - Automotive, 4 - Consumer Goods, 5 - Consulting, 6 - Manufacturing, 7 - Telecomm"""
    """Future complexity will create distribution based on job openings"""
    ind = random.randint(1, 7)
    return ind

def region_location():
    """This procedure assigns each company to a randomly selected region"""
    """1 - Southwest, 2 - Northwest, 3 - Midwest, 4, Southeast, 5 - Northeast""
    rloc = numpy.random.choice(numpy.arange(1,5), p = [0.40, 0.25, 0.10, 0.10, 0.15])
    return rloc
    
def initial_openings():
    """This procedure assigns each company with a randomly selected number of job openings, from 5 to 100"""
    open = random.randint(5, 100)
    return open
    
def min_gpa():
    """This procedure assigns each company a minimum gpa requirement"""
    wgpa = numpy.random.choice(numpy.arange(1,5), p = [0.20, 0.20, 0.20, 0.20, 0.20)
    """1 - No requirement, 2 - 2.0 GPA, 3 - 2.5 GPA, 4 - 3.0 GPA, 5 - 3.5
    return wgpa
    
def min_rank():
     """This procedure assigns each company a minimum university ranking requirement"""
    mrank = random.randint(0, 351)
    return mrank
    
def min_experience():
    """This procedure assigns each company a minimum prior experience requirement"""
    mexp = random.randint(0, 4)
    return mexp
    
def maximum_salary():
    """This procedure assigns each company a maximum salary offered from $70,000 to $120,000"""
    maxsal = random.randint(70000, 120000)
    return maxsaal
    
def maximum_bonus():
    """This procedure assigns each company a maximum salary offered from $0 to $50,000"""
    maxbonus = random.randint(0, 50000)
    return maxbonus
```

&nbsp; 

### 3) Action and Interaction 
 
**_Interaction Topology_**

The interaction topology can be thought of as a tri-partite network. Students and companies may interact with each other, but only if the company selects the university to visit. Students will not interact with other students, and companies will not interact with other companies.
 
**_Action Sequence_**
Cycle 1
1. Step 1 - Companies create a list of universities to visit. This decision is based on recruiting strategy
2. Step 2 - Students create a ranking of companies from those who are planning to visit their university
3. Step 3 - An interaction probability is calculated based on student interest. The probability is set to zero for students who do not meet the company minimum requirements.
4. Step 4 - Students and companies interact. The companies rank the students they interact with based on weighted preferences (GPA and previous experience)
5. Step 5 - Companies offer jobs to students based on available openings
6. Step 6 - Students evaluate job offers and rank them based on preferences
7. Step 7 - Students accept/decline job offers and inform companies of decision

Cycle 2
1. Step 1 - Companies create a list of universities to visit. This decision is based on recruiting strategy
2. Step 2 - Students create a ranking of companies from those who are planning to visit their university
3. Step 3 - An interaction probability is calculated based on student interest. The probability is set to zero for students who do not meet the company minimum requirements and students who accepted jobs.
4. Step 4 - Students and companies interact. The companies rank the students they interact with based on weighted preferences (GPA and previous experience)
5. Step 5 - Companies offer jobs to students based on available openings
6. Step 6 - Students evaluate job offers and rank them based on preferences
7. Step 7 - Students accept/decline job offers and inform companies of decision

&nbsp; 
### 4) Model Parameters and Initialization


The model will be initialized by creating 24,500 students (the number of comp sci/computer engineering graduates in 2016) and 1,000 companies. It will create global parameters to track beginning and ending number of job openings, along with number of student-company interactions. A list to track whether students have accepted job offers will be initialized to False


The initialization code is as follows
```python

def init():
    global cycle, time, number_students, number_companies, total_openings_start, number_openings_end, number_offers, number_interact
    
    accepted_offer = [False for x in number_students]
    cycle = 1
    time = 2
    number_students = 24,500
    number_companies = 1000


```
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

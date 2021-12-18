# The Recrutment Tool
## Motion Bootcamp – Exam 2021 - REST API
### Uses the Django Rest framework to solve the problem

* [1. Functionalities](#chapter1)
    * [1.1. Create candidate](#section_1_1)
    * [1.2. Create recruiter](#section_1_2)
    * [1.3. Create job ](#section_1_3)
    * [1.3. Remove  job  ](#section_1_4)

* [2. Endpoints](#chapter2)
    * [2.1. Candidates ](#section_2_1)
    * [2.2. Skills  ](#section_2_2)
    * [2.3. Recruiters  ](#section_2_3)
    * [2.4. Jobs  ](#section_2_4)
    * [2.5. Interviews  ](#section_2_5)

# Functionalities <a class="anchor" id="chapter1"></a>
## Create candidate  <a class="anchor" id="section_1_1"></a>
***Each candidate  have skills on the basis of which he then looks for a job, first name, last name, email and bio.***
## Create recruiter  <a class="anchor" id="section_1_2"></a>
***Each candidate  have ONE recruiter, which is created AUTOMATICALLY by creating a candidate. Each recruiter have 5 free interview slots for conducting interviews and an experience level, starting from 1. When adding a new candidate, we check if his recruiter exists. If it exists, we  increment its level with one, otherwise we create a new one.***
## Create job  <a class="anchor" id="section_1_3"></a>
***Each job has skills on the basis of which we can look for a candidate. When we create a job, an interview with a suitable candidate was created AUTOMATICALLY. A suitable candidate is one who has at least one skill required by the job. If there is more than one suitable candidate, then we create interviews for everyone. Every candidate has only one recruiter and that recruiter has only five free slots. When we create an interview, we  find the recruiter who is responsible for the candidate and increase his experience level by one.***
## Remove  job  <a class="anchor" id="section_1_4"></a>
***When we remove a particular job, we delete all interviews for this job, as well as free up the slots of the recruiters responsible for this.***

# Endpoints <a class="anchor" id="chapter2"></a>
## Candidates <a class="anchor" id="section_2_1"></a>
            ▪ POST: http://localhost:8080/candidates/
            ▪ GET: http://localhost:8080/candidates/{id}
            ▪ PUT: http://localhost:8080/candidates/{id}
            ▪ DELETE: http://localhost:8080/candidates/{id}

***Note: CamelCase was changed to snake_case in the example below***

***Note: Look at the example bellow to see the required structure of the candidates JSON objects***
```
{
		"first_name": "Ingaborg",
		"last_name": "Sothern",
		"email": "isothern0@usatoday.com",
		"bio": "Long and descriptive biography of the candidate",
		"birth_date": "1999-05-22",
		"skills": [
		  { "name": "VueJS"},
		  { "name": "Java" },
		  { "name": "Angular"},
		  { "name": "C#" }
		],
		"recruiter": {
			"last_name": "Frye",
			"email": "pfrye1@whitehouse.gov",
			"country": "Russia"
		}
 }
 ```

## Skills <a class="anchor" id="section_2_2"></a>
            ▪ GET: http://localhost:8080/skills/{id}
            ▪ GET (only skills for which we have candidates at this moment): http://localhost:8080/skills/active

## Recruiters <a class="anchor" id="section_2_3"></a>
            ▪ GET (only recruiter with available candidates): http://localhost:8080/recruiters
            ▪ GET: http://localhost:8080/recruiters?level={level}

## Jobs <a class="anchor" id="section_2_4"></a>
            ▪ POST:  http://localhost:8080/jobs
            ▪ GET: http://localhost:8080/jobs?skill={skillName}
            ▪ DELETE: http://localhost:8080/jobs/{id}

***Note: Look at the example bellow to see the required structure of the jobs JSON objects***
```
{
    "title": "Junior Java Dev",
    "description": "Long job description.",
    "salary": 100.50,
    "skills": [
		  { "name": "HTML" },
		  { "name": "Java" },
		  { "name": "Angular" }
	]
  }
```
## Interviews <a class="anchor" id="section_2_5"></a>
            ▪ GET: http://localhost:8080/interviews



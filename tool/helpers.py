from tool.models import Candidate, Interview, Recruiter, Skills


def skills_checker(data, candidate_or_job):
    for skill in data['skills']:
        if not Skills.objects.filter(name=skill['name']).exists():
            new_skill = Skills(name=skill['name'])
            new_skill.save()
        skill_obj = Skills.objects.get(name=skill['name'])
        candidate_or_job.skills.add(skill_obj)
    return candidate_or_job


def recruiter_checker(recruiter):
    recruiters = Recruiter.objects.all()
    if not recruiters.filter(email=recruiter['email']).exists():
        new_recruiter = Recruiter.objects.create(**recruiter)
        new_recruiter.save()
        searching_recruiter = new_recruiter
    else:
        rec = recruiters.get(email=recruiter['email'])
        rec.level += 1
        rec.save()
        searching_recruiter = rec
    return searching_recruiter


def create_interview(job):
    candidates = set(Candidate.objects.filter(skills__in=job.skills.all()))
    for candidate in candidates:
        recruiter = Recruiter.objects.get(email=candidate.recruiter.email)
        if recruiter.interviews < 5:
            recruiter.interviews += 1
            recruiter.level += 1
            recruiter.save()
            Interview.objects.create(job=job,
                                     candidate=candidate,
                                     recruiter=recruiter).save()

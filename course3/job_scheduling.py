def bad_greedy(jobs):
    sorted_jobs = sorted(jobs, key=lambda job: (job[0] - job[1], job[0]), reverse=True)
    sum = 0
    completion = 0
    for job in sorted_jobs:
        completion += job[1]
        sum += job[0] * completion
    return sum
def optimal_greedy(jobs):
    sorted_jobs = sorted(jobs, key=lambda job: (job[0]/job[1], job[0]), reverse=True)
    sum = 0
    completion = 0
    for job in sorted_jobs:
        completion += job[1]
        sum += job[0] * completion
    return sum

def alg(file):
    with open(file) as f:
        str_jobs = f.readlines()[1:]
        jobs = []
        for job in str_jobs:
            weight, length = job.split()
            jobs.append((int(weight), int(length)))
        return([bad_greedy(jobs), optimal_greedy(jobs)])

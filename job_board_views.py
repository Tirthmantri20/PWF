from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer

# List all companies + Create new company
class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


# Retrieve + Update single company
class CompanyRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPost, Company
from .forms import JobPostForm

# Create Job Post
def job_create(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobPostForm()

    return render(request, 'jobs/job_form.html', {'form': form})


# List Jobs + Filter by Company
def job_list(request):
    jobs = JobPost.objects.all()
    companies = Company.objects.all()

    company_id = request.GET.get('company')

    if company_id:
        jobs = jobs.filter(company_id=company_id)

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'companies': companies
    })


# Job Detail
def job_detail(request, pk):
    job = get_object_or_404(JobPost, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})
from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views import View
# Create your views here.
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class GitHubProjects(View):
    def get(self, request):
        username = 'AhmedBerkat'  # Replace with your GitHub username
        url = f'https://api.github.com/users/{username}/repos'
        response = requests.get(url)
        
        if response.status_code == 200:
            repos = response.json()
            for repo in repos:
                if not repo['fork']:  # Exclude forks
                    Project.objects.update_or_create(
                        github_url=repo['html_url'],
                        defaults={
                            'title': repo['name'],
                            'description': repo['description'] or 'No description',
                            'technologies': repo.get('language', 'Unknown'),
                            'image_url': None,  # Add a placeholder or fetch repo image if available
                        }
                    )
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({'error': 'Failed to fetch GitHub repos'}, status=400)
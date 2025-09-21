from django.http import Http404
from django.shortcuts import render

PROJECTS = [
    {
        "slug": "web-portfolio",
        "title": "Personal Portfolio Builder",
        "status": "In Planning",
        "summary": "Static site generator to help members publish personal portfolios quickly.",
        "description": "This project will explore static site generation with modern tooling. Members will learn about content modeling, Markdown workflows, and deployment pipelines.",
        "tech_stack": ["Eleventy", "Tailwind CSS", "Netlify"],
    },
    {
        "slug": "campus-map",
        "title": "Interactive Campus Map",
        "status": "Design Phase",
        "summary": "Crowdsourced map with study spots, labs, and accessibility notes.",
        "description": "We plan to prototype an interactive map to highlight resources our members find useful. The project introduces geospatial data handling, map rendering, and user research.",
        "tech_stack": ["React", "Leaflet", "Supabase"],
    },
    {
        "slug": "ml-mentorship",
        "title": "Machine Learning Mentorship",
        "status": "Recruiting Members",
        "summary": "Small group mentorship track focused on ML fundamentals and mini-projects.",
        "description": "Participants will work through curated lessons on model evaluation, experiment tracking, and deployment. The project needs mentors, curriculum contributors, and data wranglers.",
        "tech_stack": ["Python", "scikit-learn", "Weights & Biases"],
    },
]


def home(request):
    return render(request, "core/home.html")


def weekly_meetings(request):
    context = {
        "agenda_items": [
            "Welcome and announcements",
            "Lightning talk (member spotlight)",
            "Hands-on coding challenge",
            "Project team breakouts",
            "Wrap-up and next steps",
        ],
        "algorithm_spotlight": {
            "title": "Binary Search Variations",
            "description": "Explore applications of binary search beyond sorted arrays, including answer space search and rotated arrays.",
            "problems": [
                {
                    "name": "Find Minimum in Rotated Array",
                    "source": "LeetCode 153",
                },
                {
                    "name": "Parametric Search for Cable Cutting",
                    "source": "Baekjoon 1654",
                },
                {
                    "name": "Aggressive Cows",
                    "source": "SPOJ AGGRCOW",
                },
            ],
        },
    }
    return render(request, "core/meetings.html", context)


def events(request):
    context = {
        "upcoming_events": [
            {
                "title": "Python Bootcamp",
                "date": "October 12, 2025",
                "location": "Lab 3, Engineering Building",
                "description": "A weekend crash course covering Python fundamentals, web development, and automation scripts.",
            },
            {
                "title": "Fall Club Fair",
                "date": "September 30, 2025",
                "location": "Student Center Atrium",
                "description": "Stop by our booth to meet officers, learn about projects, and grab stickers!",
            },
            {
                "title": "Hackathon Prep Night",
                "date": "November 5, 2025",
                "location": "CS Lounge",
                "description": "Workshop on ideation, team formation, and pitching ahead of regional hackathons.",
            },
        ]
    }
    return render(request, "core/events.html", context)


def projects(request):
    return render(request, "core/projects.html", {"projects": PROJECTS})


def project_detail(request, slug):
    project = next((p for p in PROJECTS if p["slug"] == slug), None)
    if project is None:
        raise Http404("Project not found")
    return render(request, "core/project_detail.html", {"project": project})

from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False   

class Label(BaseModel):
    id: int  # id maxim 1 2 o 3 personal project community
    name: str
    color: str

class Note(BaseModel):
    id: int
    title: str
    content: str
    link: str
    tasks: list[Task] = []
    img:  Optional[str]
    labels: list[Label] = []
    last_modified: str
    notebook_number: int
    reminder: bool = False
   

# Labels lookup
fake_db_labels = [
    {"id": 1, "name": "Personal",  "color": "#10b98125"},
    {"id": 2, "name": "Project",   "color": "#f59f0b29"},
    {"id": 3, "name": "LGTBIQ+", "color": "#9B48B02A"},
    {"id": 4, "name": "Kriter",    "color": "#5B8DE927"},
    {"id": 5, "name": "Community", "color": "#EF3C6C28"},
    {"id": 6, "name": "AI",        "color": "#D6E7573F"},
    {"id": 7, "name": "Stop Asian Hate", "color": "#FFFF0020"},
]

# Tasks lookup (you could also inline these in each note)
fake_db_tasks = [
    {"id":  1, "title": "Prepare brainstorming questions",
        "description": "", "completed": False},
    {"id":  2, "title": "Draft session outline",
        "description": "", "completed": False},
    {"id":  3, "title": "Summarize key takeaways",
        "description": "", "completed": False},
    {"id":  4, "title": "Meet with business owner",
        "description": "", "completed": False},
    {"id":  5, "title": "Identify improvement areas",
        "description": "", "completed": False},
    {"id":  6, "title": "Draft recommendation report",
        "description": "", "completed": True},
    {"id":  7, "title": "Compile weekly metrics",
        "description": "", "completed": True},
    {"id":  8, "title": "Draft update slides",
        "description": "", "completed": True},
    {"id":  9, "title": "Schedule team meeting",
        "description": "", "completed": True},
    {"id": 10, "title": "Analyze current workflow",
        "description": "", "completed": True},
    {"id": 11, "title": "Identify bottlenecks",
        "description": "", "completed": True},
    {"id": 12, "title": "Implement automation scripts",
        "description": "", "completed": True},
    {"id": 13, "title": "Review client agenda",
        "description": "", "completed": True},
    {"id": 14, "title": "Record meeting minutes",
        "description": "", "completed": True},
    {"id": 15, "title": "Send follow-up email",
        "description": "", "completed": True},
    {"id": 16, "title": "Backup database",
        "description": "", "completed": True},
    {"id": 17, "title": "Update documentation",
        "description": "", "completed": True},
    {"id": 18, "title": "Plan next sprint",
        "description": "", "completed": True},
    {"id": 19, "title": "New Task 1",
        "description": "", "completed": False},
]


fake_db = {
    "notes": [
        {
            "id": 1,
            "title": "Brainstorming Session Highlight...",
            "content": "Capture your team's best ideas he...",
            "link": "https://www.wikipedia.org",
            "tasks": [fake_db_tasks[0], fake_db_tasks[1], fake_db_tasks[2], fake_db_tasks[17]],
            "img": "./imgs/hab.jpg",
            # Personal, Project, Community
            "labels": [fake_db_labels[0], fake_db_labels[1], fake_db_labels[4]],
            "last_modified": "03:20 PM",
            "notebook_number": 1,
            "reminder": True
        },

        {
            "id": 2,
            "title": "Helping a local business",
            "content": "Amet minim mollit non deserunt il...",
            "link": "https://www.google.com",
            "tasks": [fake_db_tasks[3], fake_db_tasks[4]],
            "img": "./imgs/hab1.jpg",
            # Project, Kriter
            "labels": [fake_db_labels[1], fake_db_labels[3]],
            "last_modified": "11:24 AM",
            "notebook_number": 1,
            "reminder": False
        },
        {
            "id": 3,
            "title": "Weekly Team Update",
            "content": "Document this week's accomplishme...",
            "link": "https://www.linkedin.com",
            "tasks": [fake_db_tasks[6], fake_db_tasks[7], fake_db_tasks[8]],
            "img": None,
            "labels": [fake_db_labels[2], fake_db_labels[5]],  # LGTBIQ+, AI
            "last_modified": "09:02 AM",
            "notebook_number": 1,
            "reminder": False
        },
        {
            "id": 4,
            "title": "Streamline Your Workflow with...",
            "content": "In today’s fast-paced environment...",
            "link": "https://www.facebook.com",
            "tasks": [fake_db_tasks[9], fake_db_tasks[10], fake_db_tasks[11]],
            "img": "./imgs/hab2.jpg",
            # Personal, Kriter
            "labels": [fake_db_labels[0], fake_db_labels[3]],
            "last_modified": "10:20 AM",
            "notebook_number": 1,
            "reminder": True
        },
        {
            "id": 5,
            "title": "Client Meeting Notes",
            "content": "Keep a record of all client inter...",
            "link": "https://www.twitter.com",
            "tasks": [fake_db_tasks[12], fake_db_tasks[13], fake_db_tasks[14]],
            "img": None,
            # Personal, Community
            "labels": [fake_db_labels[0], fake_db_labels[4]],
            "last_modified": "04:53 PM",
            "notebook_number": 1,
            "reminder": False
        },
        {
            "id": 6,
            "title": "Additional Note 1",
            "content": "This is a placeholder for overflow note 1.",
            "link": "https://www.instagram.com",
            "tasks": [fake_db_tasks[15], fake_db_tasks[16], fake_db_tasks[17]],
            "img": None,
            "labels": [fake_db_labels[0], fake_db_labels[5]],  # Personal, AI
            "last_modified": "12:00 PM",
            "notebook_number": 1,
            "reminder": False
        },
        {
            "id": 7,
            "title": "Additional Note 2",
            "content": "This is a placeholder for overflow note 2.",
            "link": "https://example.com",
            "tasks": [],
            "img": "./imgs/hab.jpg",
            "labels": [
                fake_db_labels[3],  # Kriter
                fake_db_labels[6]   # added Stop Asian Hate
            ],
            "last_modified": "01:15 PM",
            "notebook_number": 1,
            "reminder": False
        },
        {
            "id": 8,
            "title": "Additional Note 3",
            "content": "This is a placeholder for overflow note 3.",
            "link": "https://example.com",
            "tasks": [],
            "img": "./imgs/hab.jpg",
            "labels": [
                fake_db_labels[0],
                fake_db_labels[1],
                fake_db_labels[2],
                fake_db_labels[3],
                fake_db_labels[4],
                fake_db_labels[5],
                fake_db_labels[6]  # added Stop Asian Hate
            ],
            "last_modified": "02:30 PM",
            "notebook_number": 1,
            "reminder": False
        }
    ]
    
}

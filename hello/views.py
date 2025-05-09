from django.shortcuts import render

from .models import Student

def student_list(request):

    student_count = Student.objects.count()
    if student_count < 5:
        from datetime import datetime

        existing_names = list(Student.objects.values_list('name', flat=True))

        students_to_add = [
            {
                "name": "이철수",
                "age": 25,
                "birth_date": datetime.strptime("2000-03-10", "%Y-%m-%d").date(),
                "grade": "A+",
                "subject": "물리학"
            },
            {
                "name": "박미나",
                "age": 23,
                "birth_date": datetime.strptime("2002-11-05", "%Y-%m-%d").date(),
                "grade": "B+",
                "subject": "심리학"
            },
            {
                "name": "정민호",
                "age": 27,
                "birth_date": datetime.strptime("1998-07-20", "%Y-%m-%d").date(),
                "grade": "A",
                "subject": "수학"
            },
            {
                "name": "김지원",
                "age": 26,
                "birth_date": datetime.strptime("1999-12-31", "%Y-%m-%d").date(),
                "grade": "A-",
                "subject": "영문학"
            },
            {
                "name": "최준서",
                "age": 24,
                "birth_date": datetime.strptime("2001-04-15", "%Y-%m-%d").date(),
                "grade": "B",
                "subject": "통계학"
            }
        ]

        for student_data in students_to_add:
            if student_data["name"] not in existing_names and student_count < 5:
                Student.objects.create(**student_data)
                student_count += 1

    from datetime import date

    today = date.today()
    students_over_25 = Student.objects.all().filter(
        age__gte=25
    )

    all_students = Student.objects.all()
    
    context = {
        'all_students': all_students,
        'students_over_25': students_over_25
    }
    
    return render(request, 'student/list.html', context)

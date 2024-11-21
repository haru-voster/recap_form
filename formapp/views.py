from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)  
        if form.is_valid():
            form.save()  
            return redirect('student_list')  
    else:  
        form = StudentForm(instance=student)
    
    return render(request, 'edit_student.html', {'form': form, 'student': student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.delete()  
        return redirect('student_list')  
    
    return render(request, 'confirm_delete.html', {'student': student})  



    

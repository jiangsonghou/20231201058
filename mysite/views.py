from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """
    自定义首页视图
    显示开发者信息：蒋松厚 20231201058
    """
    context = {
        'developer_name': '蒋松厚',
        'student_id': '20231201058',
        'project_name': '2023 Medical Project',
    }
    return render(request, 'home.html', context)


def about(request):
    """
    关于页面视图
    """
    return HttpResponse("""
    <h1>关于本项目</h1>
    <p><strong>开发者:</strong> 蒋松厚</p>
    <p><strong>学号:</strong> 20231201058</p>
    <p><strong>项目:</strong> 2023 Medical Project</p>
    <p><strong>框架:</strong> Django</p>
    <p><a href="/">返回首页</a></p>
    """)
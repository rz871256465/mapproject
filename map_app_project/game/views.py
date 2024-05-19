from django.shortcuts import render, redirect, get_object_or_404
from .models import Map
from .forms import MapForm
import json



def create_map(request):
    # 初始化表单，要么使用 POST 数据，要么为空
    if request.method == "POST":
        form = MapForm(request.POST)
        if form.is_valid():
            new_map = form.save(commit=False)
            map_data = request.POST.get('maze', '[]') 
            try:
                maze_data = json.loads(map_data)
                maze_data[0][0] = 2  # 假设红色方格用2表示
                maze_data[17][17] = 3  # 假设绿色方格用3表示
                # ... 其余代码
                new_map.save()
                return redirect('map_detail', map_id=new_map.id)
            except json.JSONDecodeError:
                form.add_error('maze', '无效的 JSON。')
                # 如果出现 JSONDecodeError，我们向表单添加一个错误
        # 如果表单无效或 JSON 数据有错误，重新渲染表单
        context = {'form': form}
    else:
        form = MapForm()
        context = {
            'form': form,
            'range_20': range(20),
        }
    return render(request, 'create_map.html', context)


def map_detail(request, map_id):
    map_instance = get_object_or_404(Map, id=map_id)
    map_data = map_instance.maze  # 这已经是一个二维数组了

    maze = []
    for row_index, row in enumerate(map_data):
        row_classes = []
        for col_index, cell in enumerate(row):
            if row_index == 0 and col_index == 0:
                cell_class = 'red'
            elif row_index == 17 and col_index == 17:
                cell_class = 'green'
            else:
                cell_class = 'wall' if cell == 1 else 'path'
            row_classes.append(cell_class)
        maze.append(row_classes)

    context = {
        'map': map_instance,
        'maze': maze,
    }
    return render(request, 'map_detail.html', context)


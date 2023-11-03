from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TodecideSerializer
from django.http import JsonResponse
import subprocess
from .models import AllVariables, Task
import re
from .my_functions import replace_first_occurrence
import ast


# Create your views here.

class TodecideView(APIView):
    def post(self, request, task_id):
        serializer = TodecideSerializer(data= request.data)
        if serializer.is_valid():
            solution = serializer.validated_data['solution']
            my_lst = []
            
            values_to_check = AllVariables.objects.filter(task= Task.objects.get(id = task_id))
            new_data = list()
            for values in values_to_check:
                my_list = ast.literal_eval(f"[{values.variables}]")
                my_list.append(values.result)
                new_data.append(my_list)



            the_first_obj = AllVariables.objects.filter(task= Task.objects.get(id = task_id)).first()
            value1 = the_first_obj.variables
            my_list = ast.literal_eval(f"[{value1}]")
            len_my_list = len(my_list)

            kolvo = solution.count('input()')
            if len_my_list != kolvo:
                return JsonResponse({"error": "Ошибка"}, status=400)
            
            solution = solution.replace(".split(' ')", '')

            for value in new_data:   
                for i in range(len_my_list):
                        solution = replace_first_occurrence(solution, 'input()', str(value[i]))


                result = subprocess.check_output(['python3', '-c', solution], stderr=subprocess.STDOUT, text=True)
                cleaned_string = result.replace('\n', ' ')
                if cleaned_string == value[-1]:
                    my_lst.append(True)
                else:
                    my_lst.append(False)

                solution = serializer.validated_data['solution']
                solution = solution.replace(".split(' ')", '')


            return JsonResponse({'my_lst': my_lst})
        



    


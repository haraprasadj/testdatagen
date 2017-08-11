from django.shortcuts import render
from django.http import FileResponse
from django.forms import formset_factory

from jsondata.forms import DataSpecForm, FieldSpecForm
from jsondata.repository.jsonrepo import JsonRepository


def index(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    if request.method == 'POST':
        data_size = request.POST.get("data_length")
        FieldSpecFormSet = formset_factory(FieldSpecForm, extra=int(request.POST.get("field_length")))
        formset = FieldSpecFormSet()
        return render(request, 'input_fields.html', {'size': data_size, 'formset': formset})
    form = DataSpecForm()
    return render(request, 'input.html', {'form': form})


def generate(request):
    if request.method == 'POST':
        dataspec = {}
        length = int(request.POST.get("data_size"))
        count = int(request.POST.get("form-TOTAL_FORMS"))
        dataspec['length'] = length
        dataspec['fields'] = []
        for i in range(count):
            name = request.POST.get("form-%s-field_name" % str(i))
            type = request.POST.get("form-%s-data_type" % str(i))
            dataspec['fields'].append({'name': name, 'type': type})
        repo = JsonRepository(dataspec)
        filepath = repo.get_json_data(request.session.session_key)
        return FileResponse(open(filepath, 'rb'))

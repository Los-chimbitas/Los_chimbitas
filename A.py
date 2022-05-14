@login_required
def list_measurements(request):
    role = getRole(request)
    if (role == "Admin") or (role == "Supervisor"):
        measurements = get_measurements()
        context= {
            'measurements_list': measurements,
        }
        return render(request, 'measurements/measurements.html', context)
    else:
        return HttpResponse("You are not authorized to access this page")
def measurement_create(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            create_measurement(form)
            messages.add_message(request, messages.SUCCESS, 'Measurement created successfully')
            return HttpResponseRedirect(reverse('measurementsCreate'))
        else:
            print(form.errors)
    else:
        form = MeasurementForm()
    context= {
        'form': form
    }
    return render(request, 'measurements/measurementcreate.html', context)


@login_required
def variable_list(request):
    role = getRole(request)
    if (role == "Admin") or (role == "Supervisor"):
        variables = get_variables()
        context= {
            'variables_list': variables,
        }
        return render(request, 'variables/variables.html', context)
    else:
        return HttpResponse("You are not authorized to access this page")

@login_required
def single_variable(request, variable_id):
    variable = get_variable(variable_id)
    context= {
        'variable': variable
    }
    return render(request, 'variables/variable.html', context)

@login_required
def variable_create(request):
    role = getRole(request)
    if (role == "Admin") or (role == "Supervisor"):
        if request.method == 'POST':
            form = VariableForm(request.POST)
            if form.is_valid():
                create_variable(form)
                messages.add_message(request, messages.SUCCESS, 'Variable created successfully')
                return HttpResponseRedirect(reverse('variableCreate'))
            else:
                print(form.errors)
        else:
            form = VariableForm()
        context= {
            'form': form
        }
        return render(request, 'variables/variableCreate.html', context)
    else:
        return HttpResponse("You are not authorized to access this page")
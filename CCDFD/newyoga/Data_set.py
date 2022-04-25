def Data_set(request):
    Sample_data = pd.read_csv('/CCDFD/newyoga/yoga/Sample_data.csv')
    filename = 'Sample_data.csv'
    response = HttpResponse(open(filename, 'rb').read(), content_type='text/csv')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename=%s' % 'Sample_data.csv'
    return 

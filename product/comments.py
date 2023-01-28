@api_view(['GET'])
def all_products(request):
    product = productMainModel.objects.all()
    serial = serialMain(product,many=True, read_only=True)
    return Response(serial.data)

@api_view(['GET'])
def colour_products(request):
    productImage = productImageModel.objects.all()
    serial1 = serialColour(productcolour,many=True)
    return Response(serial1.data)

@api_view(['GET'])
def image_products(request):
    productImage = productImageModel.objects.all()
    serial2 = serialImage(productImage,many=True)
    return Response(serial2.data)

@api_view(['GET'])
def one_products(request,pk):
    product = productMainModel.objects.get(pk=pk)
    product = product.image
    serial = serialMain(product,many=False)
    return Response(serial.data)

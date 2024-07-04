def importe_total_carro(request):
    total = 0
    
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total += float(value["precio"]) * value["cantidad"]
    
    total = round(total)
    
    return {"importe_total_carro": total}
from api.codes.models import Code, Safebox

def get_codes(role):
    if role == "admin":
        code = Code.objects.first()
        return code.code
    else:
        code = Safebox.objects.first().values()
        return code.code
    

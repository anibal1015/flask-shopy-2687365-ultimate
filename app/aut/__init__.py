from flask import Blueprint

aut = Blueprint('aut' ,__name__ ,url_prefix='/aut' , template_folder='templates' )

@aut.route("hola")
def hola():
    return "hola"


from . import routes
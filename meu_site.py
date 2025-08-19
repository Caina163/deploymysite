from flask import Flask, render_template

app = Flask(__name__)

# === CRIAR A 1º PAGINA DO SITE ===

#==========================================================================================
#EXPLICAÇÕES PARA CRIAR UMA PAGINA
# route -> é qual link vai abrir qual pagina (o caminho depois do dominio (/)). exemplo: meusite.com/home (apos a barra é o route)
# função -> é o que você quer exibir na pagina
# templates -> é onde voce criar o vizual do seu site (html)
#===========================================================================================


#route ▼ (pagina) HOMEPAGE
@app.route("/")
#(observação: so foi colocado o app após o @ pq na linha 3 o site está se chamando de app ( app = Flask(__name__) )

#função ▼
def homepage():
    return render_template("homepage.html") #esse RETURN direciona alguma coisa / esse render_templete é uma ferramenta que ajuda a direcionar para um html

#=============================================================================================

#route ▼ (pagina) CONTATOS
@app.route("/contatos")

#função ▼
def contatos():
    return render_template("contatos.html")

#===========================================================================================

#route ▼ (pagina) USUARIOS
@app.route("/usuarios/<nome_usuario>")

#função ▼
def usuarios(nome_usuario):
   return render_template("usuarios.html",nome_usuario=nome_usuario)











# servidor online no HEROKU

#===========================================================================================

# colocar o site no ar

if __name__== "__main__": # esse linha fala que vai rodar a linha de codigo abaixo. Caso esse arquivo seja importado por um outro arquivo ele nao vai mais rodar a linha de baixo. (isso evita erros na hora do deploy)
  app.run(debug=True) #ativar o debugar do site, ele automaticamente exibe sem precisar ficar parando e iniciando o site manualmente

#=============================================================================================

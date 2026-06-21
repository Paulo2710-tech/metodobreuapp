from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "metodo-abreu-dev"

ALUNOS = [
    {"id": 1, "nome": "Juliana Santos", "status": "Ativa", "inicio": "Jan/2024", "treinos": 24, "avaliacao": "15/07/2024", "peso": 64.8, "meta": 60.0, "mensalidade": "Pendente", "valor": 150.00, "objetivo": "Emagrecimento", "telefone":"(21) 98765-4321", "email":"juliana@email.com"},
    {"id": 2, "nome": "Camila Ferreira", "status": "Ativa", "inicio": "Fev/2024", "treinos": 18, "avaliacao": "10/07/2024", "peso": 68.2, "meta": 63.0, "mensalidade": "Pago", "valor": 150.00, "objetivo": "Hipertrofia", "telefone":"(21) 91234-7788", "email":"camila@email.com"},
    {"id": 3, "nome": "Larissa Oliveira", "status": "Ativa", "inicio": "Jan/2024", "treinos": 20, "avaliacao": "12/07/2024", "peso": 59.4, "meta": 57.0, "mensalidade": "Pago", "valor": 150.00, "objetivo": "Definição", "telefone":"(21) 94444-1122", "email":"larissa@email.com"},
    {"id": 4, "nome": "Mariana Costa", "status": "Ativa", "inicio": "Mar/2024", "treinos": 16, "avaliacao": "06/07/2024", "peso": 72.1, "meta": 66.0, "mensalidade": "Pendente", "valor": 150.00, "objetivo": "Condicionamento", "telefone":"(21) 97777-9090", "email":"mariana@email.com"},
    {"id": 5, "nome": "Rafael Costa", "status": "Inativo", "inicio": "Fev/2024", "treinos": 12, "avaliacao": "05/07/2024", "peso": 81.0, "meta": 78.0, "mensalidade": "Pendente", "valor": 180.00, "objetivo": "Força", "telefone":"(21) 96666-8888", "email":"rafael@email.com"},
]

TREINOS = [
    {"grupo": "A - Peito e Tríceps", "exercicios": [
        {"nome": "Supino Reto", "series": "4", "reps": "10-12", "descanso":"60s"},
        {"nome": "Supino Inclinado Halter", "series": "3", "reps": "10", "descanso":"60s"},
        {"nome": "Crucifixo", "series": "3", "reps": "12-15", "descanso":"45s"},
        {"nome": "Tríceps Pulley", "series": "3", "reps": "12", "descanso":"45s"},
    ]},
    {"grupo": "B - Costas e Bíceps", "exercicios": [
        {"nome": "Puxada Frente", "series": "4", "reps": "10-12", "descanso":"60s"},
        {"nome": "Remada Curvada", "series": "4", "reps": "10", "descanso":"60s"},
        {"nome": "Rosca Direta", "series": "3", "reps": "12", "descanso":"45s"},
    ]}
]

@app.context_processor
def inject_now():
    return {"ano_atual": datetime.now().year}

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        if "admin" in email.lower() or "personal" in email.lower():
            return redirect(url_for("admin_dashboard"))
        return redirect(url_for("aluno_dashboard"))
    return render_template("login.html")

@app.route("/admin")
def admin_dashboard():
    receita = sum(a["valor"] for a in ALUNOS if a["mensalidade"] == "Pago")
    pendente = sum(a["valor"] for a in ALUNOS if a["mensalidade"] == "Pendente")
    return render_template("admin_dashboard.html", alunos=ALUNOS, receita=receita, pendente=pendente)

@app.route("/alunos")
def alunos():
    return render_template("alunos.html", alunos=ALUNOS)

@app.route("/aluno/<int:aluno_id>")
def aluno_perfil(aluno_id):
    aluno = next((a for a in ALUNOS if a["id"] == aluno_id), ALUNOS[0])
    return render_template("aluno_perfil.html", aluno=aluno, treinos=TREINOS)

@app.route("/treinos")
def treinos():
    return render_template("treinos.html", treinos=TREINOS)

@app.route("/financeiro")
def financeiro():
    return render_template("financeiro.html", alunos=ALUNOS)

@app.route("/aluno")
def aluno_dashboard():
    aluno = ALUNOS[0]
    return render_template("aluno_dashboard.html", aluno=aluno, treinos=TREINOS)

@app.route("/aluno/treino")
def aluno_treino():
    return render_template("aluno_treino.html", treinos=TREINOS)

@app.route("/aluno/evolucao")
def aluno_evolucao():
    return render_template("aluno_evolucao.html", aluno=ALUNOS[0])

@app.route("/aluno/financeiro")
def aluno_financeiro():
    return render_template("aluno_financeiro.html", aluno=ALUNOS[0])

@app.route("/aluno/perfil")
def aluno_perfil_mobile():
    return render_template("aluno_perfil_mobile.html", aluno=ALUNOS[0])

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

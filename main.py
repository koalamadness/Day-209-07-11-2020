from flask import Flask, jsonify, request
from conexion import crear_usuario, iniciar_sesion

app = Flask(__name__)

@app.route("/api/v1/usuarios", methods=["POST"])
def usuario():
  if request.method == "POST" and request.is_json:
    try:
        data = request.get_json()
        print(data)

        if crear_usuario(data["correo"], data["contrasena"]):
            return jsonify({"code": "ok"})
        else:
            return jsonify({"code": "existe"})
    except:
        return jsonify({"code": "error"})

@app.route("/api/v1/sesiones", methods=["POST"])
def sesion():
  if request.method  == "POST" and request.is_json:
    try:
      data = request.get_json()
      correo = data["correo"]
      contra = data["contrasena"]
      id, ok = iniciar_sesion(correo, contra)
      if ok:
        return jsonify({"code": "ok", "id": id})
      else:
        return jsonify({"code": "noexiste"})
    except:
      return jsonify({"code": "error"})

app.run(debug=True)
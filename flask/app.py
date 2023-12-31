from flask import Flask, render_template, request, jsonify, session
from its import IntelligentTutor, LearningGoals, LearningResource, authenticated
import json
from flask_cors import CORS, cross_origin
from werkzeug.datastructures import ImmutableMultiDict
from mysql.connector import errorcode
from flask_bcrypt import Bcrypt
import os
import mysql.connector
import base64
import imghdr
import requests


app = Flask(__name__,
            static_folder='../ITS/src/learning_resources/',
            static_url_path='/static'
            )
app.secret_key = '10-03_02-15_7'
CORS(app)
bcrypt = Bcrypt(app)

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='its',
        autocommit= True,        
    )
    print("conectada exitosamente")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error de acceso: Usuario o contraseña incorrectos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe")
    else:
        print(err)


learning_goals = LearningGoals()
is_authenticated = authenticated()


@cross_origin
@app.route('/')
def init():
    return 'servidor esuchando'

@cross_origin
@app.route('/subirimagen', methods=['POST'])
def subirimagen():
    picture = request.files['picture']
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": "8de0fc15a938b9bb67ef4936fa7175a7"
    }

    files = {
        'image': (picture.filename, picture.stream, picture.mimetype)
    }

    response = requests.post(url, data=payload, files=files)
    data = response.json()
    print(data)
    enlace = data['data']['url']
    print(enlace)
    return enlace

@cross_origin
@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    user = request.form.get('user')
    password = request.form.get('password')
    picture = request.files['picture']
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": "8de0fc15a938b9bb67ef4936fa7175a7"
    }

    files = {
        'image': (picture.filename, picture.stream, picture.mimetype)
    }

    response = requests.post(url, data=payload, files=files)
    data = response.json()
    print(data)
    enlace = data['data']['url']

    cursor = connection.cursor()
    check_query = "SELECT user FROM student WHERE user = %s"
    cursor.execute(check_query, (user,))
    existing_user = cursor.fetchone()   

    if existing_user:
        cursor.close()
        return jsonify({'message': 'The user is already registered'})

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    query = "INSERT INTO student (name, picture, password, user) VALUES (%s, %s, %s, %s)"
    print(name, hashed_password, user)
    cursor.execute(query, (name, enlace, hashed_password, user,))
    connection.commit
    cursor.close()
    return jsonify({'message': 'User registered successfully'})


@cross_origin
@app.route('/login', methods=['POST'])
def login():
    connection.reconnect()
    data = request.get_json()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM student WHERE user = %s"
    cursor.execute(query, (data['user'],))
    user = cursor.fetchone()
    print(user)
    cursor.close()
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        return jsonify({'message': 'Login successful', 'user': {'id': user['id']},})
    else:
        return jsonify({'message': 'Login failed'})
    
@cross_origin
@app.route('/changePassword', methods=['PUT'])
def changePassword():
    id_user = request.form['id']
    current_password = request.form['currentPassword']
    new_password = request.form['newPassword']
    new_hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
    cursor = connection.cursor()
    query = "SELECT password FROM student WHERE id = %s"
    cursor.execute(query, (id_user,))
    results = cursor.fetchone()
    
    if results:
        if bcrypt.check_password_hash(results[0], current_password):    
            cursor.execute("UPDATE student SET password = %s WHERE id = %s", (new_hashed_password, id_user))
            cursor.close()
            return jsonify({'message': 'password updated successfully'})
        else:
            return jsonify({'message': 'The current password is not correct'})
    else: 
        return jsonify({'message': 'user not found'})
    

@cross_origin
@app.route('/stateVerified/<int:id>', methods=['GET'])
def stateVerified(id):

    cursor = connection.cursor()
    id_estudiante = id 
    consulta = "SELECT TestTopic, TestStyle FROM student WHERE id = %s"
    # Ejecutar la consulta
    cursor.execute(consulta, (id_estudiante,))
    result = cursor.fetchone()
    state_topic = result[0]
    state_style = result[1]
    cursor.close()

    print('state_topic', state_topic)
    print('state_style', state_style)


    return jsonify({"TestTopic": state_topic, "TestStyle": state_style})


@cross_origin
@app.route('/styleVerified/<int:id>', methods=['GET'])
def styleVerified(id):

    cursor = connection.cursor()
    id_estudiante = id 
    consulta = "SELECT TestStyle FROM student WHERE id = %s"
    # Ejecutar la consulta
    cursor.execute(consulta, (id_estudiante,))
    state = cursor.fetchone()[0]
    cursor.close()

    print('state', state)

    return jsonify({"TestStyle": state})

@cross_origin
@app.route('/diagnosis/<int:id>', methods=['POST'])
def diagnosis_lowlvl(id):
    print('id estudiante', id)
    questions = [
        {"activity_name": "t1", "correct_answer": "a"},
        {"activity_name": "t2", "correct_answer": "c"},
        {"activity_name": "t3", "correct_answer": "a"},
        {"activity_name": "t4", "correct_answer": "d"},
        {"activity_name": "t5", "correct_answer": "a"},
        {"activity_name": "t6", "correct_answer": "d"},
        {"activity_name": "t7", "correct_answer": "b"},
        {"activity_name": "t8", "correct_answer": "b"},
        {"activity_name": "t9", "correct_answer": "c"},
        {"activity_name": "t10", "correct_answer": "a"},
        {"activity_name": "t11", "correct_answer": "c"},
        {"activity_name": "t12", "correct_answer": "a"},
        {"activity_name": "t13", "correct_answer": "d"},
        {"activity_name": "t14", "correct_answer": "a"},
        {"activity_name": "t15", "correct_answer": "d"},
        {"activity_name": "t16", "correct_answer": "b"},
        {"activity_name": "t17", "correct_answer": "b"},
        {"activity_name": "t18", "correct_answer": "c"},
        {"activity_name": "t19", "correct_answer": "a"},
        {"activity_name": "t20", "correct_answer": "c"},
        {"activity_name": "t21", "correct_answer": "a"},
        {"activity_name": "t22", "correct_answer": "d"},
        {"activity_name": "t23", "correct_answer": "a"},
        {"activity_name": "t24", "correct_answer": "d"},
        {"activity_name": "t25", "correct_answer": "b"},
        {"activity_name": "t26", "correct_answer": "b"},
        {"activity_name": "t27", "correct_answer": "c"}
    ]

    incorrect_activities = {}
    incorrect_answer = []
    data = request.json
    print('data', data)
    answers = data.get('answers', [])
    print('answers', answers)

    for i, student_answer in enumerate(answers, start=1):
        question = questions[i - 1]
        activity_name = question['activity_name']

        if student_answer == question["correct_answer"]:
            print("Student Answer:", student_answer)
            print("Correct Answer for", activity_name)
            learning_goals.mark_activity_completed(activity_name)
        else:
            print("Incorrect Answer for", activity_name)
            incorrect_activities[activity_name] = student_answer

    for activity_name, answer in incorrect_activities.items():
        incorrect_answer.append(activity_name)

    print(incorrect_answer)

    response = learning_goals.print_learning_goals()
    recommended_path = learning_goals.recommend_learning_path()

    session['recommended_path'] = recommended_path
    session['incorrect_activities'] = incorrect_answer

    if connection.is_connected():
        cursor = connection.cursor()

        id_estudiante = id 
        incorrect_answer_json = json.dumps(incorrect_answer)  # Convertir a JSON
        recommended_path_json = json.dumps(recommended_path)  # Convertir a JSON

        consulta = "UPDATE student SET TestTopic = true, incorrect_answer = %s, recommendPath = %s WHERE id = %s"

        # Ejecutar la consulta
        cursor.execute(consulta, (incorrect_answer_json, recommended_path_json, id_estudiante))

    # Confirmar la transacción
        connection.commit()

    # Cerrar el cursor y la conexión
        cursor.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")
    return jsonify(response, recommended_path, 'Done!')

@app.route('/diagnosisEvaluation/<int:id>', methods=['POST'])
def diagnosisEvaluation(id):
    questions = [
        {"activity_name": "t1", "correct_answer": "a"},
        {"activity_name": "t2", "correct_answer": "c"},
        {"activity_name": "t3", "correct_answer": "a"},
        {"activity_name": "t4", "correct_answer": "d"},
        {"activity_name": "t5", "correct_answer": "a"},
        {"activity_name": "t6", "correct_answer": "d"},
        {"activity_name": "t7", "correct_answer": "b"},
        {"activity_name": "t8", "correct_answer": "b"},
        {"activity_name": "t9", "correct_answer": "c"},
        {"activity_name": "t10", "correct_answer": "a"},
        {"activity_name": "t11", "correct_answer": "c"},
        {"activity_name": "t12", "correct_answer": "a"},
        {"activity_name": "t13", "correct_answer": "d"},
        {"activity_name": "t14", "correct_answer": "a"},
        {"activity_name": "t15", "correct_answer": "d"},
        {"activity_name": "t16", "correct_answer": "b"},
        {"activity_name": "t17", "correct_answer": "b"},
        {"activity_name": "t18", "correct_answer": "c"},
        {"activity_name": "t19", "correct_answer": "a"},
        {"activity_name": "t20", "correct_answer": "c"},
        {"activity_name": "t21", "correct_answer": "a"},
        {"activity_name": "t22", "correct_answer": "d"},
        {"activity_name": "t23", "correct_answer": "a"},
        {"activity_name": "t24", "correct_answer": "d"},
        {"activity_name": "t25", "correct_answer": "b"},
        {"activity_name": "t26", "correct_answer": "b"},
        {"activity_name": "t27", "correct_answer": "c"}
    ]

    incorrect_activities = {}
    incorrect_answer = []
    data = request.json
    print('data', data)
    answers = data.get('answers', [])
    print('answers', answers)

    for i, student_answer in enumerate(answers, start=1):
        question = questions[i - 1]
        activity_name = question['activity_name']

        if student_answer == question["correct_answer"]:
            print("Student Answer:", student_answer)
            print("Correct Answer for", activity_name)
            learning_goals.mark_activity_completed(activity_name)
        else:
            print("Incorrect Answer for", activity_name)
            incorrect_activities[activity_name] = student_answer

    for activity_name, answer in incorrect_activities.items():
        incorrect_answer.append(activity_name)

    print(incorrect_answer)

    response = learning_goals.print_learning_goals()
    recommended_path = learning_goals.recommend_learning_path()

    session['recommended_path'] = recommended_path
    session['incorrect_activities'] = incorrect_answer
    if connection.is_connected():
        cursor = connection.cursor()

        id_estudiante = id 
        incorrect_answer_json = json.dumps(incorrect_answer)  # Convertir a JSON
        recommended_path_json = json.dumps(recommended_path)  # Convertir a JSON

        consulta = "UPDATE student SET incorrect_answer = %s, recommendPath = %s WHERE id = %s"

        # Ejecutar la consulta
        cursor.execute(consulta, (incorrect_answer_json, recommended_path_json, id_estudiante))

    # Confirmar la transacción
        connection.commit()

    # Cerrar el cursor y la conexión
        cursor.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")

    return jsonify('Done!', response )

@cross_origin
@app.route('/test/<int:id>', methods=['POST', 'GET'])
def testStyles(id):
    data = request.json
    print("data", data)
    answers = []

    for idx, answer in enumerate(data['answers']):
        if answer is not None:
            question_number = idx + 1
            question_key = f"pregunta{question_number}"
            answers.append((question_key, answer))

    print("answers", answers)

    # Crear el ImmutableMultiDict
    immutable_answers = ImmutableMultiDict(answers)

    learning_styles = {
        'Activo/Reflexivo': [1, 5, 9, 13, 17],
        'Sensorial/Intuitivo': [2, 6, 10, 14, 18],
        'Visual/Verbal': [3, 7, 11, 15, 19],
        'Secuencial/Global': [4, 8, 12, 16, 20]
    }
    
    selected_styles = {}

    for ask, response in immutable_answers.items():
        ask_num = int(ask.lstrip('pregunta'))
        for style, asks in learning_styles.items():
            if ask_num in asks:
                selected_styles[ask_num] = {
                    'style': style, 'response': response}
                break

    print(selected_styles)

    results = learning_goals.calculate_learning_style_score(selected_styles)
    print(results)

    for result in results:
        print(
            f"Estilo: {result['dominant_style']}, Resta: {result['subtraction']}")

    session['results'] = results

    if connection.is_connected():
        cursor = connection.cursor()

        id_estudiante = id
        style_list_json = json.dumps(results)  # Convertir a JSON


        consulta = "UPDATE student SET TestStyle = true, style_list = %s WHERE id = %s"

    # Ejecutar la consulta
        cursor.execute(consulta, (style_list_json, id_estudiante))

    # Confirmar la transacción
        connection.commit()

    # Cerrar el cursor y la conexión
        cursor.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")

    return jsonify('styles Done', results)



@cross_origin
@app.route('/Activity/<int:id>', methods=['GET', 'POST'])
def activity(id):
    id_estudiante = id
    incorrect_answer = []
    recommendPath = []
    style_list_s = []
    if connection.is_connected():
        cursor = connection.cursor()

        consulta = "SELECT incorrect_answer, recommendPath, style_list FROM student WHERE id = %s"
        cursor.execute(consulta, (id_estudiante,))  

    
        resultado = cursor.fetchone()
        if resultado is not None:
            incorrect_answer_serializado = resultado[0]
            recommendPath_serializado = resultado[1]
            style_list_serializado = resultado[2]
        # Deserializar el arreglo
            incorrect_answer = json.loads(incorrect_answer_serializado)
            recommendPath = json.loads(recommendPath_serializado)
            style_list_s = json.loads(style_list_serializado)
            print('incorrect_answer', incorrect_answer)
            print('recommendPath', recommendPath)
            print('style_list_s', style_list_s)

            

    # Cerrar el cursor y la conexión
        cursor.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")
    incorrect_activities = incorrect_answer
    recommended_path = recommendPath
    style_list_n = style_list_s


    print('incorrect', incorrect_activities)
    print('recommended_path', recommended_path)
    print('style_list_n', style_list_n)


    last_item = style_list_n.pop()
    style_list = style_list_n
    # nav_menu = last_item['dominant_style']
    nav_menu = 'Secuencial'
    #nav_menu = 'Global'

    combined_styles = []
    for entry in style_list:
        dominant_style = entry['dominant_style']
        style = entry['style']
        combined_style = f"{style}: {dominant_style}"
        combined_styles.append(combined_style)

    print("style", style_list, "nav", nav_menu, "combined", combined_styles)

    Learning_Resource = LearningResource('localhost', 'root', '', 'its')

    resource_list = Learning_Resource.find_resource(
        recommended_path, combined_styles)
    print("list", resource_list)

    for resource in resource_list:
        print("Activity:", resource["name"])
        print("Goal:", resource["goal"])
        print("Level:", resource["lvl"])
        print("URL:", resource["url"])
        print("PT:", resource["pt"])
        print("LC:", resource["lc"])

    filtered_resource = {}
    additionalResources_1 = {}
    additionalResources_2 = {}


# Este ciclo es para separar la primera táctica pedagógica de las demás
    for resource in resource_list:
        activity = resource['name']
        pt = resource['pt']
    
        if activity not in filtered_resource:
            filtered_resource[activity] = resource
        elif activity not in additionalResources_1:
            additionalResources_1[activity] = resource
        else:
            additionalResources_2.setdefault(activity, []).append(resource)
    
    filtered_resource_list = list(filtered_resource.values())
    additional_pt_resources_1 = list(additionalResources_1.values())
    additional_pt_resources_2 = list(additionalResources_2.values())


    for resource in filtered_resource_list:
        print("Activity:", resource["name"])
        print("Goal:", resource["goal"])
        print("Level:", resource["lvl"])
        print("URL:", resource["url"])
        print("PT:", resource["pt"])
        print("LC:", resource["lc"])
        print("-----")

    Learning_Resource.close_connection()
    print('resource ', filtered_resource_list)
    print('Additional1', additional_pt_resources_1)
    print('Additional2', additional_pt_resources_2)
    print('incorrect_activities', incorrect_activities)
    print('recommended_path', recommended_path)
    print('style_list_n', style_list_n)


    data_incorrect_answer = [int(item[1:]) for item in incorrect_activities if item.startswith(
        't') and item[1:].isdigit()]

    return jsonify({
        'nav_menu': nav_menu,
        'resource_list': filtered_resource_list,
        'resource_list_additional_1': additional_pt_resources_1,
        'resource_list_additional_2': additional_pt_resources_2,
        'data_incorrect_answer': data_incorrect_answer
    })

@cross_origin
@app.route('/dataUser/<int:id>', methods=['GET'])
def dataUser(id):
    connection.reconnect()
    cursor = connection.cursor()
    query = "SELECT * FROM student WHERE id = %s"
    cursor.execute(query, (id,))
    user = cursor.fetchone()
    cursor.close()
    print(user)

    recommendPath_serializado = user[9]
    style_list_serializado = user[10]

    recommendPath = json.loads(recommendPath_serializado)
    style_list = json.loads(style_list_serializado)

    if user is None:
        return jsonify({'message': 'User not found'}), 404
    
    dataUser = {
        'Id': user[0],
        'name': user[1],
        'password': user[2],
        'users': user[3],
        'picture': user[4],
        'Ls': user[5],
        'RecommendPath': recommendPath,
        'styleList': style_list
    }

    return jsonify(dataUser)


if __name__ == '__main__':
    app.run(debug=True)



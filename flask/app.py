from flask import Flask, render_template, request, jsonify, session, redirect, render_template_string
from its import IntelligentTutor, LearningGoals, LearningResource
import json
from flask_cors import CORS, cross_origin
from werkzeug.datastructures import ImmutableMultiDict


app = Flask(__name__,
            static_folder='../ITS/src/learning_resources/',
            static_url_path='/static'
            )
app.secret_key = 'your_secret_key'
CORS(app)


# Crea una instancia
learning_goals = LearningGoals()


@cross_origin
@app.route('/')
def init():
    return 'servidor esuchando'


@cross_origin
@app.route('/diagnosisrender')
def diagnosisState():
    return render_template('diagnosisState.html')


@cross_origin
@app.route('/diagnosis', methods=['POST'])
def diagnosis_lowlvl():
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
    return jsonify(response, recommended_path, 'Done!')


@app.route('/diagnosisEvaluation', methods=['POST'])
def diagnosisEvaluation():
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
    return jsonify('Done!', response )

@cross_origin
@app.route('/test', methods=['POST', 'GET'])
def testStyles():
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

    return jsonify('styles Done', results)


@cross_origin
@app.route('/StylesResults', methods=['GET'])
def resultsStyles():
    results = session.get('results')
    print(results)

    style_dict = {}
    for item in results:
        style = item['dominant_style']
        subtraction = item['subtraction']
        if style in style_dict:
            style_dict[style].append(subtraction)
        else:
            style_dict[style] = [subtraction]

    result_str = ', '.join(
        [f'{style}: {", ".join(map(str, subtractions))}' for style, subtractions in style_dict.items()])

    print(result_str)
    return jsonify(result_str)


@cross_origin
@app.route('/Activity', methods=['GET', 'POST'])
def activity():
    incorrect_activities = session.get('incorrect_activities')
    recommended_path = session.get('recommended_path')
    style_list_n = session.get('results')
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

    Learning_Resource = LearningResource('localhost', 'root', '', 'climate')

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

    data_incorrect_answer = [int(item[1:]) for item in incorrect_activities if item.startswith(
        't') and item[1:].isdigit()]

    return jsonify({
        'nav_menu': nav_menu,
        'resource_list': filtered_resource_list,
        'resource_list_additional_1': additional_pt_resources_1,
        'resource_list_additional_2': additional_pt_resources_2,
        'data_incorrect_answer': data_incorrect_answer
    })


if __name__ == '__main__':
    app.run(debug=True)

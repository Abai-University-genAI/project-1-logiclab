[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22794589&assignment_repo_type=AssignmentRepo)
#  ЖОБА 7: «Логикалық есептер генераторы»
Бұл жоба оқушылардың логикалық ойлауын дамытуға арналған интерактивті тренажер. Бағдарлама Бульдік логика негізінде есептер құрастырады және пайдаланушының білімін тексереді.
## Команда мүшелері және рөлдері
* **Жоба менеджері (Project Manager):** Сенбайқызы Ақбота — Жұмысты ұйымдастыру, мерзімдерді бақылау және топты үйлестіру.
* **Жоба архитекторы (Software Architect):** Уралхан Самал — Жүйенің техникалық шешімдерін жобалау және функциялар құрылымын анықтау.
үйлестіру.
* **Жоба архитекторы (Software Architect):** Төлеген Еркебұлан — Жүйенің техникалық шешімдерін жобалау және функциялар құрылымын анықтау.
* **Әзірлеуші (Developer):** Эшимова Дияра — Python кодын жазу және Бульдік логика функцияларын іске асыру.
* **Әзірлеуші (Developer):** Әлмахан Азамат — Кодтағы қателерді түзету (Debug) және тестілеу жұмыстары.
## Жұмыс барысы (Timeline)
### 1-күн: Analysis & Planning
* **Анализ:** Жобаның мақсаты — AND/OR/NOT есептерін шығаратын құрал жасау деп анықталды.
* **Жоспарлау:** Кодтың архитектурасы мен негізгі модульдері (есептеу, сұрақ қою, статистика) жобаланды.
### 2-күн: Implementation & Control
* **Implementation:** **ChatGPT** көмегімен бағдарламаның функционалдығы іске асырылды.
* **Control:** Бағдарламалық қателер анықталып, түзетілді. Шешімнің тұрақтылығы тексерілді.
### 3-күн: Defense
* Жоба нәтижелері жинақталып, қорғауға дайындық жүргізілді.
##  ЖИ қолданылуы (AI Usage)
Бұл жобаны әзірлеуде **ChatGPT** құралы қолданылды.
**Қолданылған промпттар (Prompts):**
1. 1.
*"Imagine I want to design an automated Boolean logicexercise generator for students lear
ning AND, OR, and NOT
operators. Can you outline a scalable architecturethat separates UI, logic,
and data handling, allows fastgeneration of new exercises,
and supports storingprevious results?*
2. *"How can an interactive Boolean logic exercise generator improve students’ algorithmic
thinking and logical reasoning skills? Provide examples of exercises at different
difficulty levels (easy, medium, hard) and explain how the system can adapt to each
student's learning pace using immediate feedback, hints, and statistics tracking."*
3. *. "Generate a JavaScript or Python example for dynamically creating Boolean logic
exercises with random AND, OR, and NOT combinations for 2 or more variables.
Include randomization of NOT operators, automatic truth table generation, and storage of
correct answers. Explain how this approach reduces repetitive work for teachers and
improves students’ algorithmic thinking and logical reasoning."*
##  Техникалық талаптардың орындалуы
* **Бульдік логика:** `True`, `False` мәндері және логикалық операторлар толық қолданылды.
* **Функциялар:** Әр амал мен модуль жеке функцияларға бөлінді.
* **Цикл:** Пайдаланушы жұмысты аяқтағанша `while` циклі үздіксіз жұмыс істейді.

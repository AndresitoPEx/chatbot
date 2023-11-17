from django.shortcuts import render
import openai

# Create your views here.

def home(request):

    #secretkey: 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


    #procesamos el formulario
    if request.method == "POST":
        vpregunta = request.POST['pregunta']

        #conexion con openai
        openai.api_key = "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"

        #creamos una instancia de openai
        openai.Model.list()

        #realizar la completion con el modelo de openai
        response = openai.Completion.create(
            engine="davinci",
            prompt=vpregunta,
            temperature=0.9,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=["\n", " Human:", " AI:"]
        )

        #parseamos la respuesta
        response = (response['choices'][0]['text']).strip()

        return render(request, 'home.html', {'dpregunta':vpregunta, 'dresponse':response})

    return render(request, 'home.html', {})


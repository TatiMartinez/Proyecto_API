import os
import openai
from .models import Incoming

openai.api_key =os.environ.get("OPENAI_KEY")




def userMessage(payload, conversationId):

    contexto = "\n Datos útiles para el asistente:contenido y recursos significa teoría a demanda significa que puede tomar la actividad en cualquier momento si es ademanda las actividades se deben realizar según el orden cuando el estudiante pregunta cual es mi próxima clase, responder con todo el detalle de la próxima actividad tipo clase que aún no inicia, en base al día de hoy siempre enviar el link de la actividad"
    contexto += "\n Datos de la Empresa UBOT: Soporte Técnico: mesadeayuda@ubot.cl"
    contexto += "\n UML es una herramienta en el mundo actual del desarrollo de sistemas. Permite a los creadores de sistemas generar diseños que capturen sus ideas en una forma convencional y fácil de comprender para comunicarlas a otras personas. Está compuesto por diversos elementos gráficos que se combinan para conformar diagramas. La finalidad de los diagramas es presentar diversas perspectivas de un sistema a las cuales se les conoce como modelo."
    contexto += "\n Diagrama de clases, Una clase es una categoría o grupo de cosas que tienen atributos y acciones similares."
    contexto += "\n Un objeto es una instancia de clase, una entidad que tiene valores especificos de los atributos y acciones"

    # obtner la lista de registros guardados en la base de datos por converstaionId
    
    messages = list(Incoming.objects.filter(conversationId=conversationId).values()) [-9:]
    conversation = "" 
    for message in messages:
        conversation += "\nHuman: " + message["payload"]
        conversation += "\nAI: "+ message["botResponse"]
    
    conversation += " \nHuman: "+ payload + "\n AI:"

    


    response = openai.Completion.create(
        model="text-davinci-002",
        # prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",
        prompt= contexto + conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    #print("response", response["choices"][0] ["text"] )
    bot = response["choices"][0] ["text"]
    return bot


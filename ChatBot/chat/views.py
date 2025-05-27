from django.shortcuts import render
from dotenv import load_dotenv
from .forms import ConversationForm
from google import genai

from .models import Prompts

# loading env
load_dotenv()

# list to store prompts and response till the program runs
prompt_res_store = []

# Create your views here.


def index(request):
    conv_form = ConversationForm()
    context = {"form": conv_form}
    return render(request, "chat/index.html", context)


def conversation(request):

    if request.method == "POST":
        conv_form = ConversationForm(request.POST)

        if conv_form.is_valid():

            prompt = conv_form.cleaned_data["prompt"]

            # initializing and getting response from trained model
            client = genai.Client()
            response = client.models.generate_content(
                model="tunedModels/faqtunedmodel-2mi1ma079yipeb6tb1979ho6sz",  # enter your fine tuned model here
                contents=f"{prompt} .Answer for TechNova Solutions",
            )
            output = response.text

            # saving prompt and response in database
            conv = Prompts(prompt=prompt, response=output)
            prompt_res_store.append(conv)
            conv.save()

            # rendering
            return render(
                request,
                "chat/conversation.html",
                context={
                    "conv_form": conv_form,
                    "prompt": prompt,
                    "output": output,
                    "session_history": prompt_res_store,
                },
            )


def history(request):
    prompts_res = Prompts.objects.all().order_by("prompt_date")
    conv_form = ConversationForm()

    return render(
        request,
        "chat/history.html",
        context={"prompts_res": prompts_res, "conv_form": conv_form},
    )

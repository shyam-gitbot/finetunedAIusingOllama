In this self-learning project, my main goal is to download a open source foundational model, and fine tune it to answer and resolve the query reagrding the hotel experince.
So the finetuned Model going to help the customer solve any problems/issues they having.

I am using the ollama to download the model locally and then fine tuning it with my own created data. 
I am choosing the tinyllama model as I don't have the GPU on my machine. 

>For downloading the Ollama: https://ollama.com/download 
I am using the Linux machine.

>You only need to run this command in the terminal to download the ollama locally: 

```
curl -fsSL https://ollama.com/install.sh | sh
```

>the downlaod was failing multiple times, so I modified the command to retry if it fails:

```
curl -fsSL --retry 5 --retry-delay 3 https://ollama.com/install.sh | sh
```

<!-- - (sep-19-25 : 02:18 )the system is having some issues downloading the ollama, I will try downlaoding the same using my home wifi, if not then I will continue this project in my own system using WSL.  -->
<!--  -->
<!-- - downloaded in the system watching it download made it successful  -->

I have succesfully downloaded the Ollama in system.
- running the tinyllama for now as the system don't have GPU power to handle big models

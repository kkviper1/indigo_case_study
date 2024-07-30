import gradio as gr
from huggingface_hub import InferenceClient

"""
For more information on `huggingface_hub` Inference API support, please check the docs: https://huggingface.co/docs/huggingface_hub/v0.22.2/en/guides/inference
"""
# client = InferenceClient("karanzrk/bert-Causal-QA")

from transformers import pipeline
gpt = pipeline('text-generation', model = 'karanzrk/gpt2-qa', tokenizer="gpt2", max_length = 128)
bert= pipeline('text-generation', model = 'karanzrk/bert-Causal-QA', tokenizer="bert-base-uncased", max_length = 128)
t5 = pipeline('text2text-generation', model = 'karanzrk/qa_t5', tokenizer="t5-small", max_length = 128)


def inference(text,model):
    match model:
        case "gpt2": generator = gpt
        case "bert": generator = bert
        case "t5": generator = t5 
        
    text = "Question: " + text
    output = generator(text)
    answer = output[0]
    return answer

# launcher = gr.Interface(
#     fn=inference,
#     inputs=gr.Textbox(lines=5, placeholder="Essay here...."),
#     outputs="text"
# )

with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Welcome to Q&A Chatbot
        Ask your question
        """
    )
    
    model_choice = gr.Dropdown(
            ["gpt2", "bert", "t5"], label="Choose your model", info="Choose the model to generate with!"
        )
    inputs = gr.Textbox(label="Input Box",lines = 5, placeholder="Question: ")
    button = gr.Button("Ask!")
    output = gr.Textbox(label="Output Box")
    button.click(fn=inference, inputs=[inputs,model_choice], outputs = output, api_name="Autograde")
    

demo.launch()


if __name__ == "__main__":
    demo.launch()
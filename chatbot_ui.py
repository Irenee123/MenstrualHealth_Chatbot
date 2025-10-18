import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load the fine-tuned model and tokenizer
model_path = "best_model"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

def generate_answer(question):
    """
    Generate an answer using the fine-tuned T5 model.
    This function replicates the inference logic from the training notebook.
    """
    # Prepare input with the same prefix used during training
    t5_input = "question: " + question.strip().lower()

    # Tokenize input
    input_ids = tokenizer(t5_input, return_tensors="pt").input_ids

    # Move to model's device (CPU by default, or GPU if available)
    device = next(model.parameters()).device
    input_ids = input_ids.to(device)

    # Generate response
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=64,  # Same as training
            num_beams=4,    # Add beam search for better quality
            early_stopping=True
        )

    # Decode and return answer
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer

def chatbot_interface(question):
    """
    Main interface function for the chatbot.
    Takes user question and returns formatted response.
    """
    if not question.strip():
        return "Please enter a question about menstrual health."

    try:
        answer = generate_answer(question)
        return f"**Question:** {question}\n\n**Answer:** {answer}"
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}. Please try again."

# Create Gradio interface
with gr.Blocks(
    title="Menstrual Health Chatbot",
    theme=gr.themes.Soft(),
    css="""
    .gradio-container {
        max-width: 800px;
        margin: auto;
    }
    .title {
        text-align: center;
        color: #2E8B57;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 1em;
    }
    .description {
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 2em;
        color: #666;
    }
    """
) as interface:

    gr.HTML("""
    <div class="title">🌸 Menstrual Health Chatbot</div>
    <div class="description">
        Ask me anything about menstrual health! I'm here to provide accurate, helpful information
        about periods, menstrual cycles, and related topics.
    </div>
    """)

    with gr.Row():
        with gr.Column(scale=1):
            question_input = gr.Textbox(
                label="Your Question",
                placeholder="e.g., What are menstrual cramps?",
                lines=3,
                show_label=True
            )

            submit_btn = gr.Button(
                "Ask the Chatbot",
                variant="primary",
                size="lg"
            )

    with gr.Row():
        answer_output = gr.Markdown(
            label="Chatbot Response",
            show_label=True
        )

    # Examples for users
    gr.Examples(
        examples=[
            "What is a normal menstrual cycle length?",
            "How can I alleviate menstrual cramps?",
            "What are the signs of a heavy menstrual flow?",
            "Is it normal to experience mood swings during menstruation?",
            "What are some natural remedies for PMS?",
            "How do I track my menstrual cycle effectively?",
            "What is endometriosis?",
            "What are the symptoms of PCOS?",
            "When does menstruation typically begin?",
            "How much blood is lost during menstruation?"
        ],
        inputs=question_input,
        label="Example Questions (Click to try)"
    )

    # Connect the interface
    submit_btn.click(
        fn=chatbot_interface,
        inputs=question_input,
        outputs=answer_output
    )

    # Allow Enter key submission
    question_input.submit(
        fn=chatbot_interface,
        inputs=question_input,
        outputs=answer_output
    )

if __name__ == "__main__":
    # Launch the interface
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        show_api=False,
        share=False  # Set to True if you want a public link
    )
import torch
from diffusers import StableDiffusionPipeline


# =========================================================
# MODEL
# =========================================================

MODEL_ID = "runwayml/stable-diffusion-v1-5"

_pipe = None


# =========================================================
# LOAD MODEL
# =========================================================

def load_image_model():

    global _pipe

    if _pipe is None:

        _pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float32
        )

        # CPU par model run hoga
        _pipe = _pipe.to("cpu")

    return _pipe


# =========================================================
# GENERATE ROOM IMAGE
# =========================================================

def generate_room_image(
    furniture,
    interior_style,
    requirements
):
    """
    Generate an AI-generated IKEA-style
    interior room image using Stable Diffusion.
    """

    # Load model
    pipe = load_image_model()

    # Create prompt
    prompt = f"""
A highly realistic professional interior
design photograph of a beautiful IKEA-style room.

Furniture:
{furniture}

Interior Style:
{interior_style}

Room Requirements:
{requirements}

Modern Scandinavian interior,
IKEA-inspired furniture,
realistic furniture proportions,
natural daylight,
cozy atmosphere,
clean organized room,
beautiful interior decoration,
indoor plants,
realistic materials,
wooden floor,
professional architectural photography,
photorealistic,
high detail,
high quality.
"""

    # Generate image
    image = pipe(
        prompt,
        num_inference_steps=10,
        guidance_scale=6,
        height=384,
        width=384
    ).images[0]

    return image
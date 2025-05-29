import numpy as np
import cv2
import onnxruntime as ort
from PIL import Image
import gradio as gr

LABELS = {0: "door", 1: "window"}

session = ort.InferenceSession("best.onnx")
input_name = session.get_inputs()[0].name

def api_detect(image, conf_threshold=0.5):
    image_np = np.array(image.convert("RGB"))
    img = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    img = cv2.resize(img, (640, 640))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.transpose(2, 0, 1) / 255.0
    input_tensor = np.expand_dims(img, axis=0).astype(np.float32)

    outputs = session.run(None, {input_name: input_tensor})
    preds = outputs[0]
    preds = preds[0] if preds.ndim == 3 else preds 
    preds = preds.T  

    detections = []
    for pred in preds:
        x, y, w, h, conf, cls = pred
        if conf > conf_threshold:
            label = LABELS.get(int(cls), str(int(cls)))
            detections.append({
                "label": label,
                "confidence": round(float(conf), 2),
                "bbox": [round(float(x), 2), round(float(y), 2),
                         round(float(w), 2), round(float(h), 2)]
            })

    return {"detections": detections}

api = gr.Interface(
    fn=api_detect,
    inputs=gr.Image(type="pil"),
    outputs="json",
    live=False
)

# Launch locally or on Hugging Face Space
api.launch()

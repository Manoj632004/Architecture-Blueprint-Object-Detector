YOLOv8-based object detection model for identifying doors and windows in architectural blueprints. Developed as part of an assignment for Palcode.ai.

---

## Step 1: Manual Labeling

- Dataset manually labeled using **[Roboflow](https://roboflow.com)**.
- Classes: `door`, `window`.

![Manual Labeling](https://github.com/user-attachments/assets/33c556ed-dc79-44bc-b46b-3f6674b68854)


## Step 2: Dataset Preparation & Augmentation

- **Total images**: 20
- **Train/Validation Split**:  
  - Training set: 16 images  
  - Validation set: 4 images

### Preprocessing
- Auto-orient:
- Resize: **Stretched to 1024×1024**

### Augmentations
- Outputs per training image: **3**
- 90° Rotate: Clockwise, Counter-clockwise, Upside-down
- Random Rotation: Between -15° and +15°
- Brightness Adjustment: ±15%
- Exposure Adjustment: ±10%
- Noise: Up to 0.1% of pixels

### Exports
Two dataset versions were exported for evaluation:
- `640×640` resolution
- `1024×1024` resolution

## Step 3: Model Training & Evaluation

Three models were trained and evaluated for performance:

| Model      | Notes                     |
|------------|---------------------------|
| YOLOv8n    | Performed best overall    |
| YOLOv8s    | Lower accuracy            |
| YOLOv11n   | Lower accuracy            |

> After repeated fine-tuning, **YOLOv8n** delivered the best results in terms of precision and bounding box accuracy.

![image](https://github.com/user-attachments/assets/dcb72ece-60cd-4e4e-8db8-604cbad8c567)

Run Flask API:

pip install flask <br />
python app.py

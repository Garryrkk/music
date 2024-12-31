import React, { useState } from "react";
import { uploadImage } from "../../services/api";
import "./EmotionDetector.css";

const EmotionDetector = ({ onRecommendations }) => {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (e) => {
        setSelectedFile(e.target.files[0]);
    };

    const handleSubmit = async () => {
        if (selectedFile) {
            const formData = new FormData();
            formData.append("image", selectedFile);
            try {
                const response = await uploadImage(formData);
                onRecommendations(response.data);
            } catch (error) {
                console.error("Error uploading image:", error);
            }
        }
    };

    return (
        <div className="emotion-detector">
            <h2>Detect Emotion</h2>
            <input type="file" accept="image/*" onChange={handleFileChange} />
            <button onClick={handleSubmit}>Analyze</button>
        </div>
    );
};

export default EmotionDetector;

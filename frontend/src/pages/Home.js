import React, { useState } from "react";
import EmotionDetector from "../components/EmotionDetector/EmotionDetector";
import Playlist from "../components/Playlist/Playlist";

const Home = () => {
    const [recommendations, setRecommendations] = useState([]);

    const handleRecommendations = (data) => {
        setRecommendations(data.recommendations);
    };

    return (
        <div>
            <h1>Music Recommendation System</h1>
            <EmotionDetector onRecommendations={handleRecommendations} />
            {recommendations.length > 0 && <Playlist recommendations={recommendations} />}
        </div>
    );
};

export default Home;

import React from "react";
import "./Playlist.css";

const Playlist = ({ recommendations }) => {
    return (
        <div className="playlist">
            <h2>Recommended Songs</h2>
            <ul>
                {recommendations.map((song, index) => (
                    <li key={index}>
                        <strong>{song.name}</strong> by {song.artist}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Playlist;

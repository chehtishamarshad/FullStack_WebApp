// src/components/HomePage.jsx

import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
    return (
        <div>
            <h1>Welcome to Stellar Company</h1>
            <p>Your partner in stellar achievements.</p>
            <div>
                <Link to="/signup">
                    <button>Sign Up</button>
                </Link>
                <Link to="/signin">
                    <button>Sign In</button>
                </Link>
            </div>
        </div>
    );
};

export default HomePage;

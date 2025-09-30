import React from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
    return (
        <div className="dashboard">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {/* Welcome Card */}
                <div className="card col-span-full">
                    <h2 className="text-xl font-semibold text-gray-800 mb-2">
                        Welcome to SkillBridge! 🚀
                    </h2>
                    <p className="text-gray-600 mb-4">
                        Discover skill gaps and bridge them with personalized learning recommendations.
                    </p>
                    <Link 
                        to="/upload" 
                        className="btn-primary inline-block"
                    >
                        Upload Resume
                    </Link>
                </div>

                {/* Quick Stats */}
                <div className="card">
                    <h3 className="text-lg font-medium text-gray-800 mb-2">Skills Analyzed</h3>
                    <p className="text-3xl font-bold text-blue-600">0</p>
                </div>

                <div className="card">
                    <h3 className="text-lg font-medium text-gray-800 mb-2">Skill Gaps Found</h3>
                    <p className="text-3xl font-bold text-orange-600">0</p>
                </div>

                <div className="card">
                    <h3 className="text-lg font-medium text-gray-800 mb-2">Recommendations</h3>
                    <p className="text-3xl font-bold text-green-600">0</p>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
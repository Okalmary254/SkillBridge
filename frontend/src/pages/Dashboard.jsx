import React from 'react';
import DashboardComponent from '../components/Dashboard';

const Dashboard = () => {
    return (
        <div className="min-h-screen bg-gray-50 p-6">
            <div className="max-w-7xl mx-auto">
                <h1 className="text-3xl font-bold text-gray-900 mb-8">Your Skill Dashboard</h1>
                <DashboardComponent />
            </div>
        </div>
    );
};

export default Dashboard;
import React from 'react';
import { Bar } from 'react-chartjs-2';

const SkillChart = ({ userSkills, marketSkills }) => {
    const missingSkills = marketSkills.filter(skill => !userSkills.includes(skill));

    const data = {
        labels: [...userSkills, ...missingSkills],
        datasets: [
            {
                label: 'Skills',
                data: [...userSkills.map(skill => 1), ...missingSkills.map(() => 0)],
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
            },
        ],
    };

    const options = {
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    stepSize: 1,
                },
            },
        },
    };

    return (
        <div>
            <h2>Skill Chart</h2>
            <Bar data={data} options={options} />
        </div>
    );
};

export default SkillChart;
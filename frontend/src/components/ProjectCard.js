import React from 'react';
import '../App.css';

const ProjectCard = ({ project }) => {
  return (
    <div className="project-card">
      <h3>{project.title}</h3>
      <p className="project-description">{project.description}</p>
      <p><strong>Technologies:</strong> {project.technologies || 'N/A'}</p>
      <a href={project.github_url || '#'} target="_blank" rel="noopener noreferrer">
        Voir sur GitHub
      </a>
      {project.image_url && <img src={project.image_url} alt={project.title} />}
    </div>
  );
};

export default ProjectCard;
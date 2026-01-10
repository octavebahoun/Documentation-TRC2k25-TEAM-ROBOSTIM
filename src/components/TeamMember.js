import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';

// Composant réutilisable et RESPONSIVE pour les membres d'équipe
const TeamMember = ({ name, role, specialty, description, image, color }) => (
    <div className="team-member-card">
        <div className="team-member-image-container">
            <img
                src={useBaseUrl(image)}
                alt={name}
                className="team-member-image"
                style={{ borderColor: `var(--color-${color})` }}
                loading="lazy"
                decoding="async"
            />
        </div>
        <div className="team-member-content">
            <div className="team-member-header">
                <h3 className="team-member-name">
                    {name}
                </h3>
                <span
                    className="team-member-badge"
                    style={{ background: `var(--color-${color})` }}
                >
                    {color === 'electronique' ? '🔌' : color === 'it' ? '💻' : '⚙️'} {color === 'electronique' ? 'Électronique' : color === 'it' ? 'IT' : 'Mécanique'}
                </span>
            </div>
            <p className="team-member-role">
                <strong>Rôle :</strong> {role} | <strong>Spécialité :</strong> {specialty}
            </p>
            <p className="team-member-description">
                {description}
            </p>
        </div>
    </div>
);

export default TeamMember;

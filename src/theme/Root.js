
import React, { useEffect } from 'react';
import { useLocation } from '@docusaurus/router';

function ScrollToTop() {
    const { pathname } = useLocation();

    useEffect(() => {
        window.scrollTo(0, 0);
    }, [pathname]);

    return null;
}

export default function Root({ children }) {
    return (
        <>
            <ScrollToTop />
            {children}
        </>
    );
}

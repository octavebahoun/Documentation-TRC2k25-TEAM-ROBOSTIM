import React from 'react';
// Import the original mapper
import MDXComponents from '@theme-original/MDXComponents';
import InfoCard from '@site/src/components/InfoCard';
import FeatureGrid from '@site/src/components/FeatureGrid';
import Table from '@site/src/components/Table';
import StepCard from '@site/src/components/StepCard';
import CodeBlock from '@site/src/components/CodeBlock';

export default {
    // Re-use the default mapping
    ...MDXComponents,
    // Map the "<Highlight>" tag to our Highlight component
    // `Highlight` will receive all props that were passed to `<Highlight>` in MDX
    InfoCard,
    FeatureGrid,
    Table,
    StepCard,
    CodeBlock,
};

// sidebars.js

module.exports = {
  // Cette "defaultSidebar" s'appelle ainsi car c'est son "id" que nous avons utilisé dans la config ('defaultSidebar')
  defaultSidebar: [
    {
      type: 'category',
      label: 'Tests',
      items: [
        {
          type: 'doc',
          id: 'introduction',
          label: 'Introduction',
        },
        {
          type: 'category',
          label: 'Electronic Pole',
          items: [
            'Electronics/electronics-overview',
            'Electronics/electronics-test1',
            'Electronics/electronics-test2',
            'Electronics/electronics-test3',
          ],
        },
        {
          type: 'category',
          label: 'Mechanical Pole',
          items: [
            'Mechanics/mechanics-overview',
            {
              type: 'category',
              label: 'Test 1 - Conception CAO',
              items: [
                'Mechanics/mechanics-test1',
                'Mechanics/Test1_Pieces/piece1',
                'Mechanics/Test1_Pieces/piece2',
                'Mechanics/Test1_Pieces/piece3',
                'Mechanics/Test1_Pieces/piece4',
              ],
            },
            'Mechanics/mechanics-test2',
            'Mechanics/mechanics-test3',
          ],
        },
        {
          type: 'category',
          label: 'ROS Pole',
          items: [
            'ROS/ros-overview',
            'ROS/ros-test1',
            'ROS/ros-test2',
            'ROS/ros-test3',
          ],
        },
        {
          type: 'category',
          label: 'AI Pole',
          items: [
            'IA/ia-overview',
            'IA/ia-test1',
            'IA/ia-test2',
            'IA/ia-test3',
          ],
        },
      ],
    },

  ],
};
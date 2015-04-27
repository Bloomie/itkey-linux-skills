Sisyphus API Overview
===============================

Sisyphus is a tool that helps OpenStack operators and administrators to automate their work:

1. **Note**

    - ``Sisyphus is an addon feature to OpenStack``
    - ``Sisyphus allows to create condition - action rules to automate administrative work``
    - ``Sisyphus allows either to use precreated conditions and actions or to create your own``


2. **Concepts**

To use the Sisyphus API effectively, you must understand several key concepts:

    - **Action**
        Set of commands that perfomed with respect to node(s)
    - **Check-up**
        set of executable instructions representing node(s)' state
    - **Condition**
        One or more check-ups that can be assigned to node(s)

Sisyphus manages check-ups and actions on your nodes with restrictions from configuration files;
so, basically, all you have to do is to sort out your configuration

***************************************
Methods
***************************************

- **GET**

    **method provides you with a few urls to monitor current configuration state,
    more features coming soon!**

    */services/<node>/checklist*

        ``returns check-up list for specified node``

    */services/<node>/actionlist*

        ``returns action list for specified node``

    */services/<node>/conditions*

        ``return condition list: set of check-up states calling actions``

    */services/<node>/mapping*

        ``returns mapping between check-ups and actions``

- **POST**

    **posting data is expected in yaml format, more could be found at ..**



    
    
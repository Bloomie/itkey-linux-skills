API Specifications
===============================

Sisyphus manages check-ups and actions on your nodes with restrictions from configuration files;
so, basically, all you have to do is to sort out your configuration

***************************************
Methods
***************************************

- **GET**

    **method provides you with a few urls to monitor current configuration state,
    more features coming soon!**

    */<node>/checklist*

        ``returns check-up list for specified node``

    *<node>/actionlist*

        ``returns action list for specified node``

    *<node>/mapping*

        ``returns mapping between check-ups and actions``

- POST

    **posting data is expected in yaml format, more could be found at ..**


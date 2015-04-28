================================
Sisyphus custom configurations
================================

Basically, all your custom configurations divided to **check-ups**, **actions** and **conditions**

To configure them, send file requests to Sisyphus API; format's described below

Format walkthrough
""""""""""""""""""

File is to be written in recognisable yaml format

Node: <testnode>
    Operation:
        Add:
            Check-ups:
                -<check-up name1>:
                    group: <check-up group name1>
                    check-up: <test command1>
                -<check-up name2>:
                    group: <check-up group name2>
                    check-up: <test command2>

                ...

                -<check-up nameN>:
                    group: <check-up group nameN>
                    check-up: <test commandN>

             Actions:
                 -<action name1>:
                     group: <action group name1>
                     action: <test command1>

                 ...

                 -<action nameN>:
                     group: <action group nameN>
                     action: <test commandN>

             Conditions:
                 -<condition name1>:
                     failed_check_group: <check-up group name1>
                     action_group: <action group name1>

                 ...

                 -<condition nameN>:
                     failed_check_group: <check-up group nameN>
                     action_group: <action group nameN>

        Remove:
            Check-ups:
                -<check-up name1>

                ...

                -<check-up nameN>

            Actions:
                -<action name1>

                ...

                -<action nameN>

            Conditions:
                -<condition name1>

                ...

                -<condition nameN>

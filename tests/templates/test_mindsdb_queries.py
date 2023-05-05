from string import Template


def test_template_values():
    user = "Benyamin Mahmoudyan"
    ask = "What is the weather like today?"

    sql_ask_query = Template('''
    SELECT response
    FROM mindsdb.gpt_model
    WHERE author_username = "$user"
    AND text = "$ask";
    ''')

    expected_output = '''
    SELECT response
    FROM mindsdb.gpt_model
    WHERE author_username = "Benyamin Mahmoudyan"
    AND text = "What is the weather like today?";
    '''

    assert sql_ask_query.substitute(user=user, ask=ask) == expected_output

from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")


def generate_sql(question: str) -> str:
    schema = """
    Table: employees
    Columns:
        id INTEGER
        name TEXT
        department TEXT
        salary FLOAT
        hire_date DATE
    """

    prompt = f"""
    Convert the following natural language question into SQL.

    Database Schema:
    {schema}

    Question:
    {question}

    Return only SQL.
    """

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text.strip()


def main():
    question = "Show all employees in the Engineering department"

    sql = generate_sql(question)

    print("Question:", question)
    print("SQL:", sql)


if __name__ == "__main__":
    main()
    
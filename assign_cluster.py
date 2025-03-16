import os
import gsheet_connector


def get_papers_name(path):
    papers = []
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            papers.append(file)
    return papers


def assign_paper_to_person(
    sheet: gsheet_connector.Sheet, topic: str, papers: list[str], person: str
):
    sheet.set_worksheet_id(person)
    row_index = sheet.get_last_row_index() + 1
    sheet.insert_paper_vertical(row_index, 1, papers)
    topic_list = [topic] * len(papers)
    sheet.insert_paper_vertical(row_index, 2, topic_list)


def assign_paper_to_people(
    sheet: gsheet_connector.Sheet, topic: str, papers: list[str], people: list[str]
):
    for person in people:
        assign_paper_to_person(sheet, topic, papers, person)


if __name__ == "__main__":
    sheet_name = "LLM Group Paper Assignment"
    path = "/Users/armin/Desktop/HEC/Research/Data Analytics Group/LLM fairness"
    topic = path.split("/")[-1]
    people = ["Armin"]

    sheet = gsheet_connector.Sheet(sheet_name)
    papers = get_papers_name(path)
    assign_paper_to_people(sheet, topic, papers, people)

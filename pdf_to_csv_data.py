import pdfplumber
import re


# read ids in one pdf file
def get_id_list(year: str, chapter: str):
    pdf_location = 'pdf_folder/{year}{chapter}.pdf'.format(year=year, chapter=chapter)
    pdf = pdfplumber.open(pdf_location)
    page_count = len(pdf.pages)

    sum_id_list = []
    for i in range(0, page_count):
        page = pdf.pages[i]
        text = page.extract_text()
        if text is None:  # whole page empty than skip
            continue
        lines = text.split("\n")
        id_8_list = [None for i in lines]
        id_2_list = [None for i in lines]
        # 1. use regular expression to find 8 digit id,2 digit id and position, then record into array list
        for line_index in range(len(lines)):
            line = lines[line_index]
            id_data1 = re.match(r'\s*(\d{4}\.\d{2}\.\d{2})\s+(\d{2})\s+', line)  # match 0110.10.10 00
            tmp_id_8 = None
            tmp_id_2 = None
            if id_data1 is not None:
                tmp_id_8 = id_data1.group(1)
                tmp_id_2 = id_data1.group(2)
            else:
                id_data2 = re.match(r'\s*(\d{4}\.\d{2}\.\d{2})\s+', line)  # match 0110.10.10 use \s+ to avoid "3904.69.50) ......"
                if id_data2 is not None:
                    tmp_id_8 = id_data2.group(1)
                else:
                    id_data3 = re.match(r'\s*(\d\d)\s+', line)  # match 00
                    if id_data3 is not None:
                        tmp_id_2 = id_data3.group(1)
            if tmp_id_8 is not None:
                tmp_id_8 = tmp_id_8.replace(".", "")
                if int(tmp_id_8[0:2]) != int(chapter[0:2]):  # avoid "25%\nSee 9906.87.01- \n9906.87.02 (MX)"
                    tmp_id_8 = None
            id_8_list[line_index] = tmp_id_8
            id_2_list[line_index] = tmp_id_2
        # 2. splice id in the array list
        id_list = []
        tem_id_8 = None
        for line_index in range(len(lines)):
            if id_8_list[line_index] is not None:
                tem_id_8 = id_8_list[line_index]
            if id_2_list[line_index] is not None:
                if tem_id_8 is not None:
                    tem_id_2 = id_2_list[line_index]
                    id_list.append(tem_id_8 + tem_id_2)
        sum_id_list = sum_id_list + id_list
    return sum_id_list


def main():
    result = open("1994_2009_two_line.csv", 'w', encoding='utf-8')
    result.write("year,hs_10\n")
    for i in range(1994, 2010):  # year
        print(i)  # print in cmd line so that you can trace schedule of the program
        chapter_list = [i for i in range(1, 99)]
        chapter_list_plus = []
        if i < 2000:
            chapter_list_plus = [i for i in range(991, 998)]  # year95-99 have 991-995
            if i == 1994:
                chapter_list_plus = [i for i in range(991, 996)]  # year94 have 991-995
            year = str(i % 100)
        else:
            chapter_list_plus = [99]
            year = "0" + str(i % 100)
        chapter_list = chapter_list + chapter_list_plus
        sum_id_list_of_a_year = [str(i)]  # year
        for j in chapter_list:  # chapter
            if j == 77:
                continue
            if i == 2009 and j == 63:  # there is not this pdf
                continue
            if j < 10:
                chapter = "0" + str(j)
            else:
                chapter = str(j)
            sum_id_list_of_a_chapter = get_id_list(year, chapter)
            for id_in_year in sum_id_list_of_a_chapter:
                result.write(str(i) + "," + id_in_year + "\n")
            print("    "+chapter)  # print in cmd line so that you can trace schedule of the program
    result.close()


if __name__ == '__main__':
    main()

import wget
import os


def create_folder(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print("---  new folder...  ---")
    else:
        print("---  There is this folder!  ---")


def main():
    url_format_before_2005 = "https://www.usitc.gov/tata/hts/archive/{year}00/{year}{is_over_2020}0c{chapter}.pdf"
    url_format_after_2005 = "https://www.usitc.gov/publications/docs/tata/hts/bychapter/{year}{is_over_2020}0c{chapter}.pdf"
    # sample url format:
    # https://www.usitc.gov/tata/hts/archive/9600/960c14.pdf
    # https://www.usitc.gov/tata/hts/archive/0000/000c01.pdf
    # https://www.usitc.gov/tata/hts/archive/0100/0100c01.pdf
    # https://www.usitc.gov/publications/docs/tata/hts/bychapter/0500c01.pdf
    # https://www.usitc.gov/tata/hts/archive/9400/940c991.pdf
    # https://www.usitc.gov/tata/hts/archive/0100/0100c99.pdf
    pdf_folder = "pdf_folder"
    pdf_folder_path = os.path.join(os.getcwd(), pdf_folder)
    create_folder(pdf_folder_path)
    for i in range(1994, 2010):  # year
        is_over_2020 = ""
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
            if i > 2000:
                is_over_2020 = "0"
        chapter_list = chapter_list + chapter_list_plus
        for j in chapter_list:  # chapter
            if j == 77:
                continue
            if i == 2009 and j == 63:  # there is not this pdf
                continue
            if j < 10:
                chapter = "0" + str(j)
            else:
                chapter = str(j)
            if i < 2005:
                url = url_format_before_2005.format(year=year, is_over_2020=is_over_2020, chapter=chapter)
            else:
                url = url_format_after_2005.format(year=year, is_over_2020=is_over_2020, chapter=chapter)
            print(url)
            pdf_name = "{year}{chapter}.pdf".format(year=year, chapter=chapter)
            file_path = os.path.join(os.getcwd(), pdf_folder, pdf_name)
            wget.download(url, file_path)


if __name__ == '__main__':
    main()

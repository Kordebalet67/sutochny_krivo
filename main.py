from parser_class import sutochno_parser

def main():
    parser = sutochno_parser()
    parser.accept_cookies()
    while True:
        parser.get_links_on_the_page()
        if not parser.go_to_the_next_page():
            break

    print(parser.links_list)
if __name__ == "__main__":
    main()
import argparse

if __name__ == "__main__":
    print('corp analysis for help')
    corp_num = int
    parser = argparse.ArgumentParser(description='show corp info for help of invest')
    parser.add_argument('-n', '--number', help='input the number you want to see')

    args = parser.parse_args()
    corp_num = args.number
    print(f'corp num : {corp_num}')
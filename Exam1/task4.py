import argparse

def main():
    parser = argparse.ArgumentParser(description='Processing num and strings with extra options.')
    parser.add_argument('number', type=int, help='Number to output')
    parser.add_argument('text', type=str, help='Strings to output')
    parser.add_argument('--verbose', action='store_true', help='Extra info output')
    parser.add_argument('--repeat', type=int, default=1, help='Count repeated strings')
    args = parser.parse_args()

    if args.verbose:
        print(f'Received arguments: number={args.number}, text="{args.text}", repeat={args.repeat}')
    
    print(f'Num: {args.number}, Str: {args.text * args.repeat}')

if __name__ == '__main__':
    main()

    # Для зауска: python task4.py 42 "Hello" --verbose --repeat 3
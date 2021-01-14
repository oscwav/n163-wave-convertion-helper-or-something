def main():
    try:
        refresh_rate = int(input("Refresh rate (hz): "))
    except:
        print("Error: Not an integer\n")
        main()
    try:
        sample_rate = int(input("Sample rate (hz): "))
    except:
        print("Error: Not an integer\n")
        main()
    try:
        sample_length = int(input("Total length (samples): "))
    except:
        print("Error: Not an integer\n")
        main()
    frame = int(round(sample_rate / refresh_rate))
    x = 0
    for i in range(0, sample_length, frame):
        print(str(x) + ": " + str(i))
        x += 1

if __name__ == "__main__":
    main()
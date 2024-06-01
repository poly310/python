def calculate_results(marks):
    total=sum(marks)
    average=total/len(marks)
    percentage=(total/(len(marks)*100))*100
    return total,average,percentage
    def main():
        print("marks calculation program")
        marks[1000]
        for i in range(5):
            mark=float(input(f"enter marks for subject {i+1}:"))
            marks.append(mark)
            total,average,percentage=calculate_results(marks)
            print(f"total marks:{total}")
            print(f"avarage marks{avarage}")
            print(f"percentage marks{percentge}%")

import numpy as np

def generate_prime():
    num = 0
    while True:
        num = int(np.random.rand()*np.random.randint(10, 100)) + 6 # +4 -> num//2
        # print(num)
        no = 0
        for i in range(2, num//2+2):
            if num % i == 0:
                no = 1
                break
        if no == 0:
            break
    return num

def main():
    
    m = [generate_prime() for i in range(9) ]
    m = np.array(m).reshape(3,3)

    print(m)

    


if __name__=="__main__":
    main()
    # print('generate_prime()', generate_prime())
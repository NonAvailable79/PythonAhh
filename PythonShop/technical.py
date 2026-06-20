import time
class Technical:
    def loop_check(self, index=100, mul_to_continue=10, mul_to_pass=5, inner_break=(67,0), index_to_break=100):
        for i in range(index):
            if i % mul_to_continue == 0:
                print('\nSkipping')
                continue
            if i % mul_to_pass == 0:
                print('\nNot doing anything special')
                pass
            if i == index_to_break:
                print('\nBreaking out')
                break
            else:
                print('\nLooping at' , i)
                for j in range(5):
                    if i == inner_break[0] and j == inner_break[1]:
                        print('\nBreaking out of j-ail\n')
                        break

                    print('j is' , j, end='... ')
                    time.sleep(0.05)
        print("Done")

if __name__ == "__main__":
    q = Technical()
    q.loop_check()
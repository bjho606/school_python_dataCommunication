import matplotlib.pyplot as plt
import numpy as np

m_attrs = {
    'color': 'blue',
    'lw': 5,
}

dm_attrs = {
    'color': 'red',
    'lw': 5,
}

def manchester(code):
    plt.subplot(2, 1, 1)
    plt.ylim(-1.25, 2)
    plt.yticks([-1, 0, 1])
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.grid()

    plt.title ('Manchester')
    plt.xlim(0, len(code))
    prev = "0"
    for i, bit in enumerate(code):
        plt.text(i + 0.4, 1.5, bit, fontsize=20)

        if bit == "1":
            if bit == prev:
                plt.plot([i, i], [1, -1], **m_attrs)
            prev = "1"
            plt.plot([i, i + 0.5, i + 0.5, i + 1], [-1, -1, 1, 1], **m_attrs)
        else:
            if bit == prev:
                plt.plot([i, i], [-1, 1], **m_attrs)
            prev = "0"
            plt.plot([i, i + 0.5, i + 0.5, i + 1], [1, 1, -1, -1], **m_attrs)

def differential_manchester(code):
    plt.subplot(2, 1, 2)
    plt.ylim(-1.25, 2)
    plt.yticks([-1, 0, 1])
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.grid()

    plt.title ('Differential Manchester')
    plt.xlim(0, len(code))
    switch = False
    for i, bit in enumerate(code):
        plt.text(i + 0.4, 1.5, bit, fontsize=20)

        if bit == "1":
            switch = not switch

        if switch:
            if bit == "0":
                plt.plot([i, i], [-1, 1], **dm_attrs)
            plt.plot([i, i + 0.5, i + 0.5, i + 1], [-1, -1, 1, 1], **dm_attrs)

        else:
            if bit == "0":
                plt.plot([i, i], [1, -1], **dm_attrs)
            plt.plot([i, i + 0.5, i + 0.5, i + 1], [1, 1, -1, -1], **dm_attrs)

if __name__ == '__main__':    
    code = input('Insert Code (Zeros and Ones) > ')

    manchester(code)
    differential_manchester(code)

    plt.tight_layout()
    plt.show()
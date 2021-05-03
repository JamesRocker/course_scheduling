import matplotlib.pyplot as plt

fold_name = 'graphs/'
extension = '.png'

def plot_graph(x_lst, y_lst, title, x_label, y_label, filename):
    plt.scatter(x_lst, y_lst)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # plt.show()

    path = fold_name + filename + extension
    plt.savefig(path)



    
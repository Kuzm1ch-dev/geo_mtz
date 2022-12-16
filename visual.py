import numpy as np
import matplotlib.pyplot as plt


def visual_data(data_analysed, gs_kw):
    fig, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)

    ax.set_yscale("linear")
    ax.set_xticks(data_analysed.position_y)
    ax.set_yticks(data_analysed.position_z)
    ax.set_xticklabels(data_analysed.list_x)
    ax.set_yticklabels(data_analysed.list_y)
    ax.set_xlabel("Расстояние по горизонтали, км")
    ax.set_ylabel("Расстояние по вертикали, км")
    ax.set_xlim([0, data_analysed.position_y[-1]])
    ax.set_ylim([data_analysed.position_z[-1], 0])
    ax.grid()

    p = ax.imshow(data_analysed.rho, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
    fig.colorbar(p, cax=cax)
    cax.set_ylabel(r"Сопротивление, $\rho$ [$Ом \times м$]", rotation=90)
    fig.canvas.manager.set_window_title("Визуализация данных")
    fig.canvas.show()


def curve_rho(data_analysed, gs_kw):
    
    fig, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)

    cax.clear()
    ax.plot([i+1 for i in range(len(data_analysed.row_solutions))], data_analysed.row_solutions)

    ax.set_yscale('log')
    ax.set_xticks([i+1 for i in range(len(data_analysed.row_solutions))])
    ax.set_xticklabels([i+1 for i in range(len(data_analysed.row_solutions))])
    ax.set_xlim([1, len(data_analysed.row_solutions)])
    ax.set_xlabel("Номер пикета")
    ax.set_ylabel(r"Кажущееся сопротивление, $lg(\rho_{T})$")

    legend_marks = [data_analysed.t1 * 2**(i+1) for i in range(len(data_analysed.row_solutions[0]))]
    ax.legend(legend_marks, title=r"Периоды, $T [с]$")

    fig.canvas.manager.set_window_title("Визуализировать кривые rho кажущегося")
    fig.canvas.draw()

def rho_map(data_analysed, gs_kw):
    fig, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)

    ax.set_xticks(data_analysed.position_y)
    ax.set_xticklabels(data_analysed.list_x)
    ax.set_xlim([0, data_analysed.position_y[-1]])
    ax.set_xlabel("Расстояние по горизонтали, км")

    periods = [data_analysed.t1 * 2**(i+1) for i in range(len(data_analysed.row_solutions[0]))]

    ax.set_yticks([i for i in range(len(periods))])
    ax.set_yticklabels(periods)
    ax.set_ylabel(r"Периоды, $T [с]$")

    temp_mas = np.log10(np.array(data_analysed.row_solutions).transpose())
    p2 = ax.imshow(temp_mas, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
    fig.colorbar(p2, cax=cax)
    cax.set_ylabel(r"Кажущееся сопротивление, $lg(\rho_{T})$", rotation=90)
    fig.canvas.manager.set_window_title("Визуализировать карту rho кажущегося")
    fig.canvas.draw()

def curve_phi(data_analysed, gs_kw):
    fig, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)
    cax.clear()
    ax.plot([i+1 for i in range(len(data_analysed.phi_solutions))], data_analysed.phi_solutions)

    ax.set_xticks([i+1 for i in range(len(data_analysed.phi_solutions))])
    ax.set_xticklabels([i+1 for i in range(len(data_analysed.phi_solutions))])
    ax.set_xlim([1, len(data_analysed.phi_solutions)])
    ax.set_xlabel("Номер пикета")
    ax.set_ylabel(r"Фаза импеданса, $\phi$")

    legend_marks = [data_analysed.t1 * 2**(i+1) for i in range(len(data_analysed.phi_solutions[0]))]
    ax.legend(legend_marks, title=r"Периоды, $T [с]$")
    fig.canvas.manager.set_window_title("Визуализировать кривые phi")
    fig.canvas.draw()

def phi_map(data_analysed, gs_kw):
    fig, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)

    ax.set_xticks(data_analysed.position_y)
    ax.set_xticklabels(data_analysed.list_x)
    ax.set_xlim([0, data_analysed.position_y[-1]])
    ax.set_xlabel("Расстояние по горизонтали, км")

    periods = [data_analysed.t1 * 2**(i+1) for i in range(len(data_analysed.phi_solutions[0]))]

    ax.set_yticks([i for i in range(len(periods))])
    ax.set_yticklabels(periods)
    ax.set_ylabel(r"Периоды, $T [с]$")

    temp_mas = np.array(data_analysed.phi_solutions).transpose()
    p2 = ax.imshow(temp_mas, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
    fig.colorbar(p2, cax=cax)
    cax.set_ylabel(r"Фаза импеданса, $\phi$", rotation=90)
    fig.canvas.manager.set_window_title("Визуализировать карту phi")
    fig.canvas.draw()
import matplotlib.pyplot as plt
import numpy as np
import locale
import pandas as pd

from sympy import rf 
import seaborn as sns
import pandas as pd

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif", # Fontes serifadas combinam melhor com LaTeX (Computer Modern)
    "text.latex.preamble": r"\usepackage{icomma}\usepackage{amsmath}"
})

def plot_volume_vs_time(time, volume, label=None, save=None, save_csv=None, ylim=None, show=False):
    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.size'] = 20
    plt.rc('text.latex', preamble=r'\usepackage{icomma}')
    avg_vol = np.mean(volume)
    # plt.figure(figsize=(9,5))

    sc = plt.scatter(time, volume, s=20, marker='^', label=label)
    color = sc.get_facecolors()[0]

    plt.axhline(
        avg_vol,
        linestyle='--',
        color=color,
        label=rf"$\langle V \rangle$ = {avg_vol:.2f} Å$^3$"
    )

    
    plt.axhline(
        695.0,
        linestyle='-',
        color='red',
        label=rf"$ V_{{exp}} $ = 695.00 Å$^3$"
    )

    plt.xlabel("Tempo (ps)")
    plt.ylabel(r"Volume ($\mathrm{\AA}^3$)")
    plt.legend()
    locale.setlocale(locale.LC_NUMERIC, 'pt_PT.utf8')
    if ylim:
        plt.ylim(ylim)
    plt.tight_layout()
    if show:
        plt.show()
        # --- Salvamento de Dados (CSV) ---
    if save_csv:
        df = pd.DataFrame({
            'tempo_ps': time,
            'volume': volume
        })
        # index=False evita que o pandas salve uma coluna extra de números
        df.to_csv(save_csv, index=False)
        print(f"Dados salvos com sucesso em: {save_csv}")
    if save:
        plt.savefig(save, dpi=600)
    
    plt.close()




def plot_lattice_lengths(time, a, b, c, save=None, save_csv=None, ylim=None, show=False):
    # plt.figure(figsize=(9,5))
    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.size'] = 20
    plt.rc('text.latex', preamble=r'\usepackage{icomma}')
    plt.plot(time, a, label='a')
    plt.plot(time, b, label='b')
    plt.plot(time, c, label='c')
    plt.xlabel("Tempo (ps)")
    plt.ylabel(r"Comprimento ($\mathrm{\AA}$)")
    plt.legend()
    locale.setlocale(locale.LC_NUMERIC, 'pt_PT.utf8')
    plt.grid(alpha=0.3)

    if ylim:
        plt.ylim(ylim)

    plt.tight_layout()

    # --- Salvamento de Dados (CSV) ---
    if save_csv:
        df = pd.DataFrame({
            'tempo_ps': time,
            'a_angstrom': a,
            'b_angstrom': b,
            'c_angstrom': c
        })
        # index=False evita que o pandas salve uma coluna extra de números
        df.to_csv(save_csv, index=False)
        print(f"Dados salvos com sucesso em: {save_csv}")

    if save:
        plt.savefig(save, dpi=600)
    
    if show:
        plt.show()
    
    plt.close()

def plot_cell_angles(time, alpha, beta, gamma, save=None, save_csv=None,ylim=None, show=False):
    # plt.figure(figsize=(9,5))
    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.size'] = 20
    plt.rc('text.latex', preamble=r'\usepackage{icomma}')
    textsize=20
    plt.plot(time, alpha, label=r'$\alpha$')
    plt.plot(time, beta,  label=r'$\beta$')
    plt.plot(time, gamma, label=r'$\gamma$')
    plt.xlabel("Tempo (ps)", fontsize=textsize)
    plt.ylabel("Ângulo (°)", fontsize=textsize)
    plt.legend(fontsize=textsize)
    locale.setlocale(locale.LC_NUMERIC, 'pt_PT.utf8')
    plt.xticks(fontsize=textsize)
    plt.yticks(fontsize=textsize)
    plt.grid(alpha=0.3)
    if ylim:
        plt.ylim(ylim)

    plt.tight_layout()
    
    if show:
        plt.show()

    if save:
        plt.savefig(save, dpi=600)

        # --- Salvamento de Dados (CSV) ---
    if save_csv:
        df = pd.DataFrame({
            'tempo_ps': time,
            'alpha': alpha,
            'beta': beta,
            'gamma': gamma
        })
        # index=False evita que o pandas salve uma coluna extra de números
        df.to_csv(save_csv, index=False)
        print(f"Dados salvos com sucesso em: {save_csv}")

    plt.close()


def plot_split_violin(df, x_col='Temperatura', y_col='Volume', hue_col=None, save_path=None, ylabel=None):
    """
    Gera um violin plot dividido por fase.
    df: DataFrame contendo colunas para Temperatura, Volume e Fase.
    """
    plt.figure(figsize=(10, 6))
    
    # O segredo do 'split' está aqui
    sns.violinplot(
        data=df, 
        x=x_col, 
        y=y_col, 
        hue=hue_col, 
        split=True, 
        inner="quart", 
        palette="muted"
    )
    
    # plt.title(f"Distribuição de {y_col} por Temperatura e {hue_col}")
    plt.xlabel("Temperatura (K)")
    plt.ylabel(ylabel if ylabel else r"Volume ($\mathrm{\AA}^3$)")
    plt.grid(axis='y', alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
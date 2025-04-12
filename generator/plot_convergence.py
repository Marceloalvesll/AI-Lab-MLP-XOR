import matplotlib.pyplot as plt

# --------------------------
# Dados dos Experimentes
# --------------------------

# Experimento 1 (Parâmetros do professor: hidden_sizes=[2], learning_rate=0.1, epochs=1000)
# Aqui, apenas o erro da época 0 foi registrado em cada execução.
exp1_epochs = [0]
exp1_run1 = [0.2539035186489542]
exp1_run2 = [0.25344859516687934]
exp1_run3 = [0.2640033244602219]

# Experimento 2 (hidden_sizes=[4], learning_rate=0.01, epochs=5000)
exp2_epochs = [0, 1000, 2000, 3000, 4000]
exp2_run1 = [0.2831868193821763, 0.25065941520982554, 0.2503003183922761, 0.25018813349625846, 0.2500996319235922]
exp2_run2 = [0.25687068601036084, 0.25015194788893014, 0.24979992706867152, 0.2495020684986438, 0.249205442289487]
exp2_run3 = [0.2972938911835538, 0.25109470543479856, 0.2505685956762832, 0.2504950172746719, 0.2504308074188366]

# Experimento 3 (hidden_sizes=[4], learning_rate=0.5, epochs=10000)
exp3_epochs = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
exp3_run1 = [0.2543142041211701, 0.02774183667010717, 0.006113422191759367, 0.003260850273067544, 0.0021675186619372474,
             0.0015938068337395016, 0.0012417810011287518, 0.0010046169795762385, 0.0008348720522217792, 0.0007083077549892332]
exp3_run2 = [0.25697818682798945, 0.24604372527096707, 0.024413021632305274, 0.006522928566461908, 0.0035774377755681194,
             0.0024244120162198813, 0.0018179516380527902, 0.0014463220563434008, 0.0011962049203322934, 0.001016836652258257]
exp3_run3 = [0.2643339853102404, 0.06689469251025204, 0.005899798739499338, 0.0028235714560764054, 0.0018279753770743684,
             0.001343594783911046, 0.0010590197129910221, 0.0008724133771933997, 0.0007408925248017206, 0.0006433385079088594]

# Experimento 4 (hidden_sizes=[4], learning_rate=0.5, epochs=5000)  
# Note que alguns runs possuem número diferente de pontos, conforme os registros:
exp4_epochs_run1 = [0, 1000, 2000, 4000]
exp4_run1 = [0.259252150036391, 0.2492056539206032, 0.09534642029560471, 0.06543562677242097]
exp4_epochs_run2 = [0, 1000, 2000, 3000, 4000]
exp4_run2 = [0.25326587519081833, 0.22555666542009872, 0.01897885994678602, 0.004862717840364091, 0.0027021760139768662]
exp4_epochs_run3 = [0, 1000, 2000, 3000, 4000]
exp4_run3 = [0.24972112749540734, 0.0404633217459341, 0.006403624615976479, 0.003205876786330423, 0.002101107094099898]

# Experimento 5 (hidden_sizes=[2], learning_rate=0.05, epochs=5000)
exp5_epochs = [0, 1000, 2000, 3000, 4000]
exp5_run1 = [0.2747862222725476, 0.24999164442903843, 0.24999078115783646, 0.24999010591826565, 0.2499895819331614]
exp5_run2 = [0.25114774389806377, 0.24968110536173038, 0.2485277096989017, 0.24581811275433263, 0.23838861794776228]
exp5_run3 = [0.26045716121754814, 0.24993598046210364, 0.2498298949222634, 0.249638340580769, 0.24916468619080195]

# Experimento 6 (hidden_sizes=[6], learning_rate=0.1, epochs=5000)
exp6_epochs = [0, 1000, 2000, 3000, 4000]
exp6_run1 = [0.252503658379183, 0.24863524292467978, 0.2424462970095054, 0.18391949050119635, 0.08429023387100457]
exp6_run2 = [0.2538808147582962, 0.2473803737683014, 0.20990646842580482, 0.1453921932446114, 0.0736798343516888]
exp6_run3 = [0.27530763333611435, 0.2375672884341331, 0.1791784353449592, 0.12319485240267004, 0.0692437688354062]

# --------------------------
# Gerando Gráficos com subplots
# --------------------------
fig, axs = plt.subplots(2, 3, figsize=(18, 10))
axs = axs.flatten()

# Experimento 1
axs[0].plot(exp1_epochs, exp1_run1, marker='o', label="Run 1")
axs[0].plot(exp1_epochs, exp1_run2, marker='o', label="Run 2")
axs[0].plot(exp1_epochs, exp1_run3, marker='o', label="Run 3")
axs[0].set_title("Experiment 1 (Base)")
axs[0].set_xlabel("Epochs")
axs[0].set_ylabel("Error")
axs[0].legend()
axs[0].grid(True)

# Experimento 2
axs[1].plot(exp2_epochs, exp2_run1, marker='o', label="Run 1")
axs[1].plot(exp2_epochs, exp2_run2, marker='o', label="Run 2")
axs[1].plot(exp2_epochs, exp2_run3, marker='o', label="Run 3")
axs[1].set_title("Experiment 2 (hidden=[4], lr=0.01, epochs=5000)")
axs[1].set_xlabel("Epochs")
axs[1].set_ylabel("Error")
axs[1].legend()
axs[1].grid(True)

# Experimento 3
axs[2].plot(exp3_epochs, exp3_run1, marker='o', label="Run 1")
axs[2].plot(exp3_epochs, exp3_run2, marker='o', label="Run 2")
axs[2].plot(exp3_epochs, exp3_run3, marker='o', label="Run 3")
axs[2].set_title("Experiment 3 (hidden=[4], lr=0.5, epochs=10000)")
axs[2].set_xlabel("Epochs")
axs[2].set_ylabel("Error")
axs[2].legend()
axs[2].grid(True)

# Experimento 4
axs[3].plot(exp4_epochs_run1, exp4_run1, marker='o', label="Run 1")
axs[3].plot(exp4_epochs_run2, exp4_run2, marker='o', label="Run 2")
axs[3].plot(exp4_epochs_run3, exp4_run3, marker='o', label="Run 3")
axs[3].set_title("Experiment 4 (hidden=[4], lr=0.5, epochs=5000)")
axs[3].set_xlabel("Epochs")
axs[3].set_ylabel("Error")
axs[3].legend()
axs[3].grid(True)

# Experimento 5
axs[4].plot(exp5_epochs, exp5_run1, marker='o', label="Run 1")
axs[4].plot(exp5_epochs, exp5_run2, marker='o', label="Run 2")
axs[4].plot(exp5_epochs, exp5_run3, marker='o', label="Run 3")
axs[4].set_title("Experiment 5 (hidden=[2], lr=0.05, epochs=5000)")
axs[4].set_xlabel("Epochs")
axs[4].set_ylabel("Error")
axs[4].legend()
axs[4].grid(True)

# Experimento 6
axs[5].plot(exp6_epochs, exp6_run1, marker='o', label="Run 1")
axs[5].plot(exp6_epochs, exp6_run2, marker='o', label="Run 2")
axs[5].plot(exp6_epochs, exp6_run3, marker='o', label="Run 3")
axs[5].set_title("Experiment 6 (hidden=[6], lr=0.1, epochs=5000)")
axs[5].set_xlabel("Epochs")
axs[5].set_ylabel("Error")
axs[5].legend()
axs[5].grid(True)

plt.tight_layout()
plt.show()

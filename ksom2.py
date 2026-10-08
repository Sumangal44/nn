import numpy as np
import pandas as pd

# ============================================================
# KSOM
# 4 Inputs × 4 Features
# 2 Clusters
# Weight Matrix = 2 × 4
# ============================================================


# ------------------------------------------------------------
# 1. INPUT DATA
# ------------------------------------------------------------

X = np.array([
    [1, 0, 1, 0],   # 1010
    [1, 0, 0, 0],   # 1000
    [1, 1, 1, 1],   # 1111
    [0, 1, 1, 0]    # 0110
], dtype=float)


# ------------------------------------------------------------
# 2. INITIAL WEIGHTS
# ------------------------------------------------------------

W = np.array([
    [0.3, 0.5, 0.7, 0.2],   # Cluster 1
    [0.6, 0.5, 0.4, 0.2]    # Cluster 2
], dtype=float)
initial_weights = W.copy()


# ------------------------------------------------------------
# 3. PARAMETERS
# ------------------------------------------------------------

learning_rate = 0.3   # FIXED
epsilon = 0.0001
max_iterations = 100


# ------------------------------------------------------------
# 4. STORE RESULTS
# ------------------------------------------------------------

results = []


# ============================================================
# 5. KSOM TRAINING
# ============================================================

for iteration in range(1, max_iterations + 1):

    old_W = W.copy()

    # --------------------------------------------------------
    # Process all 4 input vectors
    # --------------------------------------------------------

    for input_no, x in enumerate(X, start=1):

        # --------------------------------------------
        # Euclidean distance
        # --------------------------------------------

        distance_1 = np.sqrt(
            np.sum((x - W[0]) ** 2)
        )

        distance_2 = np.sqrt(
            np.sum((x - W[1]) ** 2)
        )

        # --------------------------------------------
        # Find winner
        # --------------------------------------------

        if distance_1 < distance_2:
            winner = 0
        else:
            winner = 1

        # --------------------------------------------
        # Save old weight
        # --------------------------------------------

        old_weight = W[winner].copy()

        # --------------------------------------------
        # Update winning weight vector
        #
        # Wnew = Wold + α(X - Wold)
        # --------------------------------------------

        W[winner] = (
            W[winner]
            + learning_rate * (x - W[winner])
        )

        # --------------------------------------------
        # Weight change
        # --------------------------------------------

        change = np.max(
            np.abs(W[winner] - old_weight)
        )

        # --------------------------------------------
        # Save result
        # --------------------------------------------

        results.append({
            "Iteration": iteration,
            "Input": input_no,
            "Input_Vector": "".join(
                str(int(v)) for v in x
            ),

            "Distance_C1": distance_1,
            "Distance_C2": distance_2,

            "Winner": winner + 1,

            "Learning_Rate": learning_rate,

            "Old_W1": old_weight[0],
            "Old_W2": old_weight[1],
            "Old_W3": old_weight[2],
            "Old_W4": old_weight[3],

            "New_W1": W[winner][0],
            "New_W2": W[winner][1],
            "New_W3": W[winner][2],
            "New_W4": W[winner][3],

            "Weight_Change": change
        })


    # ========================================================
    # 6. STOPPING CONDITION
    # ========================================================

    weight_change = np.max(
        np.abs(W - old_W)
    )

    if weight_change < epsilon:
        break


# ============================================================
# 7. FINAL WEIGHTS
# ============================================================

final_weights = pd.DataFrame(
    W,
    index=["y1", "y2"],
    columns=["x1", "x2", "x3", "x4"]
)


# ============================================================
# 8. FINAL CLUSTER ASSIGNMENT
# ============================================================

clusters = []

for input_no, x in enumerate(X, start=1):

    distance_1 = np.sqrt(
        np.sum((x - W[0]) ** 2)
    )

    distance_2 = np.sqrt(
        np.sum((x - W[1]) ** 2)
    )

    if distance_1 < distance_2:
        cluster ="y1"
    else:
        cluster = "y2"

    clusters.append({
        "Input": input_no,
        "Vector": "".join(
            str(int(v)) for v in x
        ),
        "Distance_C1": distance_1,
        "Distance_C2": distance_2,
        "Cluster": cluster
    })


cluster_df = pd.DataFrame(clusters)


# ============================================================
# 9. SAVE TO EXCEL
# ============================================================

with pd.ExcelWriter(
    "KSOM3_Result.xlsx",
    engine="openpyxl"
) as writer:

    # Input data
    pd.DataFrame(
        X.astype(int),
        columns=["X1", "X2", "X3", "X4"]
    ).to_excel(
        writer,
        sheet_name="Input Data",
        index=False
    )

    # Iterations
    pd.DataFrame(
        results
    ).to_excel(
        writer,
        sheet_name="Iterations",
        index=False
    )

    # Final weights
    final_weights.to_excel(
        writer,
        sheet_name="Final Weights"
    )

    # Cluster result
    cluster_df.to_excel(
        writer,
        sheet_name="Clusters",
        index=False
    )


# ============================================================
# 10. FINAL OUTPUT
# ============================================================

print("Input Data:")
print(pd.DataFrame(
    X.astype(int),
    columns=["x1", "x2", "x3", "x4"]
).to_string(index=False))

print("\nInitial Weight Matrix:")
print(pd.DataFrame(
    initial_weights,
    index=["y1", "y2"],
    columns=["x1", "x2", "x3", "x4"]
))

print("\nLearning Rate:", learning_rate)
print("Epsilon:", epsilon)

print("\nFinal Weight Matrix:")
print(final_weights)

print("\nCluster Assignment:")
print(cluster_df)

print("\nIterations:", iteration)
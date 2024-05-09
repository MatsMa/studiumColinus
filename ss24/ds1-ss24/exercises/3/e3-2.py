import numpy as np

# a)
data = np.load("backup_data_2a.npy")
print(data)
print(data.mean())

rng = np.random.default_rng(101)

mean = np.array([0.0, 0.0])
cov = np.array([[1.0, 0.0], [0.0, 10.0]])
# cov = np.cov()

# samples = np.random.multivariate_normal(mean, cov, 2000)
samples = rng.multivariate_normal(mean, cov, 2000, check_valid="raise")

print(samples)
print(data == samples)
print(samples.T)


# b)
def get_rotation_matrix(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c, -s], [s, c]])


theta = np.radians(40)
r_matrix = get_rotation_matrix(theta)
# data_rotated = data @ r_matrix

r_matrix = get_rotation_matrix(theta)
samples_rotated = samples @ r_matrix

# c)
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].set_xlim(-15, 20)
axes[0].set_ylim(-10, 15)
axes[0].scatter(samples[:, 0], samples[:, 1], s=8, color="navy")
axes[0].scatter(
    samples_rotated[:, 0], samples_rotated[:, 1], s=8, color="darkorange"
)
mean_axs = axes[0].scatter(0, 0, marker="x", s=50, color="black", label="Mean")
axes[0].legend(handles=[mean])
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].set_title("Original and rotated point cloud")

axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
orig_data = axes[1].hist(samples[:, 0], bins=111, fc=(1, 0.5, 0, 0.5), zorder=0, label="Original data")
rot_data = axes[1].hist(samples_rotated[:, 0], bins=111, fc=(0.118, 0.25, 0.35, 0.5), zorder=1, label="Rotated data")
axes[1].set_ylabel("Count")
axes[1].set_title("Histogram of the x dimension")
axes[1].legend(handles=[orig_data, rot_data])

plt.tight_layout()
plt.show()

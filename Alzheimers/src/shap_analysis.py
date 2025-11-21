import shap
import matplotlib.pyplot as plt

def compute_shap(model, X_train):
    """
    Fits SHAP values using TreeExplainer.
    """

    explainer = shap.TreeExplainer(model)
    print("Computing SHAP values...")
    shap_values = explainer.shap_values(X_train)
    return explainer, shap_values

def plot_shap_summary(shap_values, X_train):
    """
    SHAP summary beeswarm plot.
    """
    shap.summary_plot(shap_values, X_train, show=False)
    plt.tight_layout()
    plt.show()

def plot_shap_bar(shap_values, X_train):
    """
    SHAP mean absolute value bar plot.
    """
    shap.summary_plot(shap_values, X_train, plot_type="bar", show=False)
    plt.tight_layout()
    plt.show()

def plot_dependence(feature, shap_values, X_train):
    """
    Generates a SHAP dependence plot for a given feature.
    """
    shap.dependence_plot(feature, shap_values, X_train, show=False)
    plt.show()

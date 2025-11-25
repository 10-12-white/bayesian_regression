using Plots
using CSV
using DataFrames
using Distributions
using LinearAlgebra
using Noise

# Define the polynomial function (editable by the user)
function polynomial(x, a, b, c)
    return a * x^2 + b * x + c
end
# User-defined polynomial coefficients
a, b, c = 1, 2, 1  # Example coefficients for the polynomial function
# need a function for creating a polynomial

function monomials(x, N) # N is the number of polynomials 
  m = [x^i for i in 0:N-1] # length needs changing, add different input paramete, add in an N values,
  return m # working progress 
end

# New way polynomial
# monomials generates m which is the coefficients
function generatePoly(a,x)
  m = monomials(x, length(a)) # want the length of a, a is an array
  return dot(a,m)
end 

# Define the noise addition function
# make it within a range, what level the noise it is
y = add_gauss(f.(x), 0.25); # Here we can play with the noise.

# Simple Bayesian regression (using least squares approximation)
# per Github
function bayesian_regression(x, y)
    X = hcat(ones(length(x)), x, x.^2)
    beta = X \ y  # Solves the linear system X * beta = y
    return beta
end

# Tikhonov (Ridge) Regression
# per Github
function tikhonov_regression(x, y, lambda)
    X = hcat(ones(length(x)), x, x.^2)
    I = I(size(X, 2))  # Identity matrix
    beta = inv(X' * X + lambda * I) * X' * y
    return beta
end


# Range of x values
x = -10:0.1:10

# Noise levels
noise_levels = 0:0.08:0.64

# Regularization parameters (penalty terms)
v = 1.0  # This would be the variance parameter in Bayesian regression
γ = [log(1 + 0.1 * x) for x in 0:10]  # Adjust this range as needed

# Prepare data frame to store results
# maybe 64, 32 
# thats something we need to decide, what accuracy ?
results_df = DataFrame(noise=Float[], method=String[], lambda=Float[], a_pred=Float[], b_pred=Float[], c_pred=Float[])

# Prepare plot
plot()

# Iterate over noise levels, penalty parameters, and regression types
for noise_std in noise_levels
    # Generate polynomial values and add noise
    y = polynomial.(x, a, b, c)
    y_noisy = add_gauss(y, noise_std)
    
    # Perform Bayesian regression
    # uncertainty
    b0 = bayesian_regression(x, y_noisy)
    a_pred_bayesian, b_pred_bayesian, c_pred_bayesian = b0[3], b0[2], b0[1]
    
    # Append Bayesian regression results to DataFrame
    push!(results_df, (noise_std, "Bayesian", NaN, a_pred_bayesian, b_pred_bayesian, c_pred_bayesian))
    
    # Plot Bayesian regression results
    xdense = -10:0.1:10
    y_dense_bayesian = polynomial.(xdense, a_pred_bayesian, b_pred_bayesian, c_pred_bayesian)
    plot!(xdense, y_dense_bayesian, label="Bayesian (Noise Std = $noise_std)", linewidth=2, color=:blue)

    # Perform Tikhonov regression for each lambda value
    for lambda in γ
        b_tikhonov = tikhonov_regression(x, y_noisy, lambda)
        a_pred_tikhonov, b_pred_tikhonov, c_pred_tikhonov = b_tikhonov[3], b_tikhonov[2], b_tikhonov[1]
        
        # Append Tikhonov regression results to DataFrame
        push!(results_df, (noise_std, "Tikhonov", lambda, a_pred_tikhonov, b_pred_tikhonov, c_pred_tikhonov))
        
        # Plot Tikhonov regression results
        y_dense_tikhonov = polynomial.(xdense, a_pred_tikhonov, b_pred_tikhonov, c_pred_tikhonov)
        plot!(xdense, y_dense_tikhonov, label="Tikhonov (λ=$lambda, Noise Std = $noise_std)", linewidth=2, linestyle=:dash)
    end
end

# Add scatter plot for noisy data
scatter!(x, y_noisy, label="Noisy Data", legend=:topright, xlabel="x", ylabel="y", size=(800, 400))

# Save the results to a CSV file
CSV.write("predicted_coefficients.csv", results_df)

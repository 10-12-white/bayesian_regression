using Noise
using Gadfly

include("BayesianRegression.jl")

f(t) = -2*t.^2+4*t+3 # The function to approximate
#f(t) = 3t+2

xdense = collect(LinRange(-1,1,100));
x = collect(LinRange(-1,1,5));
v = [t^i for t in x, i in 0:100] # Probably should be Chebyshev polynomials.
vdense = [t^i for t in xdense, i in 0:100] # Probably should be Chebyshev polynomials.
y = add_gauss(f.(x), 0.25); # Here we can play with the noise.
realy = f.(xdense)

# Take an increasing penalty parameter for the coefficients for the polynomial.
γ = [log(1+0.1*i) for i in 0:(size(v)[2]-1)]

b0 = BayesianRegression(y, v)
b1 = BayesianRegression(y, v, γ)  # vary the coefficients for LASSO.
b2 = BayesianRegression(y, v, 0, γ)  # vary the coefficients for Tikhonov/Ridge.
b3 = BayesianRegression(y, v, 0.2) # Normal Lasso
b4 = BayesianRegression(y, v, 0, 0.2) # Tikhonov regularisation.


set_default_plot_size(30cm, 20cm)

plot(x=x, y=y, Geom.point,
        color=["f(x)"], size=[4pt], style(line_width=2pt),
    layer(x=xdense, y=vdense*b0, Geom.line,  color=["Least Squares"]),
    layer(x=xdense, y=vdense*b1, Geom.line,  color=["Degressive LASSO"]),
    layer(x=xdense, y=vdense*b2, Geom.line,  color=["Degressive Ridge"]),
    layer(x=xdense, y=vdense*b3, Geom.line,  color=["LASSO"]),
    layer(x=xdense, y=vdense*b4, Geom.line,  color=["Tikhonov"]))

plot(x=x, y=y - f.(x), Geom.point,
        color=["f(x)"], size=[4pt], style(line_width=2pt),
    layer(x=xdense, y=vdense*b0 - realy, Geom.line,  color=["Least Squares"]),
    layer(x=xdense, y=vdense*b1 - realy, Geom.line,  color=["Degressive LASSO"]),
    layer(x=xdense, y=vdense*b2 - realy, Geom.line,  color=["Degressive Ridge"]),
    layer(x=xdense, y=vdense*b3 - realy, Geom.line,  color=["LASSO"]),
    layer(x=xdense, y=vdense*b4 - realy, Geom.line,  color=["Tikhonov"]))

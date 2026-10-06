# __The Dimension of the Quaternion Julia Sets__

## Introduction

The dimension of a quaternion Julia set is the dimension of a subset of $\mathbb{H}=\mathbb{R}^4$, and the question is whether it is computed by the two-dimensional slice together with the symmetry, or whether the fourth dimension contributes something new. The answer has two parts. The **real** parameters behave as the symmetry predicts: the set is the rotational hull of a slice, so its dimension is the dimension of the slice plus the dimension of the orbit, the orbit of a generic point of a three-dimensional vector subspace under the rotation group being a two-sphere; hence the dimension rises by $2$ and not by $1$. The **general non-real** parameters do not behave this way, because the set is not the hull of a slice — the reduction of *The Slices of the Quaternion Julia Sets* fails at such parameters — and for them only the general Lipschitz bounds survive, namely the dimension of the slice from below and the dimension of the profile plus $2$ from above.

The article proves the bounds, proves the exact formula for a real parameter, exhibits the exceptional real parameters for which the formula changes (those with the slice lying on the real axis, that is $c\le-2$ or $c>\tfrac14$), compares the results with the complex dimension and with the dimension of the limit sets of the Kleinian groups, and states plainly what is not known. The dimension itself, the Hausdorff dimension $\dim_H$ and the box dimension $\dim_B$, are those of *Fractal Geometry*, which owns the definitions and the product theorems used below.

The quadratic map and its symmetries are from *The Quaternion Quadratic Map and Its Julia Sets*; the hull theorem and the slice reduction are from *The Slices of the Quaternion Julia Sets*; the reduction of a parameter is from *The Quaternion Mandelbrot Set*; the escape radius and the potential are from *The Escape Radius and the Green's Function for Quaternions*; the complex dimension theory is from *The Hausdorff Dimension of the Julia Sets*; the limit sets of the discrete hyperbolic groups are from *Hyperbolic Geometry* and *The Dimension of the Boundary of a Hyperbolic Group*; and the pluricomplex analogue is *The Hausdorff Dimension of the Biquaternion Julia Sets*. No physics is invoked.

Throughout, $\dim_H$ is the Hausdorff dimension and $\dim_B$ the upper box dimension, $\kappa(c)=c_0+i|\mathbf c|$, and $J^{\mathbb{C}}_{\kappa}$ is the complex Julia set of $z \mapsto z^2+\kappa$.

## The Profile Map and the Bounds

**Definition.** The **profile map** is

$$
\Phi : \mathbb{H} \to \mathbb{R}\times[0,\infty) , \qquad \Phi(\tilde q) = (q_0,|\mathbf q|) ,
$$

and the **profile** of $J_c$ is $\Phi_c=\Phi(J_c)$. The profile is a subset of the closed half-plane; for a real parameter it is the $\sigma_c$ of *The Slices of the Quaternion Julia Sets*.

**Proposition (the profile map is Lipschitz, with spherical fibres).** The map $\Phi$ is $1$-Lipschitz, so $\dim_H \Phi_c \leq \dim_H J_c$. The fibre $\Phi^{-1}((a,r))$ is a point when $r=0$ and the two-sphere of radius $r$ centred at $a$ when $r>0$; consequently the fibres have dimension $2$ generically and $\dim_H J_c \leq \dim_H \Phi_c + 2$.

*Proof.* For $\tilde q,\tilde q'$ one has $\Phi(\tilde q)-\Phi(\tilde q')=(q_0-q_0',|\mathbf q|-|\mathbf q'|)$ and $||\mathbf q|-|\mathbf q'||\leq|\mathbf q-\mathbf q'|$, so $\Phi$ does not increase distances and a $1$-Lipschitz image cannot increase the Hausdorff dimension. The fibre statement is the definition of the rotation orbit; a quaternion is determined by its scalar part, the modulus of its vector part and the axis, and the axis is free. For the upper bound, cover the escaping part of the profile by the dyadic strips $\{2^{-(n+1)}<r\leq 2^{-n}\}$, $n \in \mathbb{Z}$; on each strip the section $J_c \cap \Phi^{-1}(\text{strip})$ is bi-Lipschitz equivalent to $(\Phi_c\cap\text{strip})\times S^2$, since on a strip with $r$ bounded below the map that sends $(a,r,u)$ to $a+r u$ has bounded derivative and bounded inverse; the product formula $\dim_H(X\times S^2)=\dim_H X+2$ of *Fractal Geometry* applies on each strip, and the countable stability of the Hausdorff dimension over the countable union of strips gives the bound. The axis part has dimension at most that of $\Phi_c$. $\square$

**Corollary (the slice is a lower bound).** Let $d=\dim_H J^{\mathbb{C}}_{\kappa(c)}$ be the dimension of the complex Julia set of the reduced parameter. Then

$$
d \leq \dim_H J_c \leq \dim_H \Phi_c + 2 .
$$

*Proof.* The restriction of $\Phi$ to the invariant plane $\mathbb{C}_c$ is, on the closed upper half-plane $\{b\geq0\}$ of $\mathbb{C}_c$, the bi-Lipschitz map $a+b\hat{\mathbf c}\mapsto(a,b)$ onto a half-plane; it carries $J_c\cap\mathbb{C}_c\cap\{b\geq0\}$ onto a subset of $\Phi_c$ of the same dimension, and that subset has dimension $d$ because the complex Julia set is symmetric under the reflection $y\mapsto-y$, so the whole set is the union of the two half-planes and the real part, and the maximum of the three dimensions is $d$. Hence $\dim_H\Phi_c\geq d$, and the proposition gives the bounds with the slice computed by *The Slices of the Quaternion Julia Sets*. $\square$

**Remark (the meaning of the bounds).** The upper bound says that the four-dimensional set cannot be more than two dimensions larger than its profile, because the only freedom beyond the profile is the two-dimensional sphere of the axis; the lower bound says that the set always contains its slice. The bounds differ by at most $2$, and the question is whether the upper one is attained.

## The Real Parameter

**Theorem (the exact formula for a real parameter).** Let $c \in \mathbb{R}$ and put $d=\dim_H J^{\mathbb{C}}_c$. If the slice $J^{\mathbb{C}}_c$ is not contained in the real axis, then

$$
\dim_H J_c = \dim_H\bigl(\Phi_c\cap\{r>0\}\bigr) + 2 = \dim_H\bigl(J^{\mathbb{C}}_c\cap\{y\neq0\}\bigr) + 2 ,
$$

and if in addition the top dimension of $J^{\mathbb{C}}_c$ is carried by its off-axis part, then $\dim_H J_c=d+2$. If the slice is contained in the real axis — which happens for the real parameters with $c\leq-2$ or $c>\tfrac14$ — then $\Phi_c\cap\{r>0\}=\emptyset$ and $\dim_H J_c=d$.

*Proof.* For a real parameter the set is $\Phi$-saturated: $J_c=\Phi^{-1}(\Phi_c)$, by the rotational hull theorem of *The Slices of the Quaternion Julia Sets*. Hence the fibre over every point of $\Phi_c\cap\{r>0\}$ is a full two-sphere contained in $J_c$, and the lower bound of the proposition is attained on each dyadic strip: $\dim_H J_c\geq\dim_H(\Phi_c\cap\{r>0\})+2$ by the product lower bound $\dim_H(X\times S^2)\geq\dim_HX+2$ applied to $X=\Phi_c\cap\{r\geq\eta\}$ and letting $\eta\to0$. The upper bound is the proposition. The identification of $\Phi_c$ with the profile of $J^{\mathbb{C}}_c$ is the corollary of *The Slices of the Quaternion Julia Sets*, and the restriction of $\Phi$ to $\{y>0\}$ of the complex plane is bi-Lipschitz onto $\{r>0\}$, which gives the second equality. If the slice lies in the real axis, its profile lies on $\{r=0\}$, the set is the slice embedded in $\mathbb{R}\subset\mathbb{H}$, and its dimension is $d$; the parameters $c\leq-2$ and $c>\tfrac14$ are the cases in which the real quadratic map has the Julia set a Cantor set of the real line, and $c=-2$ is the endpoint with $J^{\mathbb{C}}=[-2,2]$. $\square$

**Remark (the increase is two, and why).** The menu's dimension formula adds "the dimension of the symmetry orbit, the difference between the three-dimensional and the two-dimensional rotational hulls", which would suggest an increase of one. **The increase is two**, because the symmetry orbit of a generic point of the three-dimensional vector subspace under the rotation group is a two-sphere, not a circle: the hull of a two-dimensional slice under $SO(3)$ is a three-dimensional set, and the difference of dimensions between a slice of dimension $d$ and its hull of dimension $d+2$ is two. The case $c=0$ shows it: the slice is the unit circle of dimension $1$ and the set is the unit sphere $S^3$ of dimension $3$. A circle-orbit would give $2$ and would be wrong; the record of this correction is in the companion file.

**Corollary (the two exact examples).** For $c=0$ the slice is the unit circle, $d=1$, the profile is the upper semicircle, and $\dim_H J_0=\dim_H S^3=3=1+2$. For $c=-2$ the slice is the interval $[-2,2]$, which lies in the real axis, and $\dim_H J_{-2}=1$. The two cases are the two regimes of the theorem.

## The General Parameter

**Theorem (the bounds for a non-real parameter).** Let $c \notin \mathbb{R}$ and $d=\dim_H J^{\mathbb{C}}_{\kappa(c)}$. Then

$$
d \leq \dim_H J_c \leq \dim_H \Phi_c + 2 ,
$$

and no equality is asserted.

*Proof.* The corollary of the proposition applies to every parameter. $\square$

**Proposition (no product formula in general).** For a non-real parameter $c$ the set need not be $\Phi$-saturated, and there is no theorem of the form $\dim_H J_c=d+1$.

*Proof.* The reduction $\rho_c$ of *The Slices of the Quaternion Julia Sets* is the section of $\Phi$ that selects the plane of the parameter; it fails to intertwine the dynamics at $c=\tfrac12 e_2$, where a point with a bounded orbit has a reduction with unbounded orbit and the same profile. Hence $J_c\neq\Phi^{-1}(\Phi_c)$ for that parameter, the fibre lower bound is not available, and the only general bounds are those of the theorem. The value $d+1$ would require the symmetry orbit to be a circle, which it is not for the full rotation group; and it is not available for the stabiliser $SO(2)$ either, since the stabiliser of a non-real parameter fixes the invariant plane pointwise and contributes no orbit of the slice. $\square$

**Remark (what the general dimension is).** For a non-real parameter the dimension is caught between the slice dimension $d$ and the profile dimension plus two; the two coincide in the real case, and the numerical search of the companion file does not decide the general case. This is recorded as an open point and not as a theorem, and the article does not assert a value for a general non-real parameter beyond the bounds.

## Comparison with the Complex and the Kleinian Dimensions

### The Complex Dimension

The complex Julia set of the reduced parameter has dimension $d\in[0,2]$, and it is the invariant slice; the quaternion set contains it and adds at most the two dimensions of the axis. For a real parameter the addition is exactly two, so the quaternion dimension is the complex dimension of the slice plus two, and it ranges over $[2,4]$ in the interesting regime; for $c=-2$ it collapses to $1$ because the slice lies on the axis, and for $c\leq-2$ it is the dimension of the real Cantor set. The complex theory of *The Hausdorff Dimension of the Julia Sets* gives $d$ as the zero of the pressure function in the hyperbolic case, and the quaternion formula transports it.

### The Kleinian Limit Sets

The limit sets of the discrete groups of hyperbolic isometries are the fractal sets of Parts IV and VI, and their dimensions are those of the limit set on the sphere at infinity and of the boundary of a hyperbolic group, treated in *Hyperbolic Geometry*, *The Dimension of the Boundary of a Hyperbolic Group* and *Kleinian and Fuchsian Groups*. The comparison with the quaternion Julia sets is a comparison of two different mechanisms: the limit set is the accumulation set of a discrete group and is computed by the Patterson–Sullivan theory, while the quaternion Julia set is the non-escaping set of a polynomial and is computed by the potential of *The Escape Radius and the Green's Function for Quaternions*. The dimensions agree in no automatic way; the connection between the two is the Kleinian limit set, whose group theory is *Kleinian and Fuchsian Groups*'s and whose hyperbolic example is *The Dimension of the Boundary of a Hyperbolic Group*'s, cited rather than developed. The biquaternion analogue is *The Hausdorff Dimension of the Biquaternion Julia Sets*.

## Worked Example

**Example (three dimensions).** The values were recomputed from the definitions.

**(a) The parameter $c=0$.** The slice is the unit circle, of dimension $1$; the profile is the upper semicircle, of dimension $1$; the upper bound gives $1+2=3$ and the set is $S^3$, of dimension $3$. The formula is attained.

**(b) The parameter $c=-2$.** The slice is the interval $[-2,2]$ together with the Cantor structure of the real Julia set, which here is the whole interval, of dimension $1$, lying on the real axis; the off-axis part of the profile is empty and the set is the interval, of dimension $1$. The exceptional case of the theorem.

**(c) A real parameter with a connected off-axis slice, $c=-\tfrac12$.** The complex Julia set of $z^2-\tfrac12$ is a quasi-circle of dimension $d\in(1,2)$, not contained in the real axis, so the real parameter formula gives $\dim_H J_{-1/2}=d+2\in(3,4)$, and the set is the revolution of the quasi-circle about the real axis. For $c>\tfrac14$, by contrast, the complex Julia set is a Cantor set contained in the real axis, and the quaternion set collapses to it, of dimension $d<1$: that is the exceptional regime of the theorem.

**(d) A non-real parameter, $c=e_1$.** The slice is the complex Julia set of $z^2+i$, of dimension $d$; the bounds give $d\leq\dim_H J_{e_1}\leq\dim_H\Phi_c+2$, and the general value is not asserted. The case is the one in which the slice and the profile are the only available data, and the article states the bounds.

## Summary

The profile map $\Phi(\tilde q)=(q_0,|\mathbf q|)$ is $1$-Lipschitz with spherical fibres, and it gives the general bounds $d\leq\dim_H J_c\leq\dim_H\Phi_c+2$, where $d$ is the dimension of the complex Julia set of the reduced parameter and $\Phi_c$ is the profile. For a real parameter the set is $\Phi$-saturated, the fibres over the off-axis part of the profile are full two-spheres, and the exact formula is

$$
\dim_H J_c = \dim_H\bigl(J^{\mathbb{C}}_c\cap\{y\neq0\}\bigr)+2 ,
$$

which is $d+2$ when the off-axis part carries the top dimension; the exceptions are the parameters with the slice on the real axis ($c\leq-2$ or $c>\tfrac14$), for which the dimension is that of the slice. The increase is two and not one, because the symmetry orbit is a two-sphere and not a circle; the case $c=0$ shows it, the unit circle becoming the unit sphere $S^3$. For a non-real parameter the set is not the hull of its slice — the reduction fails at $c=\tfrac12e_2$ — and only the general bounds survive; the exact general value is stated as an open point. The complex dimension is *The Hausdorff Dimension of the Julia Sets*'s, the limit-set dimensions are those of *The Dimension of the Boundary of a Hyperbolic Group* and *Kleinian and Fuchsian Groups*, and the biquaternion analogue is *The Hausdorff Dimension of the Biquaternion Julia Sets*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\dim_H$, $\dim_B$ | Hausdorff dimension; upper box dimension, from *Fractal Geometry* |
| $\Phi(\tilde q)=(q_0,\lvert\mathbf q\rvert)$ | The profile map |
| $\Phi_c=\Phi(J_c)$ | The profile of the Julia set |
| $d=\dim_H J^{\mathbb{C}}_{\kappa(c)}$ | Dimension of the complex slice |
| $\kappa(c)=c_0+i\lvert\mathbf c\rvert$ | Reduced complex parameter |
| $\mathbb{C}_c$, $\{r>0\}$ | Invariant plane; off-axis part of the profile |
| $\rho_c$ | The reduction of *The Slices of the Quaternion Julia Sets* |
| $\dim_H J_0=3$, $\dim_H J_{-2}=1$ | The two exact examples |

## Further Reading

- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd ed. (Wiley, 2014). The Hausdorff and box dimensions and the product theorems, cited to *Fractal Geometry*.
- Kenneth Falconer, *Techniques in Fractal Geometry* (Wiley, 1997). The product and Lipschitz-image estimates used in the bounds.
- John Milnor, *Dynamics in One Complex Variable*, 3rd ed. (Princeton, 2006). The dimension of the complex Julia sets, cited to *The Hausdorff Dimension of the Julia Sets*.
- Dennis Sullivan, "The density at infinity of a discrete group of hyperbolic motions", *Publications Mathématiques de l'IHÉS* 50 (1979), 171–202. The Kleinian limit sets and their dimensions, cited to *Kleinian and Fuchsian Groups*.

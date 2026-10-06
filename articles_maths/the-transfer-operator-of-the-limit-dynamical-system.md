# __The Transfer Operator of the Limit Dynamical System__

## Introduction

Every self-similar group has a limit space, and every limit space carries a map of degree $d$: the **shift** $\varphi$, whose inverse branches $\sigma_x$ are the dilation maps of the tiles. Push a measure forward along $\varphi$ and it spreads over the $d$ branches; pull a function back along the branches and the $d$ values accumulate. The operator that performs the accumulation is the **transfer operator** $L_\varphi$, the Perron–Frobenius operator of the dynamical system, and its fixed points are the invariant measures and the invariant densities of the system. The transfer operator is the computational entry to the limit dynamical system: it converts the group's recursion into a linear operator whose spectrum governs the invariant measure, the pressure, the dimension and the decay of correlations. The article builds that operator.

The article defines the limit dynamical system of a contracting self-similar group — the shift $\varphi$ on the limit space $\mathcal{J}_G$, with the $d$ inverse branches coding the tiles — and defines the transfer operator $L_\varphi f(x)=\sum_{\varphi(y)=x}\delta(y)f(y)$ with the local degree $\delta(y)$. It proves that $L_\varphi$ is the transpose of the **Koopman operator** $U_\varphi f=f\circ\varphi$ in the duality of the invariant measure, so that the invariant measures are the fixed points of the dual, and it identifies the invariant measure with the one of *The Self-Similar Measure and the Invariant Measure*. It proves that the leading eigenvalue of $L_\varphi$ is one, that the corresponding eigenfunction is the invariant density, and that the pressure $P(t)$ of the potential $t\log d$ is the logarithmic growth rate of the transfer operator, so that the dimension of the limit space is the root of the equation $P(-s\log|\varphi'|)=0$. It reads the operator in the language of *The Transfer Operator* and *Time Reversal and the Transfer Operator* of Part III, notes that the limit map is not invertible, so that the transfer operator is not the inverse of the Koopman operator but the Perron–Frobenius operator of a non-invertible system, and states the ergodicity, the spectral gap and the exponential decay of correlations of *Ergodic Theory* in terms of the spectrum of $L_\varphi$.

The limit space, the tiles, the shift and the coding are *Limit Spaces and Schreier Graphs*; the group, the contraction and the wreath recursion are *Self-Similar Groups*; the ergodicity, the mixing, the spectral gap and the decay of correlations of the limit dynamical system are *Ergodic Theory* and *Dynamical Systems*; the transfer operator, the Koopman operator and their duality are *The Transfer Operator*, *Time Reversal and the Transfer Operator* and *The Adjoint of the Koopman Operator*, in Part III, of which this article is the fractal instance; the same operator for a reversibility structure is *The Adjoint of the Transfer Operator of the Limit Dynamical System*, the ninth article of the category; the dynamical systems that supply the invertible case are *Dynamical Systems*, and the coding map is *Fractal Geometry* and *Limit Spaces and Schreier Graphs*; the pressure, the equilibrium states and the Gibbs measures are *Ergodic Theory*, and the dimension is *Fractal Geometry*. No physics is invoked.

## The Limit Dynamical System and Its Branches

### The Limit Map

**Definition.** Let $G\le\operatorname{Aut}(\mathcal{T})$ be a contracting self-similar group on the $d$-letter alphabet $X$, with limit space $\mathcal{J}_G$ and tiles $T_v$ as in *Limit Spaces and Schreier Graphs*. The **limit map** is the shift
$$
\varphi=s:\mathcal{J}_G\longrightarrow\mathcal{J}_G,\qquad \varphi(T_{xv})=T_v ,
$$
a continuous map of degree $d$: the preimage of every point consists of one point in each tile $T_x$, so $\varphi$ is $d$-to-one counted with multiplicity, and the multiplicity is the **local degree** $\delta(y)$ of the point $y$.

**Definition.** The **inverse branches** are the maps
$$
\sigma_x:\mathcal{J}_G\longrightarrow T_x,\qquad \sigma_x=\varphi|_{T_x}^{-1},
$$
so that $\varphi\circ\sigma_x=\mathrm{id}$ for every $x\in X$ and $\varphi^{-1}(\{y\})=\{\sigma_x(y):x\in X\}$ counted with multiplicity; the branches are the contractions of the coding map of the group, and the tile $T_v$ is the image of $\mathcal{J}_G$ under the composition of the branches along $v$.

**Proposition (the coding).** The coding map $\pi:\partial\mathcal{T}\to\mathcal{J}_G$ intertwines the shift of the boundary with $\varphi$: $\pi(x\xi)=\sigma_x(\pi(\xi))$ and $\varphi(\pi(x\xi))=\pi(\xi)$. In particular the diagram of the boundary and of the limit space commutes, and the two systems are conjugate when the coding is injective.

*Proof.* The tiles are nested, $T_{x\xi}\subset T_x$, and the contraction of the composition $S_{x_1}\cdots S_{x_n}$ tends to zero, so the coded point satisfies the two identities; the conjugation is the identification of the two shifts when the coding is injective, which is the case when the group is self-replicating and the action is faithful. The statement is that of *Limit Spaces and Schreier Graphs*.

### The Local Degree

**Definition.** The **local degree** at $y$ is the number $\delta(y)=\#\{x\in X:\sigma_x(y)=z\text{ for a single }z\}$, the multiplicity of $y$ as the image of $\varphi$; it equals one away from the countable set of the vertices of the tiles and is $d$ in the interior of each tile. The **Jacobian** of $\varphi$ at $y$ is $|\varphi'(y)|=\delta(y)$ in the normalisation in which all the branches are measure-preserving; the general branch has the Jacobian $|\varphi|$ of its inverse branch, a bounded continuous function.

## The Transfer Operator

### Definition

**Definition.** Let $\varphi:\mathcal{J}_G\to\mathcal{J}_G$ be the limit map with the local degree $\delta(\cdot)$ and let $f:\mathcal{J}_G\to\mathbb{C}$ be a bounded continuous function. The **transfer operator** is
$$
L_\varphi f(x)=\sum_{\varphi(y)=x}\delta(y)\,f(y)=\sum_{x'\in X}\delta\bigl(\sigma_{x'}(x)\bigr)\,f\bigl(\sigma_{x'}(x)\bigr),
$$
the sum being over the preimage of $x$ counted with multiplicity; when the local degree is the constant $\delta=d$ this is $L_\varphi f=d\sum_{x'\in X}f\circ\sigma_{x'}$.

**Theorem (the transfer operator is the transpose of the Koopman operator).** Let $U_\varphi f=f\circ\varphi$ be the **Koopman operator** and let $\mu$ be any measure with $\varphi_*\mu=\mu$. Then
$$
\int (L_\varphi f)\,g\,\Bigl(\frac{d\varphi_*\mu}{d\mu}\Bigr)^{-1}d\mu
=\int f\,(U_\varphi g)\,d\mu ,
$$
and when $d\varphi_*\mu/d\mu\equiv 1$, that is when $\mu$ is the invariant measure with unit Jacobian normalisation, $L_\varphi$ is the transpose of $U_\varphi$ with respect to $\mu$:
$$
\int (L_\varphi f)\,g\,d\mu=\int f\,(U_\varphi g)\,d\mu .
$$

*Proof.* Change the variable $x=\varphi(y)$ in $\int f(y)g(\varphi(y))\,d\mu(y)$ and use the definition of the pushforward; the local degree is the image counting, and the Radon–Nikodym factor is the discrepancy between $\mu$ and $\varphi_*\mu$. When $\mu$ is invariant with unit Jacobian, the two agree and the identity is the transpose relation. This is the duality of *The Transfer Operator* specialised to the limit system, with the **adjoint** of the transfer operator treated in *The Adjoint of the Transfer Operator of the Limit Dynamical System* and *The Adjoint of the Koopman Operator*.

### The Dual Action on Measures

**Definition.** The **dual transfer operator** on measures is
$$
(L_\varphi^*\nu)(A)=\sum_{x\in X}\int_{A}\delta(\sigma_x(y))\,(\sigma_x^{-1})_*\nu(dy)=\sum_{x\in X}\nu_x(A), 
$$
the sum of the pushforwards of the restriction of $\nu$ to each branch, so that $\int f\,d(L_\varphi^*\nu)=\int L_\varphi f\,d\nu$ for every $f$.

**Theorem (the invariant measures are the fixed points).** A probability measure $\mu$ on $\mathcal{J}_G$ is invariant for the limit map, $\varphi_*\mu=\mu$, if and only if $L_\varphi^*\mu=\mu$; the invariant measures form a simplex, and under the coding they are the images of the invariant measures of the shift, so that the invariant measure with the weights $p$ is the pushforward $\pi_*\nu_p$ of the Bernoulli measure of *The Self-Similar Measure and the Invariant Measure*.

*Proof.* The duality $\int f\,d(L_\varphi^*\mu)=\int L_\varphi f\,d\mu=\int f\circ\varphi\,d\mu=\int f\,d\varphi_*\mu$ (the middle identity is the transpose relation with $g=1$) shows $L_\varphi^*\mu=\varphi_*\mu$; hence the fixed points are the invariant measures. The identification with $\pi_*\nu_p$ is the ergodic theorem for the shift of the boundary, which is the Bernoulli shift of the article on the invariant measure, and the weights are the pressures of the branches.

## The Invariant Density and the Pressure

### The Eigenvalue One

**Theorem (the leading eigenvalue and the invariant density).** The transfer operator $L_\varphi$ has the eigenvalue $1$ on the set of $L_\varphi^*$-invariant measures normalised so that the local degree has mean one, the corresponding left eigenvector is the constant function, and when the invariant measure $\mu$ is absolutely continuous with density $h$ with respect to a reference measure $\nu$, the density is the Perron–Frobenius eigenfunction $h=L_\varphi h$ normalised by $\int h\,d\nu=1$; the rest of the spectrum of $L_\varphi$ on the H\"older functions lies in a disc of radius strictly less than $1$ in the topologically mixing case, which is the **spectral gap**.

*Proof sketch.* The constant function is a left eigenvector because $\sum_{\varphi(y)=x}\delta(y)=1$ for every $x$, the local degree being the image multiplicity. The existence and the uniqueness of the positive eigenfunction are the Perron–Frobenius theorem of *The Transfer Operator* applied to the positive operator $L_\varphi$ with the Lasota–Yorke inequality of the contraction; the eigenfunction is the invariant density and the eigenmeasure is the invariant measure. The gap is the **Ruelle–Perron–Frobenius** theorem, quoted and applied in *Ergodic Theory*.

### The Pressure and the Dimension

**Definition.** The **pressure** of the potential $t\log d$ is
$$
P(t)=\lim_{n\to\infty}\frac1n\log\sum_{|w|=n}\Delta_w^t ,
$$
where $\Delta_w$ is the Jacobian of the branch composition along $w$, the sum being the Frobenius–Perron normalisation of the $n$-th iterate of the transfer operator; the pressure is the logarithm of the leading eigenvalue of $L_\varphi$ on the potential.

**Theorem (dimension is the root of the pressure).** If the limit map is conformal with the inverse branches of the ratios $r_x$ and the system satisfies the open set condition, then the Hausdorff dimension of the limit space is the unique root $s$ of
$$
P(-s\log|\varphi'|)=0,\qquad\text{equivalently}\qquad \sum_{x\in X}r_x^{s}=1,
$$
and the equilibrium state of the potential $-s\log|\varphi'|$ is the self-similar measure of maximal dimension of *The Self-Similar Measure and the Invariant Measure*.

*Proof.* The Frobenius–Perron normalisation at level $n$ is $\sum_{|w|=n}\Delta_w^{-s}$, and its exponential growth rate is $P(-s\log|\varphi'|)$; the covering of $\mathcal{J}_G$ by the level-$n$ tiles shows that the dimension is the root, and the equilibrium state is the Gibbs measure of the potential, whose local dimension is constant $s$. This is the Bowen equation of *Fractal Geometry* and *Ergodic Theory* in the self-similar case; the derivation of the pressure from the transfer operator is the standard one of *The Transfer Operator*.

## The Correspondence with the Transfer Operator of Part III

### The Perron–Frobenius Reading

**Remark (transfer and Koopman in the non-invertible case).** In *The Transfer Operator* and *Time Reversal and the Transfer Operator* of Part III the transfer operator of a measure-preserving dynamical system is the inverse of the Koopman operator, because the system is invertible; the limit dynamical system of a self-similar group is **not invertible** — the shift $\varphi$ is $d$-to-one — and the two operators are transposes, not inverses:
$$
L_\varphi U_\varphi(f)(x)=d\sum_{x'}f\circ\varphi\circ\sigma_{x'}(x)=d\,f(\varphi(x))=d\,(U_\varphi f)(x),
$$
so $L_\varphi U_\varphi=d\,U_\varphi\ \cdot$ the identity of the fibres, the local degree appearing as the discrepancy. The operator to which the Part III theory applies after the **natural extension** of the system — the two-sided shift whose one-sided factor is $\varphi$ — recovers the invertible case and the time-reversal involution; the reversible case is *Reversible Iterated Function Systems and the Involution*, and the adjoint relation is *The Adjoint of the Transfer Operator of the Limit Dynamical System*.

### Ergodicity, the Spectral Gap and the Decay of Correlations

**Theorem (the spectral reading of the mixing).** The limit dynamical system is ergodic with respect to the invariant measure $\mu$ exactly when the eigenvalue $1$ of $L_\varphi$ on the continuous functions is simple, and it is mixing exactly when the rest of the spectrum of $L_\varphi$ on the H\"older functions is contained in a disc of radius $<1$, in which case the correlations
$$
C_n(f,g)=\int f\circ\varphi^n\,g\,d\mu-\Bigl(\int f\,d\mu\Bigr)\Bigl(\int g\,d\mu\Bigr)
$$
decay exponentially, $|C_n(f,g)|\le C\theta^n$, and the central limit theorem holds for the Birkhoff sums.

*Proof sketch.* The eigenvalue $1$ corresponds to the invariant functions; simplicity is the ergodicity and the simplicity on the two-sided natural extension is the mixing, both of *Ergodic Theory*. The decay is the spectral gap: the resolvent of $L_\varphi$ on the H\"older space is analytic on a disc containing the unit circle except at $1$, and the correlations are the Fourier coefficients of the resolvent; the central limit theorem follows from the same gap. The statements are those of *The Transfer Operator* and *Ergodic Theory*, applied to the limit system.

## Summary

The **limit dynamical system** of a contracting self-similar group is the shift $\varphi$ on the limit space, of degree $d$, with the inverse branches $\sigma_x=\varphi|_{T_x}^{-1}$ and the local degree $\delta(y)$. The **transfer operator**
$$
L_\varphi f(x)=\sum_{\varphi(y)=x}\delta(y)f(y)=\sum_{x'\in X}\delta(\sigma_{x'}(x))f(\sigma_{x'}(x))
$$
is the transpose of the **Koopman operator** $U_\varphi f=f\circ\varphi$ with respect to the invariant measure, its dual $L_\varphi^*$ has the invariant measures as fixed points — the pushforwards $\pi_*\nu_p$ of the Bernoulli measures of *The Self-Similar Measure and the Invariant Measure* — the constant function is a left eigenvector for the eigenvalue $1$, and the invariant density is the Perron–Frobenius eigenfunction $h=L_\varphi h$. The **pressure** $P(t)$ is the logarithmic growth rate of the iterated transfer operator, and the dimension of the limit space is the root of $P(-s\log|\varphi'|)=0$, with the equilibrium state the measure of maximal dimension. Because $\varphi$ is $d$-to-one, the transfer operator is not the inverse of the Koopman operator but the Perron–Frobenius operator, with $L_\varphi U_\varphi=d\,U_\varphi$ on the fibres; the time-reversal involution returns on the natural extension, and the reversible case is *Reversible Iterated Function Systems and the Involution*. The complex eigenvalues and the covariance of the operators are the subject of *The Adjoint of the Transfer Operator of the Limit Dynamical System*. Ergodicity is the simplicity of the eigenvalue $1$, mixing is the spectral gap on the H\"older functions, and the gap gives the exponential decay of correlations and the central limit theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi=s$, $\deg\varphi=d$ | The limit map and its degree |
| $\sigma_x$, $T_x$, $\delta(y)$ | The inverse branches, the tiles, the local degree |
| $\pi:X^\omega\to\mathcal{J}_G$ | The coding map |
| $L_\varphi f(x)=\sum_{\varphi(y)=x}\delta(y)f(y)$ | The transfer operator |
| $U_\varphi f=f\circ\varphi$ | The Koopman operator |
| $L_\varphi^*\mu=\varphi_*\mu$, $L_\varphi^*\mu=\mu$ | The dual action and the invariant measures |
| $h=L_\varphi h$ | The invariant density |
| $P(t)$, $P(-s\log\|\varphi'\|)=0$ | The pressure and the Bowen equation |
| $C_n(f,g)\le C\theta^n$ | The decay of correlations |

## Further Reading

- Volodymyr Nekrashevych, *Self-similar groups*, Mathematical Surveys and Monographs **117** (American Mathematical Society, 2005), for the limit dynamical system, the tiles, the local degree and the transfer operator.
- Laurent Bartholdi, Rostislav Grigorchuk and Volodymyr Nekrashevych, "From fractal groups to fractal sets", in *Fractals in Graz 2001* (Birkhäuser, 2003), 25–118, for the limit dynamical systems, the contraction and the invariant measures.
- David Ruelle, *Thermodynamic Formalism: The Mathematical Structures of Equilibrium Statistical Mechanics* (Addison-Wesley, 1978), for the transfer operator, the pressure and the equilibrium states.
- William Parry and Mark Pollicott, "An analogue of the prime number theorem for closed orbits of Axiom A flows", *Annals of Mathematics* **118** (1983), 573–591, for the Ruelle–Perron–Frobenius theorem and the spectral gap.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the pressure, the Gibbs measures and the Bowen equation.
- Viviane Baladi, *Positive Transfer Operators and Decay of Correlations* (World Scientific, 2000), for the spectral gap, the decay of correlations and the central limit theorem.
- Kenneth Falconer, *Techniques in Fractal Geometry* (Wiley, 1997), for the pressure formula for the dimension of a self-similar set.

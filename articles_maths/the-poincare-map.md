# __The Poincaré Map__

## Introduction

A **Poincaré map** is the return map to a transverse section of a flow, and it is the operator that reduces a continuous-time system to a discrete-time one: the flow cross-cuts the section at a sequence of return times, and the transformation that carries each intersection to the next records the whole flow. What the present article develops is not the existence or the smoothness of the return map — those are the **Poincaré section theorem** of *Smooth Dynamical Systems* — but the operator-theoretic content of the reduction: the way in which the Koopman operator and the transfer operator of the flow are assembled from those of the return map and the return time, the way in which the spectrum of the flow is read from the return map through the cocycle equation, and the way in which the ergodic and the statistical properties pass from one to the other. The return map is thus the **reduction operator** of the continuous theory, and the dictionary between the two theories is its content.

The article defines the return map, the return time and the section, citing the smooth theory for their existence, and then treats the reduction. It states the **suspension dictionary**: a flow with a section is the suspension of its return map, so an observable of the flow is a function on the section and a time coordinate, and the flow operator is the translation in the time coordinate composed with the return map; it derives the **cocycle equation** relating the eigenfunctions of the flow operator to those of the return map, $g(Px)=e^{i\lambda\tau(x)}g(x)$, and reads the spectrum of the flow from the spectrum of the return map together with the return time; it treats the transfer operators of the two reductions (the return map, the **induced transformation** on a subset, and their invariant measures), with **Kac's formula** for the mean return time; and it states **Abramov's formula** for the entropy and the transfer of ergodicity, mixing and hyperbolicity. It closes with the linearised Poincaré map, the derivative $DP$ at a periodic orbit, and its relation to the monodromy of the variational equation of *The Evolution Operator*.

The flows, the periodic orbits, the transverse sections, the return map, the return time, the suspension, the Floquet multipliers and the Poincaré section theorem are those of *Smooth Dynamical Systems*, which owns the constructions and the derivative computations; the invariant measures, the ergodicity, the mixing, the entropy and Abramov's formula are those of *Ergodic Theory*; the transfer operators are *The Transfer Operator*, and the flow operator is *The Flow Operator*, both immediately preceding; the monodromy and the variational evolution operator are *The Evolution Operator*. The Koopman operator of the return map is *The Koopman Operator*. The reduction used here originates in the classical theory of **cross-sections**: the suspension, the induced transformation, the return time and the first-return map.

No physics is invoked.

## The Section and the Return Map

**Definition.** Let $\varphi_t$ be a complete flow on a manifold $M$ and let $\Sigma\subseteq M$ be a codimension-one submanifold transverse to the generating field $X$, a **section**. For $q\in\Sigma$ whose forward orbit meets $\Sigma$ again, the **first return time** is $\tau(q)=\inf\{t>0:\varphi_t(q)\in\Sigma\}$ and the **return map** (Poincaré map) is $P(q)=\varphi_{\tau(q)}(q)\in\Sigma$. The section is **global** if every orbit meets it; the return map is then defined on all of $\Sigma$, and the flow is the **suspension** of $P$ with roof $\tau$: the quotient of $\Sigma\times[0,\infty)$ by the identification $(q,\tau(q))\sim(Pq,0)$, with the flow the translation in the second coordinate modulo the identification. The existence and the smoothness of $P$ and $\tau$, and the equivalence of the flow with the suspension, are the content of the Poincaré section theorem and the suspension theorem of *Smooth Dynamical Systems*, and are cited here.

**Definition (the induced measure).** Let $\mu$ be a $\varphi_t$-invariant measure and let the section carry the induced measure $\mu_\Sigma$ defined by

$$
\mu_\Sigma(A)=\frac{1}{\bar\tau}\int_A\tau\,d\mu_\Sigma^{\natural},
$$

where $\mu_\Sigma^{\natural}$ is the measure on the section obtained by the transversal disintegration of $\mu$ and $\bar\tau$ its total mass; when the section is global, $\mu_\Sigma$ is the invariant probability of $P$ and $\bar\tau=\int_\Sigma\tau\,d\mu_\Sigma$ is the **mean return time**. The induced measure is the bridge between the invariant measures of the flow and of the return map: the invariant measures of the flow correspond bijectively to the invariant measures of the return map with finite mean return time.

## The Suspension Dictionary

### The Flow Operator as a Suspension

**Definition.** Let the flow be the suspension of $(P,\tau)$. A **suspension observable** of the flow that is independent of the time coordinate is a function $G$ on $\Sigma\times[0,\infty)$ that is $P$-equivariant in the sense $G(q,\tau(q))=G(Pq,0)$, identified with a function on the suspension manifold; the flow operator acts on it by translation of the time coordinate,

$$
(U_tG)(q,s)=G(q,s+t) \quad \text{modulo the identification}, \qquad U_t:G\mapsto G(\cdot,s+t),
$$

and after a full pass through the fundamental domain the translation rebases the point by $P$, so the discrete return map appears as the **Poincaré operator** $U_Pg=g\circ P$ on the section.

**Theorem (the cocycle equation).** A function $F\in C(M)$ is an eigenfunction of the flow operator with eigenvalue $\lambda\in\mathbb{R}$, $U_tF=e^{i\lambda t}F$ for all $t$, if and only if its restriction $g=F|_\Sigma$ is nonzero and satisfies the **$\tau$-cocycle equation**

$$
g(Px)=e^{i\lambda\tau(x)}g(x) \qquad (x\in\Sigma).
$$

More generally, if $g$ satisfies $g(Px)=e^{i\phi(x)}g(x)$ for a phase $\phi$ and the flow function is rebuilt by $F(q,s)=e^{i\phi_s(q)}g(q)$ with $\phi_s$ accumulating $\phi$ along the return, then $F$ is an eigenfunction exactly when the phase is a **coboundary** over the return map, $\phi(x)=\psi(Px)-\psi(x)$, in which case the eigenvalue is $0$.

*Proof.* If $U_tF=e^{i\lambda t}F$, evaluating along the orbit from $x\in\Sigma$ at the return time gives $F(Px)=F(\varphi_{\tau(x)}x)=e^{i\lambda\tau(x)}F(x)$, so $g=F|_\Sigma$ satisfies the cocycle equation. Conversely, if $g$ satisfies it, define $F$ on the suspension by $F(q,s)=e^{i\lambda s}g(q)$; the identification $(q,\tau(q))\sim(Pq,0)$ is respected because $e^{i\lambda\tau(q)}g(q)=g(Pq)$, and the flow $U_tF=e^{i\lambda t}F$ holds by the definition of the translation. The coboundary statement is the special case in which the cocycle $e^{i\phi}$ is a coboundary, so that it can be removed by the multiplication by $e^{i\psi}$.

**Corollary (spectral reduction).** The eigenvalues of the unitary flow operator are the numbers $\lambda$ for which there is a nonzero $g$ on the section with $g(Px)=e^{i\lambda\tau(x)}g(x)$; the flow has pure point spectrum exactly when the section is spanned by such twisted solutions. The twisted transfer operator that governs the general case is the operator-theoretic form of the cocycle equation and is *The Adjoint of the Koopman Operator* in the `- * Operator Theory` group; only the cocycle equation is derived here.

**Remark (the return time as a roof).** The eigenvalue equation is not an eigenvalue equation of $U_P$ alone unless the return time is constant: when $\tau$ is constant, say $\tau\equiv\bar\tau$, the cocycle equation reduces to $g\circ P=e^{i\lambda\bar\tau}g$, so the eigenvalues of the flow are $2\pi k/\bar\tau$ together with the eigenvalue data of the return map, and the flow is the product of the return map with a rotation. When $\tau$ is not constant the eigenvalue problem is genuinely twisted by the roof, and the flow may be weakly mixing while the return map is not, or conversely.

### Ergodicity, Mixing and Entropy

**Theorem (transfer of the ergodic properties, quoted).** Let the flow be the suspension of $(P,\tau)$ with finite mean return time. Then the flow preserves $\mu$ if and only if $P$ preserves the induced $\mu_\Sigma$, and the flow is ergodic if and only if $P$ is ergodic; the flow is mixing if and only if $P$ is mixing and the roof $\tau$ is not cohomologous to a constant, the exceptional case $\tau\equiv\bar\tau$ being the product of $P$ with the rotation of period $\bar\tau$, which is ergodic but not mixing. The entropy is given by **Abramov's formula**

$$
h_\mu(\varphi_1)=h_{\mu_\Sigma}(P)\big/\bar\tau ,
$$

the entropy per unit time of the flow being the entropy per return of the return map divided by the mean return time.

*Proof.* Quoted as standard from *Ergodic Theory* and *Smooth Dynamical Systems*; the correspondence of the invariant measures is the bijection between the invariant measures of the flow and those of the return map with finite mean return time, and the formula for the entropy is Abramov's theorem.

**Remark (the hyperbolicity transfer).** The suspension of a hyperbolic diffeomorphism is a hyperbolic flow and the suspension of an Anosov diffeomorphism is an Anosov flow, so the reduction carries the hyperbolicity of the smooth theory as well; the statements and the stable and unstable manifolds are those of *Smooth Dynamical Systems* and *Hyperbolic Dynamics and Anosov Systems*.

## The Transfer Operator of the Reduction

### The Return Map's Transfer Operator and the Induced Measure

**Theorem (the invariant measure of the section is the fixed point).** Let the flow be the suspension of $(P,\tau)$ and let $\mu_\Sigma$ be the invariant probability of $P$ with $\bar\tau=\int\tau\,d\mu_\Sigma$. Then the flow's invariant probability is the normalised suspension of $\mu_\Sigma$, and the invariant measure of the return map is the fixed point of its transfer operator,

$$
\int_\Sigma\mathcal{P}_Ph\cdot g\,d\mu_\Sigma=\int_\Sigma h\cdot(g\circ P)\,d\mu_\Sigma ,
$$

the construction and the spectrum being those of *The Transfer Operator*; the transfer operator of the flow on the section is the **twisted** operator in which each branch carries the weight $e^{i\lambda\tau}$ of the corollary above.

*Proof.* The invariance of the suspension measure under the flow and of $\mu_\Sigma$ under $P$ are the two faces of the same statement: the flow carries the slice at height $s$ to the slice at height $s+t$, and the return to the section is $P$; the normalisation by $\bar\tau$ makes the total mass $1$. The fixed-point property of $\mu_\Sigma$ for $\mathcal{P}_P$ is the elementary property of the transfer operator.

### The Induced Transformation and Kac's Formula

**Definition.** Let $T$ be a measure-preserving transformation of $(X,\mu)$ and let $A\subseteq X$ with $\mu(A)>0$. The **induced transformation** (first-return map) is

$$
T_A(x)=T^{r_A(x)}(x), \qquad r_A(x)=\inf\{n\ge1:T^n x\in A\},
$$

defined for $x\in A$; it is the Poincaré map of the discrete system on the "section" $A$. The induced measure is the normalisation $\mu_A=\mu|_A/\mu(A)$.

**Theorem (Kac's formula).** If $(X,\mu,T)$ is ergodic and measure-preserving and $\mu(A)>0$, then

$$
\int_A r_A\,d\mu=1, \qquad \int_A r_A\,d\mu_A=\frac{1}{\mu(A)} ;
$$

that is, the mean return time to $A$ with respect to the induced probability is the reciprocal of the measure of $A$.

*Proof.* By the Poincaré recurrence theorem $r_A$ is finite a.e. on $A$, and the sets $A_n=\{x\in A:r_A(x)=n\}$ partition $A$ up to a null set; the images $T^kA_n$, $0\le k<n$, tile the space $X$ up to the measure of the wandering part, so $\sum_n n\mu(A_n)=1$ and the first identity follows; the second is the first divided by $\mu(A)$.

**Example (a doubling map, verified).** For $T x=2x\bmod1$ on $[0,1)$ with Lebesgue measure and $A=[0,\tfrac12)$, the first return time $r_A$ has level sets of measure $\mu\{r_A>n\}=2^{-(n+1)}$ for every $n\ge0$; the measures were computed exactly in rational arithmetic for $n\le24$ and agree with $2^{-(n+1)}$, and the sum $\sum_{n\ge0}\mu\{r_A>n\}=\sum_{n\ge0}2^{-(n+1)}=1$ reproduces Kac's formula. Numerically the midpoint-rule integral $\int_0^{1/2}r_A\,d\mu=1.000000000008$ and the induced mean return time $\int_Ar_A\,d\mu_A=2.000000000016$, in agreement with Kac's formula and with $1/\mu(A)=2$.

**Remark (the induced transfer operator).** The transfer operator of $T_A$ with respect to $\mu_A$ is the **inducing** of $\mathcal{P}_T$ to the subset $A$; its fixed point is the induced measure and its spectral gap is the one that controls the decay of correlations of the induced system, which is the technique by which the statistical properties of a slow system are reduced to those of a uniformly expanding induced one. The induction is due to **Jakobson** and to **Bowen**, and its operator form is the **inducing operator** of the Ruelle–Perron–Frobenius theory.

## The Linearised Poincaré Map and the Monodromy

**Definition.** Let $p$ be a periodic point of the flow of period $T$, let $\Sigma$ be a section through $p$, and let $P$ be the return map. The **linearised Poincaré map** at $p$ is the derivative $DP(p)$ acting on the tangent space $T_p\Sigma$; the **monodromy** of the variational equation of *The Evolution Operator* is $M=D_p\varphi_T$ on $T_pM$.

**Theorem (the two spectra agree off the flow direction).** The vector $X(p)$ is an eigenvector of the monodromy $M=D_p\varphi_T$ with eigenvalue $1$, and

$$
\det(\mu I-DP(p))=\frac{\det(\mu I-D_p\varphi_T)}{\mu-1} \quad \text{in the reduced sense},
$$

so the eigenvalues of $DP(p)$, counted with multiplicity, are the eigenvalues of $D_p\varphi_T$ other than the trivial eigenvalue $1$; these are the **Floquet multipliers** of the periodic orbit apart from $1$.

*Proof.* Differentiating the relation $P(q)=\varphi_{\tau(q)}(q)$ at $q=p$ and using $d\tau(X(p))=1$ from transversality, one finds that $DP(p)$ and $D_p\varphi_T$ differ by a rank-one operator whose image lies in the flow direction; the characteristic polynomials therefore differ by the factor $\mu-1$ attached to that direction, which is the displayed identity. The computation is that of the return map theorem of *Smooth Dynamical Systems* and of Floquet theory in *Ordinary Differential Equations*, and is cited rather than reproved.

**Corollary (stability and the reduction).** The periodic orbit is hyperbolic exactly when $DP(p)$ has no eigenvalue on the unit circle, and its stability and its rate of return to the orbit are read from $DP(p)$; the orbit's Floquet exponents are the logarithms of the multipliers divided by the period. The dictionary thus transfers the linear stability of a periodic orbit to the linear theory of the return map, which is the operator-theoretic content of the reduction of the flow to the section.

## Summary

The **Poincaré map** $P(q)=\varphi_{\tau(q)}(q)$ is the first return map to a transverse section $\Sigma$ of a flow, and a flow with a global section is the **suspension** of $(P,\tau)$ with the return time as roof; the existence and smoothness of $P$ and $\tau$ and the suspension equivalence are the Poincaré section theorem of *Smooth Dynamical Systems*. The **reduction** is operator-theoretic: an observable of the flow is a function on the suspension, the flow operator is the translation in the time coordinate, and a function $F$ is an eigenfunction $U_tF=e^{i\lambda t}F$ exactly when its restriction $g=F|_\Sigma$ solves the **cocycle equation** $g(Px)=e^{i\lambda\tau(x)}g(x)$; from this the spectrum of the flow is read from the return map, with the simple case $\tau\equiv\bar\tau$ reducing the flow to the product of $P$ and a rotation and the general case genuinely twisted. **Ergodicity, mixing and hyperbolicity** pass from $P$ to the suspension, and the entropy per unit time is $h_{\mu_\Sigma}(P)/\bar\tau$ by **Abramov's formula**. The transfer operator $\mathcal{P}_P$ has the induced measure as its fixed point, and the **induced transformation** $T_A$ on a subset has the **Kac formula** $\int_Ar_A\,d\mu=1$, $\int_Ar_A\,d\mu_A=1/\mu(A)$; for the doubling map with $A=[0,\tfrac12)$ the level sets satisfy $\mu\{r_A>n\}=2^{-(n+1)}$ exactly, and the induced mean return time is $2=1/\mu(A)$ (both verified). The **linearised Poincaré map** $DP(p)$ at a periodic point carries the nontrivial **Floquet multipliers** of the orbit, the trivial multiplier $1$ belonging to the flow direction $X(p)$; the monodromy $D_p\varphi_T$ of *The Evolution Operator* and $DP(p)$ have the same spectrum off that direction. The twisted transfer operator that solves the cocycle equation, and the involution that reverses a reversible return map, belong to the `- * Operator Theory` group of this category and are not used here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma$, $X$, $\varphi_t$ | Section, generating field, flow |
| $\tau(q)$, $P(q)$ | First return time; return map (Poincaré map) |
| $(P,\tau)$ suspension | Quotient $\Sigma\times[0,\infty)/((q,\tau(q))\sim(Pq,0))$ |
| $\mu_\Sigma$, $\bar\tau$ | Induced measure on the section; mean return time |
| $U_t$, $U_P$ | Flow operator; Koopman operator of the return map |
| $g(Px)=e^{i\lambda\tau(x)}g(x)$ | Cocycle equation for a flow eigenfunction |
| $r_A$, $T_A$ | First return time to $A$; induced transformation |
| $\int_Ar_A\,d\mu=1$ | Kac's formula |
| $DP(p)$, $D_p\varphi_T$ | Linearised Poincaré map; monodromy |
| $h_\mu(\varphi_1)=h_{\mu_\Sigma}(P)/\bar\tau$ | Abramov's formula |

## Further Reading

- Henri Poincaré, *Les méthodes nouvelles de la mécanique céleste*, Vol. I (Gauthier-Villars, 1892), for the return map and the cross-section method.
- John Guckenheimer and Philip Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields* (Springer, 1983), for the Poincaré section in examples and the reduction of a flow.
- Anatole Katok and Boris Hasselblatt, *Introduction to the Modern Theory of Dynamical Systems* (Cambridge University Press, 1995), for the suspension, the induced transformation and the Kac formula.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for Abramov's formula and the transfer of ergodicity and mixing.
- Marek Kac, "On the notion of recurrence in discrete stochastic processes", *Bulletin of the American Mathematical Society* 53 (1947), 1002–1010, for the return-time formula.
- Nikolai S. Krylov and Nikolai N. Bogolyubov, "La théorie générale de la mesure dans son application à l'étude des systèmes dynamiques de la mécanique non linéaire", *Annals of Mathematics* 38 (1937), 65–113, for the inducing method.
- Michael Rychlik, "Lorentz attractors and the abstract variational principle" and Mark Pollicott and Michiko Yuri, *Dynamical Systems and Ergodic Theory* (Cambridge University Press, 1998), for the induced transfer operator.
- Rufus Bowen, *Equilibrium States and the Ergodic Theory of Anosov Diffeomorphisms* (Springer, 1975), for the inducing and the induced operators along a section.

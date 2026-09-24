# __The Index Theorem and the Zero-Mode Count in Biquaternionic Form__

## Introduction

The Hopf fibration of the companion article *The Hopf Fibration and the Biquaternion Gauge Bundle* supplied the geometric home of the gauge field and two integers: the winding of a map from the three-sphere, which is the instanton number, and the Chern number of a circle bundle over the two-sphere, which is the magnetic charge. This article supplies the tool that turns those integers into a *count*. The Atiyah–Singer index theorem states that the difference between the number of positive-chirality and negative-chirality zero modes of a Dirac operator is a topological integral, and in the gauge-theoretic setting that integral is the same density whose integral gave the instanton charge in *Instantons and Solitons in Biquaternionic Form*. The charge that classifies the field and the number of fermion zero modes that the field supports are therefore one and the same number.

The framework enters through two facts that are genuinely its own and one that is not.

- **The operator is the framework's.** The Dirac operator in biquaternionic form is built from the biquaternionic gradient $\tilde\nabla=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$ and its coupling to the connection, and its square returns the d'Alembertian: the framework's spinor module carries it, and *The Dirac Equation in Biquaternionic Form* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action* fix it. The index is a property of that operator.
- **The counting is by the topological density, which the framework already has.** The index density is a total derivative whose integral is the instanton number, and the abelian form of the density is the framework's invariant $I_2=\mathbf E\cdot\mathbf B$. This was established in *Instantons and Solitons in Biquaternionic Form* and is not repeated here.
- **The trace is the matrix trace, and the framework's norm form does not supply it.** The non-abelian index density is $\mathrm{Tr}(F\wedge F)$ with the matrix trace on the gauge factor. The framework's quadratic invariant, the norm form $N(\tilde F)=\tilde F\bar{\tilde F}$, is a rank-two bilinear of a *single* algebra element and has no second slot in which to trace two gauge-algebra-valued objects. This is the same rank-two limitation recorded for the topological density, and it controls what the framework can and cannot express about the index.

The article states the index theorem as the standard result it is, derives the specialisations that the framework uses, and separates the two.

**Conventions.** We use those of *Conventions in the Biquaternion Universe* and of the companion gauge articles. The algebra is $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ with $e_k^2=-e_0$, $e_1e_2=e_3$, and central $i$. The material sector is $\mathbb M_-$ and the informational sector is $\mathbb M_+$. The compact gauge algebra is $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{e_1,e_2,e_3\}$ with generators $T_a=\tfrac12 e_a$, $[T_a,T_b]=\varepsilon_{abc}T_c$, $\mathrm{Tr}(T_aT_b)=-\tfrac12\delta_{ab}$ on the anti-Hermitian convention. The gauge connection and curvature are $\mathcal A_\mu\in\mathfrak{su}(2)$ and $F_{\mu\nu}=\partial_\mu\mathcal A_\nu-\partial_\nu\mathcal A_\mu+i\kappa[\mathcal A_\mu,\mathcal A_\nu]$, with $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$. The topological charge is $Q=\frac{1}{8\pi^2}\int_{\mathbb R^4}\mathrm{Tr}(F\wedge F)\in\mathbb Z$ and the matrix trace $\mathrm{Tr}$ is distinguished from the informational trace formula $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$. On the Euclidean slice the curvature is written without the explicit factor $i$ in the commutator, as in *Instantons and Solitons in Biquaternionic Form*.

- Companion article *The Dirac Equation in Biquaternionic Form*, for the operator whose index is taken.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the module and its chirality.
- Companion article *Instantons and Solitons in Biquaternionic Form*, for the topological background and its charge.
- Companion article *The Hopf Fibration and the Biquaternion Gauge Bundle*, for the abelian bundle and its charge.
- Companion article *The ADHM Construction and Biquaternion Instanton Data*, for the moduli whose dimension the adjoint index counts.

## The Dirac Operator and Its Index

On a four-manifold with a spin structure and a gauge bundle in a representation $R$ of the structure group, the twisted Dirac operator is

$$
\slashed{D}_R \;=\; \gamma^\mu D_\mu ,
\qquad
D_\mu=\partial_\mu+i\kappa\,\mathcal A_\mu^{R} ,
$$

with $\gamma^\mu$ the Clifford generators, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$, and the connection acting in the representation $R$. The operator is elliptic, and its kernel splits under the chirality grading $\gamma_5$ into the positive and negative chirality zero-mode spaces,

$$
\ker\slashed{D}_R \;=\; \ker^+\!\slashed{D}_R \oplus \ker^-\!\slashed{D}_R ,
\qquad
n_\pm=\dim\ker^\pm\!\slashed{D}_R .
$$

The **index** is the difference

$$
\mathrm{ind}\,\slashed{D}_R \;=\; n_+ - n_- ,
$$

an integer that is invariant under continuous deformations of the connection and the metric because it is an integer-valued continuous function. In the biquaternionic framework the operator is the one built from $\tilde\nabla$; the algebraic form of the massless Dirac equation is $\tilde\nabla\psi=0$, and *The Dirac Equation in Biquaternionic Form* shows that $\tilde\nabla\bar{\tilde\nabla}=\bar{\tilde\nabla}\tilde\nabla=\Box$ with $\Box=\partial_{ict}^2+\Delta$, so the operator is the square root of the framework's d'Alembertian. The index is the property of this operator that the rest of the article computes.

## The Atiyah–Singer Theorem

For a closed even-dimensional spin manifold $M$ and a twisted Dirac operator, the index is the integral of a characteristic class,

$$
\mathrm{ind}\,\slashed{D}_R \;=\; \int_M \mathrm{ch}(E_R)\wedge \hat A(TM) ,
$$

where $\mathrm{ch}(E_R)$ is the Chern character of the twisted bundle and $\hat A(TM)$ is the $\hat A$-genus of the tangent bundle. This is the Atiyah–Singer index theorem; it is standard and is transcribed here, not derived. Its power in the gauge-theoretic setting is that the right-hand side is purely topological: it depends on the bundle data and not on the shape of the connection.

On the flat four-dimensional slice that the framework uses, the tangent bundle is trivial and its $\hat A$-genus is $1$ to all orders that contribute: $\hat A=1-\frac{p_1}{24}+\cdots$ requires the Pontryagin class of a curved manifold, which is absent. The index is therefore the degree-four part of the Chern character alone. With the trace in the representation $R$ and the standard normalisation, the degree-four part is proportional to $\mathrm{Tr}_R(F\wedge F)$, so that

$$
\mathrm{ind}\,\slashed{D}_R \;=\; \frac{1}{8\pi^2}\int_{\mathbb R^4}\mathrm{Tr}_R\bigl(F\wedge F\bigr)
\;=\; 2\,T(R)\,Q ,
$$

where $T(R)$ is the Dynkin index of the representation, normalised so that the defining representation of $SU(2)$ has $T=\tfrac12$, and $Q$ is the integer topological charge of the companion article. The two statements to read from this formula are that the index is proportional to the topological charge, and that its constant of proportionality is a representation-theoretic number.

**The Dynkin index.** For $SU(2)$ the two representations that occur inside the framework are the defining module of dimension two and the adjoint representation of dimension three, and their indices are fixed by the Casimir relation $T(R)=\dim R\,C_2(R)/\dim G$ with $\dim G=3$:

$$
T(\text{defining})=\frac{2\cdot\tfrac34}{3}=\frac12 ,
\qquad
T(\text{adjoint})=\frac{3\cdot 2}{3}=2 .
$$

Both are computed from the same commutation relations $[T_a,T_b]=\varepsilon_{abc}T_c$ that define $\mathfrak{su}(2)\subset\mathbb M_-$ in *Non-Abelian Gauge Fields in Biquaternionic Form*, so the group theory here is the framework's group theory. The index formula then reads

$$
\mathrm{ind}\,\slashed{D}_{\text{defining}}=Q ,
\qquad
\mathrm{ind}\,\slashed{D}_{\text{adjoint}}=4Q .
$$

For a self-dual configuration of charge $Q=k>0$, the index is exhausted by positive-chirality modes, $n_+=k$ and $n_-=0$ in the defining representation, and $n_+=4k$ and $n_-=0$ in the adjoint. A single BPST instanton therefore supports one fermion zero mode in the doublet and four in the triplet.

**The abelian specialisation.** For the Hopf bundle over the two-sphere, the same theorem reduces to the two-dimensional statement

$$
\mathrm{ind}\,\slashed{D}_n \;=\; \frac{1}{2\pi}\int_{S^2}F \;=\; n ,
$$

the Chern number of the bundle, which the previous article computed to be one for the minimal monopole. The number of zero modes of the Dirac operator coupled to a monopole of charge $n$ is $|n|$, with the sign of $n$ giving the chirality. The two-sphere case is the simplest instance of the same counting: index equals topological charge, and the charge is a winding number of the algebra's group.

**Boundary corrections.** On a manifold with boundary the index acquires a boundary contribution, and the theorem is replaced by the Atiyah–Patodi–Singer form

$$
\mathrm{ind}\,\slashed{D}_R \;=\; \int_M \mathrm{ch}(E_R)\wedge\hat A(TM) - \frac{h+\eta(0)}{2},
$$

where $h$ is the dimension of the space of boundary zero modes and $\eta(0)$ is the eta invariant of the boundary Dirac operator. The correction is a boundary term, and it is the reason a background with a nontrivial boundary can support zero modes whose count is not given by the bulk integral alone. The framework's instanton boundary is the three-sphere of *The Hopf Fibration and the Biquaternion Gauge Bundle*, and the eta invariant is a spectral invariant of the operator restricted to that boundary; its evaluation is a standard analytic computation and is not an algebraic statement about $\mathbb B$.

## The Density, the Charge, and the Total Derivative

The index is computed by the density $\mathrm{Tr}(F\wedge F)$, and the reason it is topological is that this density is a total derivative. The companion article established the chain

$$
\mathrm{Tr}\bigl(F\wedge F\bigr)=d\,\Omega_{\mathrm{CS}} ,
\qquad
\Omega_{\mathrm{CS}}=\mathrm{Tr}\Bigl(\mathcal A\wedge d\mathcal A+\tfrac23\,i\kappa\,\mathcal A\wedge\mathcal A\wedge\mathcal A\Bigr),
$$

so that

$$
Q=\frac{1}{8\pi^2}\oint_{\partial\mathbb R^4}\Omega_{\mathrm{CS}} ,
$$

a surface integral over the three-sphere at infinity. The index theorem's integral and the instanton's charge are therefore the same integral, computed in two ways: as the integral of the index density over the bulk, and as the Chern–Simons flux through the boundary. In the abelian case the density collapses to the framework's second invariant,

$$
\tfrac14\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=\tfrac12\,F_{\mu\nu}\star F^{\mu\nu}
=\frac{2i}{c}\,I_2 \quad(\text{Lorentzian}),
\qquad
\tfrac14\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=2\,I_2 \quad(\text{Euclidean}),
\qquad
I_2=\mathbf E\cdot\mathbf B ,
$$

<!-- CONVENTION — abelian density normalisation: $\tfrac14\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=\tfrac12 F\star F=\frac{2i}{c}I_2$ (Lorentzian), $=2I_2$ (Euclidean), following *Instantons and Solitons in Biquaternionic Form*, whose symbolic recomputation from the component matrix of the field-strength article fixes this normalisation. The identity $\tfrac14\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=\tfrac12 F_{\mu\nu}\star F^{\mu\nu}$ is why the quarter-density carries *half* the coefficient of $F_{\mu\nu}\tilde F^{\mu\nu}=\frac{4i}{c}I_2$; the two coefficients are not to be "aligned". -->

so the abelian index density is the framework's own invariant $I_2$ up to a constant. This is the affirmative half of the story: for the abelian sector the index and the charge are written in the invariant calculus the framework already possesses.

## A Worked Case: the Abelian Index and the Monopole Zero Modes

The index formula is worth exercising in the framework's abelian sector, where every ingredient is the algebra's. Take the two-sphere with a $U(1)$ gauge field whose first Chern number is $n$; the associated line bundle has $c_1=n$, and the Hopf bundle of *The Hopf Fibration and the Biquaternion Gauge Bundle* is the case $n=1$. The twisted Dirac index is

$$
\mathrm{ind}\,\slashed{D}_n=\int_{S^2}\mathrm{ch}(L)\wedge\hat A(TS^2)=\int_{S^2}c_1(L)=n ,
$$

since the $\hat A$-genus of a two-manifold is $1$. The count of zero modes is therefore $|n|$, with the sign of $n$ selecting the chirality, and for $n=1$ there is exactly one zero mode. This is the standard result that a magnetic monopole binds one fermion mode per unit magnetic charge, and it is the abelian counterpart of the $n_+=k$ count in the defining representation.

The zero modes can be exhibited explicitly, and they are the framework's monopole harmonics. In the $U(1)$ patch with $a=\tfrac12(1-\cos\theta)d\phi$ of the Hopf article, the massless two-component equation $\slashed{D}\psi=0$ separates, and the positive-chirality solutions are the sections

$$
\psi_n^{(m)}=f_n^{(m)}(\theta)\,e^{im\phi},
\qquad
m=0,1,\dots,n-1 ,
$$

in the case $n>0$, whose covariant constancy follows from the curvature being proportional to the area form. There are exactly $n$ of them, matching the index, and for $n=1$ the single mode is the constant section allowed in the patch where the connection is regular. The counting is standard — it is the degeneracy of the lowest Landau level of a charge-$n$ particle on the sphere — and the framework's contribution is the identification of the bundle and its connection with the Hopf data already computed. The key structural point is that the abelian index is written entirely in the framework's own objects: the bundle is the Hopf bundle, the charge is $c_1$, and the field is the charged biquaternionic spinor.

## The Index and the Instanton Moduli: $4k$ Adjoint Modes

The index of the adjoint Dirac operator has a second reading that ties this article to the instanton data. For a self-dual background of charge $k$ in the adjoint representation,

$$
n_+=4k ,
\qquad
n_-=0 ,
$$

and the moduli space of the background has dimension $8k$, twice this number. The relation is not a coincidence. The instanton moduli are the collective coordinates, and the adjoint zero modes are the fermionic partners of those coordinates in the supersymmetric quantum mechanics whose ground states are the instanton states: each bosonic collective coordinate of the ADHM moduli space of *The ADHM Construction and Biquaternion Instanton Data* is paired with a fermionic zero mode, so the $8k$ bosonic coordinates of the framed moduli space correspond to $4k$ adjoint zero modes counted with one chirality and to the doubled count in the full Dirac spectrum. The index

$$
\mathrm{ind}\,\slashed{D}_{\text{adjoint}}=4k=\tfrac12\dim_{\mathbb R}\mathcal M_k
$$

is the precise form of this statement for $SU(2)$.

Three consequences follow and are used in the later articles. First, the fermionic zero modes are the tangent directions of the moduli space; integrating over the moduli in the semiclassical expansion of *The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form* is integrating over the bosonic collective coordinates, and the fermionic modes are saturated by the measure. Second, the number of zero modes is a topological invariant and therefore cannot be changed by deforming the background within its charge sector. Third, the factor two between the adjoint index and the moduli dimension is the same factor that makes the supersymmetric index of the instanton moduli space equal to the Euler characteristic of the instanton moduli; the relation is standard, and it is the bridge between the elliptic index theorem and the moduli counting of the ADHM construction.

## The Biquaternion Reading and the Rank-Two Limitation

The framework's contribution to the index theorem is not the theorem but the identification of its ingredients. The operator is $\tilde\nabla$ and its square is $\Box$; the module on which it acts is the defining module $S\cong\mathbb C^2$, the unique simple module of $\mathbb B\cong M_2(\mathbb C)$; the adjoint representation is the three-dimensional subspace $\mathfrak{su}(2)\subset\mathbb M_-$ that the algebra carries as its own commutator algebra; and the group theory that produces the Dynkin indices is read directly from the quaternion commutators $[e_a,e_b]=2\varepsilon_{abc}e_c$. The zero-mode counts $k$ and $4k$ are therefore a statement about the algebra's modules: the defining module gives one mode per unit charge, and the adjoint, being the algebra acting on itself, gives four.

What the framework does not supply is the *invariant* expression of the non-abelian index density. The density $\mathrm{Tr}(F\wedge F)$ requires the matrix trace over the gauge factor and the wedge of two algebra-valued two-forms, and the framework's norm form cannot produce it. The norm form pairs a single algebra element with its conjugate through the quaternion product and returns one scalar; it has one algebra slot. The index density needs two. This is the same rank-two limitation that the companion article found for the topological density and that the energy–momentum-tensor article found for the stress tensor: the framework's quadratic invariant is rank-two and single-slot, while the non-abelian index density is traced over a second algebra factor. The consequence is precise: the framework can write the index density in components with the matrix trace, and it can identify its integral as the topological charge, but the density is not an object of the norm-form invariant calculus. The zero-mode count is expressible; the invariant whose integral computes it, in the non-abelian case, is not one of the framework's invariants.

A second place where the count is imported is the fermion itself. The index theorem counts zero modes of a Dirac operator, and the operator presupposes a spinor field, a Clifford structure and the chirality grading; those are supplied by *The Spinor Module in Biquaternionic Form and Its Lorentz Action* and *Chiral Fermions in the Biquaternion Framework*, and the physical identification of the counted modes with fermionic states is standard quantum field theory. The relevant anomaly statement — that the divergence of the axial current is proportional to the same density — belongs to the spin-half programme of the corpus and is not derived here; the index theorem is its Euclidean, elliptic counterpart, and the two are related by the standard argument.

## Summary

The index of the biquaternionic Dirac operator is the difference $n_+-n_-$ of the numbers of positive- and negative-chirality zero modes, and the Atiyah–Singer theorem computes it as the integral of the index density $\mathrm{ch}(E)\wedge\hat A(TM)$. On the flat four-dimensional slice the $\hat A$-genus is trivial and the index is $2T(R)Q$, where $Q$ is the instanton charge of *Instantons and Solitons in Biquaternionic Form* and $T(R)$ is the Dynkin index. For the framework's two representations the indices are $T(\text{defining})=\tfrac12$ and $T(\text{adjoint})=2$, giving a single zero mode in the defining module and four in the adjoint for a unit self-dual instanton, $n_+=k$ and $n_+=4k$ respectively. The abelian specialisation on the two-sphere gives index equal to the monopole charge, which is the Chern number one of the Hopf bundle.

The index density is a total derivative whose integral equals the instanton charge, and in the abelian case it is the framework's invariant $I_2=\mathbf E\cdot\mathbf B$. The operator, its defining module, the adjoint representation and the group theory of the indices are all the algebra's; the theorem itself, the $\hat A$-genus, the boundary eta invariant and the identification of the counted modes with physical fermions are standard results transcribed. The one place where the framework is silent is the invariant form of the non-abelian density: it is computable in components with the matrix trace, but it is not an object of the norm-form invariant calculus, because that calculus is rank-two and single-slot while the density is traced over a second algebra factor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ | Biquaternion algebra, $\cong M_2(\mathbb C)$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Central scalar imaginary |
| $\mathbb M_+,\mathbb M_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\mathbb H_{\mathbb B}$ | Real-quaternion subspace |
| $\tilde\nabla=e_0\partial_{ict}+e_k\partial_k$ | Biquaternionic gradient; Dirac operator |
| $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial_{ict}^2+\Delta$ | d'Alembertian (series convention) |
| $\slashed{D}_R=\gamma^\mu D_\mu$ | Twisted Dirac operator in representation $R$ |
| $\gamma_5$ | Chirality grading; $\ker\slashed{D}_R=\ker^+\oplus\ker^-$ |
| $n_\pm$ | Dimensions of the positive/negative chirality zero-mode spaces |
| $\mathrm{ind}\,\slashed{D}_R=n_+-n_-$ | Index of the Dirac operator |
| $\mathrm{ch}(E_R)\wedge\hat A(TM)$ | Index density; $\hat A=1$ on the flat slice |
| $T(R)$ | Dynkin index; $T(\text{defining})=\tfrac12$, $T(\text{adjoint})=2$ |
| $R$ | Defining (dim 2) or adjoint (dim 3) representation of $\mathfrak{su}(2)$ |
| $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{e_1,e_2,e_3\}$ | Compact gauge algebra inside $\mathbb M_-$ |
| $T_a=\tfrac12 e_a$, $[T_a,T_b]=\varepsilon_{abc}T_c$ | Normalised generators |
| $\mathcal F=d\mathcal A+i\kappa\,\mathcal A\wedge\mathcal A$ | Field-strength two-form |
| $F_{\mu\nu}=\partial_\mu\mathcal A_\nu-\partial_\nu\mathcal A_\mu+i\kappa[\mathcal A_\mu,\mathcal A_\nu]$ | Its components; $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$ |
| $Q=\frac{1}{8\pi^2}\int\mathrm{Tr}(F\wedge F)$ | Topological (instanton) charge, $Q\in\mathbb Z$ |
| $\Omega_{\mathrm{CS}}$ | Chern–Simons three-form; $d\Omega_{\mathrm{CS}}=\mathrm{Tr}(F\wedge F)$ |
| $\eta(0)$, $h$ | Eta invariant and boundary zero-mode count (APS) |
| $I_2=\mathbf E\cdot\mathbf B$ | Framework's second invariant; index density in the abelian case |
| $N(\tilde F)=\tilde F\bar{\tilde F}$ | Norm form; rank-two, single-slot, does not supply $\mathrm{Tr}(F\wedge F)$ |

## Further Reading

- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I", *Annals of Mathematics* 87 (1968) 484–530, for the index theorem and the index density.
- Michael F. Atiyah, Vijay K. Patodi and Isadore M. Singer, "Spectral asymmetry and Riemannian geometry I", *Mathematical Proceedings of the Cambridge Philosophical Society* 77 (1975) 43–69, for the index theorem with boundary and the eta invariant.
- Michael F. Atiyah, Nigel J. Hitchin and Isadore M. Singer, "Self-duality in four-dimensional Riemannian geometry", *Proceedings of the Royal Society A* 362 (1978) 425–461, for the instanton zero modes and the dimension formula.
- Thomas Eguchi, Peter B. Gilkey and Andrew J. Hanson, "Gravitation, gauge theories and differential geometry", *Physics Reports* 66 (1980) 213–393, for the index density, the Chern character and the eta invariant in a physics setting.
- Arthur L. Besse, *Einstein Manifolds* (Springer, 1987), for the $\hat A$-genus and the differential-geometric background.
- Michael F. Atiyah, *Geometry of Yang–Mills Fields* (Accademia Nazionale dei Lincei, 1979), for the index theorem in the gauge-theoretic form used here.
- Roman Jackiw and Claudio Rebbi, "Solitons with fermion number $1/2$", *Physical Review D* 13 (1976) 3398–3409, for the fermion number of the instanton zero modes.
- Gerard 't Hooft, "Symmetry breaking through Bell–Jackiw anomalies", *Physical Review Letters* 37 (1976) 8–11, for the anomalous divergence and the zero-mode count.
- Mikio Nakahara, *Geometry, Topology and Physics* (CRC Press, 2nd ed. 2003), for the index theorem and the Chern–Weil construction in a form suited to the present notation.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the Chern character and the characteristic-class calculus used throughout.

# __Biquaternion Regular Functions__

## Introduction

This article studies **regular** (equivalently **monogenic**) biquaternion-valued functions. It follows the articles on biquaternion analysis, biquaternion integration, and biquaternion analysis on subspaces, and assumes the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, its four conjugations, its norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$, its Euclidean norm, and its zero divisors.

The decisive fact is that $\mathbb{B}$ is **not a division algebra**: it has nonzero elements with no inverse, the zero divisors, forming the null quadric $N(\tilde{Q}) = 0$. Every failure of the complex analogy on the full algebra and on the indefinite subspaces is traceable to this fact; on $\mathbb{H}_{\mathbb{B}}$ the remaining failures are those of dimension and non-commutativity, so a statement of regularity must specify both the operator with respect to which the function is regular and the domain on which it is defined. The treatment is purely mathematical and no physical interpretation is used. Throughout, $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$, the units are anti-commuting with

$$
e_0 = 1, \qquad e_1^2 = e_2^2 = e_3^2 = -e_0, \qquad e_1 e_2 = e_3, \quad e_2 e_3 = e_1, \quad e_3 e_1 = e_2,
$$

and $i$ is a central scalar imaginary. We write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$, $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$.

# Part I: The Variable, the Complex Structures, and the Operators

## 1. The Biquaternion Variable and Its Two Complex Structures

A **complex structure** on a real vector space is a real-linear map $J$ with $J^2 = -\mathrm{id}$. The biquaternion algebra carries a pair of commuting complex structures,

$$
J_i(\tilde{Q}) = i\tilde{Q}, \qquad J_1(\tilde{Q}) = e_1\tilde{Q}.
$$

Both square to $-\mathrm{id}$ and commute because $i$ is central; the same construction with $e_2$ or $e_3$ gives further ones, and every root of $-1$ in $\mathbb{B}$ defines one. The two named structures are the **coefficient complex structure** $J_i$, which complexifies the coefficients $Q_\mu$, and the **quaternionic complex structure** $J_1$, which complexifies the plane spanned by $e_0, e_1$.

The quaternionic structure turns that plane into a complex line with coordinate $z = q_0 + e_1 q_1$, and the complex combinations of $e_0, e_1$ form the commutative subalgebra

$$
\mathbb{C}[e_1] = \{a e_0 + b e_1 : a, b \in \mathbb{C}\} = \mathrm{span}_{\mathbb{R}}\{e_0, e_1, i e_0, i e_1\} \cong \mathbb{C} \times \mathbb{C},
$$

the largest commutative subalgebra in which $e_1$ is the imaginary unit; the coefficient structure similarly singles out $\mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$. These two structures give two inequivalent notions of holomorphy, distinguished in Section 3: no single complex structure reduces the four real variables to one. Finally, $\mathbb{B} \cong M_2(\mathbb{C})$, so the algebra is simple, its center is $\mathbb{C}_{\mathbb{B}}$, its norm form is the determinant, and its zero divisors are the nonzero singular matrices.

## 2. The Cauchy–Riemann Operator and Its Conjugate

On a four-dimensional real subspace $V \subset \mathbb{B}$ with complex coefficients $Q_0, \dots, Q_3$, the **biquaternionic gradient**, called here the **biquaternionic Cauchy–Riemann operator**, and its **quaternion conjugate** are

$$
\tilde{\nabla} = \sum_{\mu=0}^{3} e_\mu \frac{\partial}{\partial Q_\mu}, \qquad \bar{\tilde{\nabla}} = e_0 \frac{\partial}{\partial Q_0} - \sum_{k=1}^{3} e_k \frac{\partial}{\partial Q_k}.
$$

This is the **Cauchy–Riemann operator** of the biquaternion theory, classically the Dirac operator. The pair $(\tilde{\nabla}, \bar{\tilde{\nabla}})$ plays the role of $(\partial_{\bar{z}}, \partial_z)$ in one complex variable. On the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where all coefficients are real and the partials are ordinary real derivatives, $\tilde{\nabla}$ is the **Cauchy–Riemann operator** on $\mathbb{R}^4$. The units satisfy the Clifford relation $e_\mu \bar{e}_\nu + e_\nu \bar{e}_\mu = 2\delta_{\mu\nu} e_0$, so the cross terms cancel and

$$
\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \Box := \left(\partial^2_{Q_0} + \partial^2_{Q_1} + \partial^2_{Q_2} + \partial^2_{Q_3}\right) e_0.
$$

The **d'Alembertian** $\Box$ is scalar and acts component-wise. On $\mathbb{H}_{\mathbb{B}}$ it is the Euclidean Laplacian of signature $(4,0)$; on $\mathbb{M}_-$ it is $-\partial^2_{q'_0} + \Delta_{\mathbb{M}_-}$ of signature $(3,1)$; on $\mathbb{M}_+$ it is $\partial^2_{q_0} - \Delta_{\mathbb{M}_+}$ of signature $(1,3)$; these are coordinate expressions of one abstract operator, the factors of $-i$ being a change of coordinates. The second-order operator $\tilde{\nabla}^2 = \tilde{\nabla}\tilde{\nabla} = (\partial^2_{Q_0} - \Delta_Q)e_0 + 2\sum_k e_k \partial^2_{Q_0 Q_k}$ also appears, with $\tilde{\nabla}^2 = 2\partial_{Q_0}\tilde{\nabla} - \Box \neq \Box$; it must not be confused with $\Box$, the natural second-order operator. For a function depending only on $q_0, q_1$,

$$
\tilde{\nabla}\tilde{F} = 2\partial_{\bar{z}}\tilde{F}, \qquad \bar{\tilde{\nabla}}\tilde{F} = 2\partial_{z}\tilde{F}, \qquad \partial_{\bar{z}} = \tfrac{1}{2}(\partial_{q_0} + e_1\partial_{q_1}), \qquad \partial_{z} = \tfrac{1}{2}(\partial_{q_0} - e_1\partial_{q_1}).
$$

## 3. Regular Functions: Single-Plane versus Hypercomplex

**Definition (left-regular).** Let $\Omega$ be open in a four-dimensional real subspace $V \subset \mathbb{B}$, and let $\tilde{F} : \Omega \to \mathbb{B}$ be continuously differentiable. Then $\tilde{F}$ is **left-regular**, or **left-monogenic**, if $\tilde{\nabla}\tilde{F} = 0$ on $\Omega$. It is **right-regular** if $\tilde{F}\tilde{\nabla} := \sum_\mu \partial_\mu\tilde{F}\, e_\mu = 0$ on $\Omega$. The two differ by non-commutativity — the units act on the left in the first and on the right in the second — and are exchanged by quaternion conjugation together with the interchange of $\tilde{\nabla}$ and $\bar{\tilde{\nabla}}$ ($\tilde{\nabla}\tilde{F} = 0 \iff \bar{\tilde{F}}\,\bar{\tilde{\nabla}} = 0$); a function regular with respect to $\bar{\tilde{\nabla}}$ is **anti-regular**, the analogue of an anti-holomorphic function.

**Convention.** In this series **regular** without qualification means **left-regular**, $\tilde{\nabla}\tilde{F} = 0$. This is fixed by the analysis and integration articles and determines which operator is inverted: the operator being inverted is the **first-order** operator $\tilde{\nabla}$, whose fundamental solution is the Cauchy kernel. It is not $\Box$, and it is not $\tilde{\nabla}^2$; several second-order operators can be built from $\tilde{\nabla}$, and only one has the Cauchy kernel as its fundamental solution. The opposite convention, $\bar{\tilde{\nabla}}\tilde{F} = 0$, is also common in the literature and merely interchanges regular and anti-regular.

**Single-plane holomorphy.** Fix $z = q_0 + e_1 q_1$. A function independent of $q_2, q_3$ is holomorphic in $z$ in the classical sense precisely when $\tilde{\nabla}\tilde{F} = 2\partial_{\bar{z}}\tilde{F} = 0$. Hence every classical holomorphic function of $z$, extended by constancy in the orthogonal directions, is regular: the powers $z^n$, the inverse $(z - w)^{-1}$, and so on. Such functions use one complex structure and carry no information about $q_2, q_3$.

**Hypercomplex regularity.** The hypercomplex notion uses the full dependence on all four variables and the full Clifford structure. It is strictly larger than the single-plane class: the Cauchy kernel $\tilde{G} = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$ is regular on $\mathbb{H}_{\mathbb{B}} \setminus \{0\}$ and is not holomorphic in any single-plane variable. The two notions coincide only in two real dimensions, where the biquaternionic operator reduces to the classical Cauchy–Riemann operator in one complex variable.

## 4. The System of Regularity Equations

Writing $\tilde{F} = F_0 + \mathbf{F}$ with $\mathbf{F} = F_1 e_1 + F_2 e_2 + F_3 e_3$, the analysis article gives

$$
\tilde{\nabla}\tilde{F} = \left(\partial_{Q_0}F_0 - \mathrm{div}\,\mathbf{F}\right) + \left(\partial_{Q_0}\mathbf{F} + \mathrm{grad}\,F_0 + \mathrm{rot}\,\mathbf{F}\right),
$$

with $\mathrm{div}\,\mathbf{F} = \sum_k \partial_{Q_k}F_k$, $\mathrm{grad}\,F_0 = \sum_k (\partial_{Q_k}F_0)e_k$, and $\mathrm{rot}\,\mathbf{F} = \sum_{j,k,l}\epsilon_{jkl}(\partial_{Q_j}F_k)e_l$. Therefore $\tilde{F}$ is regular if and only if

$$
\partial_{Q_0}F_0 = \mathrm{div}\,\mathbf{F}, \qquad \partial_{Q_0}\mathbf{F} + \mathrm{grad}\,F_0 + \mathrm{rot}\,\mathbf{F} = 0.
$$

This is a **system of four equations** for the four coefficients, the biquaternionic **Cauchy–Riemann–Fueter system**. It is the precise sense in which regularity is expressed by a system of equations rather than by one complex equation, and it is the local expression of the regularity notion inherited from the Clifford algebra, coupling $F_0$ to $\mathbf{F}$ through $\mathrm{div}$, $\mathrm{grad}$, and $\mathrm{rot}$.

On $\mathbb{H}_{\mathbb{B}}$ the principal symbol $s(\xi) = \sum_\mu \xi_\mu e_\mu$ satisfies $s(\xi)\bar{s}(\xi) = |\xi|^2 e_0$, so the system is **elliptic** and its solutions are smooth (indeed real-analytic). On $\mathbb{M}_-$, with $s(\xi) = -i\xi_0 e_0 + \sum_k \xi_k e_k$, one finds

$$
s(\xi)\bar{s}(\xi) = \left(-\xi_0^2 + \xi_1^2 + \xi_2^2 + \xi_3^2\right)e_0,
$$

which vanishes when $\xi_0^2 = \xi_1^2 + \xi_2^2 + \xi_3^2$. Thus on the indefinite subspaces $\tilde{\nabla}$ is not elliptic; it is a Cauchy–Riemann-type operator factoring the wave operator, and the null cone is its characteristic set. The elliptic tools of the complex theory — the maximum principle, the mean value property, and Liouville's theorem — are therefore not available on $\mathbb{M}_\pm$.

## 5. Examples of Regular Functions

**Constants.** If $\tilde{F}(\tilde{Q}) = \tilde{C}$ is constant, then $\tilde{\nabla}\tilde{F} = 0$ on any subspace; the constants form an eight-real-dimensional space of regular functions.

**Powers of a single-plane variable.** On $\mathbb{H}_{\mathbb{B}}$, with $z = q_0 + e_1 q_1$, every $z^n$, $n \geq 0$, is regular, being holomorphic in $z$ and independent of $q_2, q_3$; for $n = 1$ directly, $\tilde{\nabla} z = e_0 \cdot e_0 + e_1 \cdot e_1 = e_0 - e_0 = 0$. The negative power $(z - w)^{-1}$ is regular away from $z = w$, and more generally every classical holomorphic function of $z$, extended by constancy in the orthogonal directions, is regular. These are the regular **linear** and power functions.

**The coordinate function is not regular.** On $\mathbb{H}_{\mathbb{B}}$, $\tilde{\nabla}\tilde{Q} = \sum_{\mu} e_\mu e_\mu = e_0 - 3e_0 = -2e_0 \neq 0$. So the identity function is not regular, in sharp contrast with the complex case, where $z$ is holomorphic; the regular object that replaces it is the Cauchy kernel of Section 7.

**The Cauchy kernel.** On $\mathbb{H}_{\mathbb{B}}$, $\tilde{G}(\tilde{Q}) = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$ satisfies $\tilde{\nabla}\tilde{G} = 0$ for $\tilde{Q} \neq 0$; it is the fundamental solution of $\tilde{\nabla}$ and is singular only at the origin, since $\mathbb{H}_{\mathbb{B}}$ has no zero divisors.

**Closure properties.** Regular functions are closed under addition, under right multiplication by constants, $\tilde{\nabla}(\tilde{F}\tilde{C}) = (\tilde{\nabla}\tilde{F})\tilde{C} = 0$, and under left multiplication by complex scalars, since $\lambda$ is central. Left multiplication by a **general** constant does not preserve regularity: on $\mathbb{H}_{\mathbb{B}}$, $\tilde{\nabla}(e_2 z) = e_0 e_2 + e_1 e_2 e_1 = e_2 + e_3 e_1 = 2e_2 \neq 0$. Thus the regular functions form a right $\mathbb{B}$-module under pointwise right multiplication by constants, but not a left module. Similarly $\tilde{\nabla}(cz) = c + e_1 c e_1 = 2(c_2 e_2 + c_3 e_3)$, so $cz$ is regular exactly when $c \in \mathbb{C}[e_1]$.

## 6. Harmonicity and the Factorization of the Laplacian

Since $\Box = \bar{\tilde{\nabla}}\tilde{\nabla}$, every left-regular function is harmonic: $\Box\tilde{F} = \bar{\tilde{\nabla}}(\tilde{\nabla}\tilde{F}) = 0$, that is, $(\sum_\mu \partial^2_{Q_\mu})\tilde{F} = 0$. On $\mathbb{H}_{\mathbb{B}}$ this is the ordinary Laplace equation for each coefficient $F_\nu$; on $\mathbb{M}_\pm$ it is the wave equation. The converse fails: $q_0$ on $\mathbb{H}_{\mathbb{B}}$ is harmonic but $\tilde{\nabla} q_0 = e_0 \neq 0$. The factorization is the analogue of $\partial_z \partial_{\bar{z}} = \tfrac{1}{4}\Delta$ in one complex variable, and it explains why the harmonic functions form a strictly larger class. Right-regular functions are likewise harmonic: if $\tilde{F}\tilde{\nabla} = 0$, then

$$
0 = \left(\tilde{F}\tilde{\nabla}\right)\bar{\tilde{\nabla}} = \sum_{\mu,\nu} \partial^2_{Q_\mu Q_\nu}\tilde{F}\, e_\mu \bar{e}_\nu = \sum_{\mu=0}^{3} \partial^2_{Q_\mu}\tilde{F} = \Box\tilde{F},
$$

the mixed terms cancelling by the Clifford relation. Every regular function also satisfies $\tilde{\nabla}^2\tilde{F} = 0$, but $\tilde{\nabla}^2$ is not the natural second-order operator.

# Part II: Integral Representation and Its Limits

## 7. The Cauchy Integral Formula Where It Holds

The integral theory is developed on $\mathbb{H}_{\mathbb{B}}$, where it is the standard Clifford analysis of $\mathbb{R}^4$ and is complete because $\mathbb{H}_{\mathbb{B}}$ is a division algebra. The following results are established in the integration article.

**Theorem (fundamental solution).** On $\mathbb{H}_{\mathbb{B}}$, the function $\tilde{G}(\tilde{Q}) = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$ satisfies $\tilde{\nabla}\tilde{G} = 0$ for $\tilde{Q} \neq 0$ and, in the sense of distributions, $\tilde{\nabla}\tilde{G} = -2\pi^2 \delta_0\, e_0$.

**Theorem (Cauchy integral formula).** Let $\tilde{F}$ be continuously differentiable on a domain $\Omega \subset \mathbb{H}_{\mathbb{B}}$ with piecewise smooth boundary $\partial\Omega$, and let $\tilde{Q}_0$ be an interior point. Then

$$
\tilde{F}(\tilde{Q}_0) = \frac{1}{2\pi^2}\int_{\partial\Omega}\tilde{G}(\tilde{Q} - \tilde{Q}_0)\tilde{n}\tilde{F}(\tilde{Q})\,dS - \frac{1}{2\pi^2}\int_{\Omega}\tilde{G}(\tilde{Q} - \tilde{Q}_0)(\tilde{\nabla}\tilde{F})(\tilde{Q})\,dV,
$$

where $\tilde{n}$ is the biquaternion-valued outward unit normal. If $\tilde{F}$ is regular, the volume term vanishes and

$$
\tilde{F}(\tilde{Q}_0) = \frac{1}{2\pi^2}\int_{\partial\Omega}\tilde{G}(\tilde{Q} - \tilde{Q}_0)\tilde{n}\tilde{F}(\tilde{Q})\,dS.
$$

Three hypotheses must be emphasized: the formula holds on the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, where all four coefficients of $\tilde{Q}$ are real, and is **not** asserted on $\mathbb{M}_-$ or $\mathbb{M}_+$ or on the full algebra $\mathbb{B}$ (Section 8); regularity is required on all of $\Omega$, not merely on the boundary; and the operator inverted is the first-order operator $\tilde{\nabla}$, normalized by $\tilde{\nabla}\tilde{G} = -2\pi^2\delta_0 e_0$. The mean value property, the maximum principle, Liouville's theorem, the identity theorem, the Cauchy estimates, and the residue theory for isolated singularities then follow, as in the integration article, on $\mathbb{H}_{\mathbb{B}}$ only.

## 8. Where the Complex Analogy Fails: Zero Divisors and the Null Cone

The complex theory rests on $\mathbb{C}$ being a field. In the biquaternion algebra this fails, and every consequence below is traceable to the zero divisors.

Since $\mathbb{B} \cong M_2(\mathbb{C})$, the zero divisors are exactly the nonzero elements with $N(\tilde{Q}) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$. The zero divisor set $\mathcal{Z}$ is a complex cone of complex dimension $3$ (real dimension $6$); on the indefinite subspaces it cuts out the double cones $(q'_0)^2 = q_1^2 + q_2^2 + q_3^2$ in $\mathbb{M}_-$ and $q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2$ in $\mathbb{M}_+$, each three-dimensional with apex at the origin; in $\mathrm{Vect}(\mathbb{B})$ the norm form is complex and vanishes on the nilpotent cone, of real dimension $4$; while on $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ the norm form is definite and there are none. On the null cone there is no inverse, so no quotient $\tilde{A}/\tilde{Q}$ is defined, and the naive difference quotient of the analysis article requires $\tilde{H}^{-1}$, which may not exist.

The proof that $\tilde{\nabla}\tilde{G} = 0$ uses $\bar{\tilde{Q}}\tilde{Q} = \|\tilde{Q}\|_E^2 e_0$, which requires real coefficients; on $\mathbb{M}_\pm$ this identity fails, so $\tilde{G}$ is not a fundamental solution and no Cauchy formula of the stated form holds, and whether a modified kernel exists is open (integration article). By Section 4 the principal symbol degenerates on the null cone on $\mathbb{M}_\pm$, so the system is not elliptic and the maximum principle, the mean value property, and Liouville's theorem do not generalize; a regular function there, if defined, solves a hyperbolic rather than an elliptic system. The natural singular set is the six-real-dimensional null quadric, not a point, so there is no punctured-disk model and the residue theory of the integration article is correspondingly delicate.

On the indefinite subspaces the null cone is thus simultaneously the zero divisor set, the characteristic set of $\tilde{\nabla}$, and the set where the Cauchy kernel ceases to be a fundamental solution. A theorem about regular functions must therefore either restrict to a domain avoiding the cone — or, better, to a subspace such as $\mathbb{H}_{\mathbb{B}}$ — or state explicitly which weakened conclusion replaces the classical one. No Cauchy formula may be asserted beyond the quaternion subspace.

## 9. The Naive Inverse Function and the Role of the Null Cone

The naive transcription of $1/(z - w)$ is $\tilde{F}(\tilde{Q}) = \tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$, defined exactly on the group of units, that is, off the null quadric with the origin removed; it does not exist on the null cone. Its singular set is six-dimensional, not isolated, so there is no Laurent expansion about an isolated pole.

On $\mathbb{H}_{\mathbb{B}}$, where $N(\tilde{Q}) = \|\tilde{Q}\|_E^2$ is real and positive definite, the inverse exists for all $\tilde{Q} \neq 0$, but it is **not regular**: a direct computation gives

$$
\tilde{\nabla}\left(\frac{\bar{\tilde{Q}}}{\|\tilde{Q}\|_E^2}\right) = \frac{4e_0}{\|\tilde{Q}\|_E^2} - \frac{2e_0}{\|\tilde{Q}\|_E^2} = \frac{2e_0}{\|\tilde{Q}\|_E^2} \neq 0.
$$

The genuine regular radial function is the Cauchy kernel $\tilde{G} = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$. In four variables the fundamental solution of $\tilde{\nabla}$ has homogeneity $1 - 4 = -3$, and the exponent $4$ is exactly this homogeneity; the naive inverse carries the two-dimensional exponent and is the fundamental solution of the Cauchy–Riemann operator only in the complex plane. The single-plane inverse $(z - w)^{-1}$ is regular, so this failure is a genuinely hypercomplex phenomenon — the change of dimension from two to four — not merely a consequence of non-commutativity. The null cone thus enters in two ways: on the full algebra it makes the inverse undefined on a positive-dimensional set, and on $\mathbb{H}_{\mathbb{B}}$, where the cone is absent, the naive inverse is still the wrong function, the correct kernel being selected by the homogeneity required in four variables.

## 10. Relation to Fueter and Quaternionic Theories

Restricting to real quaternion-valued functions on $\mathbb{H}_{\mathbb{B}}$ recovers Fueter's quaternionic analysis: $\tilde{\nabla}$ is the Cauchy–Riemann operator $D$, the equation $DF = 0$ is the Cauchy–Riemann–Fueter equation, and the Cauchy formula, mean value property, maximum principle, Liouville theorem, identity theorem, Taylor and Laurent expansions, and residue theorem all hold (quaternion analysis article). Since $\mathbb{H}$ is a division algebra, this case has no zero divisors and is a complete analogue of the complex theory in the sense appropriate to four real variables; the biquaternion theory is its complexification, the variable remaining quaternionic in structure while the coefficients become complex.

The general framework is Clifford analysis. Since $\mathbb{B} \cong \mathrm{Cl}_{1,3}^{+} \cong M_2(\mathbb{C})$, the regular functions of this article are the monogenic functions of the even Clifford algebra in four dimensions; relative to the quaternionic case, the additional structure is the complex coefficients, the four conjugations, the two complex structures, and the zero divisors. The bridge between the single-plane and hypercomplex notions is the **Fueter–Sce construction**: a slice-regular function is generally not monogenic, but applying the appropriate power of the Laplacian to a slice-regular function produces a monogenic one. Due to Fueter and completed by Sce, this is the precise mechanism converting holomorphic data of a single complex variable into regular functions of four real variables; it is treated in the companion article on Fueter theory for biquaternions.

## Summary

Regularity for biquaternion-valued functions must specify both the operator and the domain. A function is **left-regular** (left-monogenic) if $\tilde{\nabla}\tilde{F} = 0$ and right-regular if $\tilde{F}\tilde{\nabla} = 0$, where $\tilde{\nabla} = \sum_\mu e_\mu \partial_{Q_\mu}$ is the biquaternionic Cauchy–Riemann operator; the two notions are exchanged by quaternion conjugation, and a function regular for $\bar{\tilde{\nabla}}$ is anti-regular, the analogue of an anti-holomorphic function. In this series regular unqualified means left-regular for the first-order operator $\tilde{\nabla}$, the operator whose fundamental solution is the Cauchy kernel; it is not $\Box$ and not $\tilde{\nabla}^2$.

Two notions of regularity must be kept apart. **Single-plane holomorphy** takes one complex variable $z = q_0 + e_1 q_1$, with $q_2, q_3$ entering only as parameters; every classical holomorphic function, extended by constancy in the orthogonal directions, is regular. **Hypercomplex regularity** uses the full dependence on all four variables and the full Clifford structure, is strictly larger, and contains the Cauchy kernel $\tilde{G} = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$, which is regular on $\mathbb{H}_{\mathbb{B}}\setminus\{0\}$ and holomorphic in no single-plane variable. Since $\Box = \bar{\tilde{\nabla}}\tilde{\nabla}$ is scalar, every regular function is harmonic, but the converse fails, and $\tilde{\nabla}^2$ annihilates regular functions without being the natural second-order operator.

The integral theory is complete on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where the algebra is a division ring: the Cauchy integral formula holds there with fundamental solution $\tilde{\nabla}\tilde{G} = -2\pi^2\delta_0 e_0$, and the mean value property, maximum principle, Liouville theorem, identity theorem, Cauchy estimates and residue theory follow. Everything that fails elsewhere fails through the zero divisors: on $\mathbb{M}_\pm$ and on the full algebra the identity $\bar{\tilde{Q}}\tilde{Q} = \|\tilde{Q}\|_E^2 e_0$ fails, the principal symbol degenerates on the null cone, the system is hyperbolic rather than elliptic, and no Cauchy formula may be asserted. The naive inverse $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ fails in two ways: on the full algebra it is undefined on the positive-dimensional null cone, and even on $\mathbb{H}_{\mathbb{B}}$, where it exists, it is not regular, the correct kernel in four variables being fixed by the homogeneity $1 - 4 = -3$ rather than the two-dimensional exponent.

Restricting to real quaternion-valued functions recovers Fueter's quaternionic analysis, where the analogous theory is complete because $\mathbb{H}$ is a division algebra, and the general framework is Clifford analysis on $\mathrm{Cl}_{1,3}^{+}$; the Fueter–Sce construction converts slice-regular data of one complex variable into monogenic functions of four real variables.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra, $\cong \mathrm{Cl}_{1,3}^{+} \cong M_2(\mathbb{C})$ |
| $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ | Biquaternion variable; $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ |
| $\tilde{\nabla} = \sum_\mu e_\mu \partial_{Q_\mu}$ | Biquaternionic Cauchy–Riemann operator |
| $\bar{\tilde{\nabla}} = e_0\partial_{Q_0} - \sum_k e_k\partial_{Q_k}$ | Quaternion conjugate operator; $(\tilde{\nabla}, \bar{\tilde{\nabla}})$ mirrors $(\partial_{\bar z}, \partial_z)$ |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$ | Scalar d'Alembertian, the sum of the four second derivatives |
| $\tilde{F}$ left-regular (left-monogenic) | $\tilde{\nabla}\tilde{F} = 0$ on a domain $\Omega$ |
| $\tilde{F}$ anti-regular | $\bar{\tilde{\nabla}}\tilde{F} = 0$ |
| $\tilde{G} = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$ | Cauchy kernel, fundamental solution of $\tilde{\nabla}$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form; the zero divisors are the nonzero elements with $N = 0$ |
| $\|\tilde{Q}\|_E$ | Euclidean norm on $\mathbb{B} \cong \mathbb{R}^8$ |
| $\mathcal{Z}$ | Zero divisor set, a complex cone of real dimension $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, a division ring; the domain of the integral theory |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853).
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* (1873).
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330.
- A. Sudbery, "Quaternionic analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979) 199–225.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, London, 1982).
- R. Delanghe, F. Sommen, and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, Dordrecht, 1992).
- G. Gentili, C. Stoppato, and D. C. Struppa, *Regular Functions of a Quaternionic Variable* (Springer, 2013).

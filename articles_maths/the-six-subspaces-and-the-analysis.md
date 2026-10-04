# __The Six Subspaces and the Analysis__

## Introduction

*Biquaternion Analysis* defines the gradient $\tilde\nabla = \sum_\mu e_\mu\,\partial/\partial Q_\mu$ and its second-order companion

$$
\Box = \tilde\nabla\tilde\nabla^{\natural} = \tilde\nabla^{\natural}\tilde\nabla = e_0\left(\frac{\partial^2}{\partial Q_0^2} + \Delta_Q\right),
$$

and studies them on a four-dimensional subspace; *Biquaternion Integration* carries the integral theory. This article reads both against the six distinguished subspaces and asks what analysis each one carries. Two questions decide everything: **which variables** a function on the subspace depends on, and **which operator** the algebra provides there.

The six fall into two classes.

**The two complex subspaces.** The centre $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ and the vector subspace $\mathrm{Vect}(\mathbb{B}) = \mathbb{C}e_1 \oplus \mathbb{C}e_2 \oplus \mathbb{C}e_3$ are stable under multiplication by the central $i$: they are complex vector spaces, of complex dimension $1$ and $3$. Their coefficients are genuinely complex, so the analysis on them is **complex analysis**, in one and in three complex variables.

**The four real forms.** The quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ and the two Hermitian subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ are of real dimension four and are **not** stable under $i$; instead $i$ interchanges $\mathbb{H}_{\mathbb{B}}$ with $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$ with $\mathbb{M}_-$. On each of them every complex coefficient $Q_\mu$ is real or purely imaginary, the partial derivative $\partial/\partial Q_\mu$ is an ordinary real derivative on a real coefficient and $-i$ times one on a purely imaginary coefficient, and the analysis is the real-variable analysis of *Biquaternion Analysis*, in one of four signatures.

The table gives the result. The null set is the set of $\tilde{Q}$ in the subspace with $N(\tilde{Q}) = 0$; the second-order operator is $\Box$ restricted to the subspace.

| subspace | $\dim_{\mathbb{R}}$ | variables | gradient | second-order operator | null set |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $Q_0$ | $e_0\,\partial_{Q_0}$ | $e_0\,\partial_{Q_0}^2$ | $\{0\}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $Q_1, Q_2, Q_3$ | $\sum_k e_k\,\partial_{Q_k}$ | $e_0\sum_k\partial_{Q_k}^2$ | $\sum_k Q_k^2 = 0$ |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $q_0, q_1, q_2, q_3$ | $\sum_\mu e_\mu\,\partial_{q_\mu}$ | $e_0\,\Delta_4$ | $\{0\}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $q'_0, q'_1, q'_2, q'_3$ | $-i\sum_\mu e_\mu\,\partial_{q'_\mu}$ | $-e_0\,\Delta_4$ | $\{0\}$ |
| $\mathbb{M}_+$ | $4$ | $q_0;\ q'_1, q'_2, q'_3$ | $e_0\partial_{q_0} - i\sum_k e_k\partial_{q'_k}$ | $e_0\left(\frac{\partial^2}{\partial q_0^2} - \sum_k\frac{\partial^2}{\partial (q'_k)^2}\right)$ | $q_0^2 = \sum_k (q'_k)^2$ |
| $\mathbb{M}_-$ | $4$ | $q'_0;\ q_1, q_2, q_3$ | $-ie_0\partial_{q'_0} + \sum_k e_k\partial_{q_k}$ | $e_0\left(-\frac{\partial^2}{\partial (q'_0)^2} + \sum_k\frac{\partial^2}{\partial q_k^2}\right)$ | $(q'_0)^2 = \sum_k q_k^2$ |

Two statements organise the table, and both are proved in §*The Second-Order Operator and the Norm*.

**The second-order operator is the operator of the norm.** On each of the four real forms the restriction of $\Box$ is $e_0$ times the differential operator obtained from the quadratic form $N$; the principal symbol of $\Box$ on the subspace is therefore $N$ itself, of signature $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$.

**The operator is elliptic exactly where there is no zero divisor.** $\Box$ is elliptic on the centre, on the quaternion subspace and on the anti-quaternion subspace — exactly the three of the six that contain no zero divisor — and non-elliptic on the vector subspace and on the two Hermitian subspaces, where the null cone is non-empty.

The treatment is purely mathematical. The elements are written $\tilde{Q}, \tilde{P}, \dots$, their complex coefficients $Q_0, Q_1, Q_2, Q_3$, and the real and imaginary parts of a coefficient $Q_\mu = q_\mu + i q'_\mu$.

## The Centre Subspace

**The variable.** The centre is $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$, isomorphic to $\mathbb{C}$, and an element is a single complex number $Q_0 = q_0 + i q'_0$.

**The operator.** On the centre the vector coordinates vanish identically, so $\partial/\partial Q_k = 0$ for $k = 1, 2, 3$ and the gradient is the single term

$$
\tilde\nabla\big|_{\mathbb{C}_{\mathbb{B}}} = e_0\,\frac{\partial}{\partial Q_0} .
$$

Because $Q_0$ is a genuine complex variable, $\partial/\partial Q_0$ is the complex derivative $\partial_z = \tfrac12(\partial_{q_0} - i\partial_{q'_0})$, and the Cauchy–Riemann operator is its conjugate $\partial_{\bar z} = \tfrac12(\partial_{q_0} + i\partial_{q'_0})$: a coefficient $F_\nu$ is holomorphic exactly when $\partial_{\bar z}F_\nu = 0$, and on holomorphic functions $\partial_{q'_0} = i\partial_{q_0}$. The second-order operator is the square of the complex derivative,

$$
\Box\big|_{\mathbb{C}_{\mathbb{B}}} = e_0\,\frac{\partial^2}{\partial Q_0^2} .
$$

It is not the Laplacian of the plane: the latter is $4\partial_{Q_0}\partial_{\bar Q_0} = \partial_{q_0}^2 + \partial_{q'_0}^2$, while the square of the complex derivative is the holomorphic operator $\partial_{Q_0}^2$.

**The analysis.** A biquaternion-valued function on the centre has four coefficients, each a function of the single variable $Q_0$, and the analysis on the centre is **the analysis of one complex variable**: the Cauchy–Riemann equations, the holomorphic and the anti-holomorphic classes, and the contour theory. The equations $\tilde\nabla\tilde{F} = 0$ reduce to $\partial F_\nu/\partial Q_0 = 0$, so that the regular functions are the functions of $\bar Q_0$ alone; with the conjugate convention, that is the holomorphic class. This is the only one of the six on which the "contour" of the integral theory is one-dimensional: a closed curve, not the three-dimensional boundary of the other five.

**The null set.** There is none. The norm is $N(Q_0e_0) = Q_0^2$, which vanishes only at $Q_0 = 0$, so the centre is a field and the analysis on it is free of the obstruction the zero divisors create elsewhere. It is worth recording that the real part of the norm on the centre is indefinite, of signature $(1,1)$: the freedom of the centre from zero divisors is the field property, not the positivity of a form.

## The Vector Subspace

**The variables.** An element is $Q_1e_1 + Q_2e_2 + Q_3e_3$ with three complex coefficients $Q_k = x_k + i y_k$; the vector subspace is $\mathbb{C}^3$ of complex dimension $3$, and of real dimension $6$.

**The operator.** On the vector subspace the scalar coordinate vanishes, so $\partial/\partial Q_0 = 0$ and the gradient has no scalar term at all:

$$
\tilde\nabla\big|_{\mathrm{Vect}(\mathbb{B})} = e_1\frac{\partial}{\partial Q_1} + e_2\frac{\partial}{\partial Q_2} + e_3\frac{\partial}{\partial Q_3} .
$$

The second-order operator is the **complex Laplacian** in three complex variables,

$$
\Box\big|_{\mathrm{Vect}(\mathbb{B})} = e_0\sum_{k=1}^{3}\frac{\partial^2}{\partial Q_k^2} .
$$

This is a sum of squares of complex derivatives and is not the Laplacian of $\mathbb{R}^6$; the real Laplacian in the six coordinates is $4\sum_k\partial_{Q_k}\partial_{\bar Q_k}$.

**The analysis.** The analysis on the vector subspace is complex analysis in three variables: the coefficients of $\tilde{F}$ are functions of $Q_1, Q_2, Q_3$, with the Wirtinger operators $\partial_{Q_k}$ and $\partial_{\bar Q_k}$ as the first-order operators, and the gradient of the subspace annihilates the functions of $\bar Q_1, \bar Q_2, \bar Q_3$ alone. The absence of the scalar term is the operator form of the vector subspace being the kernel of the scalar part.

**The null set.** The norm is $N(\tilde{Q}) = \sum_k Q_k^2$, whose vanishing set is the complex cone $\sum_k Q_k^2 = 0$. The cone is non-empty: $e_1 + ie_2$ lies on it, since $1^2 + i^2 = 0$. Its points are exactly the zero divisors of the subspace, the pure ones of *The Six Subspaces and the Zero Divisors*, and the analysis degenerates on them.

**The operator is not elliptic.** The principal symbol of $\Box$ on the vector subspace is $\tfrac14\sum_k(\xi_k - i\eta_k)^2$, and it vanishes at the null covectors of the cone: for $(\xi_1, \xi_2, \xi_3) = (1, 0, 0)$ and $(\eta_1, \eta_2, \eta_3) = (0, 1, 0)$ the sum is $1^2 + (-i)^2 = 0$. The same computation in one complex variable has no nonzero null covector, which is why the centre is the elliptic case among the two complex subspaces and the vector subspace is not.

## The Quaternion Subspace

**The variables.** All four coefficients are real, $Q_\mu = q_\mu$, and the quaternion subspace is $\mathbb{R}^4$.

**The operator.** The gradient is the Cauchy–Riemann–Fueter operator of *Biquaternion Analysis*,

$$
\tilde\nabla\big|_{\mathbb{H}_{\mathbb{B}}} = \sum_{\mu=0}^{3} e_\mu\,\frac{\partial}{\partial q_\mu},
$$

and the second-order operator is the Euclidean Laplacian in the four real coordinates,

$$
\Box\big|_{\mathbb{H}_{\mathbb{B}}} = e_0\left(\frac{\partial^2}{\partial q_0^2} + \frac{\partial^2}{\partial q_1^2} + \frac{\partial^2}{\partial q_2^2} + \frac{\partial^2}{\partial q_3^2}\right) = e_0\,\Delta_4 .
$$

Its principal symbol is $\sum_\mu\xi_\mu^2$, that is the norm $N$ restricted to the subspace, which is positive definite: the operator is **elliptic**.

**The analysis.** This is the case of *Biquaternion Analysis* and of *Biquaternion Integration* verbatim. The quaternion subspace is the one of the six on which the Cauchy integral formula, the mean value property, the maximum principle, Liouville's theorem, the identity theorem, the Cauchy estimates and the residue theory are all stated in the house articles, and the reason is the one that makes $\mathbb{H}_{\mathbb{B}}$ a division algebra: the norm is definite, hence there is no null element and no zero divisor, and the analysis meets no obstruction. The contour theory is the one of *Biquaternion Integration*, over a three-dimensional boundary, with the fundamental solutions $\tilde{G}(\tilde{Q}) = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ for the gradient and $G_\Box(\tilde{Q}) = -e_0/(4\pi^2\|\tilde{Q}\|_E^2)$ for the second-order operator.

## The Anti-Quaternion Subspace

**The variables.** All four coefficients are purely imaginary, $Q_\mu = i q'_\mu$, and the independent variables are the four real numbers $q'_\mu$.

**The operator.** Each partial derivative carries the factor $-i$, since $\partial/\partial Q_\mu = \partial/(i\partial q'_\mu) = -i\,\partial_{q'_\mu}$. Hence

$$
\tilde\nabla\big|_{i\mathbb{H}_{\mathbb{B}}} = -i\sum_{\mu=0}^{3} e_\mu\,\frac{\partial}{\partial q'_\mu},
\qquad
\Box\big|_{i\mathbb{H}_{\mathbb{B}}} = -e_0\,\Delta_4 .
$$

The principal symbol is $-\sum_\mu\xi_\mu^2$, that is $-N$ on the subspace, which is negative definite: the operator is **elliptic** as well.

**The analysis.** The substitution $\tilde{Q} = i\tilde{Q}'$ identifies $i\mathbb{H}_{\mathbb{B}}$ with $\mathbb{H}_{\mathbb{B}}$ and transports the whole analysis of the quaternion subspace to it, with two signs: the gradient is multiplied by $-i$ and the second-order operator by $-1$. Every statement of the quaternion case therefore has an anti-quaternion mirror, and the sign of the norm — positive definite on $\mathbb{H}_{\mathbb{B}}$, negative definite on $i\mathbb{H}_{\mathbb{B}}$ — is the only structural difference. There is no null element here either, and the contour theory is the one of the quaternion subspace carried by the substitution.

## The Hermitian Subspace

**The variables.** The scalar coefficient is real and the three spatial coefficients are purely imaginary: $Q_0 = q_0$, $Q_k = i q'_k$.

**The operator.** The scalar partial is an ordinary real derivative and the three spatial ones carry $-i$:

$$
\tilde\nabla\big|_{\mathbb{M}_+} = e_0\,\frac{\partial}{\partial q_0} - i\sum_{k=1}^{3} e_k\,\frac{\partial}{\partial q'_k},
\qquad
\Box\big|_{\mathbb{M}_+} = e_0\left(\frac{\partial^2}{\partial q_0^2} - \sum_{k=1}^{3}\frac{\partial^2}{\partial (q'_k)^2}\right).
$$

The principal symbol is $q_0^2 - \sum_k (q'_k)^2$, that is the norm $N$ on the subspace, of signature $(1,3)$: the second-order operator on the Hermitian subspace is the **wave operator** in the four real variables. It is not elliptic, and a null covector is $(\xi_0, \xi_1, \xi_2, \xi_3) = (1, 1, 0, 0)$.

**The null set.** The norm vanishes on the cone $q_0^2 = \sum_k (q'_k)^2$, of real dimension $3$, and its points are exactly the zero divisors of the subspace, the non-pure ones of *The Six Subspaces and the Zero Divisors*, namely the nonzero real multiples of the Hermitian idempotents.

**The analysis.** Because the operator is of wave type, the natural problem on the Hermitian subspace is an initial-value problem on a level surface of $q_0$, not the Dirichlet problem that the quaternion subspace carries; and the fundamental solution of the wave operator is a distribution supported on the null cone, so that the representation formula of *Biquaternion Integration* becomes its Kirchhoff–Green form. The Jordan algebra carried by the subspace, from *The Six Subspaces and the Jordan Algebra*, is the algebraic counterpart of this being the indefinite case.

## The Anti-Hermitian Subspace

**The variables.** The scalar coefficient is purely imaginary and the three spatial coefficients are real: $Q_0 = i q'_0$, $Q_k = q_k$.

**The operator.** The scalar partial carries $-i$ and the three spatial ones are ordinary real derivatives:

$$
\tilde\nabla\big|_{\mathbb{M}_-} = -i e_0\,\frac{\partial}{\partial q'_0} + \sum_{k=1}^{3} e_k\,\frac{\partial}{\partial q_k},
\qquad
\Box\big|_{\mathbb{M}_-} = e_0\left(-\frac{\partial^2}{\partial (q'_0)^2} + \sum_{k=1}^{3}\frac{\partial^2}{\partial q_k^2}\right).
$$

The principal symbol is $-(q'_0)^2 + \sum_k q_k^2$, that is the norm $N$ on the subspace, of signature $(3,1)$: again the **wave operator**, with the imaginary scalar coordinate in the distinguished position. It is not elliptic.

**The null set and the mirror.** The norm vanishes on the cone $(q'_0)^2 = \sum_k q_k^2$, of real dimension $3$, and its points are the zero divisors of the subspace, the nonzero purely imaginary multiples of the Hermitian idempotents. The substitution $\tilde{Q} \mapsto i\tilde{Q}$ interchanges $\mathbb{M}_+$ and $\mathbb{M}_-$; the analysis on the anti-Hermitian subspace is therefore the analysis on the Hermitian subspace with the scalar and the vector coordinates exchanged and the sign of the norm reversed, and its contour theory is the Kirchhoff–Green form of *Biquaternion Integration*.

## The Second-Order Operator and the Norm

**Theorem.** Let $V$ be one of the four real forms — $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ or $\mathbb{M}_-$ — and let $N(\partial)$ denote the differential operator obtained from the quadratic form $N|_V$ by replacing each real coordinate by the corresponding partial derivative. Then

$$
\Box\big|_{V} = e_0\,N(\partial).
$$

**Proof.** Expanding the composition, $\Box = \tilde\nabla\tilde\nabla^{\natural} = \sum_{\mu,\nu} e_\mu e_\nu^{\natural}\,\partial_\mu\partial_\nu$, with $e_0^{\natural} = e_0$ and $e_k^{\natural} = -e_k$. The diagonal coefficients are $e_\mu e_\mu^{\natural} = e_\mu(\pm e_\mu) = e_0$, and the off-diagonal ones cancel in pairs, $e_\mu e_\nu^{\natural} + e_\nu e_\mu^{\natural} = -e_\mu e_\nu - e_\nu e_\mu = 0$ for $\mu \neq \nu$. So the operator is $e_0$ times the scalar operator $\sum_\mu \partial_\mu^2$, whose restriction to a real form is $\sum_\mu \pm\partial_{q_\mu}^2$ with a minus sign exactly on the purely imaginary coordinates. The sign pattern is the one of the norm in the real basis of the subspace, and the two agree coefficient by coefficient.

**Corollary (the type of the operator).** On a real form the principal symbol of $\Box$ is the norm $N$ of the subspace, of signature $(4,0)$ on $\mathbb{H}_{\mathbb{B}}$, $(0,4)$ on $i\mathbb{H}_{\mathbb{B}}$, $(1,3)$ on $\mathbb{M}_+$ and $(3,1)$ on $\mathbb{M}_-$. Hence $\Box$ is elliptic on the quaternion and the anti-quaternion subspaces, where $N$ is definite, and of wave type on the two Hermitian subspaces, where $N$ is indefinite.

**The two complex subspaces.** On the centre and the vector subspace the operator is instead the square of a complex derivative, $e_0\partial_{Q_0}^2$ and $e_0\sum_k\partial_{Q_k}^2$, and its principal symbol is $\tfrac14(\xi - i\eta)^2$ and $\tfrac14\sum_k(\xi_k - i\eta_k)^2$. In one complex variable the symbol vanishes only at the origin, so the operator is elliptic; in three it vanishes on the complex null cone $\sum_k z_k^2 = 0$, so it is not. The real part of the symbol, read in the real coordinates, is $\sum_j s_j\xi_j^2$ with $s_j = +1$ on the coordinate vectors $e_\mu$ and $s_j = -1$ on the vectors $ie_\mu$, and this is the real part of $N$; its signatures are $(1,1)$ on the centre and $(3,3)$ on the vector subspace, as in *The Six Subspaces and the Forms*.

**Corollary (ellipticity and the zero divisors).** $\Box$ is elliptic exactly on the centre, the quaternion subspace and the anti-quaternion subspace — exactly the three of the six that contain no zero divisor — and non-elliptic on the vector subspace, the Hermitian subspace and the anti-Hermitian subspace, whose null cones are non-empty. On the four real forms the criterion is the definiteness of $N$; on the two complex subspaces it is the vanishing of the complex symbol, which holds in one variable and fails in three. The three subspaces without a zero divisor are therefore also the three on which the second-order analysis is of elliptic type, though for two different reasons: definiteness of the norm on $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and the field property of the centre.

## Summary

The analysis on the six distinguished subspaces is decided by two questions, which variables a function on the subspace depends on and which operator the algebra provides there, and the six fall into two classes. The centre and the vector subspace are the two complex subspaces, of complex dimension $1$ and $3$; on them the coefficients are genuinely complex and the analysis is complex analysis, in one and in three variables, with the complex derivative $\partial_{Q_0}$ and the complex Laplacian $\sum_k\partial_{Q_k}^2$ as the operators. The quaternion subspace, the anti-quaternion subspace and the two Hermitian subspaces are the four real forms, of real dimension $4$; on them every coefficient is real or purely imaginary, the partial derivatives are ordinary real derivatives up to the factor $\pm i$, and the analysis is the real-variable analysis of *Biquaternion Analysis*, the gradient taking the form $\sum_\mu e_\mu\partial_{q_\mu}$ on $\mathbb{H}_{\mathbb{B}}$, $-i\sum_\mu e_\mu\partial_{q'_\mu}$ on $i\mathbb{H}_{\mathbb{B}}$, $e_0\partial_{q_0} - i\sum_k e_k\partial_{q'_k}$ on $\mathbb{M}_+$ and $-ie_0\partial_{q'_0} + \sum_k e_k\partial_{q_k}$ on $\mathbb{M}_-$.

On each real form the second-order operator is the operator of the norm, $\Box = e_0 N(\partial)$: its principal symbol is the norm $N$ of the subspace, so its type is read off the signature of $N$, which is $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$ on $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$. The operator is elliptic on the quaternion and the anti-quaternion subspaces, where the norm is definite, and of wave type on the two Hermitian subspaces, where it is indefinite; the null cones $q_0^2 = \sum_k (q'_k)^2$ and $(q'_0)^2 = \sum_k q_k^2$ are the sets on which the analysis degenerates, and their points are the zero divisors of the two subspaces. On the two complex subspaces the operator is the square of the complex derivative; it is elliptic on the centre and not elliptic on the vector subspace, where the complex null cone $\sum_k Q_k^2 = 0$ carries the pure zero divisors and $e_1 + ie_2$ is a witness. The operator is therefore elliptic exactly on the centre, the quaternion subspace and the anti-quaternion subspace, which are exactly the three of the six that contain no zero divisor.

The contour theory follows the same division: on the centre it is the classical one-dimensional theory of one complex variable, over a closed curve, and it is the only one of the six on which the contour is one-dimensional; on the other five it is the theory of *Biquaternion Integration* over a three-dimensional boundary, in its Cauchy form on the quaternion subspace and its wave form on the two Hermitian subspaces. The operators themselves and the integral theory on a four-dimensional subspace are the business of *Biquaternion Analysis* and *Biquaternion Integration*; what is added here is the restriction to the six, the operator of the norm and the elliptic dichotomy.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace, the two complex subspaces |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ | the four real forms |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | an element, with $Q_\mu = q_\mu + i q'_\mu$ |
| $\tilde\nabla = \sum_\mu e_\mu\,\partial/\partial Q_\mu$ | the gradient, the Cauchy–Riemann operator of the algebra |
| $\Box = \tilde\nabla\tilde\nabla^{\natural} = \tilde\nabla^{\natural}\tilde\nabla = e_0(\partial_{Q_0}^2 + \Delta_Q)$ | the second-order operator |
| $\Delta_4$ | the Laplacian in the four real coordinates of a real form |
| $N$, $N(\partial)$ | the norm, and the operator obtained from it |
| $\partial_{Q}$ | $\partial_{q}$ or $-i\partial_{q'}$ on the real forms, the complex derivative on the complex subspaces |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *Biquaternion Analysis* (`articles_maths/biquaternion-analysis.md`), for the gradient, the d'Alembertian and the operators on a four-dimensional subspace
- *Biquaternion Integration* (`articles_maths/biquaternion-integration.md`), for the Cauchy integral formula, its consequences and the fundamental solutions on the quaternion subspace
- *The Six Subspaces and the Forms* (`articles_maths/the-six-subspaces-and-the-forms.md`), for the signatures of the norm on the six, which are the types of the second-order operator
- *The Six Subspaces and the Zero Divisors* (`articles_maths/the-six-subspaces-and-the-zero-divisors.md`), for the null elements on which the analysis degenerates
- *Quaternion Analysis* (`articles_maths/quaternion-analysis.md`), for the real quaternion case of the same operators
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the quaternion-valued analysis of four real variables.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford setting of the same first- and second-order operators.
